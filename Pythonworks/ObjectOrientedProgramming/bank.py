class Bank:

    acno:int

    balance:int

    ac_type:str

    customer_name:str


    def __init__(self,acno,balance,ac_type,customer_name):

        self.acno=acno

        self.balance=balance

        self.ac_type=ac_type

        self.customer_name=customer_name

    def deposit(self,amount):

        self.balance=self.balance+amount

        print(f"your account{self.acno} has been credited with amount {amount} avl bal{self.balance}")


    def withdraw(self,amount):

        if self.balance>amount:

            self.balance-=amount

            print(f"your account{self.acno} has been debited with amount {amount} avl bal{self.balance}")
        else:
            print("insufficient ")


    def get_balance(self):

        print("your aval bal",self.balance)


customer_instance1=Bank(10000,2500,"savings","aseed")

customer_instance1.withdraw(5000)


# object oriented programming

#class
# object
# attributes
# methods
# self
# __init__  constructor()
# 
