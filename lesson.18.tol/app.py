import urllib.parse

from flask import Flask, request
from pathlib import Path

SUBDIR_PARAM_NAME = 'subdir'

app_dir = Path(__file__).resolve().absolute().parent
app_work_dir = (app_dir / Path('photos')).resolve().absolute()

app = Flask('photo_v')


@app.route('/')
def index():
    return '<h1>Hello from Tolyan (Flask)!</h1>'


@app.route('/test/', methods=['HEAD'])
def test():
    return 'Bebebe'


def make_url_for_subdir(dir_url, path_for_url):
    return f'{dir_url}?{SUBDIR_PARAM_NAME}={urllib.parse.quote(str(path_for_url), safe="")}'


@app.route('/dir/')
def show_dir():
    subdir = request.args.get(f'{SUBDIR_PARAM_NAME}', '', str)
    dir_name = (app_work_dir / subdir).resolve().absolute()
    dir_url = request.url_root + 'dir/'

    # for security reasons :)
    if not str(dir_name).startswith(str(app_work_dir)):
        dir_name = app_work_dir
        subdir = ''

    out_text = f'<h3>Directory: {subdir if subdir else "root"}</h3><BR>'
    # out_text += f'\n<BR>app_work_dir: {app_work_dir}\n<BR>dir_name: {dir_name}'

    if app_work_dir in dir_name.parents:
        subdir_to_up = str(dir_name.parent)[len(str(app_work_dir))+1:]
        url = make_url_for_subdir(dir_url, subdir_to_up)
        out_text += f'\n<h4><a href="{url}">.. (up dir)</a></h4>'

    dir_list = sorted(list(dir_name.iterdir()), key=lambda x: (not x.is_dir(), str(x)))
    for path_obj in dir_list:
        path_for_url = path_obj.relative_to(app_work_dir)
        path_for_display = path_obj.relative_to(dir_name)
        if path_obj.is_dir():
            url = make_url_for_subdir(dir_url, path_for_url)
            out_text += f'\n<h4><a href="{url}">{path_for_display}</a></h4>'
        else:
            out_text += f'\n<h4>{path_for_display}</h4>'

    return out_text
