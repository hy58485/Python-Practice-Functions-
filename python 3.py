#Write a Python function to multiply all the numbers in a list.

def Multiply_func(n1,n2,n3,n4,n5):
    list = [n1,n2,n3,n4,n5]
    mul = list[0]*list[1]*list[2]*list[3]*list[4]
    return mul
a = Multiply_func(8, 2, 3, -1, 7)
print(a)