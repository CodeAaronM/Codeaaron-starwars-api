from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_planets = db.relationship('Favorite_Planet', backref='user', lazy=True)
    favorite_characters = db.relationship('Favorite_Character', backref='user', lazy=True)
    favorite_ships = db.relationship('Favorite_Ship', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    height = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    favorite_characters = db.relationship('Favorite_Character', backref='character', lazy=True)

    def __repr__(self):
        return '<Character %r>' % self.name

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
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250))
    population = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    diameter = db.Column(db.String(250))
    favorite_planets = db.relationship('Favorite_Planet', backref='planet', lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.name

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
    __tablename__ = 'ship'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    model = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    favorite_ships = db.relationship('Favorite_Ship', backref='ship', lazy=True)

    def __repr__(self):
        return '<Ship %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
        }

class Favorite_Planet(db.Model):
    __tablename__ = 'favorite_planet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Favorite_Planet %r>' % self.id

    def serialize(self):
        user = User.query.get(self.user_id)
        planet = Planet.query.get(self.planet_id)
        self.description = f"{user.email} likes {planet.name}"
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "description": self.description
        }

class Favorite_Character(db.Model):
    __tablename__ = 'favorite_character'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Favorite_Character %r>' % self.id

    def serialize(self):
        user = User.query.get(self.user_id)
        character = Character.query.get(self.character_id)
        self.description = f"{user.email} likes {character.name}"

        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "description": self.description
        }

class Favorite_Ship(db.Model):
    __tablename__ = 'favorite_ship'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Favorite_Ship %r>' % self.id

    def serialize(self):
        user = User.query.get(self.user_id)
        ship = Ship.query.get(self.ship_id)
        self.description = f"{user.email} likes {ship.name}"

        return {
            "id": self.id,
            "user_id": self.user_id,
            "ship_id": self.ship_id,
            "description": self.description
        }
