import csv
import time
from rich.table import Table
from rich.progress import Progress


def read_csv_cars():
    with Progress(
        transient=False, auto_refresh=True, refresh_per_second=2,
        speed_estimate_period=1
    ) as progress:
        csv_task = progress.add_task("[red]Reading CSV...", start=False)
        with open("cars.csv") as f:
            csv_reader = csv.reader(f, delimiter=',')
            csv_table = Table(title=f'Table of {f.name}')
            for num, row in enumerate(csv_reader):
                progress.update(csv_task, total=3, completed=num)
                progress.console.print(f'Completed so far: {num}')
                if num == 0:
                    for column in row:
                        csv_table.add_column(column, justify="left", style="cyan", no_wrap=True)
                else:
                    csv_table.add_row(*list(row))
                time.sleep(1)
            progress.console.print(csv_table)


if __name__ == '__main__':
    print('\n')
    read_csv_cars()

