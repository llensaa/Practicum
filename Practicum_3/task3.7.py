raw = input('Enter number: ')
try:
    num = int(raw)
    print(num) 
except ValueError:
    print('This is not a number, please, try again')