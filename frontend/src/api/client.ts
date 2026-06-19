import type { AnalysisResult, EnrichmentResult } from '../types'

const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

async function compressFile(file: File): Promise<Blob> {
  const text = await file.text()
  // Strip to rsid+genotype only — drops i-prefix IDs, chromosome, and position
  // (~75% size reduction before gzip). Backend detects this compact 2-column format.
  const lines = text.split('\n').flatMap(line => {
    if (line.startsWith('#')) return [line]
    if (!line.startsWith('rs')) return []
    const parts = line.split('\t')
    return parts.length >= 4 ? [`${parts[0]}\t${parts[3]}`] : []
  })
  const stream = new Blob([lines.join('\n')]).stream().pipeThrough(new CompressionStream('gzip'))
  return new Response(stream).blob()
}

export async function uploadFile(file: File): Promise<AnalysisResult> {
  const compressed = await compressFile(file)
  const formData = new FormData()
  formData.append('file', compressed, file.name)

  const response = await fetch(`${BASE_URL}/upload`, {
    method: 'POST',
    body: formData,
  })

  if (!response.ok) {
    const text = await response.text()
    throw new Error(`Upload failed (${response.status}): ${text}`)
  }

  return response.json()
}

export async function enrichVariant(rsid: string): Promise<EnrichmentResult> {
  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 9000)

  try {
    const response = await fetch(`${BASE_URL}/enrich/${rsid}`, {
      signal: controller.signal,
    })

    if (!response.ok) {
      const text = await response.text()
      throw new Error(`Enrichment failed (${response.status}): ${text}`)
    }

    return response.json()
  } catch (err) {
    if (err instanceof Error && err.name === 'AbortError') {
      throw new Error('Enrichment is taking too long — please try again')
    }
    throw err
  } finally {
    clearTimeout(timeoutId)
  }
}
