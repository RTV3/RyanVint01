#RVint_Module7_InterestCalculator 
# This program will determine how long it will take for an investment to double at a given interest rate



from tokenize import Double


print('Welcome to the Investment Calculator!\n')

initial_investment = float(input('How much is your intial investment?\n'))
interest_rate = float(input('What is your annual interest rate?\n'))
years = 0 
total = initial_investment


while total <= initial_investment*2:
    total = total + total * (interest_rate)/100
    years = years + 1
   
print(f'\nAt {interest_rate}%, Your investment will take {years} years to double!')






