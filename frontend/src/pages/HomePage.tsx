import DisclaimerBanner from '../components/DisclaimerBanner'
import FileUpload from '../components/FileUpload'

interface HomePageProps {
  onFileSelected: (file: File) => void
  isUploading: boolean
  error: string | null
  onClearError: () => void
}

export default function HomePage({ onFileSelected, isUploading, error, onClearError }: HomePageProps) {
  return (
    <div className="max-w-2xl mx-auto space-y-8">
      <div className="text-center space-y-3">
        <h2 className="text-3xl font-bold text-gray-900">Analyze Your Genetic Data</h2>
        <p className="text-gray-600 leading-relaxed">
          Upload your 23andMe raw data file to identify clinically significant SNP variants across
          health risks, pharmacogenomics, and traits.
        </p>
      </div>

      <FileUpload onFileSelected={onFileSelected} isUploading={isUploading} />

      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg px-4 py-3 flex items-center justify-between">
          <p className="text-sm text-red-700">{error}</p>
          <button
            onClick={onClearError}
            className="ml-3 px-3 py-1.5 text-sm font-medium text-red-700 bg-red-100 hover:bg-red-200 rounded-md transition-colors shrink-0"
          >
            Try Again
          </button>
        </div>
      )}

      <DisclaimerBanner mode="compact" />

      <div className="text-center text-xs text-gray-400 space-y-1">
        <p>Your data is processed locally and is not stored on any server.</p>
        <p>Supported: 23andMe raw data (.txt format)</p>
      </div>
    </div>
  )
}
