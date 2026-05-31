"""Abstract base parser for genetic testing raw data files."""

from abc import ABC, abstractmethod

from genesnap.models.schemas import SNP


class BaseParser(ABC):
    """Base class for genetic testing data parsers."""

    @abstractmethod
    def parse(self, text: str) -> list[SNP]:
        """Parse raw data text and return a list of valid SNPs."""
        ...
