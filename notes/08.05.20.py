# 1) Open parens must have a matching close paren (equal number of open and close)
# 2) Closed parens should come after open parens


def parensValid(stringInput):
    openCounter = 0
    closedCounter = 0

    for i in range(len(stringInput)):
        if stringInput[i] == "(":
            openCounter += 1
        if stringInput[i] == ")":
            closedCounter += 1

    if closedCounter > openCounter or openCounter > closedCounter:
        return False

    if openCounter == closedCounter:
        return True
    else:
        return False


print(parensValid("Y(3(p)p(3)r)s"))

# GO OVER REVERSE STRING AND LOOPING IN PY
