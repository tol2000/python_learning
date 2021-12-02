from configparser import ConfigParser

delimiter = 50 * '-'
mega_delimiter = '\n' + 3 * ('\n' + 100 * '*') + 2 * '\n'


def print_ini(ini):
    for section_name, section in list(ini.items())[::-1]:
        print(delimiter)
        print(f'[{section_name}]')
        for par_name, par_value in section.items():
            print(f'  {par_name} = "{par_value}"')
    print(delimiter)


def parse_config_and_write():
    ini = ConfigParser()
    ini.read("logman.ini", encoding='windows-1251')
    print_ini(ini)

    item = ('REM_Log_Tolyan_10', 'daysold')
    val = ini.getfloat(*item)
    print(f'{item}: {type(val)} = {val}')
    print(delimiter)

    section_name = 'Interface'
    interface = ini[section_name]
    par_name = 'iconblinkinterval'
    val = interface[par_name]
    print(f'{section_name}.{par_name} = {val}')
    par_name = 'dummy_int'
    val = interface.getint(par_name, fallback=0)
    print(f'{section_name}.{par_name} = {val}')
    print(delimiter)

    # Writing count demo...
    section_name = 'System'
    system = ini[section_name]
    par_name = 'Count'
    count = system.getint(par_name, fallback=0)
    count += 1
    system[par_name] = str(count)
    with open('logman.ini', 'w', encoding='windows-1251') as ini_file:
        ini.write(ini_file)


def config_as_dict():
    ini_dict = {
        'Dict Parser': {
            'regexp': "1",
            'casesensitive': "0",
            'ignorefromwords': "",
        },
        'Dict Interface': {
            'iconblinkinterval': "0",
            'silencederrors': "1",
            'program2view': "a:\\daractory\\Lister\\lister.exe",
            'program2viewparams': "//",
            'hotkey': "ctrl+c0",
            'pauseonactivatemainwindow': "1",
            'unpauseonhidemainwindow': "1",
        },
        'Dict System': {
            'readblocksize': "10240",
            'debug': "0",
        }
    }
    ini = ConfigParser()
    ini.read_dict(ini_dict)
    print_ini(ini)


if __name__ == '__main__':
    print('\n')
    parse_config_and_write()
    print(mega_delimiter)
    config_as_dict()
