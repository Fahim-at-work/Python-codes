while True:
        try:
            num = int(input('Please enter a number to calculate factorial: '))
            if num < 0:
                raise ValueError
            break
        except ValueError as val_err:
            print("Please enter a positive number ")
        
            
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


fact_num = fact(num)

print('The factorial of {} is {} '.format(num, fact_num))
