"""Immune system health risk variants: HLA tags, CTLA4, IL23R, NOD2, CFTR, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    {
        "rsid": "rs2476601",
        "gene": "PTPN22",
        "category": "health_risk",
        "name": "PTPN22 R620W (autoimmune risk)",
        "significance": "risk_factor",
        "description": (
            "Missense variant in protein tyrosine phosphatase non-receptor type 22, "
            "a key regulator of T-cell and B-cell receptor signaling. The W620 allele "
            "is a gain-of-function variant that increases risk for multiple autoimmune "
            "diseases including type 1 diabetes, rheumatoid arthritis, SLE, and "
            "autoimmune thyroid disease."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "1",
        "position": 114377568,
        "source": "clinvar",
        "publications": ["15208781", "17554300"],
        "clinvar_stars": 2,
        "odds_ratio": 1.8,
    },
    {
        "rsid": "rs3087243",
        "gene": "CTLA4",
        "category": "health_risk",
        "name": "CTLA4 +49A/G (autoimmune risk)",
        "significance": "risk_factor",
        "description": (
            "Variant in cytotoxic T-lymphocyte associated protein 4, a critical negative "
            "regulator of T-cell activation. The risk allele reduces CTLA-4 surface "
            "expression, impairing immune checkpoint function and predisposing to "
            "autoimmune disorders including Graves' disease, T1D, and autoimmune thyroiditis."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "2",
        "position": 204738919,
        "source": "clinvar",
        "publications": ["12724780", "14985372"],
        "clinvar_stars": 0,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs11209026",
        "gene": "IL23R",
        "category": "health_risk",
        "name": "IL23R R381Q (IBD protective)",
        "significance": "association",
        "description": (
            "Protective missense variant in interleukin-23 receptor. The Q381 allele "
            "reduces IL-23-driven Th17 inflammatory responses, conferring strong "
            "protection against Crohn's disease, ulcerative colitis, psoriasis, and "
            "ankylosing spondylitis. One of few well-characterized protective variants "
            "in inflammatory disease."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "1",
        "position": 67705958,
        "source": "gwas_catalog",
        "publications": ["17068223", "17554261"],
        "clinvar_stars": 0,
        "odds_ratio": 0.7,
    },
    {
        "rsid": "rs2066844",
        "gene": "NOD2",
        "category": "health_risk",
        "name": "NOD2 R702W (Crohn's disease)",
        "significance": "risk_factor",
        "description": (
            "Missense variant in nucleotide-binding oligomerization domain 2, an "
            "intracellular innate immune receptor for bacterial muramyl dipeptide. "
            "One of three NOD2 variants strongly associated with Crohn's disease. "
            "Impairs NF-kB signaling in response to bacterial products in the gut."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "16",
        "position": 50745926,
        "source": "clinvar",
        "publications": ["11385577", "11907752"],
        "clinvar_stars": 2,
        "odds_ratio": 2.2,
    },
    {
        "rsid": "rs2066845",
        "gene": "NOD2",
        "category": "health_risk",
        "name": "NOD2 G908R (Crohn's disease)",
        "significance": "risk_factor",
        "description": (
            "Missense variant in the leucine-rich repeat region of NOD2. Second major "
            "Crohn's disease susceptibility allele. Disrupts bacterial peptidoglycan "
            "sensing and downstream NF-kB and autophagy pathways important for "
            "intestinal innate immunity."
        ),
        "risk_allele": "C",
        "normal_allele": "G",
        "chromosome": "16",
        "position": 50756540,
        "source": "clinvar",
        "publications": ["11385577", "11907752"],
        "clinvar_stars": 2,
        "odds_ratio": 3.0,
    },
    {
        "rsid": "rs2066847",
        "gene": "NOD2",
        "category": "health_risk",
        "name": "NOD2 1007fs (Crohn's disease)",
        "significance": "pathogenic",
        "description": (
            "Frameshift insertion (Leu1007fsinsC) in NOD2 causing a truncated protein. "
            "The strongest individual genetic risk factor for Crohn's disease. "
            "Homozygosity or compound heterozygosity with other NOD2 variants confers "
            "up to 40-fold increased Crohn's risk."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "16",
        "position": 50763778,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000005302"},
        "publications": ["11385577", "11907752"],
        "clinvar_stars": 3,
        "odds_ratio": 4.0,
    },
    {
        "rsid": "rs75527207",
        "gene": "CFTR",
        "category": "health_risk",
        "name": "CFTR F508del (cystic fibrosis)",
        "significance": "pathogenic",
        "description": (
            "Most common cystic fibrosis mutation worldwide, accounting for ~70% of CF "
            "alleles. The deletion of phenylalanine at position 508 causes CFTR protein "
            "misfolding, ER retention, and degradation. Amenable to treatment with "
            "elexacaftor/tezacaftor/ivacaftor (Trikafta)."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "7",
        "position": 117199646,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000007105"},
        "publications": ["2475911", "31634902"],
        "clinvar_stars": 4,
        "odds_ratio": None,
    },
    {
        "rsid": "rs113993960",
        "gene": "CFTR",
        "category": "health_risk",
        "name": "CFTR deltaF508 tag SNP",
        "significance": "pathogenic",
        "description": (
            "Tag variant for the CFTR F508del mutation. Used in genotyping arrays as a "
            "surrogate marker for the deltaF508 deletion. Homozygosity indicates cystic "
            "fibrosis; heterozygous carriers have ~1:25 frequency in European populations."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "7",
        "position": 117199644,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000007105"},
        "publications": ["2475911"],
        "clinvar_stars": 4,
        "odds_ratio": None,
    },
    {
        "rsid": "rs6457620",
        "gene": "HLA-DQB1",
        "category": "health_risk",
        "name": "HLA-DQB1 type 1 diabetes risk tag",
        "significance": "risk_factor",
        "description": (
            "Tag SNP for HLA-DQB1 haplotypes associated with type 1 diabetes "
            "susceptibility. The HLA class II region on chromosome 6p21 accounts for "
            "~50% of genetic risk for T1D through effects on self-antigen presentation "
            "to CD4+ T cells."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "6",
        "position": 32658534,
        "source": "gwas_catalog",
        "publications": ["17554260", "19430480"],
        "clinvar_stars": 0,
        "odds_ratio": 2.0,
    },
    {
        "rsid": "rs9275596",
        "gene": "HLA-DQB1",
        "category": "health_risk",
        "name": "HLA-DQB1 celiac disease risk tag",
        "significance": "risk_factor",
        "description": (
            "Tag SNP in the HLA-DQB1 region associated with celiac disease risk. "
            "Celiac disease requires HLA-DQ2 or HLA-DQ8 for gluten peptide presentation "
            "to T cells. This variant tags high-risk HLA haplotypes in GWAS analyses."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "6",
        "position": 32680928,
        "source": "gwas_catalog",
        "publications": ["20190752", "22057235"],
        "clinvar_stars": 0,
        "odds_ratio": 2.5,
    },
    {
        "rsid": "rs2187668",
        "gene": "HLA-DQ2.5",
        "category": "health_risk",
        "name": "HLA-DQ2.5 (celiac disease)",
        "significance": "risk_factor",
        "description": (
            "Tag SNP for the HLA-DQ2.5 haplotype (DQA1*05:01/DQB1*02:01), present in "
            "~90-95% of celiac disease patients vs ~20-30% of the general European "
            "population. HLA-DQ2.5 is necessary but not sufficient for celiac disease; "
            "it presents deamidated gluten peptides to CD4+ T cells."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "6",
        "position": 32713862,
        "source": "clinvar",
        "publications": ["18311140", "20190752"],
        "clinvar_stars": 2,
        "odds_ratio": 7.0,
    },
    {
        "rsid": "rs7454108",
        "gene": "HLA-DQ8",
        "category": "health_risk",
        "name": "HLA-DQ8 tag (celiac/T1D)",
        "significance": "risk_factor",
        "description": (
            "Tag SNP for the HLA-DQ8 haplotype (DQA1*03:01/DQB1*03:02), the second "
            "major HLA risk factor for celiac disease and a primary risk factor for "
            "type 1 diabetes. Present in ~5-10% of celiac patients who lack DQ2.5."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "6",
        "position": 32681277,
        "source": "gwas_catalog",
        "publications": ["18311140", "19430480"],
        "clinvar_stars": 0,
        "odds_ratio": 3.0,
    },
    {
        "rsid": "rs3135388",
        "gene": "HLA-DRB1",
        "category": "health_risk",
        "name": "HLA-DRB1*15:01 tag (multiple sclerosis)",
        "significance": "risk_factor",
        "description": (
            "Tag SNP for HLA-DRB1*15:01, the strongest genetic risk factor for "
            "multiple sclerosis. This allele is present in ~25-30% of MS patients vs "
            "~15% of controls in European populations. Mediates autoimmune attack on "
            "myelin through aberrant antigen presentation."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "6",
        "position": 32556547,
        "source": "gwas_catalog",
        "publications": ["17660530", "21833088"],
        "clinvar_stars": 0,
        "odds_ratio": 3.0,
    },
    {
        "rsid": "rs9268645",
        "gene": "HLA-DRB1",
        "category": "health_risk",
        "name": "HLA-DRB1 rheumatoid arthritis risk tag",
        "significance": "risk_factor",
        "description": (
            "Tag SNP for HLA-DRB1 shared epitope alleles, the strongest genetic risk "
            "factor for seropositive rheumatoid arthritis. The shared epitope is a "
            "conserved amino acid sequence in the HLA-DRB1 peptide-binding groove that "
            "influences citrullinated peptide presentation."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "6",
        "position": 32589792,
        "source": "gwas_catalog",
        "publications": ["24390342", "20453842"],
        "clinvar_stars": 0,
        "odds_ratio": 2.5,
    },
    {
        "rsid": "rs1800896",
        "gene": "IL10",
        "category": "health_risk",
        "name": "IL10 -1082G/A (inflammation modulator)",
        "significance": "association",
        "description": (
            "Promoter variant in interleukin-10, a critical anti-inflammatory cytokine. "
            "The -1082G allele is associated with higher IL-10 production and has been "
            "studied in context of inflammatory bowel disease, transplant outcomes, "
            "susceptibility to infections, and cancer risk."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "1",
        "position": 206946897,
        "source": "gwas_catalog",
        "publications": ["9042556", "14603253"],
        "clinvar_stars": 0,
        "odds_ratio": 1.2,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # ---- rs2476601 PTPN22 R620W ----
    {
        "rsid": "rs2476601",
        "genotype": "GG",
        "interpretation": "No PTPN22 R620W variant. Typical autoimmune risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2476601",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous PTPN22 R620W carrier. ~1.8x increased risk for multiple "
            "autoimmune conditions (T1D, RA, SLE, thyroid)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2476601",
        "genotype": "AA",
        "interpretation": (
            "Homozygous PTPN22 R620W. Substantially increased autoimmune risk; "
            "particularly elevated for rheumatoid arthritis and type 1 diabetes."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs3087243 CTLA4 ----
    {
        "rsid": "rs3087243",
        "genotype": "AA",
        "interpretation": "No CTLA4 risk alleles. Typical immune checkpoint regulation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3087243",
        "genotype": "AG",
        "interpretation": "One CTLA4 risk allele. Slightly increased autoimmune risk (~1.2x).",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs3087243",
        "genotype": "GG",
        "interpretation": (
            "Two CTLA4 risk alleles. Modestly increased autoimmune risk, "
            "particularly for Graves' disease and T1D."
        ),
        "risk_level": "increased_risk",
    },
    # ---- rs11209026 IL23R R381Q ----
    {
        "rsid": "rs11209026",
        "genotype": "GG",
        "interpretation": "IL23R common genotype. Typical inflammatory bowel disease risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs11209026",
        "genotype": "AG",
        "interpretation": (
            "One IL23R protective allele (R381Q). Reduced risk for Crohn's, "
            "ulcerative colitis, and psoriasis (OR ~0.7)."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs11209026",
        "genotype": "AA",
        "interpretation": (
            "Homozygous IL23R R381Q. Strong protection against inflammatory bowel "
            "disease and psoriasis. Reduced Th17 inflammatory signaling."
        ),
        "risk_level": "normal",
    },
    # ---- rs2066844 NOD2 R702W ----
    {
        "rsid": "rs2066844",
        "genotype": "CC",
        "interpretation": "No NOD2 R702W variant. Typical Crohn's disease risk from this allele.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2066844",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous NOD2 R702W carrier. ~2.2x increased Crohn's disease risk. "
            "Check for compound heterozygosity with other NOD2 variants."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2066844",
        "genotype": "TT",
        "interpretation": (
            "Homozygous NOD2 R702W. Substantially increased Crohn's disease risk. "
            "Impaired bacterial peptidoglycan sensing in the gut."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs2066845 NOD2 G908R ----
    {
        "rsid": "rs2066845",
        "genotype": "GG",
        "interpretation": "No NOD2 G908R variant. Typical Crohn's disease risk from this allele.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2066845",
        "genotype": "GC",
        "interpretation": (
            "Heterozygous NOD2 G908R carrier. ~3x increased Crohn's disease risk. "
            "Check for compound heterozygosity with other NOD2 variants."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2066845",
        "genotype": "CC",
        "interpretation": (
            "Homozygous NOD2 G908R. High Crohn's disease risk. "
            "Significant impairment of innate immune sensing in the gut."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs2066847 NOD2 1007fs ----
    {
        "rsid": "rs2066847",
        "genotype": "wt/wt",
        "interpretation": (
            "No NOD2 1007fs frameshift. Typical Crohn's disease risk from this allele."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs2066847",
        "genotype": "wt/ins",
        "interpretation": (
            "Heterozygous NOD2 1007fs carrier. ~4x increased Crohn's disease risk. "
            "Check for compound heterozygosity with other NOD2 variants (R702W, G908R)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2066847",
        "genotype": "ins/ins",
        "interpretation": (
            "Homozygous NOD2 1007fs. Very high Crohn's disease risk (~40x with compound "
            "heterozygosity). Truncated NOD2 protein with abolished bacterial sensing."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs75527207 CFTR F508del ----
    {
        "rsid": "rs75527207",
        "genotype": "wt/wt",
        "interpretation": "No CFTR F508del mutation. Not a cystic fibrosis carrier at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs75527207",
        "genotype": "wt/del",
        "interpretation": (
            "Heterozygous CFTR F508del carrier. No cystic fibrosis but carrier status "
            "relevant for family planning (~1:25 carrier frequency in Europeans)."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs75527207",
        "genotype": "del/del",
        "interpretation": (
            "Homozygous CFTR F508del. Cystic fibrosis. Eligible for Trikafta "
            "(elexacaftor/tezacaftor/ivacaftor) modulator therapy."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs113993960 CFTR deltaF508 tag ----
    {
        "rsid": "rs113993960",
        "genotype": "wt/wt",
        "interpretation": "No CFTR deltaF508 tag variant detected. Not a carrier at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs113993960",
        "genotype": "wt/del",
        "interpretation": (
            "Heterozygous CFTR deltaF508 tag carrier. Carrier status for cystic "
            "fibrosis; relevant for reproductive counseling."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs113993960",
        "genotype": "del/del",
        "interpretation": (
            "Homozygous CFTR deltaF508 tag. Consistent with cystic fibrosis diagnosis. "
            "Confirm with clinical CFTR panel and sweat chloride test."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs6457620 HLA-DQB1 T1D ----
    {
        "rsid": "rs6457620",
        "genotype": "CC",
        "interpretation": "No HLA-DQB1 T1D risk alleles at this tag SNP.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs6457620",
        "genotype": "CT",
        "interpretation": (
            "One HLA-DQB1 T1D risk allele. Moderately increased type 1 diabetes risk (~2x)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs6457620",
        "genotype": "TT",
        "interpretation": (
            "Two HLA-DQB1 T1D risk alleles. Elevated type 1 diabetes risk; "
            "HLA typing recommended for definitive haplotype assessment."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs9275596 HLA-DQB1 celiac ----
    {
        "rsid": "rs9275596",
        "genotype": "TT",
        "interpretation": "No HLA-DQB1 celiac risk alleles at this tag SNP.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs9275596",
        "genotype": "CT",
        "interpretation": (
            "One HLA-DQB1 celiac risk allele. Increased celiac disease susceptibility (~2.5x)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs9275596",
        "genotype": "CC",
        "interpretation": (
            "Two HLA-DQB1 celiac risk alleles. High celiac disease risk; "
            "consider serological screening (tTG-IgA) if symptomatic."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs2187668 HLA-DQ2.5 celiac ----
    {
        "rsid": "rs2187668",
        "genotype": "CC",
        "interpretation": "No HLA-DQ2.5 risk alleles. Very low celiac disease probability.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2187668",
        "genotype": "CT",
        "interpretation": (
            "One HLA-DQ2.5 allele. Present in ~90% of celiac patients; necessary "
            "but not sufficient for disease. ~3% of carriers develop celiac disease."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2187668",
        "genotype": "TT",
        "interpretation": (
            "Homozygous HLA-DQ2.5. Highest genetic risk for celiac disease (OR ~7). "
            "Serological screening strongly recommended if GI symptoms present."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs7454108 HLA-DQ8 ----
    {
        "rsid": "rs7454108",
        "genotype": "TT",
        "interpretation": "No HLA-DQ8 risk alleles. Lower celiac/T1D risk from this haplotype.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs7454108",
        "genotype": "CT",
        "interpretation": (
            "One HLA-DQ8 risk allele. Increased risk for celiac disease and type 1 diabetes (~3x)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs7454108",
        "genotype": "CC",
        "interpretation": (
            "Homozygous HLA-DQ8. Elevated celiac and T1D risk. "
            "Particularly relevant if DQ2.5-negative celiac disease is suspected."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs3135388 HLA-DRB1*15:01 MS ----
    {
        "rsid": "rs3135388",
        "genotype": "GG",
        "interpretation": (
            "No HLA-DRB1*15:01 tag alleles. Lower multiple sclerosis risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs3135388",
        "genotype": "AG",
        "interpretation": (
            "One HLA-DRB1*15:01 tag allele. ~3x increased multiple sclerosis risk; "
            "the strongest common genetic risk factor for MS."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs3135388",
        "genotype": "AA",
        "interpretation": (
            "Homozygous HLA-DRB1*15:01 tag. High multiple sclerosis risk (~6x). "
            "HLA typing recommended for definitive allele confirmation."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs9268645 HLA-DRB1 RA ----
    {
        "rsid": "rs9268645",
        "genotype": "CC",
        "interpretation": "No HLA-DRB1 shared epitope tag alleles. Lower RA risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs9268645",
        "genotype": "CG",
        "interpretation": (
            "One HLA-DRB1 RA risk allele. ~2.5x increased seropositive rheumatoid "
            "arthritis risk; check anti-CCP antibodies if joint symptoms present."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs9268645",
        "genotype": "GG",
        "interpretation": (
            "Homozygous HLA-DRB1 RA risk tag. High seropositive rheumatoid arthritis "
            "risk. Shared epitope homozygosity associated with more severe disease course."
        ),
        "risk_level": "high_risk",
    },
    # ---- rs1800896 IL10 ----
    {
        "rsid": "rs1800896",
        "genotype": "CC",
        "interpretation": (
            "IL10 -1082A/A genotype. Lower IL-10 production; may have heightened inflammatory "
            "responses."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1800896",
        "genotype": "CT",
        "interpretation": "IL10 -1082G/A genotype. Intermediate IL-10 production.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800896",
        "genotype": "TT",
        "interpretation": (
            "IL10 -1082G/G genotype. Higher IL-10 production; generally stronger "
            "anti-inflammatory capacity."
        ),
        "risk_level": "normal",
    },
]
