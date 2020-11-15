class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastname,"s cart")

customer1 = Customer()
customer1.name = "Chutayu"
customer1.lastname = "Adhitayawong"
customer1.age = 20
customer1.addCart()

customer2 = Customer()
customer2.name = "Asoka"
customer2.lastname = "Yentramas"
customer2.age = 21
customer2.addCart()

customer3 = Customer()
customer3.name = "Rawiporn"
customer3.lastname = "Kudsena"
customer3.age = 49
customer3.addCart()

