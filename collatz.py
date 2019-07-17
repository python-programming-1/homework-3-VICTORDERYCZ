def collatz(num):
    if num % 2 == 0:
        num = num/2
    else:
        num = (3*num) + 1
    print(num)
    return num

def get_num():
    run = True
    while run == True:
        try:
            num = int(input('Enter a positive integer: '))
            while num <= 0:
                print('Positive integers only.')
                num = int(input('Enter a positive integer: '))
            return num
        except: ValueError
        print('Must be a whole number.')

num = get_num()
while num != 1:
    num = collatz(num)

