"""Parser for 23andMe raw data files."""

from genesnap.models.schemas import SNP

VALID_CHROMOSOMES = {str(i) for i in range(1, 23)} | {"X", "Y", "MT"}
HEADER_LINE = "rsid\tchromosome\tposition\tgenotype"


def parse_23andme(text: str) -> list[SNP]:
    """Parse 23andMe raw data text into a list of SNP objects.

    Skips comment lines (#), header line, no-call genotypes (--),
    internal IDs (i-prefix), and malformed lines.
    """
    snps: list[SNP] = []

    for line in text.splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("rsid\t"):
            continue

        parts = line.split("\t")
        if len(parts) != 4:
            continue

        rsid, chromosome, position_str, genotype = parts

        if not rsid.startswith("rs"):
            continue

        if genotype == "--":
            continue

        if chromosome not in VALID_CHROMOSOMES:
            continue

        try:
            position = int(position_str)
        except ValueError:
            continue

        snps.append(
            SNP(
                rsid=rsid,
                chromosome=chromosome,
                position=position,
                genotype=genotype,
            )
        )

    return snps
