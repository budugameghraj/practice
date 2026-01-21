class Products:
    count=0
    def __init__(self,name,price):
        self.Name=name
        self.Price=price
        Products.count+=1

    @classmethod
    def get_count(cls):
        return(f"The number of products are {cls.count}")

    @staticmethod
    def get_discount(price,discount):
        a=price-(price*discount/100)
        return(f"The offer price is {int(a)}/- only. ")

a=Products("Ice Cream",50)
b=Products("Hair dryer",1600)
c=Products("Laptop",80_000)

print(c.get_discount(c.Price,25))
print(Products.get_count())
