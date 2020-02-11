#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for tix in tickets:

        source = tix.source
        destination = tix.destination
        hash_table_insert(hashtable, source, destination)

    # source in 1st tix is none
    first_flight = hash_table_retrieve(hashtable, "NONE")
    # start of route = first tix.
    route[0] = first_flight

    # iterate hashtable
    for i in range(1, length):

        final_landing = hash_table_retrieve(hashtable, first_flight)
        route[i] = final_landing
        first_flight = final_landing

    return route
