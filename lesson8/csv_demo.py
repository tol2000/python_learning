import csv
from functools import reduce


def read_csv_cars():
    formats = [
        '>4',
        '<10',
        '<30',
        '<40',
        '>10',
    ]
    left_delimiter = '| '
    center_delimiter = ' | '
    right_delimiter = ' |'
    max_len = reduce(
        lambda x, y: x + y,
        [int(x[1:]) for x in formats]
    ) + len(right_delimiter) + (len(formats)-1) * len(center_delimiter) + len(right_delimiter)

    def print_delimiter():
        print(max_len * '-')

    with open("cars.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        print_delimiter()
        for row_num, row in enumerate(csv_reader):
            print(
                left_delimiter,
                center_delimiter.join(
                    [
                        f'{value:{formats[num]}}'
                        for num, value in enumerate(row)
                    ]
                ),
                right_delimiter,
                sep=''
            )
            if row_num == 0:
                print_delimiter()
        print_delimiter()


if __name__ == '__main__':
    print('\n')
    read_csv_cars()
