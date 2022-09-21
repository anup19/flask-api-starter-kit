from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .crypto import Crypto
from .kek import Kek
