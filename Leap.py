leap = int(input('Type a year!'))

if (leap % 4) == 0:
    if (leap % 100) == 0:
        if (leap % 400) == 0:
            print ('THATS A LEAP')
        else:
            print("Not a leap")
    else:
        print('Not a leap')