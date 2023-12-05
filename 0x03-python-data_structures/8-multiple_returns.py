#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        if sentence == 0:
            return 0, None
        return length, sentence[0]
