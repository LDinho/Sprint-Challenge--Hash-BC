#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(length):
        hash_table_insert(ht, weights[i], i)  # insert weights into hashtable

    for i in range(length):
        index_value = hash_table_retrieve(ht, limit - weights[i])  # limit - indexed weights

        print(f'value is {index_value}')

        if index_value is not None:
            if i > index_value:
                return i, index_value
            else:
                # return value first if index not larger
                return index_value, i

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


print(get_indices_of_item_weights([4, 6, 10, 15, 16], length=5, limit=31))
