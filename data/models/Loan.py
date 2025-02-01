from data.models.Borrower import Borrower
from data.models.Property import Property
from data.models.LoanStatus import LoanStatus
from data.models.LoanType import LoanType

class Loan:
    def __init__(self, loan_type: LoanType, term_years: int, loan_amount: float, borrower: Borrower, property: Property, status: LoanStatus):
        self.loan_type = loan_type
        self.term_years = term_years
        self.loan_amount = loan_amount
        self.borrower = borrower
        self.property = property
        self.status = status

    def monthly_payment(self):
        """Calculate monthly mortgage payment using standard amortization formula."""
        r = 4.5 / 12 / 100  # Placeholder interest rate
        n = self.term_years * 12
        return self.loan_amount * r * (1 + r)**n / ((1 + r)**n - 1)

    def __repr__(self):
        return f"Loan(type={self.loan_type}, amount={self.loan_amount}, status={self.status})"
