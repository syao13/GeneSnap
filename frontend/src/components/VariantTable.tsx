import { memo, useCallback, useState } from 'react'
import type { VariantMatch } from '../types'
import RiskBadge from './RiskBadge'
import VariantDetail from './VariantDetail'

interface VariantTableProps {
  matches: VariantMatch[]
  emptyMessage: string
}

interface RowProps {
  match: VariantMatch
  isExpanded: boolean
  onToggle: (rsid: string) => void
}

const DesktopRow = memo(function DesktopRow({ match, isExpanded, onToggle }: RowProps) {
  return (
    <tr className="group">
      <td colSpan={5} className="p-0">
        <button
          onClick={() => onToggle(match.snp.rsid)}
          className="w-full text-left hover:bg-gray-50 transition-colors"
        >
          <div className="flex items-center">
            <div className="px-6 py-4 w-1/6">
              <span className="font-medium text-gray-900">{match.variant.gene}</span>
              <span className="block text-xs text-gray-400 font-mono">{match.snp.rsid}</span>
            </div>
            <div className="px-6 py-4 w-1/3">
              <span className="text-sm text-gray-700">{match.variant.name}</span>
            </div>
            <div className="px-6 py-4 w-1/6">
              <span className="font-mono text-sm font-bold text-gray-900">{match.snp.genotype}</span>
            </div>
            <div className="px-6 py-4 w-1/6">
              <ScoreBadge score={match.score} />
            </div>
            <div className="px-6 py-4 w-1/6">
              <RiskBadge level={match.risk_level} />
            </div>
          </div>
        </button>
        {isExpanded && <VariantDetail match={match} />}
      </td>
    </tr>
  )
})

const MobileCard = memo(function MobileCard({ match, isExpanded, onToggle }: RowProps) {
  return (
    <div className="bg-white rounded-xl border border-gray-200 overflow-hidden">
      <button
        onClick={() => onToggle(match.snp.rsid)}
        className="w-full text-left p-4 hover:bg-gray-50 transition-colors"
      >
        <div className="flex items-start justify-between gap-3">
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <span className="font-semibold text-gray-900">{match.variant.gene}</span>
              <span className="text-xs text-gray-400 font-mono">{match.snp.rsid}</span>
            </div>
            <p className="text-sm text-gray-600 mt-0.5 truncate">{match.variant.name}</p>
          </div>
          <RiskBadge level={match.risk_level} />
        </div>
        <div className="flex items-center gap-4 mt-2">
          <div className="text-xs text-gray-500">
            Genotype:{' '}
            <span className="font-mono font-bold text-gray-900">{match.snp.genotype}</span>
          </div>
          <div className="text-xs text-gray-500">
            Score: <ScoreBadge score={match.score} />
          </div>
        </div>
      </button>
      {isExpanded && <VariantDetail match={match} />}
    </div>
  )
})

export default function VariantTable({ matches, emptyMessage }: VariantTableProps) {
  const [expandedRsid, setExpandedRsid] = useState<string | null>(null)

  const handleToggle = useCallback((rsid: string) => {
    setExpandedRsid((prev) => (prev === rsid ? null : rsid))
  }, [])

  if (matches.length === 0) {
    return (
      <div className="bg-white rounded-xl border border-gray-200 p-8 text-center text-gray-500">
        {emptyMessage}
      </div>
    )
  }

  return (
    <>
      {/* Desktop table (md and up) */}
      <div className="hidden md:block bg-white rounded-xl border border-gray-200 overflow-hidden">
        <table className="w-full">
          <thead>
            <tr className="bg-gray-50 border-b border-gray-200">
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                Gene
              </th>
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                Variant
              </th>
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                Your Genotype
              </th>
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                Score
              </th>
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                Risk Level
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {matches.map((match) => (
              <DesktopRow
                key={match.snp.rsid}
                match={match}
                isExpanded={expandedRsid === match.snp.rsid}
                onToggle={handleToggle}
              />
            ))}
          </tbody>
        </table>
      </div>

      {/* Mobile card layout (below md) */}
      <div className="md:hidden space-y-3">
        {matches.map((match) => (
          <MobileCard
            key={match.snp.rsid}
            match={match}
            isExpanded={expandedRsid === match.snp.rsid}
            onToggle={handleToggle}
          />
        ))}
      </div>
    </>
  )
}

function ScoreBadge({ score }: { score: number }) {
  const getColor = () => {
    if (score >= 100) return 'bg-red-100 text-red-800 border-red-200'
    if (score >= 40) return 'bg-orange-100 text-orange-800 border-orange-200'
    if (score >= 15) return 'bg-yellow-100 text-yellow-800 border-yellow-200'
    return 'bg-gray-100 text-gray-700 border-gray-200'
  }

  return (
    <span
      className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold border ${getColor()}`}
      title="Composite evidence score based on clinical significance, review confidence, and effect size"
    >
      {score}
    </span>
  )
}
