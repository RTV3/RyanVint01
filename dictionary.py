# Ryan Vint_09/04/2022_Module 6_Dictionaries
# This program will create and display a dictionary and allows user to selct a key value pair to display 


print('Welcome!\n' )



new_vehicle = {
    'make': 'tesla',
    'model': 'plaid',
    'color': 'red', 
    'year': 2022,
    'top_speed': 230,
    'price': 160000,
    'range': 400,
    'purchase_date': '08/26/2022',
    'purchase_loc': 'omaha',
    'warranty?': 'yes',
    }

for information in new_vehicle.keys():
    print(information.title())

user_selection = input('\nPlease select an option to see the value\n')

selection = new_vehicle.get(user_selection, 'That key is not in the dictionary')
print(f'\n{selection}')



    
