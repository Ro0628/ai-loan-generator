# Description: Property model for loan applications

class Property:
    def __init__(self, address, city, state, zip_code, value):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.value = value

    def __repr__(self):
        return f"Property(address={self.address}, city={self.city}, state={self.state}, zip_code={self.zip_code}, value={self.value})"