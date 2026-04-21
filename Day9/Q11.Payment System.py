class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")
class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}")
class UPI(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount}")
class NetBanking(Payment):
    def process_payment(self, amount):
        print(f"Processing NetBanking payment of ${amount}")
def execute_payment(payment_method, amount):
    payment_method.process_payment(amount)
execute_payment(CreditCard(), 150)
execute_payment(UPI(), 50)
