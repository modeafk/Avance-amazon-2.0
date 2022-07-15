CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products(
    "product_id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL UNIQUE,
	"price"	INTEGER NOT NULL,
	"description"	TEXT,
	"img"	BLOB NOT NULL UNIQUE,
	PRIMARY KEY("product_id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS Carrito (
    user_ID int,
    product_ID int,
    cantidad int
);
