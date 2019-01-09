#easy challenge 1
def challenge1(first_name, last_name):
    return "%s %s" % (last_name, first_name)
print(challenge1("John", "Doe"))

#easy challenge4
def numbers(number):
    if number == 0:
        print("zero")
    if number < 0:
        print("negative")
    if number > 0:
        print("positive")
numbers(0)

