from enum import Enum

class LoanType(str, Enum):
    VA = "VA"
    FHA = "FHA"
    CONVENTIONAL = "Conventional"
    JUMBO = "Jumbo"
    USDA = "USDA"
