import csv
import dearpygui.dearpygui as dpg

TABLE_TAG = "csv_table"
MAIN_WINDOW_TAG = "main_window"
READ_BUTTON_TAG = "read_csv"
READ_FILENAME_FIELD = "csv_file"
LOADED_FIELD = 'loaded'


def __read_csv_cars__():
    if dpg.does_alias_exist(TABLE_TAG):
        dpg.delete_item(TABLE_TAG, children_only=False)
    if dpg.does_alias_exist(TABLE_TAG):
        dpg.remove_alias(TABLE_TAG)
    with dpg.table(header_row=True, resizable=True, tag=TABLE_TAG, parent=MAIN_WINDOW_TAG):
        with open(dpg.get_value(READ_FILENAME_FIELD)) as f:
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
                    if num % 100 == 0:
                        dpg.set_value(value=f'Loaded so far: {num:,}', item=LOADED_FIELD)
            dpg.set_value(value=f'Loaded ALL', item=LOADED_FIELD)


if __name__ == '__main__':
    # os.environ["PYDEVD_USE_CYTHON"] = "YES"
    dpg.create_context()
    dpg.create_viewport(title='CSV reader')

    with dpg.window(
            label='Read CSV', tag=MAIN_WINDOW_TAG, width=1275, height=699
        ):
        dpg.add_text('CSV reader')
        dpg.add_input_text(
            label="Enter CSV file name", default_value='/home/tolic/Temp/10000.csv',
            tag=READ_FILENAME_FIELD
        )
        dpg.add_text('Loaded so far: ', tag=LOADED_FIELD)
        with dpg.group(horizontal=True):
            dpg.add_button(
                label="Read CSV", tag=READ_BUTTON_TAG,
                callback=__read_csv_cars__
            )
            with dpg.tooltip(READ_BUTTON_TAG):
                dpg.add_text("Read csv file")

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
