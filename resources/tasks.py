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
<<<<<<< HEAD
        return jsonify(data)
    elif data == False:
=======
        return jsonify({'Product': data})
    elif data:
>>>>>>> 8fe05e731c7ee2403db0efc93bcd252341642d0d
        return jsonify({'message': 'Internal Error'})
    else:
        return jsonify({'data': {}})


<<<<<<< HEAD
@product_bp.route('/product', methods=['PUT'])
def update_product():
    product_id = request.json['product_id']
    img = request.json['img']

    if tasks.update_task(product_id, img):
        return jsonify({'Cambio': True})
    return jsonify({'Cambio': False})


@product_bp.route('/product/<string:id_p>', methods=['GET'])
=======
product_selc_bp = Blueprint('routes-product/<string:id_p>', __name__)


@product_selc_bp.route('/product/<string:id_p>', methods=['GET'])
>>>>>>> 8fe05e731c7ee2403db0efc93bcd252341642d0d
def selec_produc(id_p):
    if tasks.select_product_by_id(id_p):
        product = tasks.select_product_by_id(id_p)
        return jsonify(product)
    return False
