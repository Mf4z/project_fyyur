from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.ARRAY(db.String(120)))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean(), nullable=False, default=False)
    seeking_description = db.Column(db.String())

    shows = db.relationship('Show',backref='venues', cascade='delete,all', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean(), nullable=False, default=False)
    seeking_description = db.Column(db.String())

    shows = db.relationship('Show',backref='artists', cascade='delete,all', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()
# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))
    start_time = db.Column(db.DateTime, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()