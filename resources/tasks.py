from math import fabs
from operator import truediv
from flask import request, jsonify, Blueprint

from database import tasks

session = { "loggedin": False,
            "id":None,
            "username": None
}


register_bp = Blueprint('routes-register', __name__)


@register_bp.route('/register', methods=['POST'])
def add_user():
    username = request.form.get('username')
    email = request.form.get("email")
    password = request.form.get("password")

    if username is not None and email is not None and password is not None:
        data = (username, email, password)
        user_id = tasks.insert_user(data)
        if user_id:
            return jsonify({'register': True})
    return jsonify({'register': False})


login_bp = Blueprint('routes-login', __name__)


@login_bp.route('/login', methods=['POST'])
def seccion_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username is not None and password is not None:
        user = tasks.user_login(username, password)
        if user:
            session['loggedin'] = True
            session['id'] = user['user_id']
            session['username'] = username
            return jsonify({'login': True})
    return jsonify({'login': False})


@login_bp.route('/login', methods=['GET'])
def loget():
    if session:
        A= {'id': session['id'], 'loggedin':session['loggedin'], 'username':session['username']}
        return jsonify (A)
    return jsonify({"loggedin":False})


logout_bp = Blueprint('routes-logout', __name__)


@logout_bp.route("/logout", methods=["POST"])
def login_render():
    if "loggedin" in session:
        session.pop('loggedin',None)
        session.pop('id', None)
        session.pop('username', None)
    print(session)
    return jsonify({'login': False})


product_bp = Blueprint('routes-product', __name__)


@product_bp.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    img = request.json['img']

    data = (name, price, description, img)
    product_id = tasks.insert_products(data)

    if product_id:
        task = tasks.select_product_by_id(product_id)
        return jsonify(task)
    return jsonify({'message': 'Internal Error'})


@product_bp.route('/product', methods=['GET'])
def get_product():
    data = tasks.select_all_products()

    if data:
        return jsonify(data)
    elif data == False:
        return jsonify({'message': 'Internal Error'})
    else:
        return jsonify({'data': {}})


@product_bp.route('/product', methods=['PUT'])
def update_product():
    product_id = request.json['product_id']
    img = request.json['img']

    if tasks.update_task(product_id, img):
        return jsonify({'Cambio': True})
    return jsonify({'Cambio': False})


@product_bp.route('/product/<string:id_p>', methods=['GET'])
def selec_produc(id_p):
    if tasks.select_product_by_id(id_p):
        product = tasks.select_product_by_id(id_p)
        return jsonify(product)
    return False


cart_product = Blueprint('routes-cart', __name__)

@cart_product.route("/cart/<string:id_p>", methods=["POST"])
def add_cart(id_p):
    if session['loggedin'] == False:
        return jsonify({'success':False})
    int_id_p = int(id_p)
    int_secID = int(session['id'])
    tasks.insert_products_cart(int_id_p, int_secID)
    return jsonify({'success':True})
