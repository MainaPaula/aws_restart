'''
import math

absolute = -5.999
floor_test = 198.42
result1 = math.fabs(absolute)
result2 = math.floor(floor_test)
print(result1, " is the absolute value of ", absolute)
print(result2, " is the flow of ", floor_test)

age = int(input("Enter your age: "))
try:
    value = 5 / 0
except ZeroDivisionError:
    value = 1

try:
    print(x)
except:
    print("An error has occurred")


def new_user():
    confirm = "N"
    while confirm != "Y":
        username = str(input("Enter the name of the user to add: "))
        print("Use the username '" + username + "'? (Y or N)")
        confirm = str(input("")).upper()
    print(username + " added")


new_user()

# Python program with 2 errors
var = "Double Value"
sumvalue = var + 4  # semantic error


def dosomething(valuetocheck):
    if valuetocheck > 4:
        print("Bad indent")

'''

txt = '''
ORIGIN      
1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
'''


x = ["ORIGIN", "1", "6", " ", "/"]
counter = 0
for i in txt:
    if i in x:
        clean = txt.replace(i, "")

print(clean)
