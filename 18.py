# #polymorphism(The same method name can perform different actions depending on the object.)
# # Poly = many
# # Morph = forms

class plane:
    def takeoff(self):
        print("Plane is Taking off")
    def fly(self):
        print("Plane is flying")
class Passenger(plane):
    def landing(self):
        print("Passenger Plane is landing")
class Cargo(plane):
    def landing(self):
        print("Cargo Plane is landing")
class Fighter(plane):
    def landing(self):
        print("Fighter Plane is landing")
p=Passenger()
c=Cargo()
f=Fighter()
def allowPlane(ref):
    ref.takeoff()
    ref.fly()
    ref.landing()
allowPlane(p)
allowPlane(c)
allowPlane(f)

#bird example
class Bird:
    def fly1(self):
        print("bird can fly")
    def eat(self):
        print("bird can eat")
class pegion(Bird):
    def fly(self):
        print("pegion can fly")
class crow(Bird):
    def fly(self):
        print("parrot can fly")
p=pegion()
c=crow()
def allow(obj):
    obj.fly1()
    obj.eat()
    obj.fly()
allow(p)
allow(c)

#olymorphism with Functions
class Bird:
    def fly(self):
        print("Bird is flying")
class Airplane:
    def fly(self):
        print("Airplane is flying")
def startFlying(obj):
    obj.fly()

b = Bird()
a = Airplane()
startFlying(b)
startFlying(a)


#payment system example
class Payment:
    def pay(self):
        pass
class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")
class UPI(Payment):
    def pay(self):
        print("Paid using UPI")
def makePayment(method):
    method.pay()
makePayment(CreditCard())
makePayment(UPI())

#best example for polymorphism
class credit:
    def process_amount(self, amount):
        return f"processing amount for credit car {amount}"

class paypal:
    def process_amount(self, amount):
        return f"processing amount for paypal car {amount}"

class bitcoin:
    def process_amount(self, amount):
        return f"processing amount for bitcoin car {amount}"

def checkout(process_method, total_amount):
    print(process_method.process_amount(total_amount))

c1 = credit()
p1 = paypal()
b1 = bitcoin()

checkout(c1, 1234)
checkout(p1, 5678)
checkout(b1, 90987)