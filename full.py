test = "hello"

try:
    test
except NameError:
    test = "sup"

print(test)
