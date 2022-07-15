from flask import request, jsonify, Blueprint

from database import tasks

session = {}


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
    print(username)
    print(password)

    if username is not None and password is not None:
        user = tasks.user_login(username, password)
        if user:
            session['loggedin'] = True
            session['id'] = user['user_id']
            session['username'] = username
            return jsonify({'login': True})
    return jsonify({'login': False})


logout_bp = Blueprint('routes-logout', __name__)


@logout_bp.route("/logout", methods=["POST"])
def login_render():
    if "loggedin" in session:
        session.pop('loggedin', None)
    if "id" in session:
        session.pop('id', None)
    if "username" in session:
        session.pop('username', None)
    return jsonify("good")


product_bp = Blueprint('routes-product', __name__)


@product_bp.route('/product', methods=['POST'])
def add_task():
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
def get_tasks():
    data = tasks.select_all_products()

    if data:
        return jsonify({'Product': data})
    elif data:
        return jsonify({'message': 'Internal Error'})
    else:
        return jsonify({'Product': {}})


product_selc_bp = Blueprint('routes-product/<string:id_p>', __name__)


@product_selc_bp.route('/product/<string:id_p>', methods=['GET'])
def selec_produc(id_p):
    if tasks.select_product_by_id(id_p):
        product = tasks.select_product_by_id(id_p)
        return jsonify(product)
    return False
