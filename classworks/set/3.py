'''14. Write a Python program to find the longest common prefix of all strings. Use the Python set. '''
strings = ["flower", "flow", "flight"]
prefix = strings[0]
for s in strings[1:]:
     while not s.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            break
print("Longest common prefix:",prefix)