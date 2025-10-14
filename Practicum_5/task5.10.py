pincode = input()
if len(pincode) == 4:
    list_numbers = [i for i in pincode]
    set_numbers = set(list_numbers)
    if len(list_numbers) == len(set_numbers):
        if int(pincode) in range(1900, 2051):
            print("ERROR")
        else:
            for j in len(pincode) - 1:
                if pincode[int(j) + 1] == int(pincode[int(j)]) + 1 or pincode[int(j) - 1] == int(pincode[int(j)]) - 1:
                    print("ERROR")
                else:
                    print("OK")
    else:
        print("ERROR")
else:
    print("ERROR")