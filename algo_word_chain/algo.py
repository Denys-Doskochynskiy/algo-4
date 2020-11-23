from write_read_helper.find_max import find_max


def find_max_chain(word_list, words_dictinary, current_max):
    largest_chain = 0
    for word in word_list:

        iterator = 0
        while iterator < len(word):
            possible_word = word[:iterator] + word[iterator + 1:]

            if possible_word in words_dictinary:
                current_max = find_max(current_max, words_dictinary[possible_word] + 1)

            iterator += 1
        words_dictinary[word] = current_max
        largest_chain = find_max(largest_chain, current_max)

    return largest_chain
