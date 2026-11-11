# class product:
#     def __init__(self,product_name,product_id,price,quantity):
#         self.product_name=product_name
#         self.product_id=product_id
#         self.price=price
#         self.quantity=quantity
#     def display_product(self):
#         print("product_name :",self.product_name)
#         print("product_id :",self.product_id)
#         print("price :",self.price)
#         print("quantity :",self.quantity)
#     def calculate_total(self):
#         print("total_stock_value :",self.price*self.quantity)
#     def update(self,new_price):
#         self.price=new_price
#         print("price update succesfully")
#         print("new price:",self.price)
        
# product1=product("laptop","p101",50000,5)
# product2=product("Mobile","p102",20000,10)
# product3=product("Headphone","p103",1500,20)
# product1.display_product()
# product1.calculate_total()
# product2.display_product()
# product2.calculate_total()
# product3.display_product()
# product3.calculate_total()



#2.
from abc import ABC,abstractmethod

class TravelBooking(ABC):
    def __init__(self,passenger_name,number_of_tickets):
        self.passenger_name=passenger_name
        self.number_of_tickets=number_of_tickets

    @abstractmethod
    def calculate_fare(self):
        pass
    @abstractmethod
    def display_booking_details(self):
        pass

class Busbooking(TravelBooking):
    def calculate_fare(self):
        return 500

    def display_booking_details(self):
        fare=self.calculate_fare()
        print("Busbooking")
        print("passenger name:",self.passenger_name)
        print("Number of tickets:",self.number_of_tickets)
        print("total fare:",self.number_of_tickets+fare)

class Trainbooking(TravelBooking):
    def calculate_fare(self):
        return 800

    def display_booking_details(self):
        fare=self.calculate_fare()
        print("Trainbooking")
        print("passenger name:",self.passenger_name)
        print("Number of tickets:",self.number_of_tickets)
        print("total fare:",self.number_of_tickets+fare)

class Flightbooking(TravelBooking):
    def calculate_fare(self):
        return 3000

    def display_booking_details(self):
        fare=self.calculate_fare()
        print("Flightbooking")
        print("passenger name:",self.passenger_name)
        print("Number of tickets:",self.number_of_tickets)
        print("total fare:",self.number_of_tickets*fare)

print("WELCOME TO TRAVEL BOOKING SYSTEM")
name=input("enter the customer name:")
ticket=int(input("enter the number of tickets:"))
print("""
1.Bus
2.Train
3.Flight"""
)
choice=int(input("select your travel type:"))
if choice==1:
    book=Busbooking(name,ticket)
elif choice==2:
    book=Trainbooking(name,ticket)
elif choice==3:
    book=Flightbooking(name,ticket)
else:
    print("Invalid type")

print("\n-------------BOOKING DETAILS------------")
book.display_booking_details()


        

        
