import sqlite3, json, os, bcrypt, datetime
from Components.Dishes.Dish import Dish

class Connector:
    def __init__(self, db_name: str = "restaurant.db", fill_db = False):
        self.db_name = db_name
        path = os.getcwd().replace('\\', '/')
        self.db_path = f"{path}/Data/Database/{db_name}"
        self.fill_db = fill_db
        self.setup()

    def setup(self):
        with sqlite3.connect(self.db_path) as connection:
            with open("setup.sql", 'r') as sql_setup:
                separated_queries = sql_setup.read().split(";")[:-1]
                for query in separated_queries:
                    connection.execute(f"{query.lstrip()};")
        
        if self.fill_db:
            filepath = os.getcwd().replace('\\', '/') + "/Data/menu_data.json"
            with open(filepath, 'r', encoding='utf8', errors="ignore") as in_file:
                all_dishes = json.load(in_file)
            
            for category, dishes in all_dishes.items():
                for dish in dishes.values():
                    self.add_dish(Dish(*dish.values()).get_tuple_data(), category)
            

    ############################################################################################
    #                                                                                          #
    #                                       DISHES                                             #
    #                                                                                          #
    ############################################################################################

    def add_dish(self, dish: tuple, category: str) ->  None:
        valid_categories = ('starters', 'mains', 'desserts')
        if category in valid_categories:
            insert_dish_query = f"INSERT INTO {category} (d_name, d_price_usd, d_price_pln, d_price_eur, d_description, d_ingredients, d_diet_type, d_cuisine) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            with sqlite3.connect(self.db_path) as connection:
                connection.execute(insert_dish_query, dish)
                connection.commit()
        else:
            raise ValueError("ERROR: Function connector.py -> Connector.add_dish: No such category found.")

    def get_dish(self, name: str, category: str) -> Dish:
        valid_categories = ('starters', 'mains', 'desserts')
        if category in valid_categories:
            select_dish_query = f"SELECT * FROM {category} WHERE d_name = (?)"
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.execute(select_dish_query, (name,))
                dish = cursor.fetchone()

                price = {
                    "price_usd": dish[2],
                    "price_pln": dish[3],
                    "price_eur": dish[4]
                }

                return Dish(dish[1], price, dish[5], json.loads(dish[6]), dish[7], dish[8])
        else:
            raise ValueError("ERROR: Function connector.py -> Connector.add_dish: No such category found.")

    # Lista krotek wszystkich dań
    def get_all_starters(self) -> dict:
        select_starters_query = "SELECT * FROM starters"
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(select_starters_query)
            starters = cursor.fetchall()

        for i in range(len(starters)):
            starters[i] = {
                "name" : starters[i][1],
                "price": {
                    "price_usd": starters[i][2],
                    "price_pln": starters[i][3],
                    "price_eur": starters[i][4]
                },
                "description": starters[i][5],
                "ingredients": json.loads(starters[i][6]),
                "diet_type"  : starters[i][7],
                "cuisine"    : starters[i][8],
            }
        return starters

    def get_all_mains(self) -> dict:
        select_mains_query = "SELECT * FROM mains"
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(select_mains_query)
            mains = cursor.fetchall()

        for i in range(len(mains)):
            mains[i] = {
                "name" : mains[i][1],
                "price": {
                    "price_usd": mains[i][2],
                    "price_pln": mains[i][3],
                    "price_eur": mains[i][4]
                },
                "description": mains[i][5],
                "ingredients": json.loads(mains[i][6]),
                "diet_type"  : mains[i][7],
                "cuisine"    : mains[i][8],
            }
        return mains


    def get_all_desserts(self) -> dict:
        select_desserts_query = "SELECT * FROM desserts"
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(select_desserts_query)
            desserts = cursor.fetchall()

        for i in range(len(desserts)):
            desserts[i] = {
                "name" : desserts[i][1],
                "price": {
                    "price_usd": desserts[i][2],
                    "price_pln": desserts[i][3],
                    "price_eur": desserts[i][4]
                },
                "description": desserts[i][5],
                "ingredients": json.loads(desserts[i][6]),
                "diet_type"  : desserts[i][7],
                "cuisine"    : desserts[i][8],
            }
        return desserts

    # Functions that remove dishes
    def remove_dish(self, name: str, category: str) -> None:
        valid_categories = ('starters', 'mains', 'desserts')
        if category in valid_categories:
            delete_dish_query = f"DELETE FROM {category} WHERE d_name = (?)"
            with sqlite3.connect(self.db_path) as connection:
                connection.execute(delete_dish_query, (name,))
                connection.commit()
        else:
            raise ValueError("ERROR: Function connector.py -> Connector.remove_dish: No such category found.")

    def remove_all_dishes(self) -> None:
        queries = ["DELETE FROM starters;", "DELETE FROM mains;", "DELETE FROM desserts;"]
        with sqlite3.connect(self.db_path) as connection:
            for query in queries:
                connection.execute(query)
            connection.commit()

    def remove_all_starters(self) -> None:
        delete_query = "DELETE FROM starters"
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(delete_query)
            connection.commit()

    def remove_all_mains(self) -> None:
        delete_query = "DELETE FROM mains"
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(delete_query)
            connection.commit()

    def remove_all_desserts(self) -> None:
        delete_query = "DELETE FROM desserts"
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(delete_query)
            connection.commit()

    ############################################################################################
    #                                                                                          #
    #                                       USERS                                              #
    #                                                                                          #
    ############################################################################################

    # To jest praktycznie rejestracja użytkownika
    def add_user(self, username: str, password: str) ->  bool:
        if self.user_exists(username):
            return False
        insert_user_query = f"INSERT INTO users (u_username, u_password, u_creation_date, u_last_login_time, u_last_logout_time) VALUES (?, ?, ?, ?, ?)"
        with sqlite3.connect(self.db_path) as connection:
            data = (
                username,
                self.password_hash(password),
                datetime.date.today(),
                datetime.datetime.now().timestamp(),
                None
            )
            connection.execute(insert_user_query, data)
            connection.commit()
        return True

    def user_exists(self, username: str):
        select_user_query = "SELECT * FROM users WHERE u_username = (?)"
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(select_user_query, (username,))
            result = cursor.fetchone()
        return result != None

    def validate_user(self, username: str, password: str) -> bool:
        select_user_query = "SELECT * FROM users WHERE u_username = (?) AND u_password = (?)"
        password = self.password_hash(password)
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(select_user_query, (username, password))
            result = cursor.fetchone()
        return result != None

    def get_user(self, username: str):
        select_user_query = "SELECT * FROM users WHERE u_username = (?)"
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(select_user_query, (username,))
            result = cursor.fetchone()
        return result

    def get_all_users(self):
        select_all_users = "SELECT * FROM users"
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(select_all_users)
            result = cursor.fetchall()
        return result

    def remove_user(self, username: str):
        delete_user_query = "DELETE FROM users WHERE u_username = (?)"
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(delete_user_query, (username,))
            connection.commit()

    def remove_all_users(self):
        delete_all_users_query = "DELETE FROM users"
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(delete_all_users_query)
            connection.commit()

    def update_user_login_time(self, username):
        update_login_time_query = "UPDATE users SET u_last_login_time = (?) WHERE u_username = (?)"
        with sqlite3.connect(self.db_path) as connection:
            current_login_time = datetime.datetime.now().timestamp()
            connection.execute(update_login_time_query, (current_login_time, username))
            connection.commit()

    def update_user_logout_time(self, username):
        update_logout_time_query = "UPDATE users SET u_last_logout_time = (?) WHERE u_username = (?)"
        with sqlite3.connect(self.db_path) as connection:
            current_logout_time = datetime.datetime.now().timestamp()
            connection.execute(update_logout_time_query, (current_logout_time, username))
            connection.commit()

    def password_hash(self, password: str):
        encoded_password = password.encode("utf-8")
        salt = b'$2b$12$pbTh4UTNZVuRERdVxicbve'
        hash_p = bcrypt.hashpw(encoded_password, salt)
        return hash_p