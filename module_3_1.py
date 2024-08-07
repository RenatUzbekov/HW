calls = 0
def count_calls(call):
    global calls
    calls += call
    return (calls)
def string_info(string):
    a = []
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    count_calls(1)
    return a
def is_contains(string_info, list_to_search):
    string_info.lower()
    is_contains = []
    count_calls(1)
    for i in list_to_search:
        is_contains.append(i.lower())
    return (string_info.lower() in is_contains)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)