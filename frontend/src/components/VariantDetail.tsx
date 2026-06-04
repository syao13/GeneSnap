import type { VariantMatch } from '../types'

interface VariantDetailProps {
  match: VariantMatch
}

export default function VariantDetail({ match }: VariantDetailProps) {
  const { snp, variant, interpretation } = match

  return (
    <div className="bg-gray-50 border-t border-gray-200 px-6 py-5 space-y-4">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <h4 className="text-sm font-medium text-gray-500 mb-1">Your Genotype</h4>
          <p className="text-lg font-mono font-bold text-gray-900">{snp.genotype}</p>
          <p className="text-sm text-gray-600 mt-1">
            Position: chr{snp.chromosome}:{snp.position.toLocaleString()}
          </p>
        </div>
        <div>
          <h4 className="text-sm font-medium text-gray-500 mb-1">Interpretation</h4>
          <p className="text-sm text-gray-800">{interpretation}</p>
          {variant.risk_allele && (
            <p className="text-xs text-gray-500 mt-2">
              Risk allele: <span className="font-mono font-bold">{variant.risk_allele}</span>
              {variant.normal_allele && (
                <>
                  {' / Normal allele: '}
                  <span className="font-mono font-bold">{variant.normal_allele}</span>
                </>
              )}
            </p>
          )}
        </div>
      </div>

      <div>
        <h4 className="text-sm font-medium text-gray-500 mb-1">Description</h4>
        <p className="text-sm text-gray-700 leading-relaxed">{variant.description}</p>
      </div>

      {/* Per-variant pathogenic disclaimer */}
      {(variant.significance === 'pathogenic' || variant.significance === 'likely_pathogenic') && (
        <div className="bg-amber-50 border border-amber-200 rounded-lg px-4 py-3">
          <p className="text-sm text-amber-800">
            This variant is classified as <strong>{variant.significance.replace('_', ' ')}</strong>.
            Clinical-grade confirmatory testing is recommended before making any medical decisions.
          </p>
        </div>
      )}

      {/* Evidence metadata */}
      <div className="flex flex-wrap gap-3">
        <div className="flex items-center gap-1.5 px-3 py-1.5 bg-white border border-gray-200 rounded-md">
          <span className="text-xs text-gray-500">ClinVar Stars:</span>
          <span className="text-xs font-semibold text-amber-600">
            {'★'.repeat(variant.clinvar_stars)}{'☆'.repeat(4 - variant.clinvar_stars)}
          </span>
        </div>
        {variant.odds_ratio != null && (
          <div className="flex items-center gap-1.5 px-3 py-1.5 bg-white border border-gray-200 rounded-md">
            <span className="text-xs text-gray-500">Odds Ratio:</span>
            <span className="text-xs font-semibold text-gray-900">{variant.odds_ratio.toFixed(1)}x</span>
          </div>
        )}
        <div className="flex items-center gap-1.5 px-3 py-1.5 bg-white border border-gray-200 rounded-md">
          <span className="text-xs text-gray-500">Evidence Score:</span>
          <span className="text-xs font-semibold text-indigo-700">{match.score}</span>
        </div>
      </div>

      {match.publications.length > 0 && (
        <div>
          <h4 className="text-sm font-medium text-gray-500 mb-2">Key Publications</h4>
          <div className="flex flex-wrap gap-2">
            {match.publications.map((pmid) => (
              <a
                key={pmid}
                href={`https://pubmed.ncbi.nlm.nih.gov/${pmid}/`}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-white border border-gray-200 text-indigo-600 hover:bg-indigo-50 hover:border-indigo-300 transition-colors"
              >
                PMID: {pmid}
                <ExternalLinkIcon />
              </a>
            ))}
          </div>
        </div>
      )}

      {/* External links */}
      <div className="flex gap-2 pt-2">
        <a
          href={`https://www.ncbi.nlm.nih.gov/snp/${variant.rsid}`}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center px-3 py-1.5 text-xs font-medium text-indigo-700 bg-indigo-50 border border-indigo-200 rounded-md hover:bg-indigo-100 hover:border-indigo-300 transition-colors"
        >
          dbSNP
          <ExternalLinkIcon />
        </a>
        <a
          href={`https://www.ncbi.nlm.nih.gov/clinvar/?term=${variant.rsid}`}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center px-3 py-1.5 text-xs font-medium text-indigo-700 bg-indigo-50 border border-indigo-200 rounded-md hover:bg-indigo-100 hover:border-indigo-300 transition-colors"
        >
          ClinVar
          <ExternalLinkIcon />
        </a>
        <a
          href={`https://www.snpedia.com/index.php/${variant.rsid}`}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center px-3 py-1.5 text-xs font-medium text-indigo-700 bg-indigo-50 border border-indigo-200 rounded-md hover:bg-indigo-100 hover:border-indigo-300 transition-colors"
        >
          SNPedia
          <ExternalLinkIcon />
        </a>
      </div>
    </div>
  )
}

function ExternalLinkIcon() {
  return (
    <svg className="ml-1 w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={2}
        d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
      />
    </svg>
  )
}
