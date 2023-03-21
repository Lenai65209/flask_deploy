from flask_sqlalchemy import SQLAlchemy
db.create_all()
db = SQLAlchemy()
__all__ = [
    "db",
]
