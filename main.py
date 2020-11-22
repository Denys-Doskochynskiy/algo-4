import csv
from typing import List
from write_read.read_file import read_csv
from write_read.write import create_write_to_file


def main(word_list: List[str]) -> int:
    word_list.sort(key=lambda len_word: len(len_word))  # asc
    print(word_list)

    words_dictinary = {}
    largest_chain = 0
    current_max = 1




if __name__ == '__main__':
    words = read_csv()
   # create_write_to_file(main(words))
    print(main(words))
