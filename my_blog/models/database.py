from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.create_all()
__all__ = [
    "db",
]
