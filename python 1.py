#Write a Python function to find the Max of three numbers.

def MaxNumber(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    elif n2>n1:
        if n2>n3:
            return n2
        else:
            return n3
Num = MaxNumber(22,13,35)
print(Num)

