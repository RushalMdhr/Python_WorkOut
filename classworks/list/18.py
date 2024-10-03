# 18. Write a Python program to generate and print a list of the first and last 5 elements where 
# the values are square numbers between 1 and 15 (both included). 
squares=[i**2 for i in range(1,16)]
result=squares[:5]+squares[-5:]
print(result)