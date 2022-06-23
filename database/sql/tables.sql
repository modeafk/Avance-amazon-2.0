
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    stars INTEGER,
    price INTEGER NOT NULL,
    img TEXT,
    description TEXT
);

INSERT INTO users (username, email, password)
VALUES
("admin", "admin@gmail.com", "perritos3");

INSERT INTO products (name, stars, price, img, description)
VALUES
(
    "Figura de Accion Krilin",
    5,
    60,
    "product-1.jpg",
    ""
),
(
    "Figura de Accion Freezer",
    5,
    60,
    "product-2.jpg",
    ""
),
(
    "Figura de Accion Bardok",
    5,
    60,
    "product-3.jpg",
    ""
),
(
    "Figura de Accion Goku",
    5,
    60,
    "product-4.png",
    ""
),
(
    "Figura de Accion Naruto",
    5,
    70,
    "product-5.png",
    ""
),
(
    "Figura de Accion Madara",
    5,
    70,
    "product-6.png",
    ""
),
(
    "Figura de Accion Jiraiya",
    5,
    70,
    "product-7.png",
    ""
),
(
    "Figura de Accion Itachi H.",
    5,
    70,
    "product-8.png",
    ""
),
(
    "Sudadera Color Rojo",
    5,
    90,
    "product-9.png",
    ""
),
(
    "Sudadera Color Plomo",
    5,
    90,
    "product-10.png",
    ""
),
(
    "Sudadera Color Plomo",
    5,
    90,
    "product-11.png",
    ""
),
(
    "Sudadera Color Negro",
    5,
    90,
    "product-12.png",
    ""
)
;