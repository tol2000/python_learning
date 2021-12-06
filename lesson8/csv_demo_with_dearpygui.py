import csv
import dearpygui.dearpygui as dpg

TABLE_TAG = "csv_table"
MAIN_WINDOW_TAG = "main_window"
READ_BUTTON_TAG = "read_csv"


def __read_csv_cars__():
    # if dpg.does_alias_exist(TABLE_TAG):
    #     dpg.delete_item(TABLE_TAG, children_only=False)
    # if dpg.does_alias_exist(TABLE_TAG):
    #     dpg.remove_alias(TABLE_TAG)
    with dpg.table(header_row=True, resizable=True, tag=TABLE_TAG, parent=MAIN_WINDOW_TAG):
        with open("cars.csv") as f:
            csv_reader = csv.reader(f, delimiter=',')
            # f'Table of {f.name}'
            for num, row in enumerate(csv_reader):
                if num == 0:
                    for column in row:
                        dpg.add_table_column(label=column, parent=TABLE_TAG)
                else:
                    with dpg.table_row(parent=TABLE_TAG):
                        for column in row:
                            dpg.add_text(column)


if __name__ == '__main__':
    # os.environ["PYDEVD_USE_CYTHON"] = "YES"
    dpg.create_context()

    with dpg.window(label='Read CSV', tag=MAIN_WINDOW_TAG):
        dpg.add_text('CSV reader result')
        with dpg.group(horizontal=True):
            dpg.add_button(label="Read CSV", tag=READ_BUTTON_TAG, callback=__read_csv_cars__)
            with dpg.tooltip(READ_BUTTON_TAG):
                dpg.add_text("Read csv file")

    dpg.create_viewport(title='CSV reader')
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
