"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Ship, Favorite_Character, Favorite_Planet, Favorite_Ship
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_user():
    all_user = User.query.all()
    results = list(map(lambda user: user.serialize(), all_user))

    return jsonify(results), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()

    return jsonify(user.serialize()), 200
 
@app.route('/character', methods=['GET'])
def get_character():
    all_characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(),all_characters))
    return jsonify(characters), 200

@app.route('/character/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    character = Character.query.filter_by(id=character_id).first()

    if character is None:
        return jsonify({"error": "Character not found"}), 404

    return jsonify(character.serialize()), 200

@app.route('/character', methods=['POST'])
def post_character():
    body = request.get_json()

    if 'name' not in body:
        return jsonify('debes poner un nombre'), 200
    if 'birth_year' not in body:
        return jsonify('debes poner un birth_year'), 200
    if 'gender' not in body:
        return jsonify('debes poner un gender'), 200
    if 'height' not in body:
        return jsonify('debes poner un height'), 200
    if 'skin_color' not in body:
        return jsonify('debes poner un skin_color'), 200
    if 'eye_color' not in body:
        return jsonify('debes poner un eye_color'), 200
    
    if body['name'] == '':
        return jsonify('el nombre no puede estar vacio'), 200
    
    character = Character(name=body['name'], birth_year=body['birth_year'], gender=body['gender'], height=body['height'], skin_color=body['skin_color'],eye_color=body['eye_color'])
    db.session.add(character)
    db.session.commit()
    return jsonify('se creo character exitosamente'), 200


@app.route('/character/<int:character_id>', methods=['DELETE'])
def delete_character_by_id(character_id):
    character = Character.query.filter_by(id=character_id).first()

    if character is None:
        return jsonify({"error": "Character not found"}), 404
    
    db.session.delete(character)
    db.session.commit()

    return jsonify(character.serialize()), 200



#planet

@app.route('/planet', methods=['GET'])
def get_planet():
    all_planets = Planet.query.all()
    planets = list(map(lambda character: character.serialize(),all_planets))
    return jsonify(planets), 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planet.query.filter_by(id=planet_id).first()

    if planet is None:
        return jsonify({"error": "planet not found"}), 404

    return jsonify(planet.serialize()), 200

@app.route('/planet', methods=['POST'])
def post_planet():
    body = request.get_json()

    if 'name' not in body:
        return jsonify('debes poner un nombre'), 200
    if 'climate' not in body:
        return jsonify('debes poner un climate'), 200
    if 'population' not in body:
        return jsonify('debes poner un population'), 200
    if 'orbital_period' not in body:
        return jsonify('debes poner un orbital_period'), 200
    if 'rotation_period' not in body:
        return jsonify('debes poner un rotation_period'), 200
    if 'diameter' not in body:
        return jsonify('debes poner un diameter'), 200
    
    if body['name'] == '':
        return jsonify('el nombre no puede estar vacio'), 200
    
    planet = Planet(**body)
    db.session.add(planet)
    db.session.commit()
    return jsonify('se creo planet exitosamente'), 200


@app.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_by_id(planet_id):
    planet = Planet.query.filter_by(id=planet_id).first()

    if planet is None:
        return jsonify({"error": "planet not found"}), 404
    
    db.session.delete(planet)
    db.session.commit()

    return jsonify(planet.serialize()), 200

#ship

@app.route('/ship', methods=['GET'])
def get_ship():
    all_ships = Ship.query.all()
    ships = list(map(lambda ship: ship.serialize(),all_ships))
    return jsonify(ships), 200

@app.route('/ship/<int:ship_id>', methods=['GET'])
def get_ship_by_id(ship_id):
    ship = Ship.query.filter_by(id=ship_id).first()

    if ship is None:
        return jsonify({"error": "ship not found"}), 404

    return jsonify(ship.serialize()), 200

@app.route('/ship', methods=['POST'])
def post_ship():
    body = request.get_json()

    if 'name' not in body:
        return jsonify('debes poner un nombre'), 200
    if 'Model' not in body:
        return jsonify('debes poner un Model'), 200
    if 'manufacturer' not in body:
        return jsonify('debes poner un manufacturer'), 200
    if 'cost_in_credits' not in body:
        return jsonify('debes poner un cost_in_credits'), 200
    if 'crew' not in body:
        return jsonify('debes poner un crew'), 200
    
    if body['name'] == '':
        return jsonify('el nombre no puede estar vacio'), 200
    
    ship = Ship(**body)
    db.session.add(ship)
    db.session.commit()
    return jsonify('se creo ship exitosamente'), 200


@app.route('/ship/<int:ship_id>', methods=['DELETE'])
def delete_ship_by_id(ship_id):
    ship = Ship.query.filter_by(id=ship_id).first()

    if ship is None:
        return jsonify({"error": "ship not found"}), 404
    
    db.session.delete(ship)
    db.session.commit()

    return jsonify(ship.serialize()), 200

#favorites user

@app.route('/user/<int:user_id>/favorites', methods=['GET'])
def get_user_favorites(user_id):
    
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return jsonify("ERROR: User not found"), 400

    favorite_character = Favorite_Character.query.filter_by(user_id=user_id).all()
    favorite_planet = Favorite_Planet.query.filter_by(user_id=user_id).all()
    favorite_ship = Favorite_Ship.query.filter_by(user_id=user_id).all()

    favorite_character_data = []
    for favorite_character in favorite_character:
        character = Character.query.filter_by(id=favorite_character.character_id).first()
        favorite_character_data.append(character.serialize())

    favorite_planet_data = []
    for favorite_planet in favorite_planet:
        planet = Planet.query.filter_by(id=favorite_planet.planet_id).first()
        favorite_planet_data.append(planet.serialize())

    favorite_ship_data = []
    for favorite_ship in favorite_ship:
        ship = Ship.query.filter_by(id=favorite_ship.ship_id).first()
        favorite_ship_data.append(ship.serialize())

    return jsonify({
        "character": favorite_character_data,
        "planet": favorite_planet_data,
        "ship": favorite_ship_data
    }), 200


#favorite planet


@app.route('/favorites/planet', methods=['POST'])
def add_favorite_planet():
    request_body = request.get_json()
       
    user = User.query.get(request_body["user_id"])
    if user is None:
        return jsonify("no existe el id de usuario"), 400

    planet = Planet.query.get(request_body["planet_id"])
    if planet is None:
        return jsonify("no existe ese id de planeta"), 400
    
    existing_favorite = Favorite_Planet.query.filter_by(user_id=request_body["user_id"], planet_id=request_body["planet_id"]).first()
    if existing_favorite:
        return jsonify("planeta favorito ya existe"), 400

    new_favorite = Favorite_Planet(
        user_id=request_body["user_id"],
        planet_id=request_body["planet_id"],
        description=f"{user.username} likes {planet.name}"
    )

    db.session.add(new_favorite)
    db.session.commit()

    return jsonify(new_favorite.serialize()), 200

@app.route('/favorites/planet/<int:favorite_planet_id>', methods=['DELETE'])
def delete_favorite_planet(favorite_planet_id):
    
    #Para confirmar que existe el id que se quiere eliminar
    favorite_planet = Favorite_Planet.query.filter_by(id=favorite_planet_id).first()
    if favorite_planet is None:
        return jsonify("ERROR: Favorite planet not found"), 400

    db.session.delete(favorite_planet)
    db.session.commit()

    return jsonify(favorite_planet.serialize()), 200

#favorite character

@app.route('/favorites/character', methods=['POST'])
def add_favorite_character():
    request_body = request.get_json()
             
    user = User.query.get(request_body["user_id"])
    if user is None:
        return jsonify("no existe el id de usuario"), 400

    character = Character.query.get(request_body["character_id"])
    if character is None:
        return jsonify("no existe ese id de personaje"), 400
    
    existing_favorite = Favorite_Character.query.filter_by(user_id=request_body["user_id"], character_id=request_body["character_id"]).first()
    if existing_favorite:
        return jsonify("personaje favorito ya existe"), 400

    new_favorite = Favorite_Character(
        user_id=request_body["user_id"],
        character_id=request_body["character_id"],
        description=f"{user.username} likes {character.name}"
    )

    db.session.add(new_favorite)
    db.session.commit()

    return jsonify(new_favorite.serialize()), 200

@app.route('/favorites/character/<int:favorite_character_id>', methods=['DELETE'])
def delete_favorite_character(favorite_character_id):
    
    favorite_character = Favorite_Character.query.filter_by(id=favorite_character_id).first()
    if favorite_character is None:
        return jsonify("no se encontro el favorito"), 400

    db.session.delete(favorite_character)
    db.session.commit()

    return jsonify(favorite_character.serialize()), 200

#favorite ship

@app.route('/favorites/ship', methods=['POST'])
def add_favorite_ship():
    request_body = request.get_json()
             
    user = User.query.get(request_body["user_id"])
    if user is None:
        return jsonify("ERROR: user_id not exist"), 400

    ship = Ship.query.get(request_body["ship_id"])
    if ship is None:
        return jsonify("ERROR: ship_id not exist"), 400
    
    existing_favorite = Favorite_Ship.query.filter_by(user_id=request_body["user_id"], ship_id=request_body["ship_id"]).first()
    if existing_favorite:
        return jsonify("ERROR: favorite ship already exists for this user"), 400

    new_favorite = Favorite_Ship(
        user_id=request_body["user_id"],
        ship_id=request_body["ship_id"],
        description=f"{user.username} likes {ship.name}"
    )

    db.session.add(new_favorite)
    db.session.commit()

    return jsonify(new_favorite.serialize()), 200

@app.route('/favorites/ship/<int:favorite_ship_id>', methods=['DELETE'])
def delete_favorite_ship(favorite_ship_id):
    
    favorite_ship = Favorite_Ship.query.filter_by(id=favorite_ship_id).first()
    if favorite_ship is None:
        return jsonify("no se encontro el favorito"), 400

    db.session.delete(favorite_ship)
    db.session.commit()

    return jsonify(favorite_ship.serialize()), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
