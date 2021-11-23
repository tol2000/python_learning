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
        for row in enumerate(csv_reader):
            print(
                left_delimiter,
                center_delimiter.join(
                    [
                        f'{x[1]:{formats[x[0]]}}'
                        for x in enumerate(row[1])
                    ]
                ),
                right_delimiter,
                sep=''
            )
            if row[0] == 0:
                print_delimiter()
        print_delimiter()


if __name__ == '__main__':
    print('\n')
    read_csv_cars()
