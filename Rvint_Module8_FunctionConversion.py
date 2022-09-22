#Rvint_Module8_FunctionConversion
#This program will convert miles to kilometers taking user input


print('Welcome to the miles to kilometers converter')



def mileage_converter():
    '''Basic function to convert miles to kilometers'''
    km = miles * 1.609344
    print(f'\n{miles} miles equals {km} kilometers')
while True:    #Prevent invalid values to be inputed by user and crash program
    try:
        miles = float (input('\nPlease enter the number of miles to be converted. '))
        break
    except ValueError:  
        print('Please enter a valid number')

mileage_converter()
    
   


        



    


