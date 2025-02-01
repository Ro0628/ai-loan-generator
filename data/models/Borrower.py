
# Importing required libraries

# Defining the Borrower class
# This class will be used to represent the borrower's information

class Borrower:
    def __init__(self, firstName, lastName, age, income, credit_score):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.income = income
        self.credit_score = credit_score

    def __repr__(self):
        return f"Borrower(name={self.name}, age={self.age}, income={self.income}, credit_score={self.credit_score})"