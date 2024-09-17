from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    __tablename__ = 'Character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    height = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))

    
    def __repr__(self):
        return '<Character %r>' % self.Character

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color
        }

class Planet(db.Model):
    __tablename__ = 'Planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250))
    population = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    diameter = db.Column(db.String(250))

    def __repr__(self):
        return '<Planet %r>' % self.Planet

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter
        }

class Ship(db.Model):
    __tablename__ = 'Ship'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    Model = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    crew = db.Column(db.Integer)

    def __repr__(self):
        return '<Ship %r>' % self.Ship

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "Model": self.Model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
        }


# class User_character(db.Model):
#     __tablename__ = 'User_character'
#     id = db.Column(db.Integer, primary_key=True)
#     User_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#     User = db.relationship(User)
#     Character_id = db.Column(db.Integer, db.ForeignKey('Character.id'))
#     Character = db.relationship(Character)

# class User_Planet(db.Model):
#     __tablename__ = 'User_Planet'
#     id = db.Column(db.Integer, primary_key=True)
#     User_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#     User = db.relationship(User)
#     Planet_id = db.Column(db.Integer, db.ForeignKey('Planet.id'))
#     Planet = db.relationship(Planet)

# class User_Ship(db.Model):
#     __tablename__ = 'User_Ship'
#     id = db.Column(db.Integer, primary_key=True)
#     User_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#     User = db.relationship(User)
#     Ship_id = db.Column(db.Integer, db.ForeignKey('Ship.id'))
#     Ship = db.relationship(Ship)

# class Character_Ship(db.Model):
#     __tablename__ = 'Character_Ship'
#     id = db.Column(db.Integer, primary_key=True)
#     Character_id = db.Column(db.Integer, db.ForeignKey('Character.id'))
#     Character = db.relationship(Character)
#     Ship_id = db.Column(db.Integer, db.ForeignKey('Ship.id'))
#     Ship = db.relationship(Ship)