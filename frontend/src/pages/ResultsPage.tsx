import { useState } from 'react'
import DisclaimerBanner from '../components/DisclaimerBanner'
import GeneticCounselingCard from '../components/GeneticCounselingCard'
import SummaryCards from '../components/SummaryCards'
import VariantTable from '../components/VariantTable'
import type { AnalysisResult } from '../types'

interface ResultsPageProps {
  result: AnalysisResult
  onReset: () => void
}

type Tab = 'health' | 'pharma' | 'traits'

const TABS: { key: Tab; label: string }[] = [
  { key: 'health', label: 'Health Risks' },
  { key: 'pharma', label: 'Pharmacogenomics' },
  { key: 'traits', label: 'Traits' },
]

function hasPathogenicVariants(result: AnalysisResult): boolean {
  const allMatches = [...result.health_risks, ...result.pharmacogenomics, ...result.traits]
  return allMatches.some(
    (m) =>
      m.variant.significance === 'pathogenic' || m.variant.significance === 'likely_pathogenic',
  )
}

export default function ResultsPage({ result, onReset }: ResultsPageProps) {
  const [activeTab, setActiveTab] = useState<Tab>('health')

  const tabData = {
    health: {
      matches: result.health_risks,
      empty: 'No health risk variants identified in your data.',
    },
    pharma: {
      matches: result.pharmacogenomics,
      empty: 'No pharmacogenomics variants identified in your data.',
    },
    traits: {
      matches: result.traits,
      empty: 'No trait-associated variants identified in your data.',
    },
  }

  const current = tabData[activeTab]
  const showCounseling = hasPathogenicVariants(result)

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-900">Analysis Results</h2>
        <button
          onClick={onReset}
          className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
        >
          Analyze Another File
        </button>
      </div>

      <SummaryCards summary={result.summary} />

      {showCounseling && <GeneticCounselingCard />}

      <div className="bg-white rounded-xl border border-gray-200 p-1.5 inline-flex gap-1.5">
        {TABS.map((tab) => {
          const count =
            tab.key === 'health'
              ? result.summary.health_risk_count
              : tab.key === 'pharma'
                ? result.summary.pharmacogenomics_count
                : result.summary.trait_count
          const isActive = activeTab === tab.key
          return (
            <button
              key={tab.key}
              onClick={() => setActiveTab(tab.key)}
              className={`px-5 py-2.5 rounded-lg text-sm font-semibold transition-all ${
                isActive
                  ? 'bg-indigo-600 text-white shadow-sm'
                  : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
              }`}
            >
              {tab.label}
              <span
                className={`ml-2 inline-flex items-center justify-center min-w-[1.5rem] px-1.5 py-0.5 text-xs font-bold rounded-full ${
                  isActive
                    ? 'bg-white/20 text-white'
                    : 'bg-gray-200 text-gray-700'
                }`}
              >
                {count}
              </span>
            </button>
          )
        })}
      </div>

      <VariantTable matches={current.matches} emptyMessage={current.empty} />

      <DisclaimerBanner mode="full" />
    </div>
  )
}
