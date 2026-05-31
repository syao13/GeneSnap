export type Category = 'health_risk' | 'pharmacogenomics' | 'trait'
export type Significance = 'pathogenic' | 'likely_pathogenic' | 'risk_factor' | 'drug_response' | 'association'
export type RiskLevel = 'normal' | 'carrier' | 'increased_risk' | 'high_risk'

export interface SNP {
  rsid: string
  chromosome: string
  position: number
  genotype: string
}

export interface CuratedVariant {
  rsid: string
  gene: string
  category: Category
  name: string
  significance: Significance
  description: string
  risk_allele: string | null
  normal_allele: string | null
  chromosome: string
  position: number
  source: string
  external_ids: Record<string, string> | null
  publications: string[] | null
  clinvar_stars: number
  odds_ratio: number | null
}

export interface VariantMatch {
  snp: SNP
  variant: CuratedVariant
  interpretation: string
  risk_level: RiskLevel
  publications: string[]
  score: number
}

export interface AnalysisSummary {
  total_snps_parsed: number
  total_variants_found: number
  health_risk_count: number
  pharmacogenomics_count: number
  trait_count: number
  high_risk_count: number
}

export interface AnalysisResult {
  summary: AnalysisSummary
  health_risks: VariantMatch[]
  pharmacogenomics: VariantMatch[]
  traits: VariantMatch[]
}

export interface ClinVarData {
  variant_id: string
  clinical_significance: string
  review_status: string
  conditions: string[]
  last_evaluated: string
  title: string
}

export interface PubMedArticle {
  pmid: string
  title: string
  authors: string[]
  journal: string
  pub_date: string
  doi: string
}

export interface GWASAssociation {
  risk_allele: string
  odds_ratio: number | null
  beta: number | null
  p_value: number | null
  trait: string
  study_accession: string
}

export interface EnrichmentResult {
  rsid: string
  clinvar: ClinVarData | null
  known_publications: PubMedArticle[]
  search_publications: PubMedArticle[]
  gwas_associations: GWASAssociation[]
}
