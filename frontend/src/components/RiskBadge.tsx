import type { RiskLevel } from '../types'

const RISK_CONFIG: Record<RiskLevel, { label: string; className: string }> = {
  high_risk: {
    label: 'High Risk',
    className: 'bg-red-100 text-red-800 border-red-200',
  },
  increased_risk: {
    label: 'Increased Risk',
    className: 'bg-orange-100 text-orange-800 border-orange-200',
  },
  carrier: {
    label: 'Carrier',
    className: 'bg-yellow-100 text-yellow-800 border-yellow-200',
  },
  normal: {
    label: 'Normal',
    className: 'bg-green-100 text-green-800 border-green-200',
  },
}

interface RiskBadgeProps {
  level: RiskLevel
}

export default function RiskBadge({ level }: RiskBadgeProps) {
  const config = RISK_CONFIG[level]
  return (
    <span
      className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border ${config.className}`}
    >
      {config.label}
    </span>
  )
}
