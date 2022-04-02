import urllib.parse
from flask import Flask, request, render_template
from PIL import Image
import base64
import io
from pathlib import Path

TAG_DIR_NAME = 'H1'
TAG_DIR_ROOT_UP = 'H1'
TAG_DIR_FILES_LIST = 'H1'

SUBDIR_PARAM_NAME = 'subdir'
PICTURE_PATH_PARAM_NAME = 'picture'
DIR_ENDPOINT = 'dir'
PICTURE_ENDPOINT = 'picture'

app_dir = Path(__file__).resolve().absolute().parent
app_work_dir = (app_dir / Path('public_files')).resolve().absolute()

app = Flask('photo_v')


@app.route('/')
def index():
    return '<h1>Hello from Tolyan (Flask)!</h1>'


@app.route('/test/', methods=['HEAD'])
def test():
    return 'Bebebe'


def make_url_for_subdir(dir_url, path_for_url):
    return f'{dir_url}?{SUBDIR_PARAM_NAME}={urllib.parse.quote(str(path_for_url), safe="")}'


def make_picture_url_for_subdir(picture_url: str, picture_subdir: Path, picture_name: Path):
    picture_path = str(Path(picture_subdir) / Path(picture_name))
    url = f'{picture_url}?{PICTURE_PATH_PARAM_NAME}={urllib.parse.quote(picture_path, safe="")}'
    url += f'&{SUBDIR_PARAM_NAME}={urllib.parse.quote(str(picture_subdir), safe="")}'
    return url


@app.route(f'/{PICTURE_ENDPOINT}/')
def show_picture():
    picture_path = request.args.get(f'{PICTURE_PATH_PARAM_NAME}', '', str)
    picture_dir_path = request.args.get(f'{SUBDIR_PARAM_NAME}', '', str)
    im = Image.open(app_work_dir / Path(picture_path))
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return render_template(
        'picture.html',
        img_data=encoded_img_data.decode('utf-8'),
        img_subdir_link=make_url_for_subdir(request.url_root + f'{DIR_ENDPOINT}/', picture_dir_path),
        tag_dir_root_up=TAG_DIR_ROOT_UP
    )


@app.route(f'/{DIR_ENDPOINT}/')
def show_dir():
    subdir = request.args.get(f'{SUBDIR_PARAM_NAME}', '', str)
    dir_name = (app_work_dir / subdir).resolve().absolute()
    dir_url = request.url_root + f'{DIR_ENDPOINT}/'
    picture_url = request.url_root + f'{PICTURE_ENDPOINT}/'

    # for security reasons :)
    if not str(dir_name).startswith(str(app_work_dir)):
        dir_name = app_work_dir
        subdir = ''

    out_text = f'<{TAG_DIR_NAME}>Directory: {subdir if subdir else "root"}</{TAG_DIR_NAME}><BR>'
    # out_text += f'\n<BR>app_work_dir: {app_work_dir}\n<BR>dir_name: {dir_name}'

    # root dir
    url = make_url_for_subdir(dir_url, '')
    out_text += f'\n<{TAG_DIR_ROOT_UP}><a href="{url}">Root directory</a></{TAG_DIR_ROOT_UP}>'

    # Parent dir (..)
    if app_work_dir in dir_name.parents:
        subdir_to_up = str(dir_name.parent)[len(str(app_work_dir))+1:]
        url = make_url_for_subdir(dir_url, subdir_to_up)
        out_text += f'\n<{TAG_DIR_ROOT_UP}><a href="{url}">.. (up dir)</a></{TAG_DIR_ROOT_UP}>'

    dir_list = sorted(list(dir_name.iterdir()), key=lambda x: (not x.is_dir(), str(x)))
    for path_obj in dir_list:
        path_for_url = path_obj.relative_to(app_work_dir)
        path_for_display = path_obj.relative_to(dir_name)
        if path_obj.is_dir():
            url = make_url_for_subdir(dir_url, path_for_url)
            out_text += f'\n<{TAG_DIR_FILES_LIST}><a href="{url}">{path_for_display}</a></{TAG_DIR_FILES_LIST}>'
        elif path_obj.suffix.lower() in ['.jpg', '.jpeg']:
            url = make_picture_url_for_subdir(picture_url, Path(subdir), Path(path_for_display))
            out_text += f'\n<{TAG_DIR_FILES_LIST}><a href="{url}">{path_for_display}</a></{TAG_DIR_FILES_LIST}>'

    return out_text
