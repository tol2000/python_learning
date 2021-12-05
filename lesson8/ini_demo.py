import configparser
from configparser import ConfigParser

from configupdater import ConfigUpdater, Option

delimiter = 50 * '-'
mega_delimiter = '\n' + 3 * ('\n' + 100 * '*') + 2 * '\n'


def print_ini(ini):
    for section_name, section in list(ini.items())[::-1]:
        print(delimiter)
        print(f'[{section_name}]')
        for par_name, par_value in section.items():
            print(f'  {par_name} = "{par_value}"')
    print(delimiter)


def print_ini_updater(ini: ConfigUpdater):
    for section_name, section in list(ini.items())[::-1]:
        print(delimiter)
        print(f'[{section_name}]')
        for name, option in section.items():
            # print(type(option), option)
            print(f'  {option.key} = "{option.value}"')
    print(delimiter)


def parse_config_and_write(if_write=False):
    # can not preserve comments at all (
    ini = ConfigParser(comment_prefixes=(';', '#'))
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

    if if_write:
        # Writing count demo...
        section_name = 'System'
        system = ini[section_name]

        system['multiline'] = """
        'This is'
        '  a multiline with quotation'
        '  and indentation test value!'
        """

        par_name = 'Count'
        count = system.getint(par_name, fallback=0)
        count += 1
        system[par_name] = str(count)
        with open('logman.ini', 'w', encoding='windows-1251') as ini_file:
            ini.write(ini_file)


def parse_config_and_write_with_configupdater():
    ini = ConfigUpdater()
    ini.read("logman.ini", encoding='windows-1251')

    print_ini_updater(ini)

    option = ini['REM_Log_Tolyan_10']['daysold']
    val = float(option.value)
    print(f'[{option.section.name}].{option.key}: {type(val)} = "{val}"')
    print(delimiter)

    section_name = 'Interface'
    interface = ini[section_name]
    par_name = 'iconblinkinterval'
    val = interface[par_name].value
    print(f'{section_name}.{par_name} = {val}')
    par_name = 'dummy_int'
    val = interface.get(par_name, default=Option(par_name, '0')).value
    val = val if val else 0
    print(f'{section_name}.{par_name} = {val}')
    par_name = 'HotKey'
    val = interface[par_name].value
    val = val if val else 0
    print(f'{section_name}.{par_name} = {val}')
    print(delimiter)

    # Writing count demo...
    section_name = 'System'
    system = ini[section_name]

    par_name = 'multiline'
    # try:
    #     # WTF! In this place exception configparser.DuplicateOptionError not raised!
    #     # It raised only during ini.update_file() !
    #     # So at this place we have duplicate option 'multiline' without even any warnings
    #     system.add_option(system.create_option(
    #         key=par_name,
    #         value="""
    #             'Ok, it's'
    #             '  a multiline with quotation'
    #             '  and indentation test value!'
    #         """
    #     ))
    # except Exception as e:
    #     # configparser.DuplicateOptionError
    #     # print(e)
    #     pass
    if not system.get(par_name):
        system.add_option(system.create_option(
                key=par_name,
                value="""
                    'Ok, it's'
                    '  a multiline with quotation'
                    '  and indentation test value!'
                """
            ))

    # Fallback/default values does not work for me for a while...
    # par_name = 'Count'
    # # count = system[par_name].value
    # # system[par_name].value raises exception if no such option, but system.get return None
    # count = system.get(key=par_name)
    # count = count if count else 0
    # count += 1
    # system[par_name].value = str(count)

    with open('logman.ini', 'w', encoding='windows-1251') as f:
        ini.write(f)


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
    # this configparser does not preserve comments :(
    # parse_config_and_write(if_write=False)

    # But this one must preserve comments and do other additional things! :)
    parse_config_and_write_with_configupdater()

    # print(mega_delimiter)
    # config_as_dict()
