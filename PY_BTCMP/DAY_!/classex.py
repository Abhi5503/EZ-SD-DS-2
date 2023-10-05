class A:
    def printt(self, z, y):
        print(z[::-1])
        print(pow(y, 2))

    def display(self, z, y, x):
        print(len(z))
        print(y % x)

a = A()
x = int(input())
y = int(input())
z = input()
a.printt(z, y)
a.display(z, y, x)

'''
class A:
    def __init__(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = input("Enter z: ")

    def printt(self):
        res = self.z[::-1]
        print(pow(self.y, 2))
        print(res)

    def display(self):
        print(len(self.z))
        print(self.y % self.x)

a = A()
a.printt()
a.display()

'''