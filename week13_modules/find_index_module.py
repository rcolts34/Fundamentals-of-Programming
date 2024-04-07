
['apple', 'oranges', 'kiwi', 'mango']
if __name__ == '__main__':
    print('Imported find index module')
    test_var = 'Test String'
    print('Running find index module: ', __name__)


def find_index(search_list, target_val):
    for idx, val in enumerate(search_list):
        # print(idx, val)
        if val == target_val:
            return idx
    return -1



# print(find_index(['apple', 'oranges', 'kiwi', 'mango'], 'purple'))


# when file is run directly
# stops imported code from running in the background
# dunder variable → double underscore

# enumerate → returns the index and the element


