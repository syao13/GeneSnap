"""Non-CYP pharmacogenomics variants: VKORC1, SLCO1B1, TPMT, DPYD, NUDT15, NAT2, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    {
        "rsid": "rs9923231",
        "gene": "VKORC1",
        "category": "pharmacogenomics",
        "name": "VKORC1 -1639G>A (warfarin sensitivity)",
        "significance": "drug_response",
        "description": (
            "VKORC1 promoter variant affecting warfarin dose requirements. AA genotype "
            "requires ~50% lower dose than GG. Combined with CYP2C9 status for dosing."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "16",
        "position": 31107689,
        "source": "pharmgkb",
        "publications": ["15930419", "19794411"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4149056",
        "gene": "SLCO1B1",
        "category": "pharmacogenomics",
        "name": "SLCO1B1*5 (statin myopathy risk)",
        "significance": "drug_response",
        "description": (
            "SLCO1B1 variant reducing hepatic statin uptake. C allele carriers have 4-17x "
            "increased risk of simvastatin-induced myopathy."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "12",
        "position": 21331549,
        "source": "pharmgkb",
        "publications": ["18650507"],
        "clinvar_stars": 3,
        "odds_ratio": 4.5,
    },
    {
        "rsid": "rs1142345",
        "gene": "TPMT",
        "category": "pharmacogenomics",
        "name": "TPMT*3C (thiopurine toxicity)",
        "significance": "drug_response",
        "description": (
            "TPMT variant causing reduced enzyme activity. Carriers require reduced "
            "thiopurine doses (azathioprine, 6-MP) to avoid severe myelosuppression."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "6",
        "position": 18130918,
        "source": "pharmgkb",
        "publications": ["10534218"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs3918290",
        "gene": "DPYD",
        "category": "pharmacogenomics",
        "name": "DPYD*2A (5-FU toxicity)",
        "significance": "drug_response",
        "description": (
            "DPD deficiency allele causing potentially fatal fluoropyrimidine (5-FU) toxicity. "
            "Pre-treatment testing is increasingly standard of care."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "1",
        "position": 97915614,
        "source": "pharmgkb",
        "publications": ["23988873"],
        "clinvar_stars": 4,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1801280",
        "gene": "NAT2",
        "category": "pharmacogenomics",
        "name": "NAT2*5 (isoniazid metabolism)",
        "significance": "drug_response",
        "description": (
            "NAT2 slow acetylator allele. Slow acetylators have higher isoniazid "
            "exposure and increased risk of drug-induced liver injury during TB treatment."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "8",
        "position": 18257854,
        "source": "pharmgkb",
        "publications": ["22315962"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # --- NEW VARIANTS ---
    # TPMT*3B
    {
        "rsid": "rs1800460",
        "gene": "TPMT",
        "category": "pharmacogenomics",
        "name": "TPMT*3B (thiopurine toxicity)",
        "significance": "drug_response",
        "description": (
            "TPMT*3B allele (Ala154Thr) causing reduced enzyme activity. Combined "
            "with *3C (rs1142345) defines the *3A haplotype. Carriers require "
            "thiopurine dose reduction to prevent severe myelosuppression."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "6",
        "position": 18130753,
        "source": "pharmgkb",
        "publications": ["10534218"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    # DPYD additional variants
    {
        "rsid": "rs1801265",
        "gene": "DPYD",
        "category": "pharmacogenomics",
        "name": "DPYD IVS14+1G>A tag (5-FU toxicity)",
        "significance": "drug_response",
        "description": (
            "DPYD variant in linkage with splicing defects affecting DPD enzyme "
            "activity. Used as a secondary marker for fluoropyrimidine toxicity "
            "risk assessment alongside the primary DPYD*2A allele."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "1",
        "position": 97915614,
        "source": "pharmgkb",
        "publications": ["23988873"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs67376798",
        "gene": "DPYD",
        "category": "pharmacogenomics",
        "name": "DPYD D949V (5-FU toxicity)",
        "significance": "drug_response",
        "description": (
            "DPYD D949V variant (c.2846A>T) causing reduced DPD activity. Carriers "
            "have increased risk of severe fluoropyrimidine toxicity. European "
            "guidelines recommend pre-treatment genotyping for this variant."
        ),
        "risk_allele": "T",
        "normal_allele": "A",
        "chromosome": "1",
        "position": 97981395,
        "source": "pharmgkb",
        "publications": ["23988873", "29152729"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs55886062",
        "gene": "DPYD",
        "category": "pharmacogenomics",
        "name": "DPYD I560S (5-FU toxicity)",
        "significance": "drug_response",
        "description": (
            "DPYD I560S variant (c.1679T>G) causing non-functional DPD enzyme. "
            "Rare but high-impact variant; carriers are at risk of life-threatening "
            "fluoropyrimidine toxicity. Included in CPIC DPYD guidelines."
        ),
        "risk_allele": "G",
        "normal_allele": "T",
        "chromosome": "1",
        "position": 98015142,
        "source": "pharmgkb",
        "publications": ["23988873"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    # NUDT15
    {
        "rsid": "rs116855232",
        "gene": "NUDT15",
        "category": "pharmacogenomics",
        "name": "NUDT15 R139C (thiopurine toxicity, Asian populations)",
        "significance": "drug_response",
        "description": (
            "NUDT15 R139C variant causing reduced nucleotide diphosphatase activity. "
            "Strongly associated with thiopurine-induced leukopenia, particularly "
            "in East Asian populations. CPIC recommends dose reduction for carriers."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "13",
        "position": 48611945,
        "source": "pharmgkb",
        "publications": ["25642906", "27959333"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    # UGT1A1 variants
    {
        "rsid": "rs8175347",
        "gene": "UGT1A1",
        "category": "pharmacogenomics",
        "name": "UGT1A1*28 (irinotecan toxicity)",
        "significance": "drug_response",
        "description": (
            "UGT1A1*28 allele with (TA)7 repeat in the promoter reducing enzyme "
            "expression. Carriers have reduced irinotecan glucuronidation and "
            "increased risk of severe neutropenia and diarrhea. Also causes Gilbert syndrome."
        ),
        "risk_allele": "TA7",
        "normal_allele": "TA6",
        "chromosome": "2",
        "position": 234668879,
        "source": "pharmgkb",
        "publications": ["15470160", "17510680"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4148323",
        "gene": "UGT1A1",
        "category": "pharmacogenomics",
        "name": "UGT1A1*6 (irinotecan toxicity, Asian populations)",
        "significance": "drug_response",
        "description": (
            "UGT1A1*6 allele (Gly71Arg) causing reduced enzyme activity. Most "
            "common UGT1A1 deficiency allele in East Asian populations. Increases "
            "risk of irinotecan-induced neutropenia and hyperbilirubinemia."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "2",
        "position": 234669144,
        "source": "pharmgkb",
        "publications": ["17510680"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs887829",
        "gene": "UGT1A1",
        "category": "pharmacogenomics",
        "name": "UGT1A1*80 (Gilbert syndrome/irinotecan)",
        "significance": "drug_response",
        "description": (
            "UGT1A1*80 promoter variant in strong linkage disequilibrium with *28. "
            "T allele associated with reduced UGT1A1 expression, Gilbert syndrome, "
            "and increased irinotecan toxicity risk. Useful as a tag SNP for *28."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "2",
        "position": 234665782,
        "source": "pharmgkb",
        "publications": ["17510680"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # ABCB1 (P-glycoprotein) variants
    {
        "rsid": "rs1045642",
        "gene": "ABCB1",
        "category": "pharmacogenomics",
        "name": "ABCB1 C3435T (P-glycoprotein function)",
        "significance": "drug_response",
        "description": (
            "ABCB1/MDR1 synonymous variant affecting P-glycoprotein expression and "
            "drug efflux activity. T allele associated with reduced P-gp expression "
            "and altered bioavailability of digoxin, cyclosporine, and HIV protease inhibitors."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "7",
        "position": 87138645,
        "source": "pharmgkb",
        "publications": ["11668225"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1128503",
        "gene": "ABCB1",
        "category": "pharmacogenomics",
        "name": "ABCB1 C1236T (P-glycoprotein function)",
        "significance": "drug_response",
        "description": (
            "ABCB1/MDR1 synonymous variant at exon 12. Part of the common ABCB1 "
            "haplotype (1236T-2677T-3435T) associated with reduced P-glycoprotein "
            "expression and altered drug transport of multiple substrates."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "7",
        "position": 87179601,
        "source": "pharmgkb",
        "publications": ["11668225"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # SLCO1B1 additional variant
    {
        "rsid": "rs2306283",
        "gene": "SLCO1B1",
        "category": "pharmacogenomics",
        "name": "SLCO1B1*1b (statin hepatic transport)",
        "significance": "drug_response",
        "description": (
            "SLCO1B1*1b allele (Asn130Asp) with increased hepatic transporter "
            "activity. May partially offset the myopathy risk of *5 when present "
            "on the same haplotype (*15 = *1b + *5). Affects statin pharmacokinetics."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "12",
        "position": 21329738,
        "source": "pharmgkb",
        "publications": ["18650507"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # VKORC1 additional variants
    {
        "rsid": "rs9934438",
        "gene": "VKORC1",
        "category": "pharmacogenomics",
        "name": "VKORC1 1173C>T (warfarin sensitivity)",
        "significance": "drug_response",
        "description": (
            "VKORC1 intronic variant in strong linkage disequilibrium with -1639G>A. "
            "T allele associated with lower VKORC1 expression and increased warfarin "
            "sensitivity. Used in some warfarin dosing algorithms as an alternative marker."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "16",
        "position": 31104878,
        "source": "pharmgkb",
        "publications": ["15930419"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs7294",
        "gene": "VKORC1",
        "category": "pharmacogenomics",
        "name": "VKORC1 3730G>A (warfarin sensitivity)",
        "significance": "drug_response",
        "description": (
            "VKORC1 3'-UTR variant associated with warfarin dose variability. "
            "Part of the VKORC1 haplotype group used in pharmacogenomic warfarin "
            "dosing. A allele linked to lower warfarin dose requirements."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "16",
        "position": 31102321,
        "source": "pharmgkb",
        "publications": ["15930419"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # CYP4F2
    {
        "rsid": "rs2108622",
        "gene": "CYP4F2",
        "category": "pharmacogenomics",
        "name": "CYP4F2 V433M (warfarin metabolism)",
        "significance": "drug_response",
        "description": (
            "CYP4F2 V433M variant reducing vitamin K1 oxidase activity. T allele "
            "carriers have higher hepatic vitamin K levels and require increased "
            "warfarin doses (~1 mg/day higher). Included in IWPC dosing algorithm."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "19",
        "position": 15990431,
        "source": "pharmgkb",
        "publications": ["18250228"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    # CYP2C cluster warfarin (African)
    {
        "rsid": "rs12777823",
        "gene": "CYP2C cluster",
        "category": "pharmacogenomics",
        "name": "CYP2C cluster (warfarin, African populations)",
        "significance": "drug_response",
        "description": (
            "Intergenic variant near the CYP2C gene cluster associated with warfarin "
            "dose requirements in African Americans. G allele associated with lower "
            "warfarin dose needs. Important for equitable pharmacogenomic dosing."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "10",
        "position": 96603878,
        "source": "pharmgkb",
        "publications": ["22006094"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # SLCO1B3
    {
        "rsid": "rs4149117",
        "gene": "SLCO1B3",
        "category": "pharmacogenomics",
        "name": "SLCO1B3 (statin/chemotherapy transport)",
        "significance": "drug_response",
        "description": (
            "SLCO1B3 transporter variant affecting hepatic uptake of statins, "
            "methotrexate, and other drugs. T allele associated with altered "
            "transporter function and modified drug pharmacokinetics."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "12",
        "position": 21370676,
        "source": "pharmgkb",
        "publications": ["18650507"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # ABCG2
    {
        "rsid": "rs2231142",
        "gene": "ABCG2",
        "category": "pharmacogenomics",
        "name": "ABCG2 Q141K (allopurinol/rosuvastatin)",
        "significance": "drug_response",
        "description": (
            "ABCG2 Q141K variant reducing efflux transporter activity. T allele "
            "associated with increased rosuvastatin exposure and better allopurinol "
            "response in gout. Also affects topotecan and sulfasalazine transport."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "4",
        "position": 89052323,
        "source": "pharmgkb",
        "publications": ["19384066", "22286173"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    # CES1
    {
        "rsid": "rs28364274",
        "gene": "CES1",
        "category": "pharmacogenomics",
        "name": "CES1 G143E (ester prodrug activation)",
        "significance": "drug_response",
        "description": (
            "CES1 G143E variant causing loss of carboxylesterase 1 activity. "
            "Carriers have impaired activation of ester prodrugs including "
            "clopidogrel, oseltamivir, and methylphenidate, and reduced metabolism "
            "of dabigatran."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "16",
        "position": 55838149,
        "source": "pharmgkb",
        "publications": ["23665868"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # IFNL3 (IL28B) variants
    {
        "rsid": "rs12979860",
        "gene": "IFNL3",
        "category": "pharmacogenomics",
        "name": "IFNL3/IL28B (HCV treatment response)",
        "significance": "drug_response",
        "description": (
            "IFNL3 (IL28B) variant strongly predicting hepatitis C treatment "
            "response. CC genotype associated with 2-3x higher sustained virologic "
            "response to pegylated interferon plus ribavirin. Less relevant with "
            "direct-acting antivirals but still informative."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "19",
        "position": 39738787,
        "source": "pharmgkb",
        "publications": ["19684573", "20639878"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs8099917",
        "gene": "IFNL3",
        "category": "pharmacogenomics",
        "name": "IFNL3 (HCV treatment response #2)",
        "significance": "drug_response",
        "description": (
            "Second IFNL3 region variant predicting HCV treatment response. TT "
            "genotype associated with favorable response to interferon-based therapy. "
            "In linkage disequilibrium with rs12979860 but independently informative "
            "in some populations."
        ),
        "risk_allele": "G",
        "normal_allele": "T",
        "chromosome": "19",
        "position": 39741000,
        "source": "pharmgkb",
        "publications": ["19684573"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # OPRM1
    {
        "rsid": "rs1061235",
        "gene": "OPRM1",
        "category": "pharmacogenomics",
        "name": "OPRM1 A118G tag (opioid response)",
        "significance": "drug_response",
        "description": (
            "OPRM1 variant tagging the A118G functional polymorphism in the mu-opioid "
            "receptor gene. Associated with altered opioid analgesic requirements, "
            "with carriers potentially needing higher morphine doses for adequate "
            "pain control."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "6",
        "position": 154360797,
        "source": "pharmgkb",
        "publications": ["14615764"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # VKORC1 warfarin
    {
        "rsid": "rs9923231",
        "genotype": "CC",
        "interpretation": "Normal VKORC1. Standard warfarin sensitivity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs9923231",
        "genotype": "CT",
        "interpretation": "Intermediate VKORC1 sensitivity. May need ~25% lower warfarin dose.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs9923231",
        "genotype": "TT",
        "interpretation": "High warfarin sensitivity. May need ~50% lower dose.",
        "risk_level": "high_risk",
    },
    # SLCO1B1 statin
    {
        "rsid": "rs4149056",
        "genotype": "TT",
        "interpretation": "Normal SLCO1B1 function. Standard statin risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4149056",
        "genotype": "TC",
        "interpretation": "SLCO1B1*5 carrier. Increased risk of statin-induced myopathy.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4149056",
        "genotype": "CC",
        "interpretation": "SLCO1B1*5 homozygous. High risk of statin-induced myopathy.",
        "risk_level": "high_risk",
    },
    # TPMT*3C (rs1142345)
    {
        "rsid": "rs1142345",
        "genotype": "TT",
        "interpretation": "Normal TPMT activity. Standard thiopurine dosing.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1142345",
        "genotype": "TC",
        "interpretation": (
            "TPMT*3C carrier. Intermediate activity; reduce thiopurine dose to avoid "
            "myelosuppression."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1142345",
        "genotype": "CC",
        "interpretation": (
            "TPMT*3C homozygous. Very low TPMT activity; drastically reduce thiopurine dose."
        ),
        "risk_level": "high_risk",
    },
    # DPYD*2A (rs3918290)
    {
        "rsid": "rs3918290",
        "genotype": "GG",
        "interpretation": "No DPYD*2A allele. Normal DPD activity; standard 5-FU dosing.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3918290",
        "genotype": "GA",
        "interpretation": (
            "DPYD*2A carrier. Reduced DPD activity; reduce 5-FU dose by at least 50%."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs3918290",
        "genotype": "AA",
        "interpretation": "DPYD*2A homozygous. No DPD activity; fluoropyrimidines contraindicated.",
        "risk_level": "high_risk",
    },
    # NAT2*5 (rs1801280)
    {
        "rsid": "rs1801280",
        "genotype": "TT",
        "interpretation": "No NAT2*5 allele. Rapid acetylator at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801280",
        "genotype": "TC",
        "interpretation": (
            "NAT2*5 carrier. Intermediate acetylator; moderate isoniazid accumulation."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1801280",
        "genotype": "CC",
        "interpretation": (
            "NAT2*5 homozygous. Slow acetylator; increased isoniazid hepatotoxicity risk."
        ),
        "risk_level": "high_risk",
    },
    # --- NEW INTERPRETATIONS ---
    # TPMT*3B (rs1800460)
    {
        "rsid": "rs1800460",
        "genotype": "GG",
        "interpretation": "No TPMT*3B allele. Normal TPMT activity at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800460",
        "genotype": "GA",
        "interpretation": (
            "TPMT*3B carrier. Intermediate TPMT activity; thiopurine dose reduction recommended."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1800460",
        "genotype": "AA",
        "interpretation": (
            "TPMT*3B homozygous. Very low TPMT activity; drastically reduce thiopurine dose."
        ),
        "risk_level": "high_risk",
    },
    # DPYD IVS14+1G>A tag (rs1801265)
    {
        "rsid": "rs1801265",
        "genotype": "GG",
        "interpretation": "No DPYD IVS14+1G>A tag variant. Normal DPD function at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801265",
        "genotype": "GA",
        "interpretation": (
            "DPYD tag variant carrier. May indicate reduced DPD function; assess with other DPYD "
            "markers."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1801265",
        "genotype": "AA",
        "interpretation": (
            "DPYD tag variant homozygous. Potentially reduced DPD function; fluoropyrimidine "
            "caution advised."
        ),
        "risk_level": "increased_risk",
    },
    # DPYD D949V (rs67376798)
    {
        "rsid": "rs67376798",
        "genotype": "AA",
        "interpretation": "No DPYD D949V variant. Normal DPD activity at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs67376798",
        "genotype": "AT",
        "interpretation": (
            "DPYD D949V carrier. Reduced DPD activity; reduce fluoropyrimidine dose by 25-50%."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs67376798",
        "genotype": "TT",
        "interpretation": (
            "DPYD D949V homozygous. Severely reduced DPD activity; fluoropyrimidine "
            "contraindicated."
        ),
        "risk_level": "high_risk",
    },
    # DPYD I560S (rs55886062)
    {
        "rsid": "rs55886062",
        "genotype": "TT",
        "interpretation": "No DPYD I560S variant. Normal DPD activity at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs55886062",
        "genotype": "TG",
        "interpretation": (
            "DPYD I560S carrier. Non-functional allele; reduce fluoropyrimidine dose by at least "
            "50%."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs55886062",
        "genotype": "GG",
        "interpretation": (
            "DPYD I560S homozygous. No DPD function; fluoropyrimidines are contraindicated."
        ),
        "risk_level": "high_risk",
    },
    # NUDT15 R139C (rs116855232)
    {
        "rsid": "rs116855232",
        "genotype": "CC",
        "interpretation": (
            "No NUDT15 R139C variant. Normal NUDT15 activity; standard thiopurine dosing."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs116855232",
        "genotype": "CT",
        "interpretation": (
            "NUDT15 R139C carrier. Intermediate activity; reduce thiopurine dose to avoid "
            "leukopenia."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs116855232",
        "genotype": "TT",
        "interpretation": (
            "NUDT15 R139C homozygous. Very low activity; drastically reduce thiopurine dose."
        ),
        "risk_level": "high_risk",
    },
    # UGT1A1*28 (rs8175347)
    {
        "rsid": "rs8175347",
        "genotype": "TA6/TA6",
        "interpretation": "UGT1A1*1/*1. Normal UGT1A1 activity; standard irinotecan dosing.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs8175347",
        "genotype": "TA6/TA7",
        "interpretation": (
            "UGT1A1*1/*28 carrier. Mildly reduced UGT1A1 activity; monitor irinotecan toxicity."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs8175347",
        "genotype": "TA7/TA7",
        "interpretation": (
            "UGT1A1*28/*28 homozygous. Significantly reduced UGT1A1; reduce irinotecan dose."
        ),
        "risk_level": "high_risk",
    },
    # UGT1A1*6 (rs4148323)
    {
        "rsid": "rs4148323",
        "genotype": "GG",
        "interpretation": "No UGT1A1*6 allele. Normal UGT1A1 activity at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4148323",
        "genotype": "GA",
        "interpretation": (
            "UGT1A1*6 carrier. Reduced UGT1A1 activity; increased irinotecan toxicity risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4148323",
        "genotype": "AA",
        "interpretation": (
            "UGT1A1*6 homozygous. Significantly reduced UGT1A1; dose reduction for irinotecan "
            "needed."
        ),
        "risk_level": "high_risk",
    },
    # UGT1A1*80 (rs887829)
    {
        "rsid": "rs887829",
        "genotype": "CC",
        "interpretation": "No UGT1A1*80 variant. Normal UGT1A1 promoter activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs887829",
        "genotype": "CT",
        "interpretation": (
            "UGT1A1*80 carrier. Reduced UGT1A1 expression; may indicate *28-linked irinotecan risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs887829",
        "genotype": "TT",
        "interpretation": (
            "UGT1A1*80 homozygous. Significantly reduced UGT1A1 expression; Gilbert syndrome "
            "likely."
        ),
        "risk_level": "high_risk",
    },
    # ABCB1 C3435T (rs1045642)
    {
        "rsid": "rs1045642",
        "genotype": "CC",
        "interpretation": (
            "ABCB1 reference genotype. Normal P-glycoprotein expression and drug efflux."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1045642",
        "genotype": "CT",
        "interpretation": (
            "ABCB1 3435T carrier. Moderately reduced P-gp expression; altered drug bioavailability."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1045642",
        "genotype": "TT",
        "interpretation": (
            "ABCB1 3435T homozygous. Reduced P-gp expression; increased digoxin/cyclosporine "
            "levels."
        ),
        "risk_level": "increased_risk",
    },
    # ABCB1 C1236T (rs1128503)
    {
        "rsid": "rs1128503",
        "genotype": "CC",
        "interpretation": "ABCB1 reference genotype at C1236T. Normal P-glycoprotein function.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1128503",
        "genotype": "CT",
        "interpretation": "ABCB1 1236T carrier. Part of common reduced-function haplotype.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1128503",
        "genotype": "TT",
        "interpretation": (
            "ABCB1 1236T homozygous. Reduced P-gp function when combined with other ABCB1 variants."
        ),
        "risk_level": "increased_risk",
    },
    # SLCO1B1*1b (rs2306283)
    {
        "rsid": "rs2306283",
        "genotype": "AA",
        "interpretation": "SLCO1B1 reference genotype. Standard hepatic statin transport.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2306283",
        "genotype": "AG",
        "interpretation": (
            "SLCO1B1*1b carrier. Increased transporter activity; may modify *5 myopathy risk."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs2306283",
        "genotype": "GG",
        "interpretation": (
            "SLCO1B1*1b homozygous. Enhanced hepatic statin uptake; generally favorable."
        ),
        "risk_level": "normal",
    },
    # VKORC1 1173C>T (rs9934438)
    {
        "rsid": "rs9934438",
        "genotype": "CC",
        "interpretation": "VKORC1 1173 reference genotype. Standard warfarin sensitivity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs9934438",
        "genotype": "CT",
        "interpretation": (
            "VKORC1 1173T carrier. Intermediate warfarin sensitivity; may need dose reduction."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs9934438",
        "genotype": "TT",
        "interpretation": (
            "VKORC1 1173T homozygous. High warfarin sensitivity; significant dose reduction likely."
        ),
        "risk_level": "high_risk",
    },
    # VKORC1 3730G>A (rs7294)
    {
        "rsid": "rs7294",
        "genotype": "GG",
        "interpretation": "VKORC1 3730 reference genotype. Standard warfarin dose requirement.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs7294",
        "genotype": "GA",
        "interpretation": "VKORC1 3730A carrier. May require modestly lower warfarin dose.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs7294",
        "genotype": "AA",
        "interpretation": "VKORC1 3730A homozygous. Lower warfarin dose requirement expected.",
        "risk_level": "increased_risk",
    },
    # CYP4F2 V433M (rs2108622)
    {
        "rsid": "rs2108622",
        "genotype": "CC",
        "interpretation": (
            "CYP4F2 reference genotype. Normal vitamin K oxidase activity; standard warfarin "
            "dosing."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs2108622",
        "genotype": "CT",
        "interpretation": (
            "CYP4F2 V433M carrier. Mildly elevated vitamin K levels; ~0.5 mg/day higher warfarin "
            "dose."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs2108622",
        "genotype": "TT",
        "interpretation": (
            "CYP4F2 V433M homozygous. Higher vitamin K levels; ~1 mg/day higher warfarin dose "
            "needed."
        ),
        "risk_level": "increased_risk",
    },
    # CYP2C cluster (rs12777823)
    {
        "rsid": "rs12777823",
        "genotype": "AA",
        "interpretation": "CYP2C cluster reference genotype. Standard warfarin metabolism.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs12777823",
        "genotype": "AG",
        "interpretation": (
            "CYP2C cluster G carrier. May require lower warfarin dose in African Americans."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs12777823",
        "genotype": "GG",
        "interpretation": (
            "CYP2C cluster G homozygous. Significantly lower warfarin dose likely in African "
            "Americans."
        ),
        "risk_level": "high_risk",
    },
    # SLCO1B3 (rs4149117)
    {
        "rsid": "rs4149117",
        "genotype": "GG",
        "interpretation": "SLCO1B3 reference genotype. Normal hepatic drug transport.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4149117",
        "genotype": "GT",
        "interpretation": (
            "SLCO1B3 variant carrier. Altered statin and methotrexate hepatic uptake."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs4149117",
        "genotype": "TT",
        "interpretation": (
            "SLCO1B3 variant homozygous. Reduced hepatic transporter function for multiple drugs."
        ),
        "risk_level": "increased_risk",
    },
    # ABCG2 Q141K (rs2231142)
    {
        "rsid": "rs2231142",
        "genotype": "GG",
        "interpretation": "ABCG2 reference genotype. Normal efflux transporter function.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2231142",
        "genotype": "GT",
        "interpretation": (
            "ABCG2 Q141K carrier. Reduced efflux; increased rosuvastatin exposure and allopurinol "
            "response."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs2231142",
        "genotype": "TT",
        "interpretation": (
            "ABCG2 Q141K homozygous. Significantly reduced efflux; lower rosuvastatin dose may be "
            "needed."
        ),
        "risk_level": "increased_risk",
    },
    # CES1 G143E (rs28364274)
    {
        "rsid": "rs28364274",
        "genotype": "GG",
        "interpretation": "CES1 reference genotype. Normal carboxylesterase 1 activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs28364274",
        "genotype": "GA",
        "interpretation": (
            "CES1 G143E carrier. Reduced ester prodrug activation (clopidogrel, oseltamivir)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs28364274",
        "genotype": "AA",
        "interpretation": (
            "CES1 G143E homozygous. Very low CES1 activity; impaired prodrug activation."
        ),
        "risk_level": "high_risk",
    },
    # IFNL3 rs12979860
    {
        "rsid": "rs12979860",
        "genotype": "CC",
        "interpretation": (
            "IFNL3 favorable genotype. Best HCV treatment response to interferon-based therapy."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs12979860",
        "genotype": "CT",
        "interpretation": "IFNL3 intermediate genotype. Moderate HCV treatment response.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs12979860",
        "genotype": "TT",
        "interpretation": (
            "IFNL3 unfavorable genotype. Lowest HCV treatment response to interferon; consider "
            "DAAs."
        ),
        "risk_level": "increased_risk",
    },
    # IFNL3 rs8099917
    {
        "rsid": "rs8099917",
        "genotype": "TT",
        "interpretation": (
            "IFNL3 favorable genotype. Good HCV treatment response to interferon-based therapy."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs8099917",
        "genotype": "TG",
        "interpretation": "IFNL3 intermediate genotype. Reduced HCV interferon treatment response.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs8099917",
        "genotype": "GG",
        "interpretation": (
            "IFNL3 unfavorable genotype. Poor HCV interferon response; direct-acting antivirals "
            "preferred."
        ),
        "risk_level": "increased_risk",
    },
    # OPRM1 A118G tag (rs1061235)
    {
        "rsid": "rs1061235",
        "genotype": "AA",
        "interpretation": (
            "OPRM1 reference genotype. Standard opioid receptor binding and analgesic response."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1061235",
        "genotype": "AG",
        "interpretation": (
            "OPRM1 variant carrier. May require higher opioid doses for adequate analgesia."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1061235",
        "genotype": "GG",
        "interpretation": (
            "OPRM1 variant homozygous. Altered mu-opioid receptor; likely needs higher morphine "
            "doses."
        ),
        "risk_level": "increased_risk",
    },
]
