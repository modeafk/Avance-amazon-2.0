import sqlite3
from sqlite3 import Error

from .connection import create_connection


# ------------------------------- users -------------------------------
def insert_user(data):
    conn = create_connection()

    sql = """ INSERT INTO users (username, email, password)
            VALUES(?, ?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(f"Error at insert_user() : {str(e)}")
        return False

    finally:
        if conn:
            cur.close()
            conn.close()


def select_user_by_id(_id):
    conn = create_connection()

    sql = f"SELECT * FROM users WHERE user_id = {_id}"

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        user = dict(cur.fetchone())
        return user
    except Error as e:
        print(f"Error at select_user_by_id : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def user_login(_username, _password):
    conn = create_connection()
    
    sql = f'''SELECT user_id FROM Users WHERE username='{_username}' 
            AND password='{_password}' '''

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        if cur.fetchall():
            cur = conn.cursor()
            cur.execute(sql)
            user_id = dict(cur.fetchone())
            return user_id
        return False
    except Error as e:
        print(f"Error at select_user_by_id : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


# ------------------------------- product -------------------------------
def insert_products(data):
    conn = create_connection()

    sql = """ INSERT INTO products (name, price, description, img)
            VALUES( ?, ?, ?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(f"Error at insert_products() : {str(e)}")
        return False

    finally:
        if conn:
            cur.close()
            conn.close()


def select_product_by_id(_id):
    conn = create_connection()

    sql = f"SELECT * FROM products WHERE product_id = {_id}"

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        product = dict(cur.fetchone())
        return product
    except Error as e:
        print(f"Error at select_product_by_id : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def select_all_products():
    conn = create_connection()

    sql = "SELECT * FROM products"
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        product_rows = cur.fetchall()
        products = [dict(row) for row in product_rows]
        return products
    except Error as e:
        print(f"Error at select_all_products() : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def update_task(_id, data):
    conn = create_connection()

    sql = f""" UPDATE products SET img = '{data}'
                WHERE product_id = {_id}
    """

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at update_task() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

# ------------------------------- cart ------------------------------- 
def insert_products_cart(_id_p, user_id):
    conn = create_connection()

    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Carrito WHERE user_ID='{user_id}' AND product_ID='{_id_p}'")
        if cur.fetchone():
            cur.execute(f"UPDATE Carrito SET cantidad=cantidad+1 WHERE user_ID='{user_id}' AND product_ID='{_id_p}'")
            conn.commit()
            print("stoy en 167")
            return True
        else:
            cur.execute(f"INSERT INTO Carrito (user_ID, product_ID, cantidad) VALUES ( '{user_id}', '{_id_p}', '{1}')")
            conn.commit()
            print("stoy en 171")
            return True
    except Error as e:
        print(f"Error at insert_products_cart() : {str(e)}")
        return False
