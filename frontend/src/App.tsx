import { useCallback, useEffect, useState } from 'react'
import { uploadFile } from './api/client'
import ErrorBoundary from './components/ErrorBoundary'
import Layout from './components/Layout'
import HomePage from './pages/HomePage'
import ResultsPage from './pages/ResultsPage'
import type { AnalysisResult } from './types'

export default function App() {
  const [result, setResult] = useState<AnalysisResult | null>(null)
  const [isUploading, setIsUploading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (result) {
      window.scrollTo(0, 0)
    }
  }, [result])

  const handleFileSelected = useCallback(async (file: File) => {
    setIsUploading(true)
    setError(null)

    try {
      const analysisResult = await uploadFile(file)
      setResult(analysisResult)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred.')
    } finally {
      setIsUploading(false)
    }
  }, [])

  const handleReset = useCallback(() => {
    setResult(null)
    setError(null)
  }, [])

  const handleClearError = useCallback(() => {
    setError(null)
  }, [])

  return (
    <ErrorBoundary>
      <Layout>
        {result ? (
          <ResultsPage result={result} onReset={handleReset} />
        ) : (
          <HomePage
            onFileSelected={handleFileSelected}
            isUploading={isUploading}
            error={error}
            onClearError={handleClearError}
          />
        )}
      </Layout>
    </ErrorBoundary>
  )
}
