from flask import Flask, request
from pathlib import Path

app_dir = Path(__file__).resolve().parent
app_work_dir = app_dir / Path('photos')

app = Flask(app_dir.name)


@app.route('/')
def index():
    return '<h1>Hello from Tolyan (Flask)!</h1>'


@app.route('/test/', methods=['HEAD'])
def test():
    return 'Bebebe'


@app.route('/dir/')
@app.route('/dir/<string:name>/')
def show_dir(name=''):
    """
    dir name like vasya/lyusya not allowed because of '/'
    so may be needed parameter like ?dir=vasya/lyusya
    '/' may be screened?..
    """
    dir_name = app_work_dir / name
    out_text = f'<h3>{name if name else "root"}</h3>>'
    root = request.url_root + 'dir/'
    for path_obj in dir_name.iterdir():
        path_for_url = path_obj.relative_to(app_work_dir)
        path_for_display = path_obj.relative_to(dir_name)
        if path_obj.is_dir():
            url = root + str(path_for_url)
            out_text += f'\n<div><a href="{url}">{path_for_display}</a></div>'
        else:
            out_text += f'\n<div>{path_for_display}</div>'
    return out_text
