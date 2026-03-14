#types of inheritance(single-level,multi-level,hierarchical,multiple,hybrid)
#single-level inheritance (One parent → one child)
print("Single-level inheritance example")
class A:
    def disp_A(self):
        print("Base or Parent class A")
class B(A):
    def disp_B(self):
        print("derived class B")
b=B()
b.disp_B()
b.disp_A()

#multi-level inheritance(here class will derive from already derived class
print("Single-level inheritance example")
class A:
    def disp_A(self):
        print("Base or Parent class A")
class B(A):
    def disp_B(self):
        print("it is act as both parent and child class B")
class C(B):
    def disp_C(self):
        print("it is derive from already derived class B")
c=C()
c.disp_C()
c.disp_A()
c.disp_A()

# hierarchical inheritance
print("hierarchical inheritance example")
class A:
    def disp_A(self):
        print("Base or Parent class A")
class B(A):
    def disp_B(self):
        print("it is derived from clas  A and class B")
class C(A):
    def disp_C(self):
        print("it is derived from class A and class C")
b=B()
b.disp_B()
b.disp_A()
c=C()
c.disp_C()

#mutliple inheritance
print("Multiple inheritance example")
class A:
    def disp_A(self):
        print("Base or Parent class A")
class B:
    def disp_B(self):
        print("it is without derived class B")
class C(A,B):
    def disp_C(self):
        print("it is derived from both class A and class B")
c=C()
c.disp_C()
c.disp_B()
c.disp_A()

#hybrid inheritance (combination of different types of inheritance