# GCD of two numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = int(input('Please enter first number '))
num2 = int(input('Please enter second number '))

ans = gcd(num1, num2)
print('the gcd is {}'.format(ans))