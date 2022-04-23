from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = "https://i.etsystatic.com/5605787/r/il/9c7ac7/2476456317/il_570xN.2476456317_s72a.jpg"


class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<name: {self.name} species: {self.species} photo_url: {self.photo_url} age: {self.age} notes: {self.notes} available: {self.available}>"