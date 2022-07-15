import sqlite3
from sqlite3 import Error

from .connection import create_connection


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

def insert_products(data):
    conn = create_connection()

    sql = """ INSERT INTO products (name, stars, price, img, description)
            VALUES(?, ?, ?, ?, ?)
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

def select_user_by_username(username):
    conn = create_connection()
    
    sql = f"SELECT * FROM tasks WHERE username = {username}" 

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        task = dict(cur.fetchone())
        return task
    except Error as e:
        print(f"Error at select_task_by_id : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def select_all_users():
    conn = create_connection()

    sql = "SELECT * FROM users"
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        user_rows = cur.fetchall()
        users = [ dict(users) for users in user_rows ]
        return users
    except Error as e:
        print(f"Error at select_all_users() : {str(e)}")
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
        products = [ dict(products) for products in product_rows ]
        return products
    except Error as e:
        print(f"Error at select_all_products: {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

