"""Metabolic health risk variants: MTHFR, FTO, TCF7L2, HFE, PNPLA3, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    {
        "rsid": "rs1801133",
        "gene": "MTHFR",
        "category": "health_risk",
        "name": "MTHFR C677T",
        "significance": "risk_factor",
        "description": (
            "Common variant reducing MTHFR enzyme activity. TT genotype has ~30% residual "
            "enzyme activity and mildly elevated homocysteine. Clinical significance is "
            "often overstated; adequate folate intake usually compensates."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "1",
        "position": 11856378,
        "source": "clinvar",
        "publications": ["7647779", "36261339"],
        "clinvar_stars": 2,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs1801131",
        "gene": "MTHFR",
        "category": "health_risk",
        "name": "MTHFR A1298C",
        "significance": "risk_factor",
        "description": (
            "Second common MTHFR variant. CC genotype has modest reduction in enzyme activity. "
            "No independent effect on folate status; clinical significance is limited."
        ),
        "risk_allele": "G",
        "normal_allele": "T",
        "chromosome": "1",
        "position": 11854476,
        "source": "clinvar",
        "publications": ["31525701"],
        "clinvar_stars": 1,
        "odds_ratio": 1.1,
    },
    {
        "rsid": "rs9939609",
        "gene": "FTO",
        "category": "health_risk",
        "name": "FTO obesity risk variant",
        "significance": "association",
        "description": (
            "The most studied obesity-associated variant. Each A allele associated with "
            "~1.2 kg higher body weight and 1.3x increased obesity risk."
        ),
        "risk_allele": "A",
        "normal_allele": "T",
        "chromosome": "16",
        "position": 53820527,
        "source": "gwas_catalog",
        "publications": ["17434869"],
        "clinvar_stars": 0,
        "odds_ratio": 1.3,
    },
    {
        "rsid": "rs7903146",
        "gene": "TCF7L2",
        "category": "health_risk",
        "name": "Type 2 diabetes risk variant",
        "significance": "risk_factor",
        "description": (
            "The strongest common genetic risk factor for type 2 diabetes. T allele carriers "
            "have impaired insulin secretion and ~1.4x increased diabetes risk per allele."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "10",
        "position": 114758349,
        "source": "gwas_catalog",
        "publications": ["16415884", "28507013"],
        "clinvar_stars": 1,
        "odds_ratio": 1.4,
    },
    {
        "rsid": "rs1800562",
        "gene": "HFE",
        "category": "health_risk",
        "name": "Hereditary hemochromatosis (C282Y)",
        "significance": "pathogenic",
        "description": (
            "Primary mutation causing hereditary hemochromatosis (iron overload). "
            "Homozygous C282Y individuals have high penetrance for iron overload, especially males."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "6",
        "position": 26093141,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000009345"},
        "publications": ["8696333"],
        "clinvar_stars": 4,
        "odds_ratio": 5.0,
    },
    {
        "rsid": "rs1799945",
        "gene": "HFE",
        "category": "health_risk",
        "name": "Hereditary hemochromatosis (H63D)",
        "significance": "risk_factor",
        "description": (
            "Secondary HFE mutation. Low penetrance alone, but compound heterozygosity "
            "with C282Y moderately increases iron overload risk."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "6",
        "position": 26091179,
        "source": "clinvar",
        "publications": ["8696333"],
        "clinvar_stars": 2,
        "odds_ratio": 1.6,
    },
    # --- NEW metabolic variants ---
    {
        "rsid": "rs738409",
        "gene": "PNPLA3",
        "category": "health_risk",
        "name": "PNPLA3 I148M (fatty liver disease)",
        "significance": "risk_factor",
        "description": (
            "PNPLA3 I148M variant, the strongest genetic risk factor for non-alcoholic "
            "fatty liver disease (NAFLD). The G allele impairs hepatic lipid remodeling, "
            "increasing liver fat content, steatohepatitis, fibrosis, and cirrhosis risk."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "22",
        "position": 44324727,
        "source": "gwas_catalog",
        "publications": ["18820647", "24911328"],
        "clinvar_stars": 1,
        "odds_ratio": 3.3,
    },
    {
        "rsid": "rs72613567",
        "gene": "HSD17B13",
        "category": "health_risk",
        "name": "HSD17B13 splice variant (liver protective)",
        "significance": "association",
        "description": (
            "Loss-of-function splice variant in HSD17B13. The A allele reduces risk "
            "of chronic liver disease progression from steatosis to steatohepatitis "
            "and cirrhosis. Protective effect is independent of PNPLA3 status."
        ),
        "risk_allele": "T",
        "normal_allele": "A",
        "chromosome": "4",
        "position": 88231392,
        "source": "gwas_catalog",
        "publications": ["30615544"],
        "clinvar_stars": 0,
        "odds_ratio": 0.7,
    },
    {
        "rsid": "rs1260326",
        "gene": "GCKR",
        "category": "health_risk",
        "name": "GCKR P446L (triglycerides/metabolic)",
        "significance": "association",
        "description": (
            "GCKR Pro446Leu variant affecting glucokinase regulation. The T allele "
            "increases hepatic glucose uptake and de novo lipogenesis, raising "
            "triglyceride levels while lowering fasting glucose. Pleiotropic effects "
            "on multiple metabolic traits."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "2",
        "position": 27730940,
        "source": "gwas_catalog",
        "publications": ["18372903", "20686565"],
        "clinvar_stars": 0,
        "odds_ratio": 1.1,
    },
    {
        "rsid": "rs780094",
        "gene": "GCKR",
        "category": "health_risk",
        "name": "GCKR intron (metabolic syndrome)",
        "significance": "association",
        "description": (
            "GCKR intronic variant in linkage disequilibrium with P446L. Robustly "
            "associated with triglyceride levels, CRP, and fasting glucose in GWAS "
            "meta-analyses. Part of the metabolic syndrome genetic architecture."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "2",
        "position": 27741237,
        "source": "gwas_catalog",
        "publications": ["18372903"],
        "clinvar_stars": 0,
        "odds_ratio": 1.1,
    },
    {
        "rsid": "rs1801282",
        "gene": "PPARG",
        "category": "health_risk",
        "name": "PPARG Pro12Ala (T2D protective)",
        "significance": "association",
        "description": (
            "PPARG Pro12Ala variant. The Ala allele (G) is associated with modestly "
            "reduced type 2 diabetes risk through improved insulin sensitivity. "
            "PPARG is the target of thiazolidinedione drugs."
        ),
        "risk_allele": "C",
        "normal_allele": "G",
        "chromosome": "3",
        "position": 12393125,
        "source": "gwas_catalog",
        "publications": ["10951254", "17463249"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs5219",
        "gene": "KCNJ11",
        "category": "health_risk",
        "name": "KCNJ11 E23K (T2D risk)",
        "significance": "association",
        "description": (
            "KCNJ11 Glu23Lys variant in the ATP-sensitive potassium channel of "
            "pancreatic beta cells. The Lys23 allele impairs insulin secretion and "
            "is associated with modestly increased type 2 diabetes risk."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "11",
        "position": 17409572,
        "source": "gwas_catalog",
        "publications": ["12829785", "17463249"],
        "clinvar_stars": 1,
        "odds_ratio": 1.15,
    },
    {
        "rsid": "rs13266634",
        "gene": "SLC30A8",
        "category": "health_risk",
        "name": "SLC30A8 R325W (T2D risk)",
        "significance": "association",
        "description": (
            "SLC30A8 Arg325Trp variant in the zinc transporter ZnT8 of pancreatic "
            "beta cells. The C allele (Arg325) is associated with increased T2D risk. "
            "Loss-of-function variants in SLC30A8 are protective against diabetes."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "8",
        "position": 118184783,
        "source": "gwas_catalog",
        "publications": ["17460697", "17463249"],
        "clinvar_stars": 0,
        "odds_ratio": 1.12,
    },
    {
        "rsid": "rs7578597",
        "gene": "THADA",
        "category": "health_risk",
        "name": "THADA T1187A (T2D risk)",
        "significance": "association",
        "description": (
            "THADA variant associated with type 2 diabetes in GWAS. THADA is involved "
            "in apoptosis signaling in thyroid tissue. The T2D risk allele may affect "
            "beta cell function and survival."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "2",
        "position": 43732823,
        "source": "gwas_catalog",
        "publications": ["18372903"],
        "clinvar_stars": 0,
        "odds_ratio": 1.15,
    },
    {
        "rsid": "rs2943641",
        "gene": "IRS1",
        "category": "health_risk",
        "name": "IRS1 insulin signaling variant",
        "significance": "association",
        "description": (
            "Variant near IRS1 (insulin receptor substrate 1) associated with insulin "
            "resistance, type 2 diabetes, and reduced IRS1 protein levels in adipose "
            "tissue. One of the established insulin signaling pathway GWAS hits."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "2",
        "position": 227020869,
        "source": "gwas_catalog",
        "publications": ["19734900"],
        "clinvar_stars": 0,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs12785878",
        "gene": "DHCR7/NADSYN1",
        "category": "health_risk",
        "name": "DHCR7 vitamin D levels",
        "significance": "association",
        "description": (
            "Variant near DHCR7 (7-dehydrocholesterol reductase) associated with "
            "circulating 25-hydroxyvitamin D levels. DHCR7 catalyzes a step in "
            "vitamin D synthesis. The T allele is associated with lower vitamin D "
            "levels, potentially impacting bone health and immune function."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "11",
        "position": 71167449,
        "source": "gwas_catalog",
        "publications": ["20541252"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs2282679",
        "gene": "GC",
        "category": "health_risk",
        "name": "GC/VDBP vitamin D binding protein",
        "significance": "association",
        "description": (
            "Variant in GC gene encoding vitamin D binding protein (VDBP), the major "
            "circulating carrier for 25(OH)D. The C allele is associated with lower "
            "total 25(OH)D levels. The strongest common genetic determinant of "
            "vitamin D status."
        ),
        "risk_allele": "C",
        "normal_allele": "A",
        "chromosome": "4",
        "position": 72608383,
        "source": "gwas_catalog",
        "publications": ["20541252"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4588",
        "gene": "GC",
        "category": "health_risk",
        "name": "GC Thr436Lys (VDBP isoform)",
        "significance": "association",
        "description": (
            "GC/VDBP coding variant (Thr436Lys) defining VDBP isoforms. Different "
            "isoforms have varying binding affinities for vitamin D metabolites. "
            "The A allele (Lys436) is associated with lower 25(OH)D levels."
        ),
        "risk_allele": "A",
        "normal_allele": "C",
        "chromosome": "4",
        "position": 72618334,
        "source": "gwas_catalog",
        "publications": ["20541252"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs10830963",
        "gene": "MTNR1B",
        "category": "health_risk",
        "name": "MTNR1B melatonin receptor (T2D/fasting glucose)",
        "significance": "association",
        "description": (
            "Variant in MTNR1B (melatonin receptor 1B) strongly associated with "
            "fasting glucose levels and type 2 diabetes risk. The G allele increases "
            "MTNR1B expression in beta cells, impairing insulin secretion. Links "
            "circadian rhythm disruption to metabolic disease."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "11",
        "position": 92708710,
        "source": "gwas_catalog",
        "publications": ["19060907", "20581827"],
        "clinvar_stars": 0,
        "odds_ratio": 1.1,
    },
    {
        "rsid": "rs174547",
        "gene": "FADS1",
        "category": "health_risk",
        "name": "FADS1 fatty acid desaturase",
        "significance": "association",
        "description": (
            "Variant in the FADS1 gene encoding delta-5 desaturase. Strongly "
            "associated with plasma levels of arachidonic acid, omega-3 fatty acids, "
            "and multiple lipid traits. The C allele is associated with higher "
            "desaturase activity and higher AA:DGLA ratio."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "11",
        "position": 61570783,
        "source": "gwas_catalog",
        "publications": ["21829377"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # MTHFR C677T
    {
        "rsid": "rs1801133",
        "genotype": "GG",
        "interpretation": "Normal MTHFR activity (wild-type C677).",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801133",
        "genotype": "AG",
        "interpretation": "One copy of MTHFR C677T. ~65% enzyme activity. Usually no concern.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1801133",
        "genotype": "AA",
        "interpretation": "Homozygous MTHFR C677T. ~30% enzyme activity. Elevated homocysteine.",
        "risk_level": "increased_risk",
    },
    # 23andMe reports on the minus strand, so A/G here = T/C on plus strand
    {
        "rsid": "rs1801133",
        "genotype": "CT",
        "interpretation": "One copy of MTHFR C677T. ~65% enzyme activity. Usually no concern.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1801133",
        "genotype": "TT",
        "interpretation": "Homozygous MTHFR C677T. ~30% enzyme activity. Elevated homocysteine.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1801133",
        "genotype": "CC",
        "interpretation": "Normal MTHFR activity (wild-type C677).",
        "risk_level": "normal",
    },
    # FTO obesity
    {
        "rsid": "rs9939609",
        "genotype": "TT",
        "interpretation": "No obesity risk alleles. Average weight tendency.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs9939609",
        "genotype": "AT",
        "interpretation": "One obesity risk allele. Slightly increased obesity risk (~1.2 kg).",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs9939609",
        "genotype": "AA",
        "interpretation": "Two obesity risk alleles. ~3 kg higher weight, 1.7x obesity risk.",
        "risk_level": "increased_risk",
    },
    # TCF7L2 diabetes
    {
        "rsid": "rs7903146",
        "genotype": "CC",
        "interpretation": "No diabetes risk alleles at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs7903146",
        "genotype": "CT",
        "interpretation": "One T2D risk allele. ~1.4x increased type 2 diabetes risk.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs7903146",
        "genotype": "TT",
        "interpretation": "Two T2D risk alleles. ~2x increased type 2 diabetes risk.",
        "risk_level": "high_risk",
    },
    # PNPLA3 fatty liver
    {
        "rsid": "rs738409",
        "genotype": "CC",
        "interpretation": "No PNPLA3 I148M variant. Lower genetic risk for fatty liver disease.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs738409",
        "genotype": "CG",
        "interpretation": (
            "One PNPLA3 I148M allele. Moderately increased NAFLD and liver fibrosis risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs738409",
        "genotype": "GG",
        "interpretation": (
            "Homozygous PNPLA3 I148M. ~3.3x NAFLD risk; strongly increased fibrosis/cirrhosis risk."
        ),
        "risk_level": "high_risk",
    },
    # HSD17B13 liver protective
    {
        "rsid": "rs72613567",
        "genotype": "AA",
        "interpretation": "HSD17B13 reference. Typical liver disease progression risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs72613567",
        "genotype": "AT",
        "interpretation": (
            "One HSD17B13 protective allele. Reduced steatohepatitis and cirrhosis risk."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs72613567",
        "genotype": "TT",
        "interpretation": (
            "Homozygous HSD17B13 loss-of-function. Strongly reduced liver disease progression risk."
        ),
        "risk_level": "normal",
    },
    # GCKR P446L
    {
        "rsid": "rs1260326",
        "genotype": "CC",
        "interpretation": "GCKR reference. Standard glucokinase regulation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1260326",
        "genotype": "CT",
        "interpretation": (
            "GCKR P446L carrier. Modestly elevated triglycerides with lower fasting glucose."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1260326",
        "genotype": "TT",
        "interpretation": "GCKR P446L homozygous. Higher triglycerides; lower fasting glucose.",
        "risk_level": "increased_risk",
    },
    # GCKR intron
    {
        "rsid": "rs780094",
        "genotype": "CC",
        "interpretation": "GCKR reference at this intronic locus. Standard metabolic profile.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs780094",
        "genotype": "CT",
        "interpretation": (
            "GCKR intronic carrier. Modestly altered triglyceride and glucose metabolism."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs780094",
        "genotype": "TT",
        "interpretation": (
            "GCKR intronic homozygous. Elevated triglycerides; metabolic syndrome association."
        ),
        "risk_level": "increased_risk",
    },
    # PPARG Pro12Ala
    {
        "rsid": "rs1801282",
        "genotype": "CC",
        "interpretation": "PPARG Pro12 (common). Standard insulin sensitivity from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801282",
        "genotype": "CG",
        "interpretation": (
            "PPARG Pro12Ala carrier. Modestly improved insulin sensitivity; lower T2D risk."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801282",
        "genotype": "GG",
        "interpretation": "PPARG Ala12 homozygous. Improved insulin sensitivity; reduced T2D risk.",
        "risk_level": "normal",
    },
    # KCNJ11 E23K
    {
        "rsid": "rs5219",
        "genotype": "CC",
        "interpretation": "KCNJ11 Glu23. Normal potassium channel function in beta cells.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs5219",
        "genotype": "CT",
        "interpretation": "KCNJ11 E23K carrier. Slightly impaired insulin secretion.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs5219",
        "genotype": "TT",
        "interpretation": (
            "KCNJ11 Lys23 homozygous. Modestly increased T2D risk via impaired insulin secretion."
        ),
        "risk_level": "increased_risk",
    },
    # SLC30A8 R325W
    {
        "rsid": "rs13266634",
        "genotype": "CC",
        "interpretation": (
            "SLC30A8 Arg325. Standard ZnT8 function; typical T2D risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs13266634",
        "genotype": "CT",
        "interpretation": "SLC30A8 R325W carrier. Intermediate zinc transport in beta cells.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs13266634",
        "genotype": "TT",
        "interpretation": "SLC30A8 Trp325 homozygous. Modestly reduced T2D risk from this locus.",
        "risk_level": "normal",
    },
    # THADA T1187A
    {
        "rsid": "rs7578597",
        "genotype": "CC",
        "interpretation": "THADA reference. Standard T2D risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs7578597",
        "genotype": "CT",
        "interpretation": "THADA variant carrier. Slightly increased T2D risk.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs7578597",
        "genotype": "TT",
        "interpretation": "THADA variant homozygous. Modestly increased T2D risk.",
        "risk_level": "increased_risk",
    },
    # IRS1 insulin signaling
    {
        "rsid": "rs2943641",
        "genotype": "TT",
        "interpretation": "IRS1 reference. Normal insulin receptor substrate signaling.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2943641",
        "genotype": "CT",
        "interpretation": (
            "IRS1 variant carrier. Mildly reduced IRS1 expression; modestly increased insulin "
            "resistance."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs2943641",
        "genotype": "CC",
        "interpretation": (
            "IRS1 variant homozygous. Reduced IRS1 in adipose tissue; increased insulin "
            "resistance risk."
        ),
        "risk_level": "increased_risk",
    },
    # DHCR7 vitamin D
    {
        "rsid": "rs12785878",
        "genotype": "GG",
        "interpretation": "DHCR7 reference. Standard vitamin D synthesis capacity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs12785878",
        "genotype": "GT",
        "interpretation": (
            "DHCR7 variant carrier. Modestly lower vitamin D levels; monitor 25(OH)D."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs12785878",
        "genotype": "TT",
        "interpretation": (
            "DHCR7 variant homozygous. Lower vitamin D levels; supplementation may benefit."
        ),
        "risk_level": "increased_risk",
    },
    # GC/VDBP vitamin D binding
    {
        "rsid": "rs2282679",
        "genotype": "AA",
        "interpretation": "GC reference. Normal vitamin D binding protein levels.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2282679",
        "genotype": "AC",
        "interpretation": "GC variant carrier. Mildly lower total 25(OH)D levels.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs2282679",
        "genotype": "CC",
        "interpretation": "GC variant homozygous. Lower total 25(OH)D; monitor vitamin D status.",
        "risk_level": "increased_risk",
    },
    # GC Thr436Lys
    {
        "rsid": "rs4588",
        "genotype": "CC",
        "interpretation": "GC Thr436. Common VDBP isoform with standard vitamin D binding.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4588",
        "genotype": "CA",
        "interpretation": "GC Thr436Lys carrier. Intermediate VDBP affinity; mildly lower 25(OH)D.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs4588",
        "genotype": "AA",
        "interpretation": (
            "GC Lys436 homozygous. Lower VDBP affinity; genetically lower 25(OH)D levels."
        ),
        "risk_level": "increased_risk",
    },
    # MTNR1B melatonin receptor
    {
        "rsid": "rs10830963",
        "genotype": "CC",
        "interpretation": "MTNR1B reference. Standard fasting glucose regulation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs10830963",
        "genotype": "CG",
        "interpretation": "MTNR1B variant carrier. Slightly elevated fasting glucose.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs10830963",
        "genotype": "GG",
        "interpretation": (
            "MTNR1B variant homozygous. Elevated fasting glucose; modestly increased T2D risk."
        ),
        "risk_level": "increased_risk",
    },
    # FADS1 fatty acid desaturase
    {
        "rsid": "rs174547",
        "genotype": "CC",
        "interpretation": (
            "FADS1 reference. Higher desaturase activity and arachidonic acid levels."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs174547",
        "genotype": "CT",
        "interpretation": "FADS1 variant carrier. Intermediate fatty acid desaturase activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs174547",
        "genotype": "TT",
        "interpretation": (
            "FADS1 variant homozygous. Lower desaturase activity; may benefit from preformed "
            "omega-3s."
        ),
        "risk_level": "normal",
    },
    # MTHFR A1298C
    {
        "rsid": "rs1801131",
        "genotype": "TT",
        "interpretation": "Normal MTHFR A1298 (wild-type). No reduction at this position.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801131",
        "genotype": "TG",
        "interpretation": "One copy of MTHFR A1298C. Modest reduction in enzyme activity.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1801131",
        "genotype": "GG",
        "interpretation": (
            "Homozygous MTHFR A1298C. Reduced enzyme activity; limited clinical significance."
        ),
        "risk_level": "increased_risk",
    },
    # HFE C282Y
    {
        "rsid": "rs1800562",
        "genotype": "GG",
        "interpretation": "No HFE C282Y mutation. Normal iron metabolism from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800562",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous HFE C282Y carrier. Low penetrance alone; check H63D status."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1800562",
        "genotype": "AA",
        "interpretation": (
            "Homozygous HFE C282Y. High risk of hereditary hemochromatosis. "
            "Serum ferritin and transferrin saturation monitoring recommended."
        ),
        "risk_level": "high_risk",
    },
    # HFE H63D
    {
        "rsid": "rs1799945",
        "genotype": "CC",
        "interpretation": "No HFE H63D variant. Normal iron metabolism from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1799945",
        "genotype": "CG",
        "interpretation": (
            "Heterozygous HFE H63D. Low risk alone; compound heterozygosity with C282Y increases "
            "risk."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1799945",
        "genotype": "GG",
        "interpretation": "Homozygous HFE H63D. Mildly increased iron overload risk.",
        "risk_level": "increased_risk",
    },
]
