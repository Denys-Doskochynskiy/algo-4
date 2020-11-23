from typing import List
from write_read_helper.read_file import read_csv
from write_read_helper.write import create_write_to_file
from algo_word_chain.algo import find_max_chain

"""
        sort list of word by there length,then 
        find max chain of this words 
        :param word_list: list of words
        :return: our max chain of word
"""


def main(word_list):
    list_word = sorted(word_list, key=len)  # asc
    words_dictionary = {}
    current_max = 1
    return find_max_chain(list_word, words_dictionary, current_max)


if __name__ == '__main__':
    file = 'input.csv'
    create_write_to_file(main(read_csv(file)))
    print(main(read_csv(file)))
