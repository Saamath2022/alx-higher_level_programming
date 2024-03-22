#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value


def test_function():
    dictionary1 = {'language': 'Python', 'number': 89, 'track': 'Low level'}


update_dictionary(dictionary1, 'number', 89)
print_dictionary(dictionary1)
dictionary2 = {'language': 'Python', 'number': 89, 'track': 'Low level'}
update_dictionary(dictionary2, 'city', 'San Francisco')
print_dictionary(dictionary2)

dictionary3 = {'language': 'Python', 'number': 89, 'track': 'Low level'}
update_dictionary(dictionary3, 'city', 'San Francisco')
update_dictionary(dictionary3, 'number', 89)
print_dictionary(dictionary3)

dictionary4 = {}
update_dictionary(dictionary4, 'city', 'San Francisco')
update_dictionary(dictionary4, 'language', 'Python')
update_dictionary(dictionary4, 'number', 89)
update_dictionary(dictionary4, 'track', 'Low level')
print_dictionary(dictionary4i)


def print_dictionar(a_dictionary):
    for key, value in a_dictionary.items():
        print(f"{key}: {value}")
        print("--")


if __name__ == "__main__":
    test_function()
