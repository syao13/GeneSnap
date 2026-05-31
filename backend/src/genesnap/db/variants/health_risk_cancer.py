"""Cancer-related health risk variants: BRCA1/2, MLH1, MSH2, APC, TP53, etc."""

from genesnap.db.variants._types import InterpretationDict, VariantDict

VARIANTS: list[VariantDict] = [
    # -------------------------------------------------------------------------
    # Existing BRCA1/2 Ashkenazi founder mutations
    # -------------------------------------------------------------------------
    {
        "rsid": "rs80357906",
        "gene": "BRCA1",
        "category": "health_risk",
        "name": "BRCA1 185delAG (Ashkenazi founder)",
        "significance": "pathogenic",
        "description": (
            "Ashkenazi Jewish founder mutation in BRCA1. Carriers have significantly elevated "
            "lifetime risk of breast cancer (60-80%) and ovarian cancer (40-60%)."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "17",
        "position": 41276045,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000017661"},
        "publications": ["8524414"],
        "clinvar_stars": 4,
        "odds_ratio": 8.0,
    },
    {
        "rsid": "rs80357713",
        "gene": "BRCA2",
        "category": "health_risk",
        "name": "BRCA2 6174delT (Ashkenazi founder)",
        "significance": "pathogenic",
        "description": (
            "Ashkenazi Jewish founder mutation in BRCA2. Carriers have elevated lifetime "
            "risk of breast cancer (45-70%) and increased risk of ovarian and other cancers."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "13",
        "position": 32914438,
        "source": "clinvar",
        "external_ids": {"clinvar": "VCV000038077"},
        "publications": ["8524414"],
        "clinvar_stars": 4,
        "odds_ratio": 6.0,
    },
    # -------------------------------------------------------------------------
    # 1. rs1799950 - BRCA1 Q356R
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1799950",
        "gene": "BRCA1",
        "category": "health_risk",
        "name": "BRCA1 Q356R",
        "significance": "risk_factor",
        "description": (
            "Missense variant in BRCA1 (Gln356Arg). Some studies report a modest increase "
            "in breast cancer risk, though penetrance is lower than truncating BRCA1 mutations."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "17",
        "position": 41244000,
        "source": "clinvar",
        "publications": ["12474142", "20104584"],
        "clinvar_stars": 2,
        "odds_ratio": 1.3,
    },
    # -------------------------------------------------------------------------
    # 2. rs11571833 - BRCA2 K3326X
    # -------------------------------------------------------------------------
    {
        "rsid": "rs11571833",
        "gene": "BRCA2",
        "category": "health_risk",
        "name": "BRCA2 K3326X",
        "significance": "risk_factor",
        "description": (
            "Stop-gain variant in the C-terminal region of BRCA2. Associated with modestly "
            "increased risk of breast, ovarian, and lung cancer. The truncated protein retains "
            "most functional domains."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "13",
        "position": 32972626,
        "source": "clinvar",
        "publications": ["20400964", "27406820"],
        "clinvar_stars": 2,
        "odds_ratio": 1.3,
    },
    # -------------------------------------------------------------------------
    # 3. rs63750447 - TP53 R248W
    # -------------------------------------------------------------------------
    {
        "rsid": "rs63750447",
        "gene": "TP53",
        "category": "health_risk",
        "name": "TP53 R248W (Li-Fraumeni)",
        "significance": "pathogenic",
        "description": (
            "Hotspot missense mutation in TP53 (Arg248Trp). One of the most frequently "
            "observed somatic TP53 mutations in human cancers. Germline carriers develop "
            "Li-Fraumeni syndrome with high lifetime cancer risk."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "17",
        "position": 7577538,
        "source": "clinvar",
        "publications": ["1568265", "15146165"],
        "clinvar_stars": 4,
        "odds_ratio": 10.0,
    },
    # -------------------------------------------------------------------------
    # 4. rs28934578 - TP53 R175H
    # -------------------------------------------------------------------------
    {
        "rsid": "rs28934578",
        "gene": "TP53",
        "category": "health_risk",
        "name": "TP53 R175H (Li-Fraumeni)",
        "significance": "pathogenic",
        "description": (
            "Hotspot missense mutation in TP53 (Arg175His). A structural mutation that "
            "disrupts p53 DNA-binding. Germline carriers are at very high risk for multiple "
            "cancers including sarcomas, breast cancer, brain tumors, and adrenocortical carcinoma."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "17",
        "position": 7578406,
        "source": "clinvar",
        "publications": ["1568265", "20522432"],
        "clinvar_stars": 4,
        "odds_ratio": 10.0,
    },
    # -------------------------------------------------------------------------
    # 5. rs121913529 - APC I1307K
    # -------------------------------------------------------------------------
    {
        "rsid": "rs121913529",
        "gene": "APC",
        "category": "health_risk",
        "name": "APC I1307K (colorectal cancer risk)",
        "significance": "risk_factor",
        "description": (
            "Missense variant in APC (Ile1307Lys) enriched in Ashkenazi Jewish populations. "
            "Creates a hypermutable poly-adenine tract leading to increased somatic APC "
            "mutations and approximately doubled colorectal cancer risk."
        ),
        "risk_allele": "A",
        "normal_allele": "T",
        "chromosome": "5",
        "position": 112175211,
        "source": "clinvar",
        "publications": ["9042909", "9716595"],
        "clinvar_stars": 3,
        "odds_ratio": 1.9,
    },
    # -------------------------------------------------------------------------
    # 6. rs267607275 - MLH1 founder mutation
    # -------------------------------------------------------------------------
    {
        "rsid": "rs267607275",
        "gene": "MLH1",
        "category": "health_risk",
        "name": "MLH1 founder mutation (Lynch syndrome)",
        "significance": "pathogenic",
        "description": (
            "Pathogenic founder mutation in MLH1 associated with Lynch syndrome "
            "(hereditary nonpolyposis colorectal cancer). Carriers have substantially "
            "elevated lifetime risk of colorectal (50-80%) and endometrial cancer (40-60%)."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "3",
        "position": 37067240,
        "source": "clinvar",
        "publications": ["9351734", "17074967"],
        "clinvar_stars": 4,
        "odds_ratio": 8.0,
    },
    # -------------------------------------------------------------------------
    # 7. rs63751710 - MSH2 (Lynch syndrome)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs63751710",
        "gene": "MSH2",
        "category": "health_risk",
        "name": "MSH2 mutation (Lynch syndrome)",
        "significance": "pathogenic",
        "description": (
            "Pathogenic variant in MSH2, a mismatch repair gene. Carriers develop "
            "Lynch syndrome with high lifetime risk of colorectal cancer (40-70%), "
            "endometrial cancer, and other malignancies."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "2",
        "position": 47702188,
        "source": "clinvar",
        "publications": ["9351734", "25559809"],
        "clinvar_stars": 4,
        "odds_ratio": 7.0,
    },
    # -------------------------------------------------------------------------
    # 8. rs587781834 - MSH6 (Lynch syndrome)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs587781834",
        "gene": "MSH6",
        "category": "health_risk",
        "name": "MSH6 mutation (Lynch syndrome)",
        "significance": "pathogenic",
        "description": (
            "Pathogenic variant in MSH6, a mismatch repair gene. MSH6 mutations confer "
            "a somewhat lower colorectal cancer risk than MLH1/MSH2 mutations but notably "
            "increased risk of endometrial cancer (up to 40%)."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "2",
        "position": 48030639,
        "source": "clinvar",
        "publications": ["9443876", "25559809"],
        "clinvar_stars": 3,
        "odds_ratio": 4.0,
    },
    # -------------------------------------------------------------------------
    # 9. rs34137742 - CHEK2 I157T
    # -------------------------------------------------------------------------
    {
        "rsid": "rs34137742",
        "gene": "CHEK2",
        "category": "health_risk",
        "name": "CHEK2 I157T",
        "significance": "risk_factor",
        "description": (
            "Missense variant in CHEK2 (Ile157Thr). Associated with a modest increase in "
            "breast cancer risk and, to a lesser extent, colorectal and prostate cancer risk. "
            "CHEK2 is a cell-cycle checkpoint kinase involved in DNA damage response."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "22",
        "position": 29121087,
        "source": "clinvar",
        "publications": ["15122511", "14559878"],
        "clinvar_stars": 2,
        "odds_ratio": 1.5,
    },
    # -------------------------------------------------------------------------
    # 10. rs555607708 - CHEK2 1100delC
    # -------------------------------------------------------------------------
    {
        "rsid": "rs555607708",
        "gene": "CHEK2",
        "category": "health_risk",
        "name": "CHEK2 1100delC",
        "significance": "pathogenic",
        "description": (
            "Frameshift deletion in CHEK2 resulting in a truncated, non-functional protein. "
            "Heterozygous carriers have approximately 2-3-fold increased breast cancer risk. "
            "The variant is most prevalent in Northern and Eastern European populations."
        ),
        "risk_allele": None,
        "normal_allele": None,
        "chromosome": "22",
        "position": 29091857,
        "source": "clinvar",
        "publications": ["12062583", "14559878"],
        "clinvar_stars": 4,
        "odds_ratio": 2.7,
    },
    # -------------------------------------------------------------------------
    # 11. rs1042522 - TP53 Pro72Arg
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1042522",
        "gene": "TP53",
        "category": "health_risk",
        "name": "TP53 Pro72Arg",
        "significance": "association",
        "description": (
            "Common functional polymorphism in TP53. The Arg72 form is more efficient at "
            "inducing apoptosis, while the Pro72 form is better at cell-cycle arrest and "
            "DNA repair. Multiple studies associate this variant with modest cancer risk "
            "differences across multiple tumor types."
        ),
        "risk_allele": "G",
        "normal_allele": "C",
        "chromosome": "17",
        "position": 7579472,
        "source": "gwas_catalog",
        "publications": ["12474142", "17311302"],
        "clinvar_stars": 1,
        "odds_ratio": 1.15,
    },
    # -------------------------------------------------------------------------
    # 12. rs2736098 - TERT
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2736098",
        "gene": "TERT",
        "category": "health_risk",
        "name": "TERT telomerase variant",
        "significance": "association",
        "description": (
            "Common variant in the TERT gene encoding the catalytic subunit of telomerase. "
            "GWAS studies associate this SNP with altered cancer risk across multiple types "
            "including lung, bladder, and prostate cancer, likely through effects on "
            "telomere maintenance."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "5",
        "position": 1297488,
        "source": "gwas_catalog",
        "publications": ["18483556", "23535729"],
        "clinvar_stars": 1,
        "odds_ratio": 1.15,
    },
    # -------------------------------------------------------------------------
    # 13. rs401681 - CLPTM1L/TERT region (lung cancer)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs401681",
        "gene": "CLPTM1L",
        "category": "health_risk",
        "name": "CLPTM1L/TERT lung cancer variant",
        "significance": "association",
        "description": (
            "Common variant in the CLPTM1L-TERT locus on 5p15.33. Robustly associated with "
            "lung cancer susceptibility, particularly lung adenocarcinoma, across multiple "
            "GWAS. CLPTM1L promotes cell survival and is frequently overexpressed in tumors."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "5",
        "position": 1322087,
        "source": "gwas_catalog",
        "publications": ["18978787", "21725308"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 14. rs6983267 - 8q24 colorectal cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs6983267",
        "gene": "8q24",
        "category": "health_risk",
        "name": "8q24 colorectal cancer risk locus",
        "significance": "association",
        "description": (
            "Intergenic variant in the 8q24 cancer susceptibility region. Strongly and "
            "reproducibly associated with colorectal cancer risk in GWAS. The risk allele "
            "is located in an enhancer element that binds TCF7L2 and may regulate MYC "
            "proto-oncogene expression."
        ),
        "risk_allele": "G",
        "normal_allele": "T",
        "chromosome": "8",
        "position": 128413305,
        "source": "gwas_catalog",
        "publications": ["17618284", "18372905"],
        "clinvar_stars": 1,
        "odds_ratio": 1.27,
    },
    # -------------------------------------------------------------------------
    # 15. rs13281615 - 8q24 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs13281615",
        "gene": "8q24",
        "category": "health_risk",
        "name": "8q24 breast cancer risk locus",
        "significance": "association",
        "description": (
            "Intergenic variant in the 8q24 region associated with breast cancer risk in "
            "large GWAS. The 8q24 region harbors multiple independent cancer susceptibility "
            "loci affecting different cancer types through long-range regulatory mechanisms."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "8",
        "position": 128355618,
        "source": "gwas_catalog",
        "publications": ["17529973", "19088017"],
        "clinvar_stars": 1,
        "odds_ratio": 1.08,
    },
    # -------------------------------------------------------------------------
    # 16. rs1447295 - 8q24 prostate cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1447295",
        "gene": "8q24",
        "category": "health_risk",
        "name": "8q24 prostate cancer risk locus",
        "significance": "association",
        "description": (
            "One of the first GWAS-identified variants for prostate cancer, located in the "
            "8q24 region. The risk allele is associated with moderately increased prostate "
            "cancer susceptibility across multiple ethnic populations."
        ),
        "risk_allele": "A",
        "normal_allele": "C",
        "chromosome": "8",
        "position": 128554220,
        "source": "gwas_catalog",
        "publications": ["16862161", "17401363"],
        "clinvar_stars": 1,
        "odds_ratio": 1.3,
    },
    # -------------------------------------------------------------------------
    # 17. rs4242382 - 8q24 prostate cancer #2
    # -------------------------------------------------------------------------
    {
        "rsid": "rs4242382",
        "gene": "8q24",
        "category": "health_risk",
        "name": "8q24 prostate cancer risk locus (region 2)",
        "significance": "association",
        "description": (
            "Independent prostate cancer risk locus within the 8q24 region. Multiple "
            "independent signals at 8q24 contribute additively to prostate cancer risk, "
            "suggesting complex regulatory architecture in this cancer-associated region."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "8",
        "position": 128535110,
        "source": "gwas_catalog",
        "publications": ["17401363", "18264098"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 18. rs10993994 - MSMB prostate cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10993994",
        "gene": "MSMB",
        "category": "health_risk",
        "name": "MSMB prostate cancer variant",
        "significance": "association",
        "description": (
            "Variant in the promoter region of MSMB (microseminoprotein beta). The risk "
            "allele reduces MSMB expression, a protein whose levels are decreased in "
            "prostate cancer. One of the most robustly replicated prostate cancer GWAS loci."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "10",
        "position": 51549496,
        "source": "gwas_catalog",
        "publications": ["18264098", "20668437"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 19. rs1859962 - 17q24.3 prostate cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1859962",
        "gene": "17q24.3",
        "category": "health_risk",
        "name": "17q24.3 prostate cancer risk locus",
        "significance": "association",
        "description": (
            "Intergenic variant at 17q24.3 associated with prostate cancer risk. Identified "
            "in GWAS and replicated across multiple populations. The underlying biological "
            "mechanism may involve long-range enhancer activity."
        ),
        "risk_allele": "G",
        "normal_allele": "T",
        "chromosome": "17",
        "position": 69108753,
        "source": "gwas_catalog",
        "publications": ["17603485", "18264098"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 20. rs4430796 - HNF1B prostate cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs4430796",
        "gene": "HNF1B",
        "category": "health_risk",
        "name": "HNF1B prostate cancer variant",
        "significance": "association",
        "description": (
            "Variant in the HNF1B (hepatocyte nuclear factor 1-beta) gene associated with "
            "prostate cancer risk. HNF1B is a transcription factor involved in prostate "
            "development. Interestingly, the prostate cancer risk allele is protective "
            "against type 2 diabetes."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "17",
        "position": 36098040,
        "source": "gwas_catalog",
        "publications": ["17603485", "18264098"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 21. rs3803662 - TOX3/TNRC9 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs3803662",
        "gene": "TOX3",
        "category": "health_risk",
        "name": "TOX3/TNRC9 breast cancer variant",
        "significance": "association",
        "description": (
            "One of the strongest common breast cancer susceptibility loci identified by "
            "GWAS, located near the TOX3 (TNRC9) gene. The risk allele is associated with "
            "increased breast cancer risk, particularly ER-positive subtypes. TOX3 encodes "
            "a transcription factor with roles in chromatin remodeling."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "16",
        "position": 52586341,
        "source": "gwas_catalog",
        "publications": ["17529973", "19330030"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 22. rs2981582 - FGFR2 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2981582",
        "gene": "FGFR2",
        "category": "health_risk",
        "name": "FGFR2 breast cancer variant",
        "significance": "association",
        "description": (
            "Intronic variant in FGFR2 (fibroblast growth factor receptor 2), one of the "
            "strongest common breast cancer susceptibility loci. The risk allele increases "
            "FGFR2 expression, promoting mammary epithelial proliferation. Effect is "
            "strongest for ER-positive breast cancer."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "10",
        "position": 123337335,
        "source": "gwas_catalog",
        "publications": ["17529973", "18438407"],
        "clinvar_stars": 1,
        "odds_ratio": 1.26,
    },
    # -------------------------------------------------------------------------
    # 23. rs13387042 - 2q35 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs13387042",
        "gene": "2q35",
        "category": "health_risk",
        "name": "2q35 breast cancer risk locus",
        "significance": "association",
        "description": (
            "Intergenic variant at 2q35 associated with breast cancer susceptibility. "
            "Located in a gene desert but within a regulatory region that may influence "
            "IGFBP5 expression. Replicated across multiple GWAS in diverse populations."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "2",
        "position": 217905832,
        "source": "gwas_catalog",
        "publications": ["17529974", "19330030"],
        "clinvar_stars": 1,
        "odds_ratio": 1.12,
    },
    # -------------------------------------------------------------------------
    # 24. rs889312 - MAP3K1 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs889312",
        "gene": "MAP3K1",
        "category": "health_risk",
        "name": "MAP3K1 breast cancer variant",
        "significance": "association",
        "description": (
            "Variant near MAP3K1 (mitogen-activated protein kinase kinase kinase 1) "
            "associated with breast cancer risk. MAP3K1 participates in the JNK signaling "
            "pathway regulating cell proliferation and apoptosis. Somatic MAP3K1 mutations "
            "are also observed in breast tumors."
        ),
        "risk_allele": "C",
        "normal_allele": "A",
        "chromosome": "5",
        "position": 56031884,
        "source": "gwas_catalog",
        "publications": ["17529973", "19330030"],
        "clinvar_stars": 1,
        "odds_ratio": 1.13,
    },
    # -------------------------------------------------------------------------
    # 25. rs1801516 - ATM D1853N
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1801516",
        "gene": "ATM",
        "category": "health_risk",
        "name": "ATM D1853N",
        "significance": "association",
        "description": (
            "Missense variant in ATM (ataxia-telangiectasia mutated), a key DNA "
            "double-strand break repair kinase. The Asp1853Asn change has been associated "
            "with modest breast cancer risk and may modify radiosensitivity."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "11",
        "position": 108175462,
        "source": "gwas_catalog",
        "publications": ["16832357", "21285378"],
        "clinvar_stars": 2,
        "odds_ratio": 1.1,
    },
    # -------------------------------------------------------------------------
    # 26. rs4986764 - BRIP1 (breast cancer)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs4986764",
        "gene": "BRIP1",
        "category": "health_risk",
        "name": "BRIP1 breast cancer variant",
        "significance": "association",
        "description": (
            "Common variant in BRIP1 (BRCA1-interacting protein 1), a Fanconi anemia "
            "gene involved in DNA interstrand crosslink repair. BRIP1 interacts directly "
            "with BRCA1 and truncating mutations confer increased breast and ovarian cancer risk."
        ),
        "risk_allele": "C",
        "normal_allele": "T",
        "chromosome": "17",
        "position": 59763347,
        "source": "gwas_catalog",
        "publications": ["16959974", "25452441"],
        "clinvar_stars": 1,
        "odds_ratio": 1.08,
    },
    # -------------------------------------------------------------------------
    # 27. rs16260 - CDH1 promoter (gastric cancer)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs16260",
        "gene": "CDH1",
        "category": "health_risk",
        "name": "CDH1 promoter variant (gastric cancer)",
        "significance": "association",
        "description": (
            "Promoter polymorphism in CDH1 (E-cadherin). The variant allele reduces CDH1 "
            "transcription activity and is associated with increased risk of gastric cancer, "
            "particularly diffuse-type gastric carcinoma. E-cadherin loss is a hallmark of "
            "epithelial-mesenchymal transition in cancer."
        ),
        "risk_allele": "A",
        "normal_allele": "C",
        "chromosome": "16",
        "position": 68771195,
        "source": "gwas_catalog",
        "publications": ["11683307", "16331254"],
        "clinvar_stars": 1,
        "odds_ratio": 1.3,
    },
    # -------------------------------------------------------------------------
    # 28. rs2279744 - MDM2 SNP309
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2279744",
        "gene": "MDM2",
        "category": "health_risk",
        "name": "MDM2 SNP309",
        "significance": "association",
        "description": (
            "Intronic promoter polymorphism in MDM2 (SNP309). The G allele increases "
            "MDM2 expression through enhanced Sp1 transcription factor binding, leading "
            "to accelerated p53 degradation. Associated with earlier onset of cancers in "
            "both sporadic and hereditary settings."
        ),
        "risk_allele": "G",
        "normal_allele": "T",
        "chromosome": "12",
        "position": 69201956,
        "source": "gwas_catalog",
        "publications": ["15607981", "17311302"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 29. rs25487 - XRCC1 Arg399Gln
    # -------------------------------------------------------------------------
    {
        "rsid": "rs25487",
        "gene": "XRCC1",
        "category": "health_risk",
        "name": "XRCC1 Arg399Gln (DNA repair)",
        "significance": "association",
        "description": (
            "Missense polymorphism in XRCC1 (Arg399Gln), a scaffold protein in base "
            "excision repair. The Gln399 variant has reduced DNA repair capacity and has "
            "been associated with increased risk of several cancers including breast, "
            "lung, and gastric cancer in meta-analyses."
        ),
        "risk_allele": "A",
        "normal_allele": "G",
        "chromosome": "19",
        "position": 44055726,
        "source": "gwas_catalog",
        "publications": ["12115545", "18384453"],
        "clinvar_stars": 1,
        "odds_ratio": 1.1,
    },
    # -------------------------------------------------------------------------
    # 30. rs1799782 - XRCC1 Arg194Trp
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1799782",
        "gene": "XRCC1",
        "category": "health_risk",
        "name": "XRCC1 Arg194Trp (DNA repair)",
        "significance": "association",
        "description": (
            "Missense polymorphism in XRCC1 (Arg194Trp), located in the linker region "
            "between the N-terminal and PARP-binding domains. Studies suggest this variant "
            "may modulate lung cancer risk, particularly in Asian populations."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "19",
        "position": 44047826,
        "source": "gwas_catalog",
        "publications": ["12115545", "21538992"],
        "clinvar_stars": 1,
        "odds_ratio": 1.1,
    },
    # -------------------------------------------------------------------------
    # 31. rs1048943 - CYP1A1 Ile462Val
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1048943",
        "gene": "CYP1A1",
        "category": "health_risk",
        "name": "CYP1A1 Ile462Val (carcinogen metabolism)",
        "significance": "association",
        "description": (
            "Missense polymorphism in CYP1A1 (Ile462Val), a cytochrome P450 enzyme "
            "involved in the metabolic activation of polycyclic aromatic hydrocarbons "
            "and other procarcinogens. The Val462 variant has higher catalytic activity "
            "and is associated with increased lung cancer risk, particularly in smokers."
        ),
        "risk_allele": "G",
        "normal_allele": "A",
        "chromosome": "15",
        "position": 75012985,
        "source": "gwas_catalog",
        "publications": ["9230222", "20615924"],
        "clinvar_stars": 1,
        "odds_ratio": 1.2,
    },
    # -------------------------------------------------------------------------
    # 32. rs10411210 - RHPN2 colorectal cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10411210",
        "gene": "RHPN2",
        "category": "health_risk",
        "name": "RHPN2 colorectal cancer variant",
        "significance": "association",
        "description": (
            "Variant in RHPN2 (rhophilin 2) associated with colorectal cancer risk in GWAS. "
            "RHPN2 is involved in Rho GTPase signaling pathways that regulate cell migration "
            "and cytoskeletal organization, processes relevant to tumor invasion."
        ),
        "risk_allele": "T",
        "normal_allele": "C",
        "chromosome": "19",
        "position": 33532300,
        "source": "gwas_catalog",
        "publications": ["18372901", "20972440"],
        "clinvar_stars": 1,
        "odds_ratio": 1.15,
    },
    # -------------------------------------------------------------------------
    # 33. rs961253 - 20p12.3 colorectal cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs961253",
        "gene": "20p12.3",
        "category": "health_risk",
        "name": "20p12.3 colorectal cancer risk locus",
        "significance": "association",
        "description": (
            "Intergenic variant at 20p12.3 associated with colorectal cancer risk in "
            "large GWAS meta-analyses. Located near BMP2, a bone morphogenetic protein "
            "involved in intestinal cell differentiation and proliferation control."
        ),
        "risk_allele": "A",
        "normal_allele": "C",
        "chromosome": "20",
        "position": 6404281,
        "source": "gwas_catalog",
        "publications": ["18372901", "20972440"],
        "clinvar_stars": 1,
        "odds_ratio": 1.1,
    },
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    # -------------------------------------------------------------------------
    # rs80357906 - BRCA1 185delAG
    # -------------------------------------------------------------------------
    {
        "rsid": "rs80357906",
        "genotype": "normal/normal",
        "interpretation": (
            "No BRCA1 185delAG mutation detected. Average population risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs80357906",
        "genotype": "normal/del",
        "interpretation": (
            "Heterozygous carrier of BRCA1 185delAG. Significantly elevated lifetime risk "
            "of breast (60-80%) and ovarian cancer (40-60%). Genetic counseling recommended."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs80357906",
        "genotype": "del/del",
        "interpretation": (
            "Homozygous for BRCA1 185delAG. Very high cancer risk. Immediate clinical "
            "follow-up and genetic counseling essential."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs80357713 - BRCA2 6174delT
    # -------------------------------------------------------------------------
    {
        "rsid": "rs80357713",
        "genotype": "normal/normal",
        "interpretation": (
            "No BRCA2 6174delT mutation detected. Average population risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs80357713",
        "genotype": "normal/del",
        "interpretation": (
            "Heterozygous carrier of BRCA2 6174delT. Elevated lifetime risk of breast "
            "(45-70%) and ovarian cancer. Genetic counseling recommended."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs80357713",
        "genotype": "del/del",
        "interpretation": (
            "Homozygous for BRCA2 6174delT. Very high cancer risk. Immediate clinical "
            "follow-up and genetic counseling essential."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs1799950 - BRCA1 Q356R
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1799950",
        "genotype": "GG",
        "interpretation": "No BRCA1 Q356R variant. Typical population risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1799950",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for BRCA1 Q356R. Modestly increased breast cancer risk. "
            "Consider comprehensive BRCA1 panel if family history is suggestive."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1799950",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for BRCA1 Q356R risk allele. Moderately increased breast cancer "
            "risk. Clinical assessment and possible genetic counseling advised."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs11571833 - BRCA2 K3326X
    # -------------------------------------------------------------------------
    {
        "rsid": "rs11571833",
        "genotype": "GG",
        "interpretation": "No BRCA2 K3326X variant. Typical population risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs11571833",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous carrier of BRCA2 K3326X stop-gain variant. Modestly increased "
            "risk of breast, ovarian, and lung cancer."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs11571833",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for BRCA2 K3326X. Increased risk of multiple cancers. "
            "Genetic counseling recommended."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs63750447 - TP53 R248W
    # -------------------------------------------------------------------------
    {
        "rsid": "rs63750447",
        "genotype": "CC",
        "interpretation": "No TP53 R248W mutation. Normal p53 function from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs63750447",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous for TP53 R248W. Consistent with Li-Fraumeni syndrome. Very high "
            "lifetime risk of multiple cancers. Urgent genetic counseling recommended."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs63750447",
        "genotype": "TT",
        "interpretation": (
            "Homozygous for TP53 R248W. Extremely high cancer risk consistent with "
            "Li-Fraumeni syndrome. Immediate specialist referral essential."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs28934578 - TP53 R175H
    # -------------------------------------------------------------------------
    {
        "rsid": "rs28934578",
        "genotype": "GG",
        "interpretation": "No TP53 R175H mutation. Normal p53 function from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs28934578",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for TP53 R175H. Consistent with Li-Fraumeni syndrome. Very high "
            "lifetime cancer risk. Urgent genetic counseling recommended."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs28934578",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for TP53 R175H. Extremely high cancer risk. "
            "Immediate specialist referral essential."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs121913529 - APC I1307K
    # -------------------------------------------------------------------------
    {
        "rsid": "rs121913529",
        "genotype": "TT",
        "interpretation": "No APC I1307K variant. Typical colorectal cancer risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs121913529",
        "genotype": "AT",
        "interpretation": (
            "Heterozygous for APC I1307K. Approximately doubled colorectal cancer risk. "
            "Enhanced colorectal cancer screening recommended."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs121913529",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for APC I1307K. Significantly elevated colorectal cancer risk. "
            "Early and frequent colonoscopy screening strongly recommended."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs267607275 - MLH1 founder (Lynch syndrome)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs267607275",
        "genotype": "normal/normal",
        "interpretation": (
            "No MLH1 founder mutation detected. Average Lynch syndrome risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs267607275",
        "genotype": "normal/mut",
        "interpretation": (
            "Heterozygous carrier of MLH1 pathogenic variant. Consistent with Lynch syndrome. "
            "High lifetime risk of colorectal (50-80%) and endometrial cancer. "
            "Enhanced cancer surveillance recommended."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs267607275",
        "genotype": "mut/mut",
        "interpretation": (
            "Homozygous for MLH1 pathogenic variant. Very high risk of Lynch-associated "
            "cancers. Immediate specialist referral essential."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs63751710 - MSH2 (Lynch syndrome)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs63751710",
        "genotype": "normal/normal",
        "interpretation": (
            "No MSH2 pathogenic variant detected. Average Lynch syndrome risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs63751710",
        "genotype": "normal/mut",
        "interpretation": (
            "Heterozygous carrier of MSH2 pathogenic variant. Consistent with Lynch syndrome. "
            "High lifetime risk of colorectal (40-70%) and endometrial cancer. "
            "Enhanced cancer surveillance recommended."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs63751710",
        "genotype": "mut/mut",
        "interpretation": (
            "Homozygous for MSH2 pathogenic variant. Very high risk of Lynch-associated "
            "cancers. Immediate specialist referral essential."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs587781834 - MSH6 (Lynch syndrome)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs587781834",
        "genotype": "normal/normal",
        "interpretation": (
            "No MSH6 pathogenic variant detected. Average Lynch syndrome risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs587781834",
        "genotype": "normal/mut",
        "interpretation": (
            "Heterozygous carrier of MSH6 pathogenic variant. Moderate risk of Lynch-associated "
            "cancers, particularly endometrial cancer (up to 40%). Cancer surveillance recommended."
        ),
        "risk_level": "high_risk",
    },
    {
        "rsid": "rs587781834",
        "genotype": "mut/mut",
        "interpretation": (
            "Homozygous for MSH6 pathogenic variant. Elevated risk of colorectal and "
            "endometrial cancer. Specialist referral recommended."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs34137742 - CHEK2 I157T
    # -------------------------------------------------------------------------
    {
        "rsid": "rs34137742",
        "genotype": "TT",
        "interpretation": "No CHEK2 I157T variant. Typical population risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs34137742",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous for CHEK2 I157T. Modestly increased breast cancer risk (~1.5x). "
            "Standard screening guidelines with consideration of family history."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs34137742",
        "genotype": "CC",
        "interpretation": (
            "Homozygous for CHEK2 I157T risk allele. Moderately increased cancer risk. "
            "Enhanced screening may be appropriate, especially with family history."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs555607708 - CHEK2 1100delC
    # -------------------------------------------------------------------------
    {
        "rsid": "rs555607708",
        "genotype": "normal/normal",
        "interpretation": (
            "No CHEK2 1100delC mutation detected. Typical population risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs555607708",
        "genotype": "normal/del",
        "interpretation": (
            "Heterozygous carrier of CHEK2 1100delC. Approximately 2-3-fold increased "
            "breast cancer risk. Enhanced breast cancer screening recommended."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs555607708",
        "genotype": "del/del",
        "interpretation": (
            "Homozygous for CHEK2 1100delC. Substantially elevated breast cancer risk. "
            "Genetic counseling and intensive screening strongly recommended."
        ),
        "risk_level": "high_risk",
    },
    # -------------------------------------------------------------------------
    # rs1042522 - TP53 Pro72Arg
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1042522",
        "genotype": "CC",
        "interpretation": (
            "Homozygous Pro72. Better cell-cycle arrest and DNA repair activity. "
            "Some studies suggest modest protective effect against certain cancers."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1042522",
        "genotype": "CG",
        "interpretation": (
            "Heterozygous Pro72Arg. Intermediate p53 functional profile. "
            "Average population cancer risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1042522",
        "genotype": "GG",
        "interpretation": (
            "Homozygous Arg72. More efficient apoptosis induction. Some studies associate "
            "with modestly increased cancer risk in certain populations."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs2736098 - TERT
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2736098",
        "genotype": "GG",
        "interpretation": "No TERT risk allele. Average cancer risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2736098",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for TERT variant. Slightly increased risk of lung, bladder, "
            "and prostate cancer."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2736098",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for TERT risk allele. Modestly elevated risk of multiple cancer types "
            "through altered telomerase regulation."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs401681 - CLPTM1L/TERT lung cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs401681",
        "genotype": "TT",
        "interpretation": "No CLPTM1L risk allele. Average lung cancer risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs401681",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous for CLPTM1L variant. Slightly increased lung cancer risk, "
            "particularly for adenocarcinoma subtype."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs401681",
        "genotype": "CC",
        "interpretation": (
            "Homozygous for CLPTM1L risk allele. Modestly elevated lung cancer risk. "
            "Smoking cessation especially important."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs6983267 - 8q24 colorectal cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs6983267",
        "genotype": "TT",
        "interpretation": "No 8q24 colorectal risk allele at this locus. Average risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs6983267",
        "genotype": "GT",
        "interpretation": (
            "Heterozygous for 8q24 colorectal cancer risk variant. Slightly increased "
            "colorectal cancer risk (~1.27x per allele)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs6983267",
        "genotype": "GG",
        "interpretation": (
            "Homozygous for 8q24 colorectal cancer risk allele. Moderately elevated "
            "colorectal cancer risk. Standard screening guidelines apply."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs13281615 - 8q24 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs13281615",
        "genotype": "AA",
        "interpretation": "No 8q24 breast cancer risk allele at this locus. Average risk.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs13281615",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for 8q24 breast cancer variant. Slightly increased breast cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs13281615",
        "genotype": "GG",
        "interpretation": (
            "Homozygous for 8q24 breast cancer risk allele. Modestly increased breast "
            "cancer risk from this locus."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs1447295 - 8q24 prostate cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1447295",
        "genotype": "CC",
        "interpretation": (
            "No 8q24 prostate cancer risk allele at this locus. Average prostate cancer risk."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1447295",
        "genotype": "AC",
        "interpretation": (
            "Heterozygous for 8q24 prostate cancer variant. Moderately increased prostate "
            "cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1447295",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for 8q24 prostate cancer risk allele. Notably increased prostate "
            "cancer risk. PSA screening may be discussed with physician."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs4242382 - 8q24 prostate cancer #2
    # -------------------------------------------------------------------------
    {
        "rsid": "rs4242382",
        "genotype": "GG",
        "interpretation": (
            "No 8q24 region 2 prostate cancer risk allele. Average risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs4242382",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for 8q24 region 2 prostate cancer variant. Slightly increased "
            "prostate cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4242382",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for 8q24 region 2 risk allele. Modestly elevated prostate cancer "
            "risk from this independent signal."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs10993994 - MSMB prostate cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10993994",
        "genotype": "CC",
        "interpretation": (
            "No MSMB risk allele. Normal MSMB expression expected. Average prostate cancer risk."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs10993994",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous for MSMB variant. Slightly reduced MSMB expression and "
            "modestly increased prostate cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs10993994",
        "genotype": "TT",
        "interpretation": (
            "Homozygous for MSMB risk allele. Reduced MSMB expression associated with "
            "moderately increased prostate cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs1859962 - 17q24.3 prostate cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1859962",
        "genotype": "TT",
        "interpretation": (
            "No 17q24.3 prostate cancer risk allele. Average prostate cancer risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs1859962",
        "genotype": "GT",
        "interpretation": (
            "Heterozygous for 17q24.3 prostate cancer variant. Slightly increased prostate "
            "cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1859962",
        "genotype": "GG",
        "interpretation": (
            "Homozygous for 17q24.3 prostate cancer risk allele. Modestly elevated prostate "
            "cancer risk from this locus."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs4430796 - HNF1B prostate cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs4430796",
        "genotype": "GG",
        "interpretation": (
            "No HNF1B prostate cancer risk allele. Average prostate cancer risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs4430796",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for HNF1B prostate cancer variant. Slightly increased prostate "
            "cancer risk. Note: this allele may be protective against type 2 diabetes."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4430796",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for HNF1B prostate cancer risk allele. Modestly elevated prostate "
            "cancer risk from this locus."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs3803662 - TOX3/TNRC9 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs3803662",
        "genotype": "GG",
        "interpretation": (
            "No TOX3/TNRC9 breast cancer risk allele. Average breast cancer risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs3803662",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for TOX3/TNRC9 breast cancer variant. Slightly increased breast "
            "cancer risk, particularly ER-positive subtype."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs3803662",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for TOX3/TNRC9 risk allele. Moderately increased breast cancer "
            "risk. One of the stronger common breast cancer susceptibility signals."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs2981582 - FGFR2 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2981582",
        "genotype": "CC",
        "interpretation": (
            "No FGFR2 breast cancer risk allele. Average breast cancer risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs2981582",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous for FGFR2 breast cancer variant. Increased breast cancer risk, "
            "particularly ER-positive subtype (~1.26x per allele)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2981582",
        "genotype": "TT",
        "interpretation": (
            "Homozygous for FGFR2 risk allele. Among the strongest common breast cancer "
            "susceptibility signals. Enhanced FGFR2 expression may drive epithelial proliferation."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs13387042 - 2q35 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs13387042",
        "genotype": "GG",
        "interpretation": "No 2q35 breast cancer risk allele. Average risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs13387042",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for 2q35 breast cancer variant. Slightly increased breast cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs13387042",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for 2q35 breast cancer risk allele. Modestly increased breast "
            "cancer risk from this locus."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs889312 - MAP3K1 breast cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs889312",
        "genotype": "AA",
        "interpretation": (
            "No MAP3K1 breast cancer risk allele. Average breast cancer risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs889312",
        "genotype": "AC",
        "interpretation": (
            "Heterozygous for MAP3K1 breast cancer variant. Slightly increased breast "
            "cancer risk (~1.13x per allele)."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs889312",
        "genotype": "CC",
        "interpretation": (
            "Homozygous for MAP3K1 risk allele. Modestly elevated breast cancer risk "
            "from this locus."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs1801516 - ATM D1853N
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1801516",
        "genotype": "GG",
        "interpretation": "No ATM D1853N variant. Normal ATM function from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1801516",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous for ATM D1853N. Modestly increased breast cancer risk. "
            "May influence radiosensitivity."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1801516",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for ATM D1853N. Slightly elevated breast cancer risk and "
            "possible altered DNA repair capacity."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs4986764 - BRIP1
    # -------------------------------------------------------------------------
    {
        "rsid": "rs4986764",
        "genotype": "TT",
        "interpretation": (
            "No BRIP1 risk allele at this position. Average breast cancer risk from this locus."
        ),
        "risk_level": "normal",
    },
    {
        "rsid": "rs4986764",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous for BRIP1 variant. Slightly increased breast cancer risk. "
            "BRIP1 interacts with BRCA1 in DNA repair."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs4986764",
        "genotype": "CC",
        "interpretation": (
            "Homozygous for BRIP1 risk allele. Modestly increased breast cancer risk "
            "from this DNA repair pathway variant."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs16260 - CDH1 promoter (gastric cancer)
    # -------------------------------------------------------------------------
    {
        "rsid": "rs16260",
        "genotype": "CC",
        "interpretation": "No CDH1 promoter risk allele. Normal E-cadherin expression expected.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs16260",
        "genotype": "AC",
        "interpretation": (
            "Heterozygous for CDH1 promoter variant. Reduced E-cadherin transcription "
            "and modestly increased gastric cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs16260",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for CDH1 promoter risk allele. Notably reduced E-cadherin "
            "expression. Increased risk of diffuse-type gastric cancer."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs2279744 - MDM2 SNP309
    # -------------------------------------------------------------------------
    {
        "rsid": "rs2279744",
        "genotype": "TT",
        "interpretation": "No MDM2 SNP309 risk allele. Normal MDM2 expression and p53 regulation.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs2279744",
        "genotype": "GT",
        "interpretation": (
            "Heterozygous for MDM2 SNP309. Increased MDM2 expression leading to "
            "accelerated p53 degradation. May influence cancer onset age."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs2279744",
        "genotype": "GG",
        "interpretation": (
            "Homozygous for MDM2 SNP309 risk allele. Significantly elevated MDM2 "
            "expression and enhanced p53 degradation. Associated with earlier cancer onset."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs25487 - XRCC1 Arg399Gln
    # -------------------------------------------------------------------------
    {
        "rsid": "rs25487",
        "genotype": "GG",
        "interpretation": "Homozygous Arg399. Normal XRCC1-mediated base excision repair capacity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs25487",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous Arg399Gln. Intermediate DNA repair capacity. Modestly "
            "increased risk of certain cancers in some populations."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs25487",
        "genotype": "AA",
        "interpretation": (
            "Homozygous Gln399. Reduced base excision repair efficiency. Modestly "
            "increased risk of breast, lung, and gastric cancer."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs1799782 - XRCC1 Arg194Trp
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1799782",
        "genotype": "CC",
        "interpretation": "Homozygous Arg194. Normal XRCC1 function from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1799782",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous Arg194Trp. May modestly alter DNA repair and lung cancer "
            "risk, particularly in Asian populations."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1799782",
        "genotype": "TT",
        "interpretation": (
            "Homozygous Trp194. Altered XRCC1 linker domain. Some studies report "
            "modestly increased cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs1048943 - CYP1A1 Ile462Val
    # -------------------------------------------------------------------------
    {
        "rsid": "rs1048943",
        "genotype": "AA",
        "interpretation": "Homozygous Ile462. Normal CYP1A1 catalytic activity.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs1048943",
        "genotype": "AG",
        "interpretation": (
            "Heterozygous Ile462Val. Intermediate CYP1A1 activity. May moderately "
            "increase carcinogen activation and lung cancer risk in smokers."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs1048943",
        "genotype": "GG",
        "interpretation": (
            "Homozygous Val462. Higher CYP1A1 catalytic activity leading to enhanced "
            "procarcinogen activation. Increased lung cancer risk, especially in smokers."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs10411210 - RHPN2 colorectal cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs10411210",
        "genotype": "CC",
        "interpretation": "No RHPN2 colorectal cancer risk allele. Average risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs10411210",
        "genotype": "CT",
        "interpretation": (
            "Heterozygous for RHPN2 colorectal cancer variant. Slightly increased "
            "colorectal cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs10411210",
        "genotype": "TT",
        "interpretation": (
            "Homozygous for RHPN2 colorectal cancer risk allele. Modestly elevated "
            "colorectal cancer risk from this locus."
        ),
        "risk_level": "increased_risk",
    },
    # -------------------------------------------------------------------------
    # rs961253 - 20p12.3 colorectal cancer
    # -------------------------------------------------------------------------
    {
        "rsid": "rs961253",
        "genotype": "CC",
        "interpretation": "No 20p12.3 colorectal cancer risk allele. Average risk from this locus.",
        "risk_level": "normal",
    },
    {
        "rsid": "rs961253",
        "genotype": "AC",
        "interpretation": (
            "Heterozygous for 20p12.3 colorectal cancer variant. Slightly increased "
            "colorectal cancer risk."
        ),
        "risk_level": "increased_risk",
    },
    {
        "rsid": "rs961253",
        "genotype": "AA",
        "interpretation": (
            "Homozygous for 20p12.3 colorectal cancer risk allele. Modestly elevated "
            "colorectal cancer risk. Located near BMP2 involved in gut differentiation."
        ),
        "risk_level": "increased_risk",
    },
]
