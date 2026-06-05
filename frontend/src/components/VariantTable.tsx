import { memo, useCallback, useEffect, useState } from 'react'
import type { VariantMatch } from '../types'
import Pagination from './Pagination'
import RiskBadge from './RiskBadge'
import VariantDetail from './VariantDetail'

const PAGE_SIZE = 100

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
      <td colSpan={4} className="p-0">
        <button
          onClick={() => onToggle(match.snp.rsid)}
          className="w-full text-left hover:bg-gray-50 transition-colors"
        >
          <div className="flex items-center">
            <div className="px-6 py-4 w-1/5">
              <span className="font-medium text-gray-900">{match.variant.gene}</span>
              <span className="block text-xs text-gray-400 font-mono">{match.snp.rsid}</span>
            </div>
            <div className="px-6 py-4 w-2/5">
              <span className="text-sm text-gray-700">{match.variant.name}</span>
            </div>
            <div className="px-6 py-4 w-1/5">
              <span className="font-mono text-sm font-bold text-gray-900">{match.snp.genotype}</span>
            </div>
            <div className="px-6 py-4 w-1/5">
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

        </div>
      </button>
      {isExpanded && <VariantDetail match={match} />}
    </div>
  )
})

export default function VariantTable({ matches, emptyMessage }: VariantTableProps) {
  const [expandedRsid, setExpandedRsid] = useState<string | null>(null)
  const [page, setPage] = useState(1)

  useEffect(() => {
    setPage(1)
  }, [matches])

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

  const totalPages = Math.ceil(matches.length / PAGE_SIZE)
  const pageMatches = matches.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE)

  return (
    <>
      {/* Desktop table (md and up) */}
      <div className="hidden md:block bg-white rounded-xl border border-gray-200 overflow-hidden">
        <table className="w-full">
          <thead>
            <tr className="bg-gray-50 border-b border-gray-200">
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider w-1/5">
                Gene
              </th>
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider w-2/5">
                Variant
              </th>
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider w-1/5">
                Your Genotype
              </th>
              <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider w-1/5">
                Risk Level
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {pageMatches.map((match) => (
              <DesktopRow
                key={match.snp.rsid}
                match={match}
                isExpanded={expandedRsid === match.snp.rsid}
                onToggle={handleToggle}
              />
            ))}
          </tbody>
        </table>
        <Pagination page={page} totalPages={totalPages} onPageChange={setPage} />
      </div>

      {/* Mobile card layout (below md) */}
      <div className="md:hidden space-y-3">
        {pageMatches.map((match) => (
          <MobileCard
            key={match.snp.rsid}
            match={match}
            isExpanded={expandedRsid === match.snp.rsid}
            onToggle={handleToggle}
          />
        ))}
        <Pagination page={page} totalPages={totalPages} onPageChange={setPage} />
      </div>
    </>
  )
}

