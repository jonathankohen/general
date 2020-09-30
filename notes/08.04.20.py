# def isPal(stringInput):
#     firstString = ''
#     revString = ''

#     for i in range(0, len(stringInput) - 1, 1):
#         firstString += stringInput[i]

#     for i in range(len(stringInput) - 1, 0, 1):
#         revString += stringInput[i]

#     if firstString == revString:
#         print("true!")
#     else:
#         print("false!")


# isPal('racecar')

# ourString = "Welcome to Python"


# def reverseString(stringInput):
#     newstr = ""
#     for i in range(len(stringInput)-1, -1, -1):
#         newstr += stringInput[i]
#     return newstr


# def isPal(stringInput):
#     if stringInput != reverseString(stringInput):
#         return False
#     else:
#         return True


# print(isPal("racecar"))

# def a(b, c):
#     if b < c:
#         return 7
#     else:
#         return 14
#     return 3


# print(a(2, 3))
# print(a(5, 3))
# print(a(2, 3) + a(5, 3))

# b = 500
# print(b)


# def a():
#     b = 300
#     print(b)
#     return b


# print(b)

# thang = {"name": "Noelle", "language": "Python"}

# for k in thang:
#     # keys
#     print(k)

# for k in thang:
#     # values at those keys
#     print(thang[k])

# for var1, var2 in thang.items():
#     # print either keys or values
#     print(f"{var1} - {var2}")

def ultimeate_analysis(someList):
    output = {'sumTotal': sum_total(someList), 'average': average(someList)...}
    print(output)
