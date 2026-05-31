"""Trait-associated variants: eye color, hair, taste, chronotype, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    {
        "rsid": "rs4988235",
        "gene": "MCM6/LCT",
        "category": "trait",
        "name": "Lactose tolerance/intolerance",
        "significance": "association",
        "description": (
            "Primary variant determining lactase persistence in European populations. "
            "A allele = lactase persistent (can digest lactose into adulthood). "
            "GG genotype = lactase non-persistent (lactose intolerant)."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "2",
        "position": 136608646,
        "source": "gwas_catalog",
        "publications": ["11788828"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1815739",
        "gene": "ACTN3",
        "category": "trait",
        "name": "ACTN3 R577X (muscle fiber type)",
        "significance": "association",
        "description": (
            "Determines alpha-actinin-3 expression in fast-twitch muscle fibers. "
            "CC = functional protein (sprint/power advantage). "
            "TT = no alpha-actinin-3 (may favor endurance). "
            "Very common variant with modest athletic effects."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "11",
        "position": 66560624,
        "source": "gwas_catalog",
        "publications": ["12879365"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs671",
        "gene": "ALDH2",
        "category": "trait",
        "name": "Alcohol flush reaction",
        "significance": "association",
        "description": (
            "ALDH2 deficiency causing alcohol flush reaction. Common in East Asian "
            "populations. A allele carriers accumulate acetaldehyde, causing facial "
            "flushing and nausea. Also associated with increased esophageal cancer risk "
            "with chronic alcohol use."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "12",
        "position": 112241766,
        "source": "clinvar",
        "publications": ["16385451"],
        "clinvar_stars": 2,
        "odds_ratio": None,
    },
    {
        "rsid": "rs601338",
        "gene": "FUT2",
        "category": "trait",
        "name": "Secretor status (norovirus resistance)",
        "significance": "association",
        "description": (
            "Determines FUT2 secretor status. AA genotype = non-secretor, "
            "conferring ~3x resistance to norovirus. Also affects gut microbiome "
            "composition and vitamin B12 levels."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "19",
        "position": 49206674,
        "source": "gwas_catalog",
        "publications": ["21321315"],
        "clinvar_stars": 0,
        "odds_ratio": 3.0,
    },
    {
        "rsid": "rs1800497",
        "gene": "DRD2/ANKK1",
        "category": "trait",
        "name": "Taq1A (dopamine receptor density)",
        "significance": "association",
        "description": (
            "Located near the DRD2 gene. A1 allele (T) is associated with reduced "
            "striatal D2/D3 receptor density and has been extensively studied in "
            "context of addiction susceptibility and reward processing."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "11",
        "position": 113270828,
        "source": "gwas_catalog",
        "publications": ["2234286"],
        "clinvar_stars": 0,
        "odds_ratio": 1.3,
    },
    {
        "rsid": "rs53576",
        "gene": "OXTR",
        "category": "trait",
        "name": "Oxytocin receptor (empathy/social behavior)",
        "significance": "association",
        "description": (
            "Oxytocin receptor variant associated with social behavior. GG genotype "
            "linked to higher empathic ability and social sensitivity. AA/AG genotypes "
            "associated with lower dispositional empathy and higher stress reactivity."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "3",
        "position": 8804371,
        "source": "gwas_catalog",
        "publications": ["19934046"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4680",
        "gene": "COMT",
        "category": "trait",
        "name": "COMT Val158Met (stress response)",
        "significance": "association",
        "description": (
            "COMT enzyme activity variant. GG (Val/Val) = 'warrior' phenotype with "
            "higher stress tolerance but lower cognitive performance under no stress. "
            "AA (Met/Met) = 'worrier' phenotype with better cognitive performance "
            "but higher stress sensitivity."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "22",
        "position": 19951271,
        "source": "gwas_catalog",
        "publications": ["14592368"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1695",
        "gene": "GSTP1",
        "category": "trait",
        "name": "GSTP1 Ile105Val (detoxification)",
        "significance": "association",
        "description": (
            "Phase II detoxification enzyme variant. G allele (Val) reduces enzyme "
            "activity, potentially affecting clearance of certain environmental toxins "
            "and chemotherapy drugs."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "11",
        "position": 67352689,
        "source": "gwas_catalog",
        "publications": ["10987263"],
        "clinvar_stars": 0,
        "odds_ratio": 1.2,
    },
    {
        "rsid": "rs1042713",
        "gene": "ADRB2",
        "category": "trait",
        "name": "Beta-2 adrenergic receptor (Arg16Gly)",
        "significance": "association",
        "description": (
            "Beta-2 adrenergic receptor variant studied in asthma and exercise "
            "response. Gly16 (G allele) associated with enhanced receptor "
            "downregulation and variable bronchodilator response."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "5",
        "position": 148206440,
        "source": "gwas_catalog",
        "publications": ["10762530"],
        "clinvar_stars": 0,
        "odds_ratio": 1.3,
    },
    # ---- New trait variants ----
    {
        "rsid": "rs12913832",
        "gene": "HERC2",
        "category": "trait",
        "name": "HERC2/OCA2 eye color (blue/brown)",
        "significance": "association",
        "description": (
            "Primary determinant of blue vs. brown eye color in Europeans. This "
            "intronic HERC2 variant regulates OCA2 expression. AA genotype strongly "
            "predicts blue eyes; GG predicts brown eyes. Explains ~75% of eye color "
            "variation in European populations."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "15",
        "position": 28365618,
        "source": "gwas_catalog",
        "publications": ["18172690"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1800407",
        "gene": "OCA2",
        "category": "trait",
        "name": "OCA2 R419Q eye color modifier",
        "significance": "association",
        "description": (
            "Modifier of eye color within the OCA2 gene. The T allele (419Q) can shift "
            "eye color toward green or hazel in individuals who otherwise would have "
            "brown eyes. Contributes to the continuous spectrum of iris pigmentation."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "15",
        "position": 28230318,
        "source": "gwas_catalog",
        "publications": ["17236130"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs16891982",
        "gene": "SLC45A2",
        "category": "trait",
        "name": "SLC45A2 L374F (skin pigmentation)",
        "significance": "association",
        "description": (
            "Major contributor to light skin pigmentation in Europeans. The G allele "
            "(Leu374) is associated with darker pigmentation, while C (Phe374) is "
            "nearly fixed in European populations and associated with lighter skin."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "5",
        "position": 33951693,
        "source": "gwas_catalog",
        "publications": ["17182896"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1426654",
        "gene": "SLC24A5",
        "category": "trait",
        "name": "SLC24A5 A111T (skin pigmentation)",
        "significance": "association",
        "description": (
            "One of the strongest determinants of skin pigmentation difference between "
            "European and African populations. The A allele (Thr111) is nearly fixed "
            "in Europeans and is associated with lighter skin pigmentation."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "15",
        "position": 48426484,
        "source": "gwas_catalog",
        "publications": ["16357253"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1805007",
        "gene": "MC1R",
        "category": "trait",
        "name": "MC1R R151C (red hair / fair skin)",
        "significance": "association",
        "description": (
            "Loss-of-function variant in the melanocortin 1 receptor. T allele (Cys151) "
            "is one of the strongest red hair determinants. Homozygotes or compound "
            "heterozygotes with other MC1R variants frequently have red hair, fair "
            "skin, and increased UV sensitivity."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "16",
        "position": 89986091,
        "source": "gwas_catalog",
        "publications": ["11260714"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1805008",
        "gene": "MC1R",
        "category": "trait",
        "name": "MC1R R160W (red hair / fair skin)",
        "significance": "association",
        "description": (
            "Another MC1R loss-of-function variant. The T allele (Trp160) reduces "
            "receptor signaling, shifting melanin production from eumelanin to "
            "pheomelanin. Contributes to red hair and freckling phenotype."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "16",
        "position": 89986117,
        "source": "gwas_catalog",
        "publications": ["11260714"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4481887",
        "gene": "OR6A2",
        "category": "trait",
        "name": "OR6A2 cilantro taste perception (soapy)",
        "significance": "association",
        "description": (
            "Olfactory receptor variant associated with detecting aldehydes in cilantro "
            "that give it a soapy taste. A allele carriers are more likely to perceive "
            "cilantro as soapy or unpleasant."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "11",
        "position": 7915250,
        "source": "gwas_catalog",
        "publications": ["22927872"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs713598",
        "gene": "TAS2R38",
        "category": "trait",
        "name": "TAS2R38 A49P (bitter taste / PTC)",
        "significance": "association",
        "description": (
            "One of three key SNPs in the bitter taste receptor TAS2R38 determining "
            "ability to taste PTC/PROP. C allele (Pro49) contributes to the taster "
            "haplotype (PAV). Part of the PAV/AVI haplotype system."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "7",
        "position": 141673345,
        "source": "gwas_catalog",
        "publications": ["12595690"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1726866",
        "gene": "TAS2R38",
        "category": "trait",
        "name": "TAS2R38 V262A (bitter taste #2)",
        "significance": "association",
        "description": (
            "Second of three TAS2R38 haplotype-defining SNPs. The C allele (Ala262) "
            "is part of the PAV taster haplotype. Combined with rs713598 and rs10246939, "
            "determines PTC/PROP bitter taste sensitivity."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "7",
        "position": 141672604,
        "source": "gwas_catalog",
        "publications": ["12595690"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs10246939",
        "gene": "TAS2R38",
        "category": "trait",
        "name": "TAS2R38 I296V (bitter taste #3)",
        "significance": "association",
        "description": (
            "Third TAS2R38 haplotype SNP. The C allele (Val296) completes the PAV "
            "taster haplotype. Individuals homozygous for PAV are supertasters of "
            "PTC/PROP bitter compounds."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "7",
        "position": 141672705,
        "source": "gwas_catalog",
        "publications": ["12595690"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4950928",
        "gene": "CHI3L1",
        "category": "trait",
        "name": "CHI3L1 -131C/G (asparagus anosmia)",
        "significance": "association",
        "description": (
            "Variant near the CHI3L1 gene associated with the ability to smell "
            "asparagus metabolites in urine. G allele carriers are more likely to "
            "experience asparagus anosmia (inability to detect the odor)."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "1",
        "position": 203156090,
        "source": "gwas_catalog",
        "publications": ["27189318"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs17822931",
        "gene": "ABCC11",
        "category": "trait",
        "name": "ABCC11 G180R (ear wax type)",
        "significance": "association",
        "description": (
            "Determines wet vs. dry earwax type and apocrine gland secretion. "
            "TT genotype = dry earwax (common in East Asians); CC/CT = wet earwax "
            "(common in Europeans/Africans). Also associated with axillary odor."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "16",
        "position": 48258198,
        "source": "gwas_catalog",
        "publications": ["16444273"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1800795",
        "gene": "IL6",
        "category": "trait",
        "name": "IL-6 -174G/C (inflammation response)",
        "significance": "association",
        "description": (
            "Promoter variant in the interleukin-6 gene affecting IL-6 expression. "
            "C allele is associated with lower IL-6 levels. GG genotype linked to "
            "higher inflammatory response, which may influence recovery, aging, "
            "and exercise adaptation."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "7",
        "position": 22766645,
        "source": "gwas_catalog",
        "publications": ["9804220"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs7495174",
        "gene": "OCA2",
        "category": "trait",
        "name": "OCA2 intron 1 eye color #2",
        "significance": "association",
        "description": (
            "Intronic OCA2 variant contributing to eye color variation. Works in "
            "combination with rs12913832 (HERC2) and other OCA2 SNPs to fine-tune "
            "iris pigmentation levels."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "15",
        "position": 28288121,
        "source": "gwas_catalog",
        "publications": ["17236130"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs12821256",
        "gene": "KITLG",
        "category": "trait",
        "name": "KITLG blonde hair association",
        "significance": "association",
        "description": (
            "Regulatory variant near KITLG (KIT ligand / stem cell factor) associated "
            "with blonde hair in Europeans. The C allele is associated with lighter "
            "hair color through effects on melanocyte development and function."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "12",
        "position": 89328335,
        "source": "gwas_catalog",
        "publications": ["24927565"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4778138",
        "gene": "OCA2",
        "category": "trait",
        "name": "OCA2 eye color #3",
        "significance": "association",
        "description": (
            "OCA2 variant contributing to iris pigmentation. Part of the multi-SNP "
            "haplotype in the HERC2-OCA2 region that collectively determines eye "
            "color through regulation of melanin production in melanocytes."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "15",
        "position": 28335820,
        "source": "gwas_catalog",
        "publications": ["18252222"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1799971",
        "gene": "OPRM1",
        "category": "trait",
        "name": "OPRM1 A118G (pain sensitivity)",
        "significance": "association",
        "description": (
            "Mu-opioid receptor variant. G allele (Asp118) alters receptor binding "
            "and is associated with higher pain sensitivity, increased opioid "
            "requirements for analgesia, and altered stress and reward responses."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "6",
        "position": 154360797,
        "source": "gwas_catalog",
        "publications": ["15583226"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4778241",
        "gene": "OCA2",
        "category": "trait",
        "name": "OCA2 eye color #4",
        "significance": "association",
        "description": (
            "Additional OCA2 regulatory variant involved in eye color determination. "
            "Contributes to the polygenic model of iris pigmentation in combination "
            "with other variants in the HERC2-OCA2 locus."
        ),
        "risk_allele": "A",
        "normal_allele": "C",
        "chromosome": "15",
        "position": 28344238,
        "source": "gwas_catalog",
        "publications": ["18252222"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs2228479",
        "gene": "MC1R",
        "category": "trait",
        "name": "MC1R V92M (red hair modifier)",
        "significance": "association",
        "description": (
            "Partial loss-of-function MC1R variant. The A allele (Met92) has a milder "
            "effect than R151C or R160W but still shifts melanin balance toward "
            "pheomelanin. Can contribute to red/auburn hair when combined with other "
            "MC1R variants."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "16",
        "position": 89985844,
        "source": "gwas_catalog",
        "publications": ["11260714"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1800955",
        "gene": "DRD4",
        "category": "trait",
        "name": "DRD4 -521C/T (novelty seeking)",
        "significance": "association",
        "description": (
            "Promoter variant in the dopamine receptor D4 gene. The T allele reduces "
            "transcriptional efficiency and has been associated with novelty seeking "
            "behavior and attention traits in some populations."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "11",
        "position": 637451,
        "source": "gwas_catalog",
        "publications": ["10205525"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs4633",
        "gene": "COMT",
        "category": "trait",
        "name": "COMT synonymous (pain sensitivity haplotype)",
        "significance": "association",
        "description": (
            "Synonymous COMT variant in strong linkage disequilibrium with rs4680 "
            "(Val158Met). Contributes to the COMT pain sensitivity haplotype. "
            "C allele is associated with higher COMT activity and lower pain "
            "sensitivity."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "22",
        "position": 19951207,
        "source": "gwas_catalog",
        "publications": ["16380905"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs324420",
        "gene": "FAAH",
        "category": "trait",
        "name": "FAAH C385A (endocannabinoid levels)",
        "significance": "association",
        "description": (
            "Fatty acid amide hydrolase variant. A allele (Thr385) leads to reduced "
            "FAAH protein levels and elevated endocannabinoid (anandamide) signaling. "
            "Associated with reduced anxiety, enhanced threat extinction, and lower "
            "reported pain."
        ),
        "risk_allele": "A",
        "normal_allele": "C",
        "chromosome": "1",
        "position": 46870484,
        "source": "gwas_catalog",
        "publications": ["15205295"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1800588",
        "gene": "LIPC",
        "category": "trait",
        "name": "LIPC -514C/T (HDL cholesterol)",
        "significance": "association",
        "description": (
            "Promoter variant in hepatic lipase gene. The T allele reduces hepatic "
            "lipase activity and is associated with higher HDL cholesterol levels. "
            "One of the established HDL-modifying variants from GWAS."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "15",
        "position": 58723675,
        "source": "gwas_catalog",
        "publications": ["10373914"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs662799",
        "gene": "APOA5",
        "category": "trait",
        "name": "APOA5 -1131T/C (triglycerides)",
        "significance": "association",
        "description": (
            "Promoter variant in apolipoprotein A5. The C allele is associated with "
            "higher triglyceride levels (approximately 15-20% increase) and modestly "
            "increased cardiovascular risk. Robust GWAS signal for triglyceride levels."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "11",
        "position": 116662407,
        "source": "gwas_catalog",
        "publications": ["11788828"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs1801260",
        "gene": "CLOCK",
        "category": "trait",
        "name": "CLOCK 3111T/C (chronotype / morningness)",
        "significance": "association",
        "description": (
            "Variant in the 3'-UTR of the circadian clock gene CLOCK. C allele has "
            "been associated with evening preference (delayed sleep phase) and "
            "differences in sleep duration. Contributes to the genetic basis of "
            "chronotype variation."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "4",
        "position": 56294068,
        "source": "gwas_catalog",
        "publications": ["11562457"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
    {
        "rsid": "rs57875989",
        "gene": "BHLHE41",
        "category": "trait",
        "name": "DEC2/BHLHE41 P384R (short sleeper)",
        "significance": "association",
        "description": (
            "Rare variant in the DEC2 transcription repressor. Carriers naturally "
            "require less sleep (~6 hours instead of 8) without adverse effects. "
            "Identified through a family-based study of natural short sleepers."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "12",
        "position": 26123753,
        "source": "gwas_catalog",
        "publications": ["19641203"],
        "clinvar_stars": 0,
        "odds_ratio": None,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # Lactose tolerance
    {
        "rsid": "rs4988235",
        "genotype": "AA",
        "interpretation": "Lactase persistent. Can digest lactose into adulthood.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4988235",
        "genotype": "AG",
        "interpretation": "Lactase persistent (A is dominant). Can digest lactose.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4988235",
        "genotype": "GG",
        "interpretation": "Lactase non-persistent. Likely lactose intolerant.",
        "risk_level": "increased_risk",
    },
    # ACTN3 muscle type
    {
        "rsid": "rs1815739",
        "genotype": "CC",
        "interpretation": "Functional ACTN3. Fast-twitch muscle fibers. Sprint/power favored.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1815739",
        "genotype": "CT",
        "interpretation": "One functional copy. Mixed muscle fiber advantage.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1815739",
        "genotype": "TT",
        "interpretation": "No ACTN3 in fast-twitch fibers. May favor endurance activities.",
        "risk_level": "normal",
    },
    # ALDH2 alcohol flush
    {
        "rsid": "rs671",
        "genotype": "GG",
        "interpretation": "Normal ALDH2 function. No alcohol flush reaction.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs671",
        "genotype": "AG",
        "interpretation": "Reduced ALDH2 activity. Alcohol flush reaction likely.",
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs671",
        "genotype": "AA",
        "interpretation": "ALDH2 deficient. Strong alcohol flush. Elevated esophageal cancer risk.",
        "risk_level": "high_risk",
    },
    # COMT
    {
        "rsid": "rs4680",
        "genotype": "GG",
        "interpretation": (
            "Val/Val ('warrior'). Higher COMT activity, better stress"
            " tolerance, lower baseline cognition."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs4680",
        "genotype": "AG",
        "interpretation": "Val/Met (intermediate). Balanced COMT activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4680",
        "genotype": "AA",
        "interpretation": (
            "Met/Met ('worrier'). Lower COMT activity, higher cognitive"
            " performance, more stress-sensitive."
        ),
        "risk_level": "normal",
    },
    # FUT2 secretor status
    {
        "rsid": "rs601338",
        "genotype": "GG",
        "interpretation": "Secretor (FUT2 functional). Standard norovirus susceptibility.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs601338",
        "genotype": "GA",
        "interpretation": "Secretor (G dominant). Carrier of non-secretor allele.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs601338",
        "genotype": "AA",
        "interpretation": "Non-secretor. ~3x resistance to norovirus; altered gut microbiome.",
        "risk_level": "normal",
    },
    # DRD2/ANKK1 Taq1A
    {
        "rsid": "rs1800497",
        "genotype": "CC",
        "interpretation": "No Taq1A variant. Normal D2/D3 receptor density.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800497",
        "genotype": "CT",
        "interpretation": "One Taq1A allele. Modestly reduced D2 receptor density.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800497",
        "genotype": "TT",
        "interpretation": (
            "Homozygous Taq1A. Reduced D2/D3 receptor density; studied in addiction context."
        ),
        "risk_level": "increased_risk",
    },
    # OXTR empathy
    {
        "rsid": "rs53576",
        "genotype": "GG",
        "interpretation": "Higher empathic ability and social sensitivity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs53576",
        "genotype": "AG",
        "interpretation": "Intermediate social sensitivity and empathy.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs53576",
        "genotype": "AA",
        "interpretation": "Lower dispositional empathy; higher stress reactivity.",
        "risk_level": "normal",
    },
    # GSTP1 detox
    {
        "rsid": "rs1695",
        "genotype": "AA",
        "interpretation": "Normal GSTP1 (Ile/Ile). Standard detoxification capacity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1695",
        "genotype": "AG",
        "interpretation": "GSTP1 Ile/Val. Slightly reduced detoxification activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1695",
        "genotype": "GG",
        "interpretation": "GSTP1 Val/Val. Reduced detoxification of certain environmental toxins.",
        "risk_level": "increased_risk",
    },
    # ADRB2 Arg16Gly
    {
        "rsid": "rs1042713",
        "genotype": "AA",
        "interpretation": "Arg16 homozygous. Normal beta-2 receptor downregulation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1042713",
        "genotype": "AG",
        "interpretation": "Arg16Gly heterozygous. Intermediate receptor downregulation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1042713",
        "genotype": "GG",
        "interpretation": (
            "Gly16 homozygous. Enhanced receptor downregulation; variable bronchodilator response."
        ),
        "risk_level": "normal",
    },
    # ---- New genotype interpretations ----
    # HERC2/OCA2 eye color
    {
        "rsid": "rs12913832",
        "genotype": "AA",
        "interpretation": "Strongly predicts blue or light-colored eyes.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs12913832",
        "genotype": "AG",
        "interpretation": "Green or hazel eyes likely. Intermediate OCA2 expression.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs12913832",
        "genotype": "GG",
        "interpretation": "Strongly predicts brown eyes. Full OCA2 expression.",
        "risk_level": "normal",
    },
    # OCA2 R419Q eye color modifier
    {
        "rsid": "rs1800407",
        "genotype": "CC",
        "interpretation": "Typical OCA2 function. No modification of baseline eye color.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800407",
        "genotype": "CT",
        "interpretation": "May shift eye color toward green/hazel from brown.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800407",
        "genotype": "TT",
        "interpretation": "Reduced OCA2 function. Green or lighter eye color more likely.",
        "risk_level": "normal",
    },
    # SLC45A2 skin pigmentation
    {
        "rsid": "rs16891982",
        "genotype": "CC",
        "interpretation": "Phe374 homozygous. Associated with lighter skin pigmentation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs16891982",
        "genotype": "CG",
        "interpretation": "Heterozygous. Intermediate pigmentation effect.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs16891982",
        "genotype": "GG",
        "interpretation": "Leu374 homozygous. Associated with darker skin pigmentation.",
        "risk_level": "normal",
    },
    # SLC24A5 skin pigmentation
    {
        "rsid": "rs1426654",
        "genotype": "AA",
        "interpretation": (
            "Thr111 homozygous. Associated with lighter skin (nearly fixed in Europeans)."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1426654",
        "genotype": "AG",
        "interpretation": "Heterozygous. Intermediate skin pigmentation effect.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1426654",
        "genotype": "GG",
        "interpretation": "Ala111 homozygous. Associated with darker skin pigmentation.",
        "risk_level": "normal",
    },
    # MC1R R151C (red hair)
    {
        "rsid": "rs1805007",
        "genotype": "CC",
        "interpretation": "Normal MC1R function at this position. No red hair from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1805007",
        "genotype": "CT",
        "interpretation": (
            "Carrier of R151C. Possible auburn tones; red hair if compound heterozygous."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1805007",
        "genotype": "TT",
        "interpretation": (
            "Homozygous R151C. High likelihood of red hair, fair skin, and freckling."
        ),
        "risk_level": "normal",
    },
    # MC1R R160W (red hair)
    {
        "rsid": "rs1805008",
        "genotype": "CC",
        "interpretation": "Normal MC1R function at this position. No red hair from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1805008",
        "genotype": "CT",
        "interpretation": (
            "Carrier of R160W. Possible auburn tones; red hair if compound heterozygous."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1805008",
        "genotype": "TT",
        "interpretation": "Homozygous R160W. High likelihood of red hair and fair skin.",
        "risk_level": "normal",
    },
    # OR6A2 cilantro taste
    {
        "rsid": "rs4481887",
        "genotype": "GG",
        "interpretation": "Typical cilantro perception. Less likely to find cilantro soapy.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4481887",
        "genotype": "AG",
        "interpretation": "Possible mild soapy perception of cilantro.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4481887",
        "genotype": "AA",
        "interpretation": "Increased likelihood of perceiving cilantro as soapy/unpleasant.",
        "risk_level": "normal",
    },
    # TAS2R38 A49P (bitter taste / PTC)
    {
        "rsid": "rs713598",
        "genotype": "CC",
        "interpretation": "Pro49 homozygous (PAV haplotype component). PTC/PROP taster.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs713598",
        "genotype": "CG",
        "interpretation": "Heterozygous. Intermediate PTC/PROP bitter sensitivity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs713598",
        "genotype": "GG",
        "interpretation": "Ala49 homozygous (AVI haplotype component). PTC/PROP non-taster likely.",
        "risk_level": "normal",
    },
    # TAS2R38 V262A (bitter taste #2)
    {
        "rsid": "rs1726866",
        "genotype": "CC",
        "interpretation": "Ala262 homozygous (PAV component). Contributes to taster haplotype.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1726866",
        "genotype": "CT",
        "interpretation": "Heterozygous. Intermediate bitter taste perception.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1726866",
        "genotype": "TT",
        "interpretation": "Val262 homozygous (AVI component). Contributes to non-taster haplotype.",
        "risk_level": "normal",
    },
    # TAS2R38 I296V (bitter taste #3)
    {
        "rsid": "rs10246939",
        "genotype": "CC",
        "interpretation": "Val296 homozygous (PAV component). Strong PTC/PROP taster.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs10246939",
        "genotype": "CT",
        "interpretation": "Heterozygous. Medium PTC/PROP bitter taste sensitivity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs10246939",
        "genotype": "TT",
        "interpretation": "Ile296 homozygous (AVI component). PTC/PROP non-taster likely.",
        "risk_level": "normal",
    },
    # CHI3L1 asparagus smell
    {
        "rsid": "rs4950928",
        "genotype": "CC",
        "interpretation": "Likely able to smell asparagus metabolites in urine.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4950928",
        "genotype": "CG",
        "interpretation": "Reduced ability to detect asparagus odor in urine.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4950928",
        "genotype": "GG",
        "interpretation": "Asparagus anosmia likely. Cannot smell asparagus metabolites.",
        "risk_level": "normal",
    },
    # ABCC11 ear wax type
    {
        "rsid": "rs17822931",
        "genotype": "CC",
        "interpretation": "Wet earwax type. Typical apocrine gland secretion.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs17822931",
        "genotype": "CT",
        "interpretation": "Wet earwax type (C is dominant). Carrier of dry earwax allele.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs17822931",
        "genotype": "TT",
        "interpretation": "Dry earwax type. Reduced apocrine secretion and body odor.",
        "risk_level": "normal",
    },
    # IL6 -174G/C inflammation
    {
        "rsid": "rs1800795",
        "genotype": "GG",
        "interpretation": "Higher IL-6 expression. Stronger inflammatory response.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800795",
        "genotype": "GC",
        "interpretation": "Intermediate IL-6 expression. Moderate inflammatory response.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800795",
        "genotype": "CC",
        "interpretation": "Lower IL-6 expression. Reduced inflammatory baseline.",
        "risk_level": "normal",
    },
    # OCA2 eye color #2
    {
        "rsid": "rs7495174",
        "genotype": "GG",
        "interpretation": "Typical OCA2 regulation. Brown eye color contribution.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs7495174",
        "genotype": "AG",
        "interpretation": "Intermediate effect on OCA2 expression and eye color.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs7495174",
        "genotype": "AA",
        "interpretation": "Reduced OCA2 expression. Contributes to lighter eye color.",
        "risk_level": "normal",
    },
    # KITLG blonde hair
    {
        "rsid": "rs12821256",
        "genotype": "TT",
        "interpretation": "Typical hair pigmentation at this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs12821256",
        "genotype": "CT",
        "interpretation": "Carrier of blonde-associated allele. Modestly lighter hair color.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs12821256",
        "genotype": "CC",
        "interpretation": "Blonde hair association. Lighter hair color likely in Europeans.",
        "risk_level": "normal",
    },
    # OCA2 eye color #3
    {
        "rsid": "rs4778138",
        "genotype": "GG",
        "interpretation": "Standard OCA2 expression. Brown eye color contribution.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4778138",
        "genotype": "AG",
        "interpretation": "Intermediate iris pigmentation effect.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4778138",
        "genotype": "AA",
        "interpretation": "Reduced melanin in iris. Lighter eye color contribution.",
        "risk_level": "normal",
    },
    # OPRM1 pain sensitivity
    {
        "rsid": "rs1799971",
        "genotype": "AA",
        "interpretation": (
            "Typical mu-opioid receptor. Normal pain sensitivity and opioid response."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1799971",
        "genotype": "AG",
        "interpretation": (
            "Carrier of 118G. Modestly increased pain sensitivity; may need higher opioid doses."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1799971",
        "genotype": "GG",
        "interpretation": (
            "Homozygous 118G. Higher pain sensitivity; may require significantly more opioid for "
            "analgesia."
        ),
        "risk_level": "increased_risk",
    },
    # OCA2 eye color #4
    {
        "rsid": "rs4778241",
        "genotype": "CC",
        "interpretation": "Standard OCA2 regulation at this locus. Brown eye contribution.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4778241",
        "genotype": "AC",
        "interpretation": "Intermediate effect on iris pigmentation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4778241",
        "genotype": "AA",
        "interpretation": "Contributes to lighter iris pigmentation.",
        "risk_level": "normal",
    },
    # MC1R V92M (red hair modifier)
    {
        "rsid": "rs2228479",
        "genotype": "GG",
        "interpretation": "Normal MC1R function at Val92. No red hair effect from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2228479",
        "genotype": "AG",
        "interpretation": (
            "Carrier of V92M. Mild shift toward pheomelanin; may contribute to auburn tones."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs2228479",
        "genotype": "AA",
        "interpretation": "Homozygous V92M. Moderate shift toward red/auburn hair pigmentation.",
        "risk_level": "normal",
    },
    # DRD4 novelty seeking
    {
        "rsid": "rs1800955",
        "genotype": "CC",
        "interpretation": "Higher DRD4 promoter activity. Typical novelty seeking behavior.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800955",
        "genotype": "CT",
        "interpretation": "Intermediate DRD4 expression. Modestly altered novelty seeking.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800955",
        "genotype": "TT",
        "interpretation": (
            "Reduced DRD4 expression. Associated with higher novelty seeking in some studies."
        ),
        "risk_level": "normal",
    },
    # COMT rs4633 pain sensitivity
    {
        "rsid": "rs4633",
        "genotype": "CC",
        "interpretation": "Higher COMT activity haplotype. Lower pain sensitivity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4633",
        "genotype": "CT",
        "interpretation": "Intermediate COMT haplotype. Moderate pain sensitivity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs4633",
        "genotype": "TT",
        "interpretation": "Lower COMT activity haplotype. Higher pain sensitivity.",
        "risk_level": "increased_risk",
    },
    # FAAH endocannabinoid
    {
        "rsid": "rs324420",
        "genotype": "CC",
        "interpretation": "Normal FAAH activity. Typical endocannabinoid signaling.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs324420",
        "genotype": "CA",
        "interpretation": "Reduced FAAH protein. Mildly elevated anandamide levels.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs324420",
        "genotype": "AA",
        "interpretation": (
            "Significantly reduced FAAH. Elevated endocannabinoid tone; lower anxiety trait."
        ),
        "risk_level": "normal",
    },
    # LIPC HDL cholesterol
    {
        "rsid": "rs1800588",
        "genotype": "CC",
        "interpretation": "Higher hepatic lipase activity. Lower HDL cholesterol levels.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800588",
        "genotype": "CT",
        "interpretation": "Intermediate hepatic lipase activity. Moderate HDL levels.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1800588",
        "genotype": "TT",
        "interpretation": "Lower hepatic lipase activity. Higher HDL cholesterol levels.",
        "risk_level": "normal",
    },
    # APOA5 triglycerides
    {
        "rsid": "rs662799",
        "genotype": "TT",
        "interpretation": "Typical APOA5 expression. Normal triglyceride levels from this variant.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs662799",
        "genotype": "TC",
        "interpretation": (
            "Carrier of -1131C. Modestly elevated triglyceride levels (~15% increase)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs662799",
        "genotype": "CC",
        "interpretation": (
            "Homozygous -1131C. Significantly elevated triglycerides (~30% increase)."
        ),
        "risk_level": "increased_risk",
    },
    # CLOCK chronotype
    {
        "rsid": "rs1801260",
        "genotype": "TT",
        "interpretation": "Morning chronotype tendency. Earlier sleep/wake preference.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801260",
        "genotype": "TC",
        "interpretation": "Intermediate chronotype. Slight evening tendency.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801260",
        "genotype": "CC",
        "interpretation": "Evening chronotype tendency. Later sleep/wake preference.",
        "risk_level": "normal",
    },
    # BHLHE41 short sleeper
    {
        "rsid": "rs57875989",
        "genotype": "CC",
        "interpretation": "Typical DEC2 function. Normal sleep duration requirement (~8 hours).",
        "risk_level": "normal",
    },
    {
        "rsid": "rs57875989",
        "genotype": "CG",
        "interpretation": "Carrier of P384R. May naturally require less sleep (~6-7 hours).",
        "risk_level": "normal",
    },
    {
        "rsid": "rs57875989",
        "genotype": "GG",
        "interpretation": "Homozygous P384R (very rare). Natural short sleeper (~6 hours).",
        "risk_level": "normal",
    },
]
