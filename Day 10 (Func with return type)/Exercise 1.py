# Functions with output

def fullname(fname, lname):
    if fname == "" or lname == "":
        return "You didn't provide valid inputs."
    name = fname + " " + lname
    return name.title()

fname = input("What is your first name? ")
lname = input("What is your last name? ")
print(fullname(fname, lname))
