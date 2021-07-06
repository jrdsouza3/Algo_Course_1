    
def main():
    x = input("enter 1st number")
    y = input("enter 2nd number")
    #x,y = 5678,1234

    result = karatsuba(int(x),int(y))

    print("Your result is :", result)


def karatsuba(num1, num2):
    len1 = len(str(num1))
    len2 = len(str(num2))
    if len1 == 1 or len2 == 1:
        return num1*num2


    a = int(num1 / (10**(len1/2)))
    b = int(num1 % (10**(len1/2)))
    c = int(num2 / (10**(len1/2)))
    d = int(num2 % (10**(len1/2)))
    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    abcd = karatsuba((a+b),(c+d))
    gauss = abcd-ac-bd #ad +bc

    first_term = int((10**len1) *ac)
    second_term = int((10**(len1/2)) * gauss)
    product = first_term + second_term + bd

    return product


    
if __name__ == "__main__":
    main()

