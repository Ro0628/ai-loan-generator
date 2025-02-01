from enum import Enum

class LoanStatus(str, Enum):
    PENDING = "pending"
    UNDERWRITING = "underwriting"
    APPROVED = "approved"
    REJECTED = "rejected"
