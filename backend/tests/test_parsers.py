"""Tests for 23andMe raw data parser."""

from genesnap.models.schemas import SNP
from genesnap.parsers.twentythreeandme import parse_23andme


class TestParse23andMe:
    """Tests for the 23andMe parser."""

    def test_parses_valid_snps(self, sample_23andme_text: str) -> None:
        """Should parse valid rs-prefixed SNPs from the file."""
        snps = parse_23andme(sample_23andme_text)
        rsids = {s.rsid for s in snps}

        assert "rs548049170" in rsids
        assert "rs6025" in rsids
        assert "rs429358" in rsids

    def test_skips_comment_lines(self, sample_23andme_text: str) -> None:
        """Should skip all lines starting with #."""
        snps = parse_23andme(sample_23andme_text)
        for snp in snps:
            assert not snp.rsid.startswith("#")

    def test_skips_no_call_genotypes(self, sample_23andme_text: str) -> None:
        """Should skip entries with -- genotype (no-call)."""
        snps = parse_23andme(sample_23andme_text)
        for snp in snps:
            assert snp.genotype != "--"

    def test_skips_internal_ids(self, sample_23andme_text: str) -> None:
        """Should skip entries with internal IDs (i-prefix)."""
        snps = parse_23andme(sample_23andme_text)
        for snp in snps:
            assert snp.rsid.startswith("rs")

    def test_returns_snp_models(self, sample_23andme_text: str) -> None:
        """Each result should be a properly structured SNP model."""
        snps = parse_23andme(sample_23andme_text)
        assert len(snps) > 0

        first = snps[0]
        assert isinstance(first, SNP)
        assert first.rsid.startswith("rs")
        assert first.chromosome in {str(i) for i in range(1, 23)} | {"X", "Y", "MT"}
        assert first.position > 0
        assert len(first.genotype) == 2

    def test_correct_snp_count(self, sample_23andme_text: str) -> None:
        """Should parse the correct number of valid SNPs from sample data.

        Sample has 19 data lines: 1 is no-call (--), 1 is internal (i-prefix).
        Expected: 17 valid SNPs.
        """
        snps = parse_23andme(sample_23andme_text)
        assert len(snps) == 17

    def test_parses_genotype_correctly(self, sample_23andme_text: str) -> None:
        """Should correctly capture genotype values."""
        snps = parse_23andme(sample_23andme_text)
        snp_map = {s.rsid: s for s in snps}

        assert snp_map["rs548049170"].genotype == "TT"
        assert snp_map["rs9283150"].genotype == "AG"
        assert snp_map["rs6025"].genotype == "AG"

    def test_parses_chromosome_correctly(self, sample_23andme_text: str) -> None:
        """Should correctly capture chromosome values."""
        snps = parse_23andme(sample_23andme_text)
        snp_map = {s.rsid: s for s in snps}

        assert snp_map["rs548049170"].chromosome == "1"
        assert snp_map["rs429358"].chromosome == "19"
        assert snp_map["rs4988235"].chromosome == "2"

    def test_parses_position_as_int(self, sample_23andme_text: str) -> None:
        """Position should be parsed as an integer."""
        snps = parse_23andme(sample_23andme_text)
        snp_map = {s.rsid: s for s in snps}

        assert snp_map["rs548049170"].position == 69869
        assert snp_map["rs6025"].position == 169519049

    def test_empty_input(self) -> None:
        """Should return empty list for empty input."""
        assert parse_23andme("") == []

    def test_comments_only_input(self) -> None:
        """Should return empty list for input with only comments."""
        text = "# comment line 1\n# comment line 2\n"
        assert parse_23andme(text) == []

    def test_handles_mitochondrial_chromosome(self) -> None:
        """Should handle MT (mitochondrial) chromosome."""
        text = "rs123\tMT\t100\tAA\n"
        snps = parse_23andme(text)
        assert len(snps) == 1
        assert snps[0].chromosome == "MT"

    def test_handles_x_y_chromosomes(self) -> None:
        """Should handle X and Y chromosomes."""
        text = "rs100\tX\t500\tAA\nrs200\tY\t600\tTT\n"
        snps = parse_23andme(text)
        assert len(snps) == 2
        assert snps[0].chromosome == "X"
        assert snps[1].chromosome == "Y"

    def test_skips_malformed_lines(self) -> None:
        """Should skip lines that don't have exactly 4 tab-separated fields."""
        text = "rs123\t1\t100\tAA\nbadline\nrs456\t2\t200\tGG\n"
        snps = parse_23andme(text)
        assert len(snps) == 2

    def test_header_line_skipped(self) -> None:
        """Should skip the column header line (rsid, chromosome, position, genotype)."""
        text = "rsid\tchromosome\tposition\tgenotype\nrs123\t1\t100\tAA\n"
        snps = parse_23andme(text)
        assert len(snps) == 1
        assert snps[0].rsid == "rs123"
