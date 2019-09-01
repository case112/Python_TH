class Product(object):
    # we use TWO underscores to denote these are PRIVATE class values
    __name = "object"
    __price = 0
    __tax_rate = 0
    __discount = 0

    def __init__(self, name, price=0, discount=0, tax_rate=0):
        self.__name = name
        self.__price = price
        self.__discount = discount
        self.__tax_rate = tax_rate

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = value    

    @property
    def tax_rate(self):
        return self.__tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self.__tax_rate = value

    def calculated_discount_price(self, taxable=False):
        # callable method
        item_price = self.__price - (self.__price * self.__discount)
        if taxable:
            tax = self.__tax_rate
        else:
            tax = 0
        return item_price + (item_price * tax)

    def calculated_retail_price(self, taxable=False):
        # callable method
        # full retail price is discounted price with a zero discount
        item_price = self.__price
        if taxable:
            tax = self.__tax_rate
        else:
            tax = 0
        return item_price + (item_price * tax)    

    @property
    def retail_price(self):
        return self.calculated_retail_price()
    @property
    def retail_price_tax(self):
        return self.calculated_retail_price(taxable=True)
    @property
    def discount_price(self):
        return self.calculated_discount_price()
    @property
    def discount_price_tax(self):
        return self.calculated_discount_price(taxable=True)    



    def __str__(self):
        return """
        name: "{}"
        price: ${}
        discount: {} %
        discount price: ${}
        tax rate: {} %
        --------------------
        price with tax: ${}
        price with tax and discount ${}
        """.format(
               self.__name,
               self.__price,
               self.__discount * 100,
               self.discount_price,
               self.__tax_rate * 100,
               self.retail_price_tax,
               self.discount_price_tax
           )



if __name__ == '__main__':

    basic_grocery_tax_rate = 0.07
    luxury_item_tax_rate = 0.12

    apple = Product("Granny Smith Apple")
    apple.price = 1.25
    apple.tax_rate = 0.08
    apple.discount = 0.25

    print(apple)

    coke = Product("Coca Cola (six-pack)",
                   price=3.00,
                   discount=0.10, 
                   tax_rate=luxury_item_tax_rate)
    print(coke)

    simple = Product("Simple Simon Snack Pie",
                   price=1.00,
                   discount=0.10, 
                   tax_rate=luxury_item_tax_rate)
    print(simple)
