"""Pharmacogenomics CYP enzyme variants: CYP2C9, CYP2C19, CYP2D6, CYP3A5, CYP1A2, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    {
        "rsid": "rs1799853",
        "gene": "CYP2C9",
        "category": "pharmacogenomics",
        "name": "CYP2C9*2 (warfarin metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP2C9*2 allele reduces warfarin metabolism to ~12% of wild-type activity. "
            "Carriers require lower warfarin doses to avoid bleeding complications."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "10",
        "position": 96702047,
        "source": "pharmgkb",
        "publications": ["9399854", "19794411"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1057910",
        "gene": "CYP2C9",
        "category": "pharmacogenomics",
        "name": "CYP2C9*3 (warfarin metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP2C9*3 allele reduces warfarin metabolism to ~5% of wild-type activity. "
            "Stronger effect than *2; carriers need significantly lower warfarin doses."
        ),
        "risk_allele": "C",
        "normal_allele": "A",
        "chromosome": "10",
        "position": 96741053,
        "source": "pharmgkb",
        "publications": ["9399854"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4244285",
        "gene": "CYP2C19",
        "category": "pharmacogenomics",
        "name": "CYP2C19*2 (clopidogrel metabolism)",
        "significance": "drug_response",
        "description": (
            "Most common CYP2C19 loss-of-function allele. Carriers have reduced "
            "activation of clopidogrel, leading to decreased antiplatelet effect "
            "and higher cardiovascular risk."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "10",
        "position": 96541616,
        "source": "pharmgkb",
        "publications": ["20802479"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4986893",
        "gene": "CYP2C19",
        "category": "pharmacogenomics",
        "name": "CYP2C19*3 (clopidogrel metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP2C19 loss-of-function allele, more common in East Asian populations. "
            "Creates a premature stop codon, abolishing enzyme activity."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "10",
        "position": 96540410,
        "source": "pharmgkb",
        "publications": ["20802479"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs12248560",
        "gene": "CYP2C19",
        "category": "pharmacogenomics",
        "name": "CYP2C19*17 (ultra-rapid metabolizer)",
        "significance": "drug_response",
        "description": (
            "CYP2C19 gain-of-function allele. Carriers are ultra-rapid metabolizers, "
            "potentially requiring higher doses of drugs like clopidogrel and PPIs."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "10",
        "position": 96521657,
        "source": "pharmgkb",
        "publications": ["17164811"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs762551",
        "gene": "CYP1A2",
        "category": "pharmacogenomics",
        "name": "CYP1A2*1F (caffeine metabolism)",
        "significance": "drug_response",
        "description": (
            "Determines caffeine metabolism speed. AA genotype = fast metabolizer "
            "(rapid caffeine clearance). AC/CC = slow metabolizer (prolonged effects). "
            "Also affects metabolism of theophylline and some antipsychotics."
        ),
        "risk_allele": "C",
        "normal_allele": "A",
        "chromosome": "15",
        "position": 75041917,
        "source": "pharmgkb",
        "publications": ["22578330"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # --- NEW CYP2D6 variants ---
    {
        "rsid": "rs16947",
        "gene": "CYP2D6",
        "category": "pharmacogenomics",
        "name": "CYP2D6*2 (codeine/tamoxifen metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP2D6*2 allele associated with normal to increased enzyme function. "
            "Relevant to codeine activation to morphine and tamoxifen activation "
            "to endoxifen. Copy number changes may further alter metabolizer status."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "22",
        "position": 42523805,
        "source": "pharmgkb",
        "publications": ["16958828"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs3892097",
        "gene": "CYP2D6",
        "category": "pharmacogenomics",
        "name": "CYP2D6*4 (poor metabolizer)",
        "significance": "drug_response",
        "description": (
            "Most common non-functional CYP2D6 allele in Europeans (~20% allele "
            "frequency). Splicing defect abolishes enzyme activity. Homozygotes are "
            "poor metabolizers of codeine, tramadol, tamoxifen, and many antidepressants."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "22",
        "position": 42524947,
        "source": "pharmgkb",
        "publications": ["16958828", "17301693"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs5030655",
        "gene": "CYP2D6",
        "category": "pharmacogenomics",
        "name": "CYP2D6*6 (poor metabolizer)",
        "significance": "drug_response",
        "description": (
            "CYP2D6*6 allele contains a single-base deletion causing a frameshift. "
            "Results in non-functional enzyme. Carriers have reduced capacity to "
            "metabolize CYP2D6 substrates including codeine and antidepressants."
        ),
        "risk_allele": "A",
        "normal_allele": "T",
        "chromosome": "22",
        "position": 42524244,
        "source": "pharmgkb",
        "publications": ["16958828"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1065852",
        "gene": "CYP2D6",
        "category": "pharmacogenomics",
        "name": "CYP2D6*10 (reduced function)",
        "significance": "drug_response",
        "description": (
            "CYP2D6*10 allele causing Pro34Ser substitution with reduced but not "
            "absent enzyme activity. Most common reduced-function allele in East "
            "Asian populations (~40% allele frequency). Affects codeine and tamoxifen."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "22",
        "position": 42526694,
        "source": "pharmgkb",
        "publications": ["11668218"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs28371725",
        "gene": "CYP2D6",
        "category": "pharmacogenomics",
        "name": "CYP2D6*41 (reduced function)",
        "significance": "drug_response",
        "description": (
            "CYP2D6*41 allele causing reduced enzyme expression through aberrant "
            "splicing. Carriers have decreased metabolism of CYP2D6 substrates. "
            "Common in Middle Eastern and North African populations."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "22",
        "position": 42523610,
        "source": "pharmgkb",
        "publications": ["12815606"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # --- NEW CYP3A5 / CYP3A4 variants ---
    {
        "rsid": "rs776746",
        "gene": "CYP3A5",
        "category": "pharmacogenomics",
        "name": "CYP3A5*3 (tacrolimus metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP3A5*3 allele causes a splicing defect leading to absent CYP3A5 "
            "expression. Non-expressors (*3/*3) require lower tacrolimus doses. "
            "~85-95% of Europeans are CYP3A5 non-expressors."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "7",
        "position": 99270539,
        "source": "pharmgkb",
        "publications": ["11668219", "20101188"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs2032582",
        "gene": "CYP3A4",
        "category": "pharmacogenomics",
        "name": "CYP3A4*1B (midazolam metabolism)",
        "significance": "drug_response",
        "description": (
            "Promoter variant in CYP3A4 associated with altered expression. May "
            "affect metabolism of midazolam, cyclosporine, and other CYP3A4 "
            "substrates. Clinical significance is moderate and context-dependent."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "7",
        "position": 99361466,
        "source": "pharmgkb",
        "publications": ["11038293"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs2242480",
        "gene": "CYP3A4",
        "category": "pharmacogenomics",
        "name": "CYP3A4*1G (drug metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP3A4*1G intronic variant common in East Asian populations. Associated "
            "with altered metabolism of fentanyl, tacrolimus, and other CYP3A4 "
            "substrates. May influence dose requirements for immunosuppressants."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "7",
        "position": 99358524,
        "source": "pharmgkb",
        "publications": ["15514072"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # --- NEW CYP2B6 variants ---
    {
        "rsid": "rs3745274",
        "gene": "CYP2B6",
        "category": "pharmacogenomics",
        "name": "CYP2B6*6 (efavirenz metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP2B6*6 allele with Gln172His substitution causing reduced enzyme "
            "activity. Carriers have elevated efavirenz plasma levels, increasing "
            "risk of CNS side effects. Dose reduction may be needed for HIV treatment."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "19",
        "position": 41512841,
        "source": "pharmgkb",
        "publications": ["16220112", "17192773"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs28399504",
        "gene": "CYP2B6",
        "category": "pharmacogenomics",
        "name": "CYP2B6*4 (efavirenz metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP2B6*4 allele associated with increased enzyme activity. Carriers "
            "may have lower efavirenz plasma levels and potentially reduced "
            "antiretroviral efficacy at standard doses."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "19",
        "position": 41515263,
        "source": "pharmgkb",
        "publications": ["17192773"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs28399499",
        "gene": "CYP2B6",
        "category": "pharmacogenomics",
        "name": "CYP2B6*18 (efavirenz metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP2B6*18 allele predominantly found in African populations. Causes "
            "severely reduced enzyme activity, leading to markedly elevated efavirenz "
            "plasma concentrations and increased risk of neuropsychiatric toxicity."
        ),
        "risk_allele": "G",
        "normal_allele": "T",
        "chromosome": "19",
        "position": 41497274,
        "source": "pharmgkb",
        "publications": ["17192773"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # --- NEW CYP2C8 variants ---
    {
        "rsid": "rs10509681",
        "gene": "CYP2C8",
        "category": "pharmacogenomics",
        "name": "CYP2C8*3 (paclitaxel metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP2C8*3 allele (Lys399Arg) reducing paclitaxel metabolism. Carriers "
            "may have increased paclitaxel exposure and higher risk of peripheral "
            "neuropathy. Also affects amodiaquine and repaglinide metabolism."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "10",
        "position": 96798749,
        "source": "pharmgkb",
        "publications": ["11526218"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs11572080",
        "gene": "CYP2C8",
        "category": "pharmacogenomics",
        "name": "CYP2C8*3 Arg139Lys tag (paclitaxel)",
        "significance": "drug_response",
        "description": (
            "Second tag SNP for CYP2C8*3 haplotype (Arg139Lys). In strong linkage "
            "disequilibrium with rs10509681. Together they define the *3 allele "
            "associated with reduced paclitaxel and amodiaquine metabolism."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "10",
        "position": 96788773,
        "source": "pharmgkb",
        "publications": ["11526218"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # --- Additional CYP2D6 variants ---
    {
        "rsid": "rs28371706",
        "gene": "CYP2D6",
        "category": "pharmacogenomics",
        "name": "CYP2D6*17 (reduced function, African populations)",
        "significance": "drug_response",
        "description": (
            "CYP2D6*17 allele common in African populations (~20-35% allele "
            "frequency). Causes reduced enzyme activity with altered substrate "
            "specificity. Affects codeine, risperidone, and tamoxifen metabolism."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "22",
        "position": 42525772,
        "source": "pharmgkb",
        "publications": ["12172209"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs61736512",
        "gene": "CYP2D6",
        "category": "pharmacogenomics",
        "name": "CYP2D6*29 (reduced function)",
        "significance": "drug_response",
        "description": (
            "CYP2D6*29 allele with reduced enzyme activity. Found primarily in "
            "African populations. Carriers have intermediate metabolizer phenotype "
            "for CYP2D6 substrates including codeine and nortriptyline."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "22",
        "position": 42524175,
        "source": "pharmgkb",
        "publications": ["12815606"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs72552267",
        "gene": "CYP2D6",
        "category": "pharmacogenomics",
        "name": "CYP2D6*8 (non-functional)",
        "significance": "drug_response",
        "description": (
            "CYP2D6*8 allele with a premature stop codon resulting in a "
            "non-functional truncated protein. Rare allele contributing to poor "
            "metabolizer phenotype for CYP2D6 substrates."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "22",
        "position": 42523943,
        "source": "pharmgkb",
        "publications": ["16958828"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # --- NAT2 variants (CYP-adjacent, metabolism enzymes) ---
    {
        "rsid": "rs1799930",
        "gene": "NAT2",
        "category": "pharmacogenomics",
        "name": "NAT2*6 (isoniazid slow acetylator)",
        "significance": "drug_response",
        "description": (
            "NAT2*6 allele (Arg197Gln) causing slow acetylator phenotype. Carriers "
            "have reduced NAT2 activity, leading to higher isoniazid plasma levels "
            "and increased risk of hepatotoxicity during TB treatment."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "8",
        "position": 18258103,
        "source": "pharmgkb",
        "publications": ["22315962"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1208",
        "gene": "NAT2",
        "category": "pharmacogenomics",
        "name": "NAT2*4/*12 tag (acetylation status)",
        "significance": "drug_response",
        "description": (
            "NAT2 variant used to infer acetylator status. The G allele tags the "
            "rapid acetylator NAT2*4 reference haplotype. Combined with other NAT2 "
            "SNPs to predict isoniazid and hydralazine metabolism phenotype."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "8",
        "position": 18258370,
        "source": "pharmgkb",
        "publications": ["22315962"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # --- CYP2C9*8 (African warfarin) ---
    {
        "rsid": "rs4149015",
        "gene": "CYP2C9",
        "category": "pharmacogenomics",
        "name": "CYP2C9*8 (warfarin, African populations)",
        "significance": "drug_response",
        "description": (
            "CYP2C9*8 allele found predominantly in African-descent populations "
            "(~5-10% allele frequency). Causes reduced warfarin metabolism and is "
            "important for warfarin dosing algorithms in diverse populations."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "10",
        "position": 96701405,
        "source": "pharmgkb",
        "publications": ["22006094"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # CYP2C9*2 warfarin
    {
        "rsid": "rs1799853",
        "genotype": "CC",
        "interpretation": "Normal CYP2C9 metabolism. Standard warfarin dosing.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1799853",
        "genotype": "CT",
        "interpretation": "CYP2C9*2 carrier. May need reduced warfarin dose.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1799853",
        "genotype": "TT",
        "interpretation": "CYP2C9*2 homozygous. Significantly reduced warfarin metabolism.",
        "risk_level": "high_risk",
    },
    # CYP2C9*3 warfarin
    {
        "rsid": "rs1057910",
        "genotype": "AA",
        "interpretation": "Normal CYP2C9*3 status. Standard warfarin dosing.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1057910",
        "genotype": "AC",
        "interpretation": "CYP2C9*3 carrier. May need significantly reduced warfarin dose.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1057910",
        "genotype": "CC",
        "interpretation": "CYP2C9*3 homozygous. Very poor warfarin metabolism.",
        "risk_level": "high_risk",
    },
    # CYP1A2 caffeine
    {
        "rsid": "rs762551",
        "genotype": "AA",
        "interpretation": "Fast caffeine metabolizer. Rapid caffeine clearance.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs762551",
        "genotype": "AC",
        "interpretation": "Slow caffeine metabolizer. Prolonged caffeine effects.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs762551",
        "genotype": "CC",
        "interpretation": "Slow caffeine metabolizer. Significantly prolonged caffeine effects.",
        "risk_level": "increased_risk",
    },
    # CYP2C19*2 clopidogrel
    {
        "rsid": "rs4244285",
        "genotype": "GG",
        "interpretation": "Normal CYP2C19 function. Standard clopidogrel activation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4244285",
        "genotype": "GA",
        "interpretation": (
            "CYP2C19*2 carrier. Intermediate metabolizer; reduced clopidogrel activation."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4244285",
        "genotype": "AA",
        "interpretation": (
            "CYP2C19*2 homozygous. Poor metabolizer; clopidogrel largely ineffective. Alternative "
            "antiplatelet recommended."
        ),
        "risk_level": "high_risk",
    },
    # CYP2C19*3 clopidogrel
    {
        "rsid": "rs4986893",
        "genotype": "GG",
        "interpretation": "No CYP2C19*3 allele. Normal CYP2C19 function at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4986893",
        "genotype": "GA",
        "interpretation": (
            "CYP2C19*3 carrier. Loss-of-function allele; reduced clopidogrel activation."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4986893",
        "genotype": "AA",
        "interpretation": (
            "CYP2C19*3 homozygous. No CYP2C19 enzyme activity; clopidogrel ineffective."
        ),
        "risk_level": "high_risk",
    },
    # CYP2C19*17 ultra-rapid
    {
        "rsid": "rs12248560",
        "genotype": "CC",
        "interpretation": "No CYP2C19*17 allele. Normal CYP2C19 metabolizer status at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs12248560",
        "genotype": "CT",
        "interpretation": (
            "CYP2C19*17 carrier. Rapid metabolizer; enhanced clopidogrel activation but faster "
            "PPI clearance."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs12248560",
        "genotype": "TT",
        "interpretation": (
            "CYP2C19*17 homozygous. Ultra-rapid metabolizer; may need higher PPI doses."
        ),
        "risk_level": "increased_risk",
    },
    # --- NEW INTERPRETATIONS ---
    # CYP2D6*2 (rs16947)
    {
        "rsid": "rs16947",
        "genotype": "GG",
        "interpretation": "CYP2D6 wild-type at this position. Normal metabolizer baseline.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs16947",
        "genotype": "GA",
        "interpretation": "CYP2D6*2 heterozygote. Normal to slightly increased CYP2D6 activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs16947",
        "genotype": "AA",
        "interpretation": (
            "CYP2D6*2 homozygote. Normal to increased CYP2D6 activity; consider copy number for "
            "full status."
        ),
        "risk_level": "normal",
    },
    # CYP2D6*4 (rs3892097)
    {
        "rsid": "rs3892097",
        "genotype": "GG",
        "interpretation": "No CYP2D6*4 allele. Normal CYP2D6 function at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3892097",
        "genotype": "GA",
        "interpretation": (
            "CYP2D6*4 carrier. Intermediate metabolizer; reduced codeine and tamoxifen activation."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs3892097",
        "genotype": "AA",
        "interpretation": (
            "CYP2D6*4 homozygous. Poor metabolizer; codeine ineffective, tamoxifen activation "
            "impaired."
        ),
        "risk_level": "high_risk",
    },
    # CYP2D6*6 (rs5030655)
    {
        "rsid": "rs5030655",
        "genotype": "TT",
        "interpretation": "No CYP2D6*6 allele. Normal CYP2D6 function at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs5030655",
        "genotype": "TA",
        "interpretation": "CYP2D6*6 carrier. Intermediate metabolizer for CYP2D6 substrates.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs5030655",
        "genotype": "AA",
        "interpretation": "CYP2D6*6 homozygous. Poor metabolizer; non-functional CYP2D6.",
        "risk_level": "high_risk",
    },
    # CYP2D6*10 (rs1065852)
    {
        "rsid": "rs1065852",
        "genotype": "CC",
        "interpretation": "No CYP2D6*10 allele. Normal CYP2D6 function at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1065852",
        "genotype": "CT",
        "interpretation": (
            "CYP2D6*10 carrier. Reduced CYP2D6 activity; may need dose adjustment for "
            "codeine/tamoxifen."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1065852",
        "genotype": "TT",
        "interpretation": (
            "CYP2D6*10 homozygous. Significantly reduced CYP2D6 activity; common in East Asian "
            "populations."
        ),
        "risk_level": "high_risk",
    },
    # CYP2D6*41 (rs28371725)
    {
        "rsid": "rs28371725",
        "genotype": "CC",
        "interpretation": "No CYP2D6*41 allele. Normal CYP2D6 expression at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs28371725",
        "genotype": "CT",
        "interpretation": "CYP2D6*41 carrier. Reduced CYP2D6 expression via aberrant splicing.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs28371725",
        "genotype": "TT",
        "interpretation": (
            "CYP2D6*41 homozygous. Markedly reduced CYP2D6 expression; intermediate-to-poor "
            "metabolizer."
        ),
        "risk_level": "high_risk",
    },
    # CYP3A5*3 (rs776746)
    {
        "rsid": "rs776746",
        "genotype": "AA",
        "interpretation": (
            "CYP3A5 expresser (*1/*1). Normal tacrolimus metabolism; may need higher doses."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs776746",
        "genotype": "AG",
        "interpretation": "CYP3A5 heterozygous (*1/*3). Intermediate tacrolimus metabolism.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs776746",
        "genotype": "GG",
        "interpretation": (
            "CYP3A5 non-expresser (*3/*3). Reduced tacrolimus clearance; lower doses may suffice."
        ),
        "risk_level": "increased_risk",
    },
    # CYP3A4*1B (rs2032582)
    {
        "rsid": "rs2032582",
        "genotype": "GG",
        "interpretation": (
            "CYP3A4 reference genotype. Standard midazolam and CYP3A4 substrate metabolism."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs2032582",
        "genotype": "GA",
        "interpretation": (
            "CYP3A4*1B heterozygote. Possibly altered CYP3A4 expression; clinical effect is modest."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs2032582",
        "genotype": "AA",
        "interpretation": (
            "CYP3A4*1B homozygote. Altered CYP3A4 expression may affect midazolam and "
            "cyclosporine levels."
        ),
        "risk_level": "increased_risk",
    },
    # CYP3A4*1G (rs2242480)
    {
        "rsid": "rs2242480",
        "genotype": "CC",
        "interpretation": "CYP3A4 reference genotype at *1G locus. Standard metabolism.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2242480",
        "genotype": "CT",
        "interpretation": "CYP3A4*1G carrier. May have altered fentanyl and tacrolimus metabolism.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs2242480",
        "genotype": "TT",
        "interpretation": (
            "CYP3A4*1G homozygote. Altered CYP3A4 activity; dose adjustment may be warranted."
        ),
        "risk_level": "increased_risk",
    },
    # CYP2B6*6 (rs3745274)
    {
        "rsid": "rs3745274",
        "genotype": "GG",
        "interpretation": "Normal CYP2B6 function. Standard efavirenz metabolism.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3745274",
        "genotype": "GT",
        "interpretation": (
            "CYP2B6*6 carrier. Elevated efavirenz levels; monitor for CNS side effects."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs3745274",
        "genotype": "TT",
        "interpretation": (
            "CYP2B6*6 homozygous. Markedly elevated efavirenz levels; dose reduction recommended."
        ),
        "risk_level": "high_risk",
    },
    # CYP2B6*4 (rs28399504)
    {
        "rsid": "rs28399504",
        "genotype": "AA",
        "interpretation": "No CYP2B6*4 allele. Standard CYP2B6 activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs28399504",
        "genotype": "AG",
        "interpretation": (
            "CYP2B6*4 carrier. Increased CYP2B6 activity; may have lower efavirenz levels."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs28399504",
        "genotype": "GG",
        "interpretation": (
            "CYP2B6*4 homozygous. Rapid efavirenz metabolism; monitor for subtherapeutic levels."
        ),
        "risk_level": "increased_risk",
    },
    # CYP2B6*18 (rs28399499)
    {
        "rsid": "rs28399499",
        "genotype": "TT",
        "interpretation": "No CYP2B6*18 allele. Standard CYP2B6 activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs28399499",
        "genotype": "TG",
        "interpretation": (
            "CYP2B6*18 carrier. Severely reduced CYP2B6 activity; elevated efavirenz levels likely."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs28399499",
        "genotype": "GG",
        "interpretation": (
            "CYP2B6*18 homozygous. Minimal CYP2B6 activity; high risk of efavirenz toxicity."
        ),
        "risk_level": "high_risk",
    },
    # CYP2C8*3 (rs10509681)
    {
        "rsid": "rs10509681",
        "genotype": "TT",
        "interpretation": "No CYP2C8*3 allele at Lys399Arg. Normal paclitaxel metabolism.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs10509681",
        "genotype": "TC",
        "interpretation": (
            "CYP2C8*3 carrier (Lys399Arg). Reduced paclitaxel metabolism; neuropathy risk may be "
            "increased."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs10509681",
        "genotype": "CC",
        "interpretation": (
            "CYP2C8*3 homozygous (Lys399Arg). Significantly reduced paclitaxel clearance."
        ),
        "risk_level": "high_risk",
    },
    # CYP2C8*3 tag 2 (rs11572080)
    {
        "rsid": "rs11572080",
        "genotype": "CC",
        "interpretation": "No CYP2C8*3 allele at Arg139Lys. Normal CYP2C8 function.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs11572080",
        "genotype": "CT",
        "interpretation": (
            "CYP2C8*3 carrier (Arg139Lys tag). Reduced paclitaxel and amodiaquine metabolism."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs11572080",
        "genotype": "TT",
        "interpretation": (
            "CYP2C8*3 homozygous (Arg139Lys tag). Significantly reduced CYP2C8 activity."
        ),
        "risk_level": "high_risk",
    },
    # CYP2D6*17 (rs28371706)
    {
        "rsid": "rs28371706",
        "genotype": "GG",
        "interpretation": "No CYP2D6*17 allele. Normal CYP2D6 activity at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs28371706",
        "genotype": "GA",
        "interpretation": (
            "CYP2D6*17 carrier. Reduced CYP2D6 activity; common in African populations."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs28371706",
        "genotype": "AA",
        "interpretation": (
            "CYP2D6*17 homozygous. Significantly reduced CYP2D6 activity; intermediate metabolizer."
        ),
        "risk_level": "high_risk",
    },
    # CYP2D6*29 (rs61736512)
    {
        "rsid": "rs61736512",
        "genotype": "CC",
        "interpretation": "No CYP2D6*29 allele. Normal CYP2D6 activity at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs61736512",
        "genotype": "CT",
        "interpretation": (
            "CYP2D6*29 carrier. Reduced CYP2D6 activity for codeine and nortriptyline."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs61736512",
        "genotype": "TT",
        "interpretation": (
            "CYP2D6*29 homozygous. Intermediate metabolizer; dose adjustments may be needed."
        ),
        "risk_level": "high_risk",
    },
    # CYP2D6*8 (rs72552267)
    {
        "rsid": "rs72552267",
        "genotype": "GG",
        "interpretation": "No CYP2D6*8 allele. Normal CYP2D6 function at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs72552267",
        "genotype": "GT",
        "interpretation": "CYP2D6*8 carrier. One non-functional allele; intermediate metabolizer.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs72552267",
        "genotype": "TT",
        "interpretation": "CYP2D6*8 homozygous. Non-functional CYP2D6; poor metabolizer phenotype.",
        "risk_level": "high_risk",
    },
    # NAT2*6 (rs1799930)
    {
        "rsid": "rs1799930",
        "genotype": "GG",
        "interpretation": "No NAT2*6 allele. Rapid acetylator at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1799930",
        "genotype": "GA",
        "interpretation": (
            "NAT2*6 carrier. Intermediate acetylator; moderate isoniazid accumulation."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1799930",
        "genotype": "AA",
        "interpretation": (
            "NAT2*6 homozygous. Slow acetylator; elevated isoniazid levels and hepatotoxicity risk."
        ),
        "risk_level": "high_risk",
    },
    # NAT2*4/*12 tag (rs1208)
    {
        "rsid": "rs1208",
        "genotype": "GG",
        "interpretation": (
            "NAT2 rapid acetylator haplotype. Normal isoniazid and hydralazine metabolism."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1208",
        "genotype": "GA",
        "interpretation": "NAT2 intermediate acetylator. Moderately reduced acetylation capacity.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1208",
        "genotype": "AA",
        "interpretation": (
            "NAT2 slow acetylator tag. Reduced acetylation; combine with other NAT2 SNPs for full "
            "phenotype."
        ),
        "risk_level": "increased_risk",
    },
    # CYP2C9*8 (rs4149015)
    {
        "rsid": "rs4149015",
        "genotype": "AA",
        "interpretation": "No CYP2C9*8 allele. Standard warfarin metabolism at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4149015",
        "genotype": "AG",
        "interpretation": (
            "CYP2C9*8 carrier. Reduced warfarin metabolism; relevant for African-descent dosing "
            "algorithms."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4149015",
        "genotype": "GG",
        "interpretation": (
            "CYP2C9*8 homozygous. Significantly reduced warfarin metabolism; lower doses needed."
        ),
        "risk_level": "high_risk",
    },
]
