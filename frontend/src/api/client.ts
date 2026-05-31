import type { AnalysisResult, EnrichmentResult } from '../types'

const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

export async function uploadFile(file: File): Promise<AnalysisResult> {
  const formData = new FormData()
  formData.append('file', file)

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
  const response = await fetch(`${BASE_URL}/enrich/${rsid}`)

  if (!response.ok) {
    const text = await response.text()
    throw new Error(`Enrichment failed (${response.status}): ${text}`)
  }

  return response.json()
}
