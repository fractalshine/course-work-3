import logging

# path config
POST_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"
BOOKMARKS_PATH = "data/bookmarks.json"
UPLOAD_FOLDER = "uploads/images"
LOGS_PATH = "logs/basic.log"
LOGS_API_PATH = "logs/api.log"

# ext conf
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# logs conf

# basic logger
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOGS_PATH)
log_formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

# logger for api
logger_api = logging.getLogger("logger_api")
logger_api.setLevel(logging.INFO)
file_handler_api = logging.FileHandler(LOGS_API_PATH)
log_formatter_api = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler_api.setFormatter(log_formatter_api)
logger_api.addHandler(file_handler_api)
