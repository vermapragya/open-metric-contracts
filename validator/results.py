from dataclasses import dataclass
from typing import List

@dataclass
class ValidationResult:
    errors: List[str]
    warnings: List[str]

    def is_valid(self) -> bool:
        return len(self.errors)==0