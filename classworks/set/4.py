'''15. Write a  Python program to find the two numbers whose product is maximum among all the 
pairs in a given list of numbers. Use the Python set.'''
numbers = [1, 10, 3, 9, 2, 8, 5, 7]
numbers = sorted(set(numbers))
max_product = 0#float('-inf')
max_pair = (None, None)
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = numbers[i] * numbers[j]
        if product > max_product:
            max_product = product
            max_pair = (numbers[i], numbers[j])
print(f"The pair with the maximum product is: {max_pair}")
print(f"The maximum product is:{max_product}")