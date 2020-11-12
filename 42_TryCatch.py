import sys

randomList = ['a',0,2,]

for entry in randomList:
    try:
        print("The entry is",entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

x = "goodbye"
assert x == "goodbye","x should be 'hello'"

y = 101
assert  y <= 100 and y >= 0,"go 100 - 0"