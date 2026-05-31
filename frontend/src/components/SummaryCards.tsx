import type { AnalysisSummary } from '../types'

interface SummaryCardsProps {
  summary: AnalysisSummary
}

export default function SummaryCards({ summary }: SummaryCardsProps) {
  const cards = [
    {
      label: 'SNPs Analyzed',
      value: summary.total_snps_parsed.toLocaleString(),
      color: 'bg-blue-50 text-blue-700 border-blue-200',
    },
    {
      label: 'Variants Found',
      value: summary.total_variants_found,
      color: 'bg-indigo-50 text-indigo-700 border-indigo-200',
    },
    {
      label: 'Health Risks',
      value: summary.health_risk_count,
      color: 'bg-orange-50 text-orange-700 border-orange-200',
    },
    {
      label: 'Pharmacogenomics',
      value: summary.pharmacogenomics_count,
      color: 'bg-purple-50 text-purple-700 border-purple-200',
    },
    {
      label: 'Traits',
      value: summary.trait_count,
      color: 'bg-teal-50 text-teal-700 border-teal-200',
    },
    {
      label: 'High Risk',
      value: summary.high_risk_count,
      color:
        summary.high_risk_count > 0
          ? 'bg-red-50 text-red-700 border-red-200'
          : 'bg-green-50 text-green-700 border-green-200',
    },
  ]

  return (
    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
      {cards.map((card) => (
        <div key={card.label} className={`rounded-xl border p-4 ${card.color}`}>
          <p className="text-2xl font-bold">{card.value}</p>
          <p className="text-sm mt-1 opacity-80">{card.label}</p>
        </div>
      ))}
    </div>
  )
}
