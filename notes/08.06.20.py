def acro(str):
    acronym = f"{str[0]}"
    for i in range(len(str)):
        if str[i] == " ":
            acronym += (str[i + 1])
    return acronym


print(acro("National Basketball Association"))
print(acro("Central Intelligence Agency"))
print(acro("Federal Bureau of Investigation"))

# .split
# .join

string = "National Basketball Association"
acronym = ''.join(word[0] for word in string.upper().split())
print(acronym)
