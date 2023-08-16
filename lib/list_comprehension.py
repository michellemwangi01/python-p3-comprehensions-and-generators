#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [num for num in num_list if num % 2 == 0]
    return evens_list


print(return_evens([1, 2,3, 5, 7]))


def make_exclamation(sentence_list):
    exclamation_sentence = [(sentence + "!") for sentence in sentence_list]
    return exclamation_sentence


print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
