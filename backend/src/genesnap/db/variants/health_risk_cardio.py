"""Cardiovascular health risk variants: APOE, F5, F2, PCSK9, LPA, 9p21, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    {
        "rsid": "rs429358",
        "gene": "APOE",
        "category": "health_risk",
        "name": "APOE e4 determinant (C112R)",
        "significance": "risk_factor",
        "description": (
            "One of two SNPs that define APOE isoforms. The e4 allele (C at rs429358) "
            "is the strongest common genetic risk factor for late-onset Alzheimer's disease. "
            "One e4 copy increases risk ~3x; two copies increase risk ~12x."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "19",
        "position": 45411941,
        "source": "clinvar",
        "publications": ["7842013", "9343467"],
        "clinvar_stars": 3,
        "odds_ratio": 3.2,
    },
    {
        "rsid": "rs7412",
        "gene": "APOE",
        "category": "health_risk",
        "name": "APOE e2 determinant (R158C)",
        "significance": "risk_factor",
        "description": (
            "Second SNP defining APOE isoforms. The e2 allele (T at rs7412) is associated "
            "with reduced Alzheimer's risk but increased risk of type III hyperlipoproteinemia."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "19",
        "position": 45412079,
        "source": "clinvar",
        "publications": ["7842013"],
        "clinvar_stars": 2,
        "odds_ratio": 0.6,
    },
    {
        "rsid": "rs6025",
        "gene": "F5",
        "category": "health_risk",
        "name": "Factor V Leiden",
        "significance": "pathogenic",
        "description": (
            "Factor V Leiden mutation causes activated protein C resistance, significantly "
            "increasing risk of venous thromboembolism (DVT and pulmonary embolism). "
            "Heterozygous carriers have 5-10x increased risk; homozygous have 50-100x."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "1",
        "position": 169519049,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000001168"},
        "publications": ["7989264", "8275930"],
        "clinvar_stars": 3,
        "odds_ratio": 7.0,
    },
    {
        "rsid": "rs1799963",
        "gene": "F2",
        "category": "health_risk",
        "name": "Prothrombin G20210A",
        "significance": "pathogenic",
        "description": (
            "Prothrombin gene mutation leads to elevated prothrombin levels and 2-5x increased "
            "risk of venous thromboembolism."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "11",
        "position": 46761055,
        "source": "clinvar",
        "publications": ["8740443"],
        "clinvar_stars": 3,
        "odds_ratio": 3.0,
    },
    # -------------------------------------------------------------------------
    # 9p21.3 region (CDKN2A/CDKN2B-AS1) - coronary heart disease risk
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10757274",
        "gene": "CDKN2B-AS1",
        "category": "health_risk",
        "name": "9p21.3 CHD risk variant",
        "significance": "association",
        "description": (
            "Common variant on chromosome 9p21.3 near CDKN2A/CDKN2B. This locus is one of "
            "the first and most replicated GWAS signals for coronary heart disease, conferring "
            "a ~1.3x increased risk per G allele independent of traditional risk factors."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "9",
        "position": 22096055,
        "source": "gwas_catalog",
        "publications": ["17478679", "17634449"],
        "clinvar_stars": 1,
        "odds_ratio": 1.3,
    },
    {
        "rsid": "rs1333049",
        "gene": "CDKN2B-AS1",
        "category": "health_risk",
        "name": "9p21.3 CHD risk variant #2",
        "significance": "association",
        "description": (
            "Second independent signal at the 9p21.3 locus associated with coronary heart "
            "disease. The C allele confers approximately 1.3x increased risk of myocardial "
            "infarction and coronary artery disease."
        ),
        "risk_allele": "C",
        "normal_allele": "G",
        "chromosome": "9",
        "position": 22125503,
        "source": "gwas_catalog",
        "publications": ["17554300", "17634449"],
        "clinvar_stars": 1,
        "odds_ratio": 1.3,
    },
    # -------------------------------------------------------------------------
    # APOC1 / APOE region - lipid levels
    # -------------------------------------------------------------------------
    {
        "rsid": "rs4420638",
        "gene": "APOC1",
        "category": "health_risk",
        "name": "APOC1/APOE region lipid variant",
        "significance": "risk_factor",
        "description": (
            "Variant near APOC1 in the APOE gene cluster on chromosome 19. Associated with "
            "elevated LDL cholesterol and increased risk of coronary artery disease and "
            "Alzheimer's disease, partly tagging the APOE e4 haplotype."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "19",
        "position": 45422946,
        "source": "gwas_catalog",
        "publications": ["18193043", "19060906"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # LPA - lipoprotein(a) levels
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10455872",
        "gene": "LPA",
        "category": "health_risk",
        "name": "LPA Lp(a) level variant",
        "significance": "risk_factor",
        "description": (
            "Intronic variant in the LPA gene strongly associated with elevated lipoprotein(a) "
            "levels, a causal risk factor for coronary artery disease, aortic valve stenosis, "
            "and ischaemic stroke. Each G allele raises Lp(a) substantially."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "6",
        "position": 161010118,
        "source": "gwas_catalog",
        "publications": ["19060911", "22003152"],
        "clinvar_stars": 1,
        "odds_ratio": 1.5,
    },
    {
        "rsid": "rs3798220",
        "gene": "LPA",
        "category": "health_risk",
        "name": "LPA I4399M variant",
        "significance": "risk_factor",
        "description": (
            "Missense variant (I4399M) in LPA associated with elevated lipoprotein(a) and "
            "increased risk of coronary artery disease. Carriers have significantly higher "
            "Lp(a) concentrations and ~1.5x increased CHD risk."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "6",
        "position": 160961137,
        "source": "gwas_catalog",
        "publications": ["19060911", "19474294"],
        "clinvar_stars": 1,
        "odds_ratio": 1.5,
    },
    # -------------------------------------------------------------------------
    # PCSK9 - LDL cholesterol (protective loss-of-function)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs11591147",
        "gene": "PCSK9",
        "category": "health_risk",
        "name": "PCSK9 R46L (protective)",
        "significance": "association",
        "description": (
            "Loss-of-function missense variant (R46L) in PCSK9. Carriers have ~15% lower "
            "LDL cholesterol and approximately 30% reduced risk of coronary heart disease. "
            "This variant informed the development of PCSK9 inhibitor therapies."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "1",
        "position": 55505647,
        "source": "clinvar",
        "publications": ["16554528", "17044105"],
        "clinvar_stars": 2,
        "odds_ratio": 0.7,
    },
    # -------------------------------------------------------------------------
    # ABO blood group - venous thromboembolism and cardiovascular risk
    # -------------------------------------------------------------------------
    {
        "rsid": "rs505922",
        "gene": "ABO",
        "category": "health_risk",
        "name": "ABO blood group VTE risk variant",
        "significance": "risk_factor",
        "description": (
            "Variant in the ABO gene that tags non-O blood groups. Non-O blood types have "
            "higher levels of von Willebrand factor and factor VIII, resulting in ~1.4x "
            "increased risk of venous thromboembolism."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "9",
        "position": 136149229,
        "source": "gwas_catalog",
        "publications": ["19690346", "17903295"],
        "clinvar_stars": 1,
        "odds_ratio": 1.4,
    },
    {
        "rsid": "rs8176719",
        "gene": "ABO",
        "category": "health_risk",
        "name": "ABO O blood type determinant",
        "significance": "association",
        "description": (
            "Frameshift variant in the ABO gene that determines O blood type. Deletion of G "
            "(delG) leads to a non-functional glycosyltransferase and O blood type, which is "
            "associated with lower VTE risk but may affect other cardiovascular traits."
        ),
        "risk_allele": "G",
        "normal_allele": "delG",
        "chromosome": "9",
        "position": 136131322,
        "source": "gwas_catalog",
        "publications": ["19690346", "20139978"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    # -------------------------------------------------------------------------
    # PITX2 - atrial fibrillation
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2200733",
        "gene": "PITX2",
        "category": "health_risk",
        "name": "PITX2 atrial fibrillation risk variant",
        "significance": "risk_factor",
        "description": (
            "Intergenic variant on chromosome 4q25 near the PITX2 transcription factor gene. "
            "This is the strongest common genetic risk locus for atrial fibrillation, with "
            "each T allele conferring ~1.3x increased AF risk."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "4",
        "position": 111710169,
        "source": "gwas_catalog",
        "publications": ["17603472", "19597491"],
        "clinvar_stars": 1,
        "odds_ratio": 1.3,
    },
    {
        "rsid": "rs10033464",
        "gene": "PITX2",
        "category": "health_risk",
        "name": "PITX2 atrial fibrillation risk variant #2",
        "significance": "risk_factor",
        "description": (
            "Second independent signal at the 4q25 locus near PITX2 associated with atrial "
            "fibrillation. The T allele confers approximately 1.2x increased risk of AF."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "4",
        "position": 111714145,
        "source": "gwas_catalog",
        "publications": ["17603472", "19597491"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 2q36.3 - coronary artery disease
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2943634",
        "gene": "IRS1",
        "category": "health_risk",
        "name": "2q36.3 CAD risk variant",
        "significance": "association",
        "description": (
            "Intergenic variant on chromosome 2q36.3 near the IRS1 locus associated with "
            "coronary artery disease risk. The C allele has been linked to modestly increased "
            "susceptibility to CAD in large GWAS meta-analyses."
        ),
        "risk_allele": "C",
        "normal_allele": "A",
        "chromosome": "2",
        "position": 227100698,
        "source": "gwas_catalog",
        "publications": ["17634449", "21378990"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # CELSR2/SORT1 - LDL cholesterol
    # -------------------------------------------------------------------------
    {
        "rsid": "rs6795735",
        "gene": "CELSR2",
        "category": "health_risk",
        "name": "CELSR2/SORT1 LDL cholesterol variant",
        "significance": "association",
        "description": (
            "Variant at the CELSR2-PSRC1-SORT1 locus on chromosome 1p13. This region has a "
            "well-established effect on LDL cholesterol levels and coronary artery disease "
            "risk through regulation of hepatic SORT1 expression."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "1",
        "position": 109821511,
        "source": "gwas_catalog",
        "publications": ["18193043", "20686565"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # CXCL12 - coronary artery disease
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1746048",
        "gene": "CXCL12",
        "category": "health_risk",
        "name": "CXCL12 coronary artery disease variant",
        "significance": "risk_factor",
        "description": (
            "Variant near CXCL12 (SDF-1) on chromosome 10q11. CXCL12 encodes a chemokine "
            "involved in inflammation and vascular remodelling. The C allele is associated "
            "with ~1.2x increased risk of coronary artery disease."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "10",
        "position": 44751986,
        "source": "gwas_catalog",
        "publications": ["17554300", "19198609"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # MIA3/AGTRAP - coronary artery disease
    # -------------------------------------------------------------------------
    {
        "rsid": "rs17465637",
        "gene": "MIA3",
        "category": "health_risk",
        "name": "MIA3/AGTRAP CAD risk variant",
        "significance": "association",
        "description": (
            "Variant in the MIA3 (TANGO1) gene on chromosome 1q41 associated with coronary "
            "artery disease. MIA3 is involved in collagen secretion and may influence "
            "atherosclerotic plaque stability. The C allele confers ~1.2x increased risk."
        ),
        "risk_allele": "C",
        "normal_allele": "A",
        "chromosome": "1",
        "position": 222823529,
        "source": "gwas_catalog",
        "publications": ["17554300", "19198609"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # MRAS - coronary artery disease
    # -------------------------------------------------------------------------
    {
        "rsid": "rs9818870",
        "gene": "MRAS",
        "category": "health_risk",
        "name": "MRAS coronary artery disease variant",
        "significance": "association",
        "description": (
            "Variant near the MRAS gene on chromosome 3q22. MRAS encodes a Ras-related GTPase "
            "involved in cell growth and differentiation. The T allele has been associated with "
            "a modest ~1.1x increased risk of coronary artery disease."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "3",
        "position": 138119952,
        "source": "gwas_catalog",
        "publications": ["19198612", "21378990"],
        "clinvar_stars": 1,
        "odds_ratio": 1.1,
    },
    # -------------------------------------------------------------------------
    # PHACTR1 - coronary artery disease
    # -------------------------------------------------------------------------
    {
        "rsid": "rs12526453",
        "gene": "PHACTR1",
        "category": "health_risk",
        "name": "PHACTR1 CAD risk variant",
        "significance": "association",
        "description": (
            "Variant in the PHACTR1 gene on chromosome 6p24. PHACTR1 regulates protein "
            "phosphatase 1 and actin dynamics. The C allele is associated with ~1.1x increased "
            "risk of coronary artery disease and myocardial infarction."
        ),
        "risk_allele": "C",
        "normal_allele": "G",
        "chromosome": "6",
        "position": 12903957,
        "source": "gwas_catalog",
        "publications": ["21378990", "22319020"],
        "clinvar_stars": 1,
        "odds_ratio": 1.1,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # -------------------------------------------------------------------------
    # APOE rs429358
    # -------------------------------------------------------------------------
    {
        "rsid": "rs429358",
        "genotype": "TT",
        "interpretation": "No e4 allele at this position (likely e2/e3 or e3/e3)",
        "risk_level": "normal",
    },
    {
        "rsid": "rs429358",
        "genotype": "CT",
        "interpretation": "One e4-associated allele (heterozygous); confirm with rs7412",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs429358",
        "genotype": "CC",
        "interpretation": "Two e4-associated alleles (homozygous); confirm with rs7412",
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # APOE rs7412
    # -------------------------------------------------------------------------
    {
        "rsid": "rs7412",
        "genotype": "CC",
        "interpretation": "No e2 allele at this position",
        "risk_level": "normal",
    },
    {
        "rsid": "rs7412",
        "genotype": "CT",
        "interpretation": "One e2 allele (may be protective against Alzheimer's)",
        "risk_level": "normal",
    },
    {
        "rsid": "rs7412",
        "genotype": "TT",
        "interpretation": "Two e2 alleles; associated with type III hyperlipoproteinemia risk",
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # Factor V Leiden (rs6025)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs6025",
        "genotype": "GG",
        "interpretation": "No Factor V Leiden mutation. Normal clotting risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs6025",
        "genotype": "AG",
        "interpretation": "Heterozygous carrier of Factor V Leiden. 5-10x increased VTE risk.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs6025",
        "genotype": "AA",
        "interpretation": "Homozygous Factor V Leiden. 50-100x increased VTE risk.",
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # Prothrombin G20210A (rs1799963)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1799963",
        "genotype": "GG",
        "interpretation": "No prothrombin mutation. Normal prothrombin levels.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1799963",
        "genotype": "AG",
        "interpretation": "Heterozygous carrier of prothrombin G20210A. 2-5x increased VTE risk.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1799963",
        "genotype": "AA",
        "interpretation": "Homozygous prothrombin G20210A. Significantly elevated VTE risk.",
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # 9p21.3 rs10757274
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10757274",
        "genotype": "AA",
        "interpretation": (
            "No risk alleles at 9p21.3 (rs10757274). Average CHD risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs10757274",
        "genotype": "AG",
        "interpretation": "One risk allele at 9p21.3. Modestly increased CHD risk (~1.3x).",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs10757274",
        "genotype": "GG",
        "interpretation": "Two risk alleles at 9p21.3. Increased CHD risk (~1.6x).",
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # 9p21.3 rs1333049
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1333049",
        "genotype": "GG",
        "interpretation": (
            "No risk alleles at 9p21.3 (rs1333049). Average CHD risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1333049",
        "genotype": "CG",
        "interpretation": "One risk allele at 9p21.3. Modestly increased CHD risk (~1.3x).",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1333049",
        "genotype": "CC",
        "interpretation": "Two risk alleles at 9p21.3. Increased CHD risk (~1.6x).",
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # APOC1 rs4420638
    # -------------------------------------------------------------------------
    {
        "rsid": "rs4420638",
        "genotype": "AA",
        "interpretation": (
            "No risk alleles at APOC1/APOE region. Average lipid levels from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs4420638",
        "genotype": "AG",
        "interpretation": (
            "One risk allele in APOC1/APOE region. Modestly elevated LDL cholesterol."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4420638",
        "genotype": "GG",
        "interpretation": (
            "Two risk alleles in APOC1/APOE region. Elevated LDL cholesterol and CAD risk."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # LPA rs10455872
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10455872",
        "genotype": "AA",
        "interpretation": "No risk alleles at LPA. Normal lipoprotein(a) levels expected.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs10455872",
        "genotype": "AG",
        "interpretation": "One risk allele at LPA. Elevated Lp(a) and ~1.5x increased CAD risk.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs10455872",
        "genotype": "GG",
        "interpretation": (
            "Two risk alleles at LPA. Significantly elevated Lp(a) and high CAD risk."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # LPA rs3798220
    # -------------------------------------------------------------------------
    {
        "rsid": "rs3798220",
        "genotype": "TT",
        "interpretation": "No risk alleles at LPA I4399M. Normal Lp(a) levels from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3798220",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous LPA I4399M carrier. Elevated Lp(a) and ~1.5x increased CAD risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs3798220",
        "genotype": "CC",
        "interpretation": "Homozygous LPA I4399M. Significantly elevated Lp(a) and high CAD risk.",
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # PCSK9 rs11591147 (protective - risk levels inverted)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs11591147",
        "genotype": "GG",
        "interpretation": "No PCSK9 R46L variant. Standard LDL cholesterol metabolism.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs11591147",
        "genotype": "GT",
        "interpretation": (
            "Heterozygous PCSK9 R46L carrier. ~15% lower LDL cholesterol and ~30% reduced "
            "CHD risk. This is a protective variant."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs11591147",
        "genotype": "TT",
        "interpretation": (
            "Homozygous PCSK9 R46L. Substantially lower LDL cholesterol and significantly "
            "reduced CHD risk. Protective genotype."
        ),
        "risk_level": "normal",
    },
    # -------------------------------------------------------------------------
    # ABO rs505922
    # -------------------------------------------------------------------------
    {
        "rsid": "rs505922",
        "genotype": "TT",
        "interpretation": "Likely O blood group genotype. Lower VTE and cardiovascular risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs505922",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous non-O blood group tag. Modestly increased VTE risk (~1.4x)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs505922",
        "genotype": "CC",
        "interpretation": "Non-O blood group genotype. Increased VTE risk (~1.4-1.8x).",
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # ABO rs8176719
    # -------------------------------------------------------------------------
    {
        "rsid": "rs8176719",
        "genotype": "delG/delG",
        "interpretation": "Homozygous deletion; O blood type. Associated with lower VTE risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs8176719",
        "genotype": "G/delG",
        "interpretation": (
            "Heterozygous; carrier of one functional ABO allele (A or B) and one O allele."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs8176719",
        "genotype": "GG",
        "interpretation": (
            "Non-O blood type (A, B, or AB). Modestly increased VTE and cardiovascular risk."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # PITX2 rs2200733
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2200733",
        "genotype": "CC",
        "interpretation": "No risk alleles at PITX2 locus. Average atrial fibrillation risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2200733",
        "genotype": "CT",
        "interpretation": (
            "One risk allele at PITX2 locus. ~1.3x increased atrial fibrillation risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2200733",
        "genotype": "TT",
        "interpretation": (
            "Two risk alleles at PITX2 locus. ~1.7x increased atrial fibrillation risk."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # PITX2 rs10033464
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10033464",
        "genotype": "GG",
        "interpretation": "No risk alleles at PITX2 secondary locus. Average AF risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs10033464",
        "genotype": "GT",
        "interpretation": "One risk allele at PITX2 secondary locus. ~1.2x increased AF risk.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs10033464",
        "genotype": "TT",
        "interpretation": "Two risk alleles at PITX2 secondary locus. Increased AF risk (~1.4x).",
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # 2q36.3 rs2943634
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2943634",
        "genotype": "AA",
        "interpretation": "No risk alleles at 2q36.3 locus. Average CAD risk from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2943634",
        "genotype": "AC",
        "interpretation": "One risk allele at 2q36.3 locus. Modestly increased CAD risk (~1.2x).",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2943634",
        "genotype": "CC",
        "interpretation": "Two risk alleles at 2q36.3 locus. Increased CAD risk (~1.4x).",
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # CELSR2/SORT1 rs6795735
    # -------------------------------------------------------------------------
    {
        "rsid": "rs6795735",
        "genotype": "TT",
        "interpretation": (
            "No risk alleles at CELSR2/SORT1 locus. Average LDL cholesterol from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs6795735",
        "genotype": "CT",
        "interpretation": (
            "One risk allele at CELSR2/SORT1 locus. Modestly elevated LDL cholesterol."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs6795735",
        "genotype": "CC",
        "interpretation": (
            "Two risk alleles at CELSR2/SORT1 locus. Elevated LDL cholesterol and CAD risk."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # CXCL12 rs1746048
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1746048",
        "genotype": "TT",
        "interpretation": "No risk alleles at CXCL12 locus. Average CAD risk from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1746048",
        "genotype": "CT",
        "interpretation": "One risk allele at CXCL12 locus. Modestly increased CAD risk (~1.2x).",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1746048",
        "genotype": "CC",
        "interpretation": "Two risk alleles at CXCL12 locus. Increased CAD risk (~1.4x).",
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # MIA3 rs17465637
    # -------------------------------------------------------------------------
    {
        "rsid": "rs17465637",
        "genotype": "AA",
        "interpretation": "No risk alleles at MIA3 locus. Average CAD risk from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs17465637",
        "genotype": "AC",
        "interpretation": "One risk allele at MIA3 locus. Modestly increased CAD risk (~1.2x).",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs17465637",
        "genotype": "CC",
        "interpretation": "Two risk alleles at MIA3 locus. Increased CAD risk (~1.4x).",
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # MRAS rs9818870
    # -------------------------------------------------------------------------
    {
        "rsid": "rs9818870",
        "genotype": "CC",
        "interpretation": "No risk alleles at MRAS locus. Average CAD risk from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs9818870",
        "genotype": "CT",
        "interpretation": "One risk allele at MRAS locus. Slightly increased CAD risk (~1.1x).",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs9818870",
        "genotype": "TT",
        "interpretation": "Two risk alleles at MRAS locus. Modestly increased CAD risk (~1.2x).",
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # PHACTR1 rs12526453
    # -------------------------------------------------------------------------
    {
        "rsid": "rs12526453",
        "genotype": "GG",
        "interpretation": "No risk alleles at PHACTR1 locus. Average CAD risk from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs12526453",
        "genotype": "CG",
        "interpretation": "One risk allele at PHACTR1 locus. Slightly increased CAD risk (~1.1x).",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs12526453",
        "genotype": "CC",
        "interpretation": "Two risk alleles at PHACTR1 locus. Modestly increased CAD risk (~1.2x).",
        "risk_level": "increased_risk",
    },
]
