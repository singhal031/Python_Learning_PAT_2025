# Create Patterns Using Nested Loops:-
# *
# **
# ***
# ****
# *****

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

# 1
# 12
# 123
# 1234
# 12345

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

#     *
#    ***
#   *****
#  *******
# *********
# rows = 5
# for i in range(1, rows + 1):
#     for s in range(rows - i):
#         print(" ", end="")
#     for k in range(2*i - 1):
#         print("*", end="")
#     print()


