import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class PostgreSQLAdapter:
    def __init__(self, host="localhost", database="QuantumOSdb", user="user", password="password"):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        print("Connection to PostgreSQL DB successful.")

    def create_table(self):
        commands = (
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                middle_names VARCHAR(255),
                last_names VARCHAR(255) NOT NULL,
                ssn CHAR(11),
                email VARCHAR(255) UNIQUE NOT NULL,
                additional_data JSONB
            )
            """,
        )
        cursor = self.conn.cursor()
        for command in commands:
            cursor.execute(command)
        cursor.close()
        print("Table created successfully.")

    def insert_user(self, first_name, middle_names, last_names, ssn, email, additional_data={}):
        cursor = self.conn.cursor()
        query = sql.SQL("""
            INSERT INTO users (first_name, middle_names, last_names, ssn, email, additional_data)
            VALUES (%s, %s, %s, %s, %s, %s)
        """)
        cursor.execute(query, (first_name, middle_names, last_names, ssn, email, json.dumps(additional_data)))
        cursor.close()
        print("User inserted successfully.")

    def query_users(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM users;"
        cursor.execute(query)
        print("Query results:")
        for record in cursor.fetchall():
            print(record)
        cursor.close()

    def update_user(self, user_id, **kwargs):
        cursor = self.conn.cursor()
        set_values = [f"{k} = %s" for k in kwargs.keys()]
        query = sql.SQL("UPDATE users SET " + ", ".join(set_values) + " WHERE user_id = %s")
        cursor.execute(query, list(kwargs.values()) + [user_id])
        cursor.close()
        print("User updated successfully.")

    def delete_user(self, user_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM users WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        cursor.close()
        print("User deleted successfully.")

# Example usage
if __name__ == "__main__":
    adapter = PostgreSQLAdapter("localhost", "QuantumOSdb", "your_username", "your_password")
    adapter.create_table()
    adapter.insert_user("Jacob", "Thomas", "Messer Redmond", "243-39-5449", "jrbiltmore@icloud.com", {"occupation": "Intelligence"})
    adapter.query_users()
    adapter.update_user(1, first_name="AEVespers")
    adapter.delete_user(1)
