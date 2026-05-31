"""Neurological health risk variants: LRRK2, GBA, BDNF, MAPT, SNCA, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    {
        "rsid": "rs34637584",
        "gene": "LRRK2",
        "category": "health_risk",
        "name": "LRRK2 G2019S (Parkinson's)",
        "significance": "pathogenic",
        "description": (
            "Most common genetic cause of familial and sporadic Parkinson's disease. "
            "The G2019S substitution in the kinase domain increases LRRK2 kinase activity, "
            "leading to neuronal toxicity. Penetrance is age-dependent, reaching ~30-75% "
            "by age 80 depending on ethnicity."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "12",
        "position": 40734202,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000001940"},
        "publications": ["15680455", "15541309"],
        "clinvar_stars": 4,
        "odds_ratio": 9.0,
    },
    {
        "rsid": "rs76763715",
        "gene": "GBA",
        "category": "health_risk",
        "name": "GBA N370S (Parkinson's/Gaucher)",
        "significance": "risk_factor",
        "description": (
            "Most common GBA mutation in Ashkenazi Jewish populations. Homozygous state "
            "causes Gaucher disease type 1. Heterozygous carriers have approximately "
            "5-fold increased risk for Parkinson's disease through impaired lysosomal "
            "function and alpha-synuclein accumulation."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "1",
        "position": 155205634,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000004288"},
        "publications": ["14647384", "19846850"],
        "clinvar_stars": 3,
        "odds_ratio": 5.0,
    },
    {
        "rsid": "rs6265",
        "gene": "BDNF",
        "category": "health_risk",
        "name": "BDNF Val66Met",
        "significance": "association",
        "description": (
            "Functional polymorphism in brain-derived neurotrophic factor. The Met allele "
            "reduces activity-dependent BDNF secretion and is associated with reduced "
            "hippocampal volume, impaired episodic memory, and susceptibility to "
            "neuropsychiatric disorders including depression and anxiety."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "11",
        "position": 27679916,
        "source": "gwas_catalog",
        "publications": ["12624268", "17135278"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1800547",
        "gene": "MAPT",
        "category": "health_risk",
        "name": "MAPT H1/H2 haplotype (tauopathy risk)",
        "significance": "association",
        "description": (
            "Tag SNP for the MAPT H1/H2 haplotype inversion on chromosome 17. The H1 "
            "haplotype is associated with increased risk for progressive supranuclear "
            "palsy, corticobasal degeneration, and Parkinson's disease through effects "
            "on tau expression and splicing."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "17",
        "position": 44069678,
        "source": "gwas_catalog",
        "publications": ["11226185", "17052657"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs356219",
        "gene": "SNCA",
        "category": "health_risk",
        "name": "SNCA Parkinson's risk variant",
        "significance": "association",
        "description": (
            "Common variant near the alpha-synuclein gene, consistently replicated as a "
            "Parkinson's disease risk locus. May influence SNCA expression levels, "
            "contributing to alpha-synuclein aggregation and Lewy body pathology."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "4",
        "position": 90626111,
        "source": "gwas_catalog",
        "publications": ["19915575", "21738487"],
        "clinvar_stars": 0,
        "odds_ratio": 1.3,
    },
    {
        "rsid": "rs9271192",
        "gene": "HLA-DRB5",
        "category": "health_risk",
        "name": "HLA-DRB5 Alzheimer's risk variant",
        "significance": "association",
        "description": (
            "Alzheimer's disease risk locus in the HLA region. Suggests a role for "
            "immune-mediated mechanisms and neuroinflammation in Alzheimer's pathogenesis. "
            "Effect size is modest but well-replicated in large GWAS meta-analyses."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "6",
        "position": 32578530,
        "source": "gwas_catalog",
        "publications": ["23571587", "24162737"],
        "clinvar_stars": 0,
        "odds_ratio": 1.1,
    },
    {
        "rsid": "rs3764650",
        "gene": "ABCA7",
        "category": "health_risk",
        "name": "ABCA7 Alzheimer's risk variant",
        "significance": "risk_factor",
        "description": (
            "Variant in the ATP-binding cassette transporter A7 gene, involved in lipid "
            "metabolism and phagocytic clearance of amyloid-beta. Loss of ABCA7 function "
            "accelerates amyloid deposition. Risk effect may be stronger in "
            "African-American populations."
        ),
        "risk_allele": "G",
        "normal_allele": "T",
        "chromosome": "19",
        "position": 1063443,
        "source": "gwas_catalog",
        "publications": ["21460841", "23571587"],
        "clinvar_stars": 0,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs744373",
        "gene": "BIN1",
        "category": "health_risk",
        "name": "BIN1 Alzheimer's risk variant",
        "significance": "association",
        "description": (
            "Second strongest common genetic risk factor for Alzheimer's disease after APOE. "
            "BIN1 is involved in endocytosis, membrane dynamics, and tau pathology. "
            "The risk allele may increase BIN1 expression, disrupting synaptic vesicle "
            "recycling and promoting tau propagation."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "2",
        "position": 127894615,
        "source": "gwas_catalog",
        "publications": ["19734903", "23571587"],
        "clinvar_stars": 0,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs3851179",
        "gene": "PICALM",
        "category": "health_risk",
        "name": "PICALM Alzheimer's protective variant",
        "significance": "association",
        "description": (
            "Variant in the phosphatidylinositol-binding clathrin assembly protein gene. "
            "PICALM is critical for clathrin-mediated endocytosis at synapses and for "
            "amyloid-beta clearance across the blood-brain barrier. The minor allele "
            "appears protective against Alzheimer's disease."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "11",
        "position": 85868640,
        "source": "gwas_catalog",
        "publications": ["19734903", "23571587"],
        "clinvar_stars": 0,
        "odds_ratio": 0.9,
    },
    {
        "rsid": "rs11136000",
        "gene": "CLU",
        "category": "health_risk",
        "name": "CLU (clusterin) Alzheimer's protective variant",
        "significance": "association",
        "description": (
            "Variant in the clusterin (apolipoprotein J) gene. Clusterin is a chaperone "
            "protein involved in amyloid-beta clearance, complement regulation, and "
            "apoptosis. The minor allele is associated with reduced Alzheimer's risk, "
            "possibly by enhancing amyloid clearance."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "8",
        "position": 27464519,
        "source": "gwas_catalog",
        "publications": ["19734903", "21460841"],
        "clinvar_stars": 0,
        "odds_ratio": 0.9,
    },
    {
        "rsid": "rs165932",
        "gene": "PSEN1",
        "category": "health_risk",
        "name": "PSEN1 intronic polymorphism",
        "significance": "association",
        "description": (
            "Common intronic variant in presenilin-1, a catalytic subunit of the "
            "gamma-secretase complex that cleaves amyloid precursor protein. While "
            "rare PSEN1 coding mutations cause early-onset familial Alzheimer's, this "
            "common polymorphism has been studied for modest late-onset AD associations."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "14",
        "position": 73653568,
        "source": "gwas_catalog",
        "publications": ["10867782", "12915468"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs63750264",
        "gene": "PSEN1",
        "category": "health_risk",
        "name": "PSEN1 A79V (early-onset Alzheimer's)",
        "significance": "likely_pathogenic",
        "description": (
            "Missense variant in presenilin-1 associated with early-onset familial "
            "Alzheimer's disease. Alters gamma-secretase function, shifting the ratio "
            "of amyloid-beta 42/40 peptides and promoting amyloid plaque formation. "
            "Onset typically in the 50s-60s."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "14",
        "position": 73653568,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000067516"},
        "publications": ["8577393", "9462980"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1800977",
        "gene": "ABCA1",
        "category": "health_risk",
        "name": "ABCA1 promoter variant (cholesterol/neuro)",
        "significance": "association",
        "description": (
            "Promoter variant in the ATP-binding cassette transporter A1 gene, a key "
            "regulator of cholesterol efflux and HDL biogenesis. In the brain, ABCA1 "
            "modulates apoE lipidation and amyloid-beta metabolism. Studied for "
            "associations with both cardiovascular disease and Alzheimer's."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "9",
        "position": 107583466,
        "source": "gwas_catalog",
        "publications": ["12835591", "17241179"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs6656401",
        "gene": "CR1",
        "category": "health_risk",
        "name": "CR1 Alzheimer's risk variant",
        "significance": "association",
        "description": (
            "Variant in complement receptor 1, a protein that mediates immune complex "
            "clearance and complement regulation. CR1 is expressed on erythrocytes and "
            "in the brain, where it may influence amyloid-beta clearance through "
            "complement-dependent mechanisms."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "1",
        "position": 207692049,
        "source": "gwas_catalog",
        "publications": ["19734903", "21460841"],
        "clinvar_stars": 0,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs2075650",
        "gene": "TOMM40",
        "category": "health_risk",
        "name": "TOMM40 Alzheimer's/longevity variant",
        "significance": "association",
        "description": (
            "Variant in the translocase of outer mitochondrial membrane 40 gene, located "
            "adjacent to APOE on chromosome 19. Strong linkage disequilibrium with APOE "
            "e4 makes independent effect assessment challenging. May influence "
            "mitochondrial function, Alzheimer's onset age, and longevity."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "19",
        "position": 45395619,
        "source": "gwas_catalog",
        "publications": ["19734903", "20061627"],
        "clinvar_stars": 0,
        "odds_ratio": 1.5,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # ---- rs34637584 LRRK2 G2019S ----
    {
        "rsid": "rs34637584",
        "genotype": "GG",
        "interpretation": "No LRRK2 G2019S mutation. Typical Parkinson's risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs34637584",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous LRRK2 G2019S carrier. Significantly increased Parkinson's "
            "disease risk with age-dependent penetrance (~30-75% by age 80)."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs34637584",
        "genotype": "AA",
        "interpretation": (
            "Homozygous LRRK2 G2019S. Very high Parkinson's disease risk; clinical "
            "presentation similar to heterozygous carriers."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs76763715 GBA N370S ----
    {
        "rsid": "rs76763715",
        "genotype": "GG",
        "interpretation": "No GBA N370S mutation. Typical risk for Parkinson's from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs76763715",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous GBA N370S carrier. ~5x increased Parkinson's risk; carrier "
            "for Gaucher disease (autosomal recessive)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs76763715",
        "genotype": "AA",
        "interpretation": (
            "Homozygous GBA N370S. Gaucher disease type 1; substantially elevated "
            "Parkinson's disease risk."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs6265 BDNF Val66Met ----
    {
        "rsid": "rs6265",
        "genotype": "CC",
        "interpretation": "BDNF Val/Val (wild-type). Normal activity-dependent BDNF secretion.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs6265",
        "genotype": "CT",
        "interpretation": (
            "BDNF Val/Met. Modestly reduced BDNF secretion; associated with subtle "
            "changes in hippocampal function and memory."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs6265",
        "genotype": "TT",
        "interpretation": (
            "BDNF Met/Met. Reduced activity-dependent BDNF secretion; associated with "
            "lower hippocampal volume and increased susceptibility to stress-related disorders."
        ),
        "risk_level": "increased_risk",
    },
    # ---- rs1800547 MAPT H1/H2 ----
    {
        "rsid": "rs1800547",
        "genotype": "AA",
        "interpretation": "MAPT H1/H1 haplotype. Increased risk for tauopathies (PSP, CBD, PD).",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1800547",
        "genotype": "AG",
        "interpretation": "MAPT H1/H2 haplotype. Intermediate tauopathy risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800547",
        "genotype": "GG",
        "interpretation": (
            "MAPT H2/H2 haplotype. Reduced risk for progressive supranuclear palsy and related "
            "tauopathies."
        ),
        "risk_level": "normal",
    },
    # ---- rs356219 SNCA ----
    {
        "rsid": "rs356219",
        "genotype": "AA",
        "interpretation": "No SNCA risk alleles at this locus. Typical Parkinson's risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs356219",
        "genotype": "AG",
        "interpretation": "One SNCA Parkinson's risk allele. Modestly elevated risk (~1.3x).",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs356219",
        "genotype": "GG",
        "interpretation": "Two SNCA risk alleles. Mildly increased Parkinson's risk.",
        "risk_level": "increased_risk",
    },
    # ---- rs9271192 HLA-DRB5 ----
    {
        "rsid": "rs9271192",
        "genotype": "TT",
        "interpretation": "No HLA-DRB5 Alzheimer's risk alleles.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs9271192",
        "genotype": "CT",
        "interpretation": "One HLA-DRB5 Alzheimer's risk allele. Small increase in risk (~1.1x).",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs9271192",
        "genotype": "CC",
        "interpretation": "Two HLA-DRB5 risk alleles. Modestly increased Alzheimer's risk.",
        "risk_level": "increased_risk",
    },
    # ---- rs3764650 ABCA7 ----
    {
        "rsid": "rs3764650",
        "genotype": "TT",
        "interpretation": "No ABCA7 Alzheimer's risk alleles.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3764650",
        "genotype": "GT",
        "interpretation": "One ABCA7 risk allele. Slightly increased Alzheimer's risk (~1.2x).",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs3764650",
        "genotype": "GG",
        "interpretation": "Two ABCA7 risk alleles. Modestly increased Alzheimer's risk.",
        "risk_level": "increased_risk",
    },
    # ---- rs744373 BIN1 ----
    {
        "rsid": "rs744373",
        "genotype": "TT",
        "interpretation": "No BIN1 Alzheimer's risk alleles.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs744373",
        "genotype": "CT",
        "interpretation": "One BIN1 risk allele. Modestly increased Alzheimer's risk (~1.2x).",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs744373",
        "genotype": "CC",
        "interpretation": "Two BIN1 risk alleles. Increased Alzheimer's risk.",
        "risk_level": "increased_risk",
    },
    # ---- rs3851179 PICALM ----
    {
        "rsid": "rs3851179",
        "genotype": "CC",
        "interpretation": "PICALM common genotype. Typical Alzheimer's risk at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3851179",
        "genotype": "CT",
        "interpretation": "One PICALM protective allele. Slightly reduced Alzheimer's risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3851179",
        "genotype": "TT",
        "interpretation": (
            "Two PICALM protective alleles. Modestly reduced Alzheimer's risk (OR ~0.9)."
        ),
        "risk_level": "normal",
    },
    # ---- rs11136000 CLU ----
    {
        "rsid": "rs11136000",
        "genotype": "CC",
        "interpretation": "CLU common genotype. Typical Alzheimer's risk at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs11136000",
        "genotype": "CT",
        "interpretation": "One CLU protective allele. Slightly reduced Alzheimer's risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs11136000",
        "genotype": "TT",
        "interpretation": (
            "Two CLU protective alleles. Modestly reduced Alzheimer's risk (OR ~0.9)."
        ),
        "risk_level": "normal",
    },
    # ---- rs165932 PSEN1 polymorphism ----
    {
        "rsid": "rs165932",
        "genotype": "GG",
        "interpretation": "PSEN1 common intronic genotype. No significant effect reported.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs165932",
        "genotype": "GT",
        "interpretation": "Heterozygous PSEN1 intronic variant. No clear clinical significance.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs165932",
        "genotype": "TT",
        "interpretation": "Homozygous PSEN1 intronic variant. Studied for modest AD association.",
        "risk_level": "carrier",
    },
    # ---- rs63750264 PSEN1 A79V ----
    {
        "rsid": "rs63750264",
        "genotype": "CC",
        "interpretation": "No PSEN1 A79V mutation. Typical Alzheimer's risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs63750264",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous PSEN1 A79V. Likely pathogenic for early-onset Alzheimer's "
            "disease (autosomal dominant). Genetic counseling recommended."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs63750264",
        "genotype": "TT",
        "interpretation": (
            "Homozygous PSEN1 A79V. Likely pathogenic for early-onset Alzheimer's "
            "disease. Very rare genotype; genetic counseling strongly recommended."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs1800977 ABCA1 ----
    {
        "rsid": "rs1800977",
        "genotype": "CC",
        "interpretation": "ABCA1 common promoter genotype. Typical cholesterol efflux activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800977",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous ABCA1 promoter variant. Studied for lipid and neurodegeneration "
            "associations."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800977",
        "genotype": "TT",
        "interpretation": (
            "Homozygous ABCA1 promoter variant. May modestly influence HDL and brain cholesterol "
            "metabolism."
        ),
        "risk_level": "carrier",
    },
    # ---- rs6656401 CR1 ----
    {
        "rsid": "rs6656401",
        "genotype": "GG",
        "interpretation": "No CR1 Alzheimer's risk alleles.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs6656401",
        "genotype": "AG",
        "interpretation": "One CR1 risk allele. Modestly increased Alzheimer's risk (~1.2x).",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs6656401",
        "genotype": "AA",
        "interpretation": (
            "Two CR1 risk alleles. Increased Alzheimer's risk via complement pathway."
        ),
        "risk_level": "increased_risk",
    },
    # ---- rs2075650 TOMM40 ----
    {
        "rsid": "rs2075650",
        "genotype": "AA",
        "interpretation": (
            "No TOMM40 risk alleles. Typical Alzheimer's/longevity profile at this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs2075650",
        "genotype": "AG",
        "interpretation": (
            "One TOMM40 risk allele. Moderately increased Alzheimer's risk (~1.5x); "
            "in strong LD with APOE e4."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2075650",
        "genotype": "GG",
        "interpretation": (
            "Two TOMM40 risk alleles. Elevated Alzheimer's risk; likely reflects "
            "APOE e4 homozygosity due to linkage disequilibrium."
        ),
        "risk_level": "high_risk",
    },
]
