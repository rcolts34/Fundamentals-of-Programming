test_dictionary = {1 : "1", 2: "2", 3: "3", 4: "4"}
print(test_dictionary.items())
print(list(test_dictionary.items()))
print(list(test_dictionary.items())[-2:])
print(dict(list(test_dictionary.items())[-2:]))
