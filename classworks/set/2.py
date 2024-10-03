'''13. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given 
value. '''
lst = [1, 4, 3, 2, 5, 7, 8, 6]
target_sum = 10
pairs = []
seen = set()
for number in lst:
    complement = target_sum - number
    if complement in seen:
        pairs.append((complement, number))
    seen.add(number)
print(f"Pairs in the list whose sum is equal to {target_sum}:")
print(pairs)