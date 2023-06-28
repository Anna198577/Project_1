-- Tables storing the different types of dishes
CREATE TABLE IF NOT EXISTS starters(
    d_id INTEGER PRIMARY KEY AUTOINCREMENT,
    d_name TEXT NOT NULL,
        d_price_usd FLOAT NOT NULL,
        d_price_pln FLOAT NOT NULL,
        d_price_eur FLOAT NOT NULL,
    d_description TEXT NOT NULL,
    d_ingredients TEXT NOT NULL,
    d_diet_type TEXT NOT NULL,
    d_cuisine TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS mains(
    d_id INTEGER PRIMARY KEY AUTOINCREMENT,
    d_name TEXT NOT NULL,
        d_price_usd FLOAT NOT NULL,
        d_price_pln FLOAT NOT NULL,
        d_price_eur FLOAT NOT NULL,
    d_description TEXT NOT NULL,
    d_ingredients TEXT NOT NULL,
    d_diet_type TEXT NOT NULL,
    d_cuisine TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS desserts(
    d_id INTEGER PRIMARY KEY AUTOINCREMENT,
    d_name TEXT NOT NULL,
        d_price_usd FLOAT NOT NULL,
        d_price_pln FLOAT NOT NULL,
        d_price_eur FLOAT NOT NULL,
    d_description TEXT NOT NULL,
    d_ingredients TEXT NOT NULL,
    d_diet_type TEXT NOT NULL,
    d_cuisine TEXT NOT NULL
);

-- Table storing users data
CREATE TABLE IF NOT EXISTS users(
    u_id INTEGER PRIMARY KEY AUTOINCREMENT,
    u_username TEXT NOT NULL,
    u_password TEXT NOT NULL,
    u_creation_date NUMERIC NOT NULL,
    u_last_login_time NUMERIC NOT NULL,
    u_last_logout_time NUMERIC
);