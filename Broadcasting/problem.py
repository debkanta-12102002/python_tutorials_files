"""
it calculate very fast then loop 
it is important two arrays are in shape shape or dimention
"""

prices=[100,200,300]
discount=10
final_prices=[]

for i in prices:
    final_price = i-(i*discount//100)
    final_prices.append(final_price)
print(final_prices)

# Too much lenghty code and very slow using loop for big data set