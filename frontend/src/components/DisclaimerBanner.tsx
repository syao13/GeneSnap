import { useState } from 'react'

interface DisclaimerBannerProps {
  mode: 'compact' | 'full'
}

export default function DisclaimerBanner({ mode }: DisclaimerBannerProps) {
  const [isExpanded, setIsExpanded] = useState(false)

  if (mode === 'compact') {
    return (
      <div className="bg-amber-50 border border-amber-200 rounded-lg px-4 py-3">
        <p className="text-sm text-amber-800">
          <strong>Disclaimer:</strong> This tool is for informational and educational purposes only.
          Results are not medical advice. Consumer genotyping arrays test a small fraction of the
          genome and may miss important variants. Consult a healthcare professional or genetic
          counselor for clinical interpretation.
        </p>
      </div>
    )
  }

  return (
    <div className="bg-amber-50 border border-amber-200 rounded-lg overflow-hidden">
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="w-full px-4 py-3 flex items-center justify-between text-left hover:bg-amber-100/50 transition-colors"
      >
        <p className="text-sm text-amber-800">
          <strong>Important:</strong> These results are for informational purposes only and should
          not be used for medical decisions. Consumer genotyping may miss variants.
        </p>
        <svg
          className={`w-5 h-5 text-amber-600 shrink-0 ml-2 transition-transform ${isExpanded ? 'rotate-180' : ''}`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {isExpanded && (
        <div className="px-4 pb-4 border-t border-amber-200">
          <ul className="mt-3 space-y-2 text-sm text-amber-900">
            <li className="flex gap-2">
              <span className="text-amber-600 font-bold shrink-0">1.</span>
              <span>
                <strong>Not a diagnostic tool</strong> &mdash; Results are informational only and do
                not constitute medical advice or a diagnosis.
              </span>
            </li>
            <li className="flex gap-2">
              <span className="text-amber-600 font-bold shrink-0">2.</span>
              <span>
                <strong>Genotyping is not sequencing</strong> &mdash; Consumer SNP arrays test
                approximately 0.02% of the genome and may miss many clinically important variants.
              </span>
            </li>
            <li className="flex gap-2">
              <span className="text-amber-600 font-bold shrink-0">3.</span>
              <span>
                <strong>Rare variant accuracy</strong> &mdash; For variants with frequency below
                0.1%, SNP chip accuracy drops significantly. False positives and negatives are
                possible.
              </span>
            </li>
            <li className="flex gap-2">
              <span className="text-amber-600 font-bold shrink-0">4.</span>
              <span>
                <strong>Confirmation needed</strong> &mdash; Clinically significant findings should
                be confirmed with clinical-grade laboratory testing (e.g., Sanger sequencing).
              </span>
            </li>
            <li className="flex gap-2">
              <span className="text-amber-600 font-bold shrink-0">5.</span>
              <span>
                <strong>Genetic counseling recommended</strong> &mdash; Especially for
                pathogenic or likely pathogenic results, consult a certified genetic counselor for
                proper interpretation and guidance.
              </span>
            </li>
          </ul>
        </div>
      )}
    </div>
  )
}
