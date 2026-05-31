export default function GeneticCounselingCard() {
  return (
    <div className="bg-amber-50 border border-amber-300 rounded-lg px-5 py-4">
      <div className="flex items-start gap-3">
        <svg
          className="w-6 h-6 text-amber-600 shrink-0 mt-0.5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4.5c-.77-.833-2.694-.833-3.464 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z"
          />
        </svg>
        <div className="space-y-2">
          <h3 className="text-base font-semibold text-amber-900">
            Genetic Counseling Recommended
          </h3>
          <p className="text-sm text-amber-800 leading-relaxed">
            Your results include one or more variants classified as pathogenic or likely pathogenic.
            We strongly recommend discussing these findings with a certified genetic counselor who
            can provide personalized interpretation and guidance.
          </p>
          <a
            href="https://findageneticcounselor.nsgc.org/"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1.5 px-4 py-2 text-sm font-medium text-amber-900 bg-amber-200 hover:bg-amber-300 rounded-lg transition-colors"
          >
            Find a Genetic Counselor (NSGC)
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
              />
            </svg>
          </a>
        </div>
      </div>
    </div>
  )
}
