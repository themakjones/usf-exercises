"""Flask app for Cupcakes"""

from flask import Flask, redirect, request, render_template, flash, jsonify
from models import Cupcake, connect_db, db, Default_Img
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jY*j9t79Jhf8'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mj_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def index_page():
    """Renders page listing cupcakes"""

    cupcakes = Cupcake.query.all()

    return render_template('index.html', cupcakes=cupcakes)

@app.route('/api/cupcakes')
def list_cupcakes():
    """List all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:id>')
def show_cupcake(id):
    """Shows cupcake based on id"""

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=['POST'])
def create_cupcake():
    """Creates a new cupcake in database"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json.get("image", Default_Img )

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Update cupcake and return json"""

    cupcake = Cupcake.query.get_or_404(id)
    db.session.query(Cupcake).filter_by(id=id).update(request.json)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Deletes cupcake"""

    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")