import csv


def read_csv():
    word_list = []
    with open("input.csv") as input_file:
        csv_reader = csv.reader(input_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            word_list.append(row[0])
        print(word_list)
    return word_list
