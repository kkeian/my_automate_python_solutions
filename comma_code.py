# This code creates a comma separated sentence out of a list.

def returns_sentence_of_list(list_to_change):
    for i in range(len(list_to_change)):
        if i != len(list_to_change) - 1:
            print(list_to_change[0 + i] + ',', end =' ')
        else:
            print('and ' + list_to_change[-1])
