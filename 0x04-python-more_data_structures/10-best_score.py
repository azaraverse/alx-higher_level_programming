#!/usr/bin/python3
def best_score(a_dictionary):
    return (
        max(a_dictionary, key=lambda key: a_dictionary[key])
        if a_dictionary
        else None
    )
