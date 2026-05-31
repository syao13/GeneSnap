import { useCallback, useState } from 'react'
import { enrichVariant } from '../api/client'
import type { EnrichmentResult, GWASAssociation, PubMedArticle, VariantMatch } from '../types'

interface VariantDetailProps {
  match: VariantMatch
}

export default function VariantDetail({ match }: VariantDetailProps) {
  const { snp, variant, interpretation } = match
  const [enrichment, setEnrichment] = useState<EnrichmentResult | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleEnrich = useCallback(async () => {
    setIsLoading(true)
    setError(null)
    try {
      const data = await enrichVariant(snp.rsid)
      setEnrichment(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load research data.')
    } finally {
      setIsLoading(false)
    }
  }, [snp.rsid])

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

      {/* Static PMID links */}
      {match.publications.length > 0 && !(enrichment?.known_publications?.length) && (
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

      {/* Enrichment section */}
      {!enrichment && !isLoading && (
        <button
          onClick={handleEnrich}
          className="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors"
        >
          <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
          Load Latest Research
        </button>
      )}

      {isLoading && (
        <div className="flex items-center gap-3 text-sm text-gray-600">
          <div className="w-5 h-5 border-2 border-indigo-200 border-t-indigo-600 rounded-full animate-spin" />
          Fetching from ClinVar, PubMed, and GWAS Catalog...
        </div>
      )}

      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg px-4 py-3 flex items-center justify-between">
          <p className="text-sm text-red-700">{error}</p>
          <button
            onClick={handleEnrich}
            className="ml-3 px-3 py-1.5 text-sm font-medium text-red-700 bg-red-100 hover:bg-red-200 rounded-md transition-colors shrink-0"
          >
            Retry
          </button>
        </div>
      )}

      {enrichment && <EnrichmentDisplay data={enrichment} />}

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

function EnrichmentDisplay({ data }: { data: EnrichmentResult }) {
  return (
    <div className="space-y-4 border-t border-gray-200 pt-4">
      <h4 className="text-sm font-semibold text-indigo-700 uppercase tracking-wider">
        Live Research Data
      </h4>

      {/* ClinVar */}
      {data.clinvar && (
        <div className="bg-white rounded-lg border border-gray-200 p-4 space-y-2">
          <h5 className="text-sm font-medium text-gray-900">ClinVar</h5>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm">
            <div>
              <span className="text-gray-500">Significance: </span>
              <span className="font-medium">{data.clinvar.clinical_significance || 'N/A'}</span>
            </div>
            <div>
              <span className="text-gray-500">Review: </span>
              <span className="font-medium">{data.clinvar.review_status || 'N/A'}</span>
            </div>
            {data.clinvar.conditions.length > 0 && (
              <div className="md:col-span-2">
                <span className="text-gray-500">Conditions: </span>
                <span className="font-medium">{data.clinvar.conditions.join(', ')}</span>
              </div>
            )}
            {data.clinvar.title && (
              <div className="md:col-span-2">
                <span className="text-gray-500">Title: </span>
                <span className="font-medium text-xs font-mono">{data.clinvar.title}</span>
              </div>
            )}
          </div>
        </div>
      )}

      {/* GWAS Catalog Associations */}
      {data.gwas_associations?.length > 0 && (
        <div className="bg-white rounded-lg border border-gray-200 p-4 space-y-2">
          <h5 className="text-sm font-medium text-gray-900">GWAS Catalog</h5>
          <div className="space-y-2">
            {data.gwas_associations.map((assoc, i) => (
              <GWASRow key={i} assoc={assoc} />
            ))}
          </div>
        </div>
      )}

      {/* Known Publications (with full details) */}
      {data.known_publications.length > 0 && (
        <div>
          <h5 className="text-sm font-medium text-gray-900 mb-2">Key Publications</h5>
          <div className="space-y-2">
            {data.known_publications.map((article) => (
              <ArticleCard key={article.pmid} article={article} />
            ))}
          </div>
        </div>
      )}

      {/* Additional PubMed results */}
      {data.search_publications.length > 0 && (
        <div>
          <h5 className="text-sm font-medium text-gray-900 mb-2">Additional Research</h5>
          <div className="space-y-2">
            {data.search_publications.map((article) => (
              <ArticleCard key={article.pmid} article={article} />
            ))}
          </div>
        </div>
      )}

      {!data.clinvar &&
        data.known_publications.length === 0 &&
        data.search_publications.length === 0 &&
        (!data.gwas_associations || data.gwas_associations.length === 0) && (
          <p className="text-sm text-gray-500">No additional data found in external databases.</p>
        )}
    </div>
  )
}

function GWASRow({ assoc }: { assoc: GWASAssociation }) {
  const formatPValue = (p: number | null) => {
    if (p == null) return 'N/A'
    if (p < 1e-100) return '< 1e-100'
    return p.toExponential(1)
  }

  return (
    <div className="flex flex-wrap gap-x-4 gap-y-1 text-sm border-b border-gray-100 pb-2 last:border-0 last:pb-0">
      {assoc.trait && (
        <div>
          <span className="text-gray-500">Trait: </span>
          <span className="font-medium">{assoc.trait}</span>
        </div>
      )}
      {assoc.odds_ratio != null && (
        <div>
          <span className="text-gray-500">OR: </span>
          <span className="font-semibold text-orange-700">{assoc.odds_ratio.toFixed(2)}</span>
        </div>
      )}
      {assoc.beta != null && (
        <div>
          <span className="text-gray-500">Beta: </span>
          <span className="font-medium">{assoc.beta.toFixed(3)}</span>
        </div>
      )}
      <div>
        <span className="text-gray-500">p-value: </span>
        <span className="font-mono text-xs">{formatPValue(assoc.p_value)}</span>
      </div>
      {assoc.risk_allele && (
        <div>
          <span className="text-gray-500">Risk allele: </span>
          <span className="font-mono font-bold">{assoc.risk_allele}</span>
        </div>
      )}
    </div>
  )
}

function ArticleCard({ article }: { article: PubMedArticle }) {
  const authorStr =
    article.authors.length > 3
      ? `${article.authors.slice(0, 3).join(', ')} et al.`
      : article.authors.join(', ')

  return (
    <a
      href={`https://pubmed.ncbi.nlm.nih.gov/${article.pmid}/`}
      target="_blank"
      rel="noopener noreferrer"
      className="block bg-white rounded-lg border border-gray-200 p-3 hover:border-indigo-300 hover:shadow-sm transition-all"
    >
      <p className="text-sm font-medium text-gray-900 leading-snug">{article.title}</p>
      <div className="mt-1 flex flex-wrap gap-x-3 text-xs text-gray-500">
        {authorStr && <span>{authorStr}</span>}
        {article.journal && <span className="italic">{article.journal}</span>}
        {article.pub_date && <span>{article.pub_date}</span>}
      </div>
    </a>
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
