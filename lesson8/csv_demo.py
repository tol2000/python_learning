import csv
from csv import DictWriter
from functools import reduce
from pprint import pprint


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


def read_dict_cars():
    with open("cars.csv") as f:
        cars_dict = csv.DictReader(f)
        print(", ".join(cars_dict.fieldnames))
        for car in cars_dict:
            print(
                ", ".join([
                    f'{title}: "{value}"' for title, value in car.items()
                ])
            )


def write_csv_dict():
    NAME = 'name'
    DEPT = 'dept'
    BM = 'birth_month'
    with open('employees.csv', 'w') as f:
        csv_writer = DictWriter(f, [NAME, DEPT, BM])
        csv_writer.writeheader()
        csv_writer.writerows(
            [
                {
                    NAME: 'Tolyan',
                    DEPT: 'IT',
                    BM: 'July'
                },
                {
                    NAME: 'Mommy',
                    DEPT: 'Mothers',
                    BM: 'June'
                },
                {
                    NAME: 'Mike',
                    DEPT: '7th km',
                    BM: 'August'
                },
                {
                    NAME: 'Marine',
                    DEPT: 'Cutting shop',
                    BM: 'March'
                },
                {
                    NAME: 'Tucson',
                    DEPT: 'plant, garage',
                    BM: None
                },
            ]
        )


if __name__ == '__main__':
    print('\n')
    read_csv_cars()
    # read_dict_cars()
    # write_csv_dict()
