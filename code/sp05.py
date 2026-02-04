# a product would cost $100, how much tax do we pay?


# product = 100 #in dollars
# tax_rate = 0.0625 #tax rate in massachusetts 6.25%
# tax = product * tax_rate
# print(f'The tax for the product, which costs ${product}, is ${tax}') 
# # f means an f-string, which means format string.
# # It allows us to include variables inside the string, using {}

from tifffile import product

computer_price = 1200
iphone_price = 800

def calc_tax(price, tax_rate):
    """Calculate product tax based on given price and return the tax amount.""" #docstring
    tax_rate = 0.0625 #tax rate in massachusetts 6.25%
    tax = price * tax_rate
    #print(f'The tax for the product, which costs ${price}, is ${tax}')
    #print(tax)
    #if the does not explicitly return any value, it would return None.

    return tax
print(calc_tax(computer_price, 0.0625))
print(calc_tax(iphone_price, 0.0625))

computer_price = float(input('Enter the product price:'))
iphone_price = 1100
mass_rate = 0.0625
ny_rate = 0.08875
tax_computer = calc_tax(computer_price, mass_rate)
tax_iphone = calc_tax(iphone_price, ny_rate)

total_tax = tax_computer + tax_iphone
print(total_tax)

# def calc_tax(price):
#     """Calculate product tax based on given price.""" #docstring
#     tax_rate = 0.0625 #tax rate in massachusetts 6.25%
#     tax = price * tax_rate
#     print(f'The tax for the product, which costs ${price}, is ${tax}')

# calc_tax(1200)
# calc_tax(800)

#function is a set of instructions that performs a certain task. 