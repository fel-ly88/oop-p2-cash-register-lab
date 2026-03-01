class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity

        for _ in range(quantity):
            self.items.append(title)
    def apply_discount(self):
          if self.discount > 0:
              # discount is a percentage, e.g., 20
              self.total = self.total * (1 - self.discount / 100)
              print(f"After the discount, the total comes to ${int(self.total)}.")
          else:
              print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            self.total -= self.last_transaction
            self.last_transaction = 0

            # remove last items from list
            while self.items and self.total >= 0:
                self.items.pop()
                break

            if self.total < 0:
                self.total = 0.0