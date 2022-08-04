from app import db

class user(db.Model): # db.Model is a base class for all models from Flask-SQLAlchemy, it defines several fiels as class variables
  # fields are created as instances of teh db.Column class which take the field type as an argument plus
  # other optional argumes e.g. unique, indexed
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  # __repr__ tells Python how to print objects of this class
  def __repr__(self):
    return '<User {}>'.format(self.username)