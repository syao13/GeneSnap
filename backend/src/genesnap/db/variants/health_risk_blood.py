"""Blood disorder health risk variants: HBB, G6PD, F13A1, ABO, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    {
        "rsid": "rs334",
        "gene": "HBB",
        "category": "health_risk",
        "name": "Sickle cell trait (HbS)",
        "significance": "pathogenic",
        "description": (
            "The sickle cell mutation in beta-globin. Heterozygous carriers (sickle cell trait) "
            "have malaria resistance. Homozygous causes sickle cell disease."
        ),
        "risk_allele": "A",
        "normal_allele": "T",
        "chromosome": "11",
        "position": 5248232,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000015126"},
        "publications": ["1346618"],
        "clinvar_stars": 4,
        "odds_ratio": None,
    },
    {
        "rsid": "rs33930165",
        "gene": "HBB",
        "category": "health_risk",
        "name": "HbC trait (HBB E6K)",
        "significance": "pathogenic",
        "description": (
            "Hemoglobin C mutation (Glu6Lys) in beta-globin. Homozygous HbCC causes mild "
            "hemolytic anemia. Compound heterozygosity with HbS (HbSC disease) causes "
            "moderate sickle cell disease. Common in West African populations."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "11",
        "position": 5248233,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000015129"},
        "publications": ["1346618"],
        "clinvar_stars": 4,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1050828",
        "gene": "G6PD",
        "category": "health_risk",
        "name": "G6PD A- (Val68Met)",
        "significance": "pathogenic",
        "description": (
            "G6PD A- variant causing moderate enzyme deficiency. X-linked, primarily "
            "affecting males. Carriers are at risk of hemolytic anemia triggered by "
            "oxidative stress from infections, fava beans, or certain drugs "
            "(primaquine, dapsone, nitrofurantoin)."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "X",
        "position": 153764217,
        "source": "clinvar",
        "publications": ["2399226"],
        "clinvar_stars": 3,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1050829",
        "gene": "G6PD",
        "category": "health_risk",
        "name": "G6PD A+ (Asn126Asp)",
        "significance": "association",
        "description": (
            "G6PD A+ variant common in African populations. Alone it causes mild "
            "enzyme deficiency with normal clinical phenotype. Combined with the "
            "A- variant (rs1050828), defines the G6PD A- haplotype with moderate "
            "deficiency and hemolytic risk."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "X",
        "position": 153763492,
        "source": "clinvar",
        "publications": ["2399226"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs5030868",
        "gene": "G6PD",
        "category": "health_risk",
        "name": "G6PD Mediterranean (Ser188Phe)",
        "significance": "pathogenic",
        "description": (
            "G6PD Mediterranean variant causing severe enzyme deficiency. Common in "
            "Middle Eastern, Mediterranean, and South Asian populations. Causes severe "
            "hemolytic crises triggered by fava beans (favism) and oxidative drugs."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "X",
        "position": 153764051,
        "source": "clinvar",
        "publications": ["2399226"],
        "clinvar_stars": 4,
        "odds_ratio": None,
    },
    {
        "rsid": "rs6050",
        "gene": "FGA",
        "category": "health_risk",
        "name": "Fibrinogen alpha Thr312Ala",
        "significance": "association",
        "description": (
            "Fibrinogen alpha chain variant (Thr312Ala). The Ala312 allele produces "
            "thicker fibrin fibers that are more resistant to lysis, modestly increasing "
            "the risk of venous thromboembolism and stroke."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "4",
        "position": 155529187,
        "source": "gwas_catalog",
        "publications": ["11893757"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs1801020",
        "gene": "F12",
        "category": "health_risk",
        "name": "Factor XII 46C>T (Hageman factor deficiency)",
        "significance": "association",
        "description": (
            "Variant in the 5'-UTR of coagulation factor XII. The T allele reduces "
            "Factor XII levels, which paradoxically may protect against thrombosis "
            "while causing prolonged aPTT in lab tests. Factor XII deficiency is not "
            "associated with clinical bleeding."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "5",
        "position": 176837532,
        "source": "clinvar",
        "publications": ["10799386"],
        "clinvar_stars": 1,
        "odds_ratio": None,
    },
    {
        "rsid": "rs5985",
        "gene": "F13A1",
        "category": "health_risk",
        "name": "Factor XIII Val34Leu",
        "significance": "association",
        "description": (
            "Factor XIII A subunit variant (Val34Leu). The Leu34 allele is activated "
            "faster by thrombin, producing a finer and more tightly cross-linked fibrin "
            "clot. Associated with modestly reduced risk of venous thrombosis but "
            "may increase risk of certain hemorrhagic conditions."
        ),
        "risk_allele": "T",
        "normal_allele": "G",
        "chromosome": "6",
        "position": 6318795,
        "source": "gwas_catalog",
        "publications": ["10369261"],
        "clinvar_stars": 1,
        "odds_ratio": 0.8,
    },
    {
        "rsid": "rs3218713",
        "gene": "VWF",
        "category": "health_risk",
        "name": "VWF promoter variant (von Willebrand levels)",
        "significance": "association",
        "description": (
            "Von Willebrand factor promoter variant affecting VWF plasma levels. "
            "VWF is essential for primary hemostasis; low levels cause von Willebrand "
            "disease (the most common bleeding disorder), while high levels increase "
            "thrombotic risk."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "12",
        "position": 6128085,
        "source": "gwas_catalog",
        "publications": ["21339740"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # HBB sickle cell
    {
        "rsid": "rs334",
        "genotype": "TT",
        "interpretation": "Normal hemoglobin. No sickle cell trait.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs334",
        "genotype": "AT",
        "interpretation": "Sickle cell trait carrier. Malaria resistance; generally asymptomatic.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs334",
        "genotype": "AA",
        "interpretation": "Sickle cell disease. Requires medical management.",
        "risk_level": "high_risk",
    },
    # HBB HbC trait
    {
        "rsid": "rs33930165",
        "genotype": "GG",
        "interpretation": "Normal hemoglobin at this locus. No HbC trait.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs33930165",
        "genotype": "AG",
        "interpretation": (
            "HbC carrier. Usually asymptomatic; compound heterozygosity with HbS causes HbSC "
            "disease."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs33930165",
        "genotype": "AA",
        "interpretation": "Homozygous HbCC. Mild hemolytic anemia; splenomegaly possible.",
        "risk_level": "increased_risk",
    },
    # G6PD A- (Val68Met)
    {
        "rsid": "rs1050828",
        "genotype": "TT",
        "interpretation": "Normal G6PD at this position. No A- variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1050828",
        "genotype": "CT",
        "interpretation": (
            "G6PD A- carrier (female heterozygous). Mosaic enzyme deficiency due to X-inactivation."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs1050828",
        "genotype": "CC",
        "interpretation": (
            "G6PD A- deficient. Hemolytic risk from oxidative drugs, fava beans, and infections."
        ),
        "risk_level": "high_risk",
    },
    # G6PD A+ (Asn126Asp)
    {
        "rsid": "rs1050829",
        "genotype": "AA",
        "interpretation": "Normal G6PD at this position. No A+ variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1050829",
        "genotype": "AG",
        "interpretation": (
            "G6PD A+ carrier. Mild enzyme variant; clinical significance mainly with A- "
            "(rs1050828)."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1050829",
        "genotype": "GG",
        "interpretation": (
            "G6PD A+ homozygous/hemizygous. Mild enzyme alteration; check A- status for full "
            "phenotype."
        ),
        "risk_level": "carrier",
    },
    # G6PD Mediterranean
    {
        "rsid": "rs5030868",
        "genotype": "CC",
        "interpretation": "Normal G6PD at this position. No Mediterranean variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs5030868",
        "genotype": "CT",
        "interpretation": (
            "G6PD Mediterranean carrier (female). Variable enzyme deficiency due to X-inactivation."
        ),
        "risk_level": "carrier",
    },
    {
        "rsid": "rs5030868",
        "genotype": "TT",
        "interpretation": (
            "G6PD Mediterranean deficient. Severe favism risk; avoid fava beans and oxidative "
            "drugs."
        ),
        "risk_level": "high_risk",
    },
    # FGA Thr312Ala
    {
        "rsid": "rs6050",
        "genotype": "AA",
        "interpretation": "Fibrinogen Thr312. Normal fibrin structure and clot properties.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs6050",
        "genotype": "AG",
        "interpretation": "Heterozygous Thr312Ala. Slightly altered fibrin fiber thickness.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs6050",
        "genotype": "GG",
        "interpretation": (
            "Fibrinogen Ala312 homozygous. Thicker fibrin fibers; modestly increased VTE risk."
        ),
        "risk_level": "increased_risk",
    },
    # F12 46C>T
    {
        "rsid": "rs1801020",
        "genotype": "CC",
        "interpretation": "Normal Factor XII levels. Standard aPTT expected.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801020",
        "genotype": "CT",
        "interpretation": (
            "Reduced Factor XII levels. May have mildly prolonged aPTT without bleeding risk."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801020",
        "genotype": "TT",
        "interpretation": "Low Factor XII. Prolonged aPTT in lab tests; no clinical bleeding risk.",
        "risk_level": "normal",
    },
    # F13A1 Val34Leu
    {
        "rsid": "rs5985",
        "genotype": "GG",
        "interpretation": "Factor XIII Val34. Standard fibrin cross-linking kinetics.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs5985",
        "genotype": "GT",
        "interpretation": (
            "Heterozygous Val34Leu. Faster Factor XIII activation; slightly altered clot structure."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs5985",
        "genotype": "TT",
        "interpretation": (
            "Factor XIII Leu34 homozygous. Faster activation; modestly reduced VTE risk."
        ),
        "risk_level": "normal",
    },
    # VWF promoter
    {
        "rsid": "rs3218713",
        "genotype": "GG",
        "interpretation": "Normal VWF promoter. Standard von Willebrand factor levels.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs3218713",
        "genotype": "AG",
        "interpretation": "Heterozygous VWF promoter variant. May have mildly altered VWF levels.",
        "risk_level": "carrier",
    },
    {
        "rsid": "rs3218713",
        "genotype": "AA",
        "interpretation": (
            "Homozygous VWF promoter variant. Altered VWF levels; assess if bleeding symptoms "
            "present."
        ),
        "risk_level": "increased_risk",
    },
]
