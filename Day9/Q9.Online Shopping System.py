class Product:
    def __init__(self, product_id):
        self.product_id = product_id
class ElectronicProduct(Product):
    def __init__(self, product_id, power_usage):
        super().__init__(product_id)
        self.power_usage = power_usage
class MobilePhone(ElectronicProduct):
    def __init__(self, product_id, power_usage, brand):
        super().__init__(product_id, power_usage)
        self.brand = brand
    def display(self):
        print(f"Mobile: {self.brand} | ID: {self.product_id} | Power: {self.power_usage}W")
phone = MobilePhone("P-101", 20, "Samsung")
phone.display()
