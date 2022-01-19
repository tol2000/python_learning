import logging
# import uuid
# from datetime import datetime
from pathlib import Path

LOG_FILE_EXTENSION = '.log'
base_dir = Path(__file__).resolve().parent
logs_subdir = 'logs'
logs_dir = base_dir.joinpath(logs_subdir)
# log_filename = f'{datetime.today().strftime("%Y-%m-%d-%H-%M-%S")}___{uuid.uuid4()}{LOG_FILE_EXTENSION}'
log_filename = f'main{LOG_FILE_EXTENSION}'
log_filename_with_path = logs_dir.joinpath(log_filename)

logs_dir.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="[LINE:%(lineno)-10d] # %(levelname)-8s [%(asctime)s] %(message)s",
    filename=log_filename_with_path,
    filemode='w'
)

# In productive mode this option may be turned off, if logging to file exists
duplicate_logging_to_stderr = True

# Duplicating logging to screen
if duplicate_logging_to_stderr:
    console = logging.StreamHandler()
    logging.getLogger('').addHandler(console)

debug = logging.getLogger('').isEnabledFor(logging.DEBUG)
