from itertools import permutations
def gpermutations(s):
    tuples = permutations(s)
    list = [''.join(p) for p in tuples]
    return list
string = "abc"
result = gpermutations(string)
print(result)
