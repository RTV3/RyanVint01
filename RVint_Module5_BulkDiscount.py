# Ryan Vint_09/03/2022_Module 5 Cost Calculator with Bulk Discount
# This program will calculate the price of fiber optic cable for a company

from tkinter import ttk




website_name = 'Super Cheap Fiber Optics'
rate = .87

print(f'Welcome to the {website_name} price calculator\n')

company_name = input('What is the name of your company?\n') #User inputs company name

while True:    #Prevent invalid values to be inputed by user and crash program
    try:
        cable_feet = float (input('\nHow many feet of cable do you need?\n'))
        break
    except ValueError:  
        print('Please enter a valid number')

if cable_feet>=500: # Applies discount depending on how many feet of cable are bought
    rate = .50

elif cable_feet>=250:
    rate = .70

elif cable_feet>=100:
    rate = .80

price = cable_feet * rate    #Price is in USD


print(f'\n{company_name}, that amount of fiber optic cable will cost ${price}')

print(f'\nThank you for shopping with {website_name}!')













