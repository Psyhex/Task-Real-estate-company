class Customer:
    def __init__(self, email: str, name: str, tax: int = 2):
        self.email = email
        self.name = name
        self.tax = tax

    def total_amount(self, price_of_flat: float):
        return round(self.tax / 100 * price_of_flat + price_of_flat)


class LoyalCustomer(Customer):
    def __init__(self, email: str, name: str, tax: int = 1):
        super().__init__(email, name, tax)


class Flat:
    def __init__(self, flat_price: float, flat_address: str):
        self.flat_price = flat_price
        self.flat_address = flat_address


class RealEstateCompany:
    def __init__(self, client_list: list[Customer | LoyalCustomer], flat_list: list[Flat]):
        self.client_list = client_list
        self.flat_list = flat_list

    def cheapest(self):
        if len(self.flat_list) > 0:
            cheapest_flat = self.flat_list[0]
            for flat in self.flat_list:
                if flat.flat_price < cheapest_flat.flat_price:
                    cheapest_flat = flat
            return cheapest_flat
        else:
            return print("No flats")

    def sell(self, flat: list[Flat], client: list[Customer]):
        if flat in self.flat_list and client in self.client_list:
            print(f"Flat address: {flat.flat_address}, "
                    f"Customer email: {client.email}, "
                    f"Name: {client.name}"
                    f"Total payed: {client.total_amount}")
            self.flat_list.remove(flat)
        else:
            print("Client or Flat not found")
