"""Aggregated curated variant data from all category modules."""

from genesnap.db.variants._types import InterpretationDict, VariantDict
from genesnap.db.variants.health_risk_blood import (
    GENOTYPE_INTERPRETATIONS as BLOOD_INTERPS,
)
from genesnap.db.variants.health_risk_blood import (
    VARIANTS as BLOOD_VARIANTS,
)
from genesnap.db.variants.health_risk_cancer import (
    GENOTYPE_INTERPRETATIONS as CANCER_INTERPS,
)
from genesnap.db.variants.health_risk_cancer import (
    VARIANTS as CANCER_VARIANTS,
)
from genesnap.db.variants.health_risk_cardio import (
    GENOTYPE_INTERPRETATIONS as CARDIO_INTERPS,
)
from genesnap.db.variants.health_risk_cardio import (
    VARIANTS as CARDIO_VARIANTS,
)
from genesnap.db.variants.health_risk_immune import (
    GENOTYPE_INTERPRETATIONS as IMMUNE_INTERPS,
)
from genesnap.db.variants.health_risk_immune import (
    VARIANTS as IMMUNE_VARIANTS,
)
from genesnap.db.variants.health_risk_metabolic import (
    GENOTYPE_INTERPRETATIONS as METABOLIC_INTERPS,
)
from genesnap.db.variants.health_risk_metabolic import (
    VARIANTS as METABOLIC_VARIANTS,
)
from genesnap.db.variants.health_risk_neuro import (
    GENOTYPE_INTERPRETATIONS as NEURO_INTERPS,
)
from genesnap.db.variants.health_risk_neuro import (
    VARIANTS as NEURO_VARIANTS,
)
from genesnap.db.variants.pharma_cyp import (
    GENOTYPE_INTERPRETATIONS as CYP_INTERPS,
)
from genesnap.db.variants.pharma_cyp import (
    VARIANTS as CYP_VARIANTS,
)
from genesnap.db.variants.pharma_other import (
    GENOTYPE_INTERPRETATIONS as OTHER_PHARMA_INTERPS,
)
from genesnap.db.variants.pharma_other import (
    VARIANTS as OTHER_PHARMA_VARIANTS,
)
from genesnap.db.variants.traits import (
    GENOTYPE_INTERPRETATIONS as TRAIT_INTERPS,
)
from genesnap.db.variants.traits import (
    VARIANTS as TRAIT_VARIANTS,
)

VARIANTS: list[VariantDict] = [
    *CARDIO_VARIANTS,
    *CANCER_VARIANTS,
    *METABOLIC_VARIANTS,
    *NEURO_VARIANTS,
    *BLOOD_VARIANTS,
    *IMMUNE_VARIANTS,
    *CYP_VARIANTS,
    *OTHER_PHARMA_VARIANTS,
    *TRAIT_VARIANTS,
]

GENOTYPE_INTERPRETATIONS: list[InterpretationDict] = [
    *CARDIO_INTERPS,
    *CANCER_INTERPS,
    *METABOLIC_INTERPS,
    *NEURO_INTERPS,
    *BLOOD_INTERPS,
    *IMMUNE_INTERPS,
    *CYP_INTERPS,
    *OTHER_PHARMA_INTERPS,
    *TRAIT_INTERPS,
]

__all__ = ["GENOTYPE_INTERPRETATIONS", "InterpretationDict", "VARIANTS", "VariantDict"]  # noqa: RUF022
