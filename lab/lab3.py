# numbers = [2,3,4,5,6,7]
# found_prime = False

# for num in numbers:
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(f"{num} is a prime number")
#             found_prime = True

# if not found_prime:
#     print("No prime numbers")


lst = [[1, 2], [5, 6], [3, 4]]

# Implementing a basic sort using a loop (Bubble Sort example)
for i in range(len(lst)):
    for j in range(len(lst) - 1 - i):
        # Compare the last elements of the inner lists
        if lst[j][-1] > lst[j + 1][-1]:
            # Swap the lists if they are out of order
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)