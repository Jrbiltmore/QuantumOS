import mysql.connector
from mysql.connector import Error

class MySQLConnector:
    def __init__(self, host="localhost", user="user", password="password", database="QuantumOSdb"):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print("MySQL database connection successful.")
        except Error as e:
            print(f"Error: '{e}'")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Failed to execute query: '{e}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Failed to read query: '{e}'")
            return None

# Example usage
if __name__ == "__main__":
    connector = MySQLConnector("localhost", "your_username", "your_password", "QuantumOSdb")
    
    # Create a new table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        role VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    ) ENGINE = InnoDB;
    """
    connector.execute_query(create_table_query)

    # Insert new data
    insert_query = """
    INSERT INTO users (name, role) VALUES
    ('Alice', 'Admin'),
    ('Bob', 'User');
    """
    connector.execute_query(insert_query)

    # Read data
    select_query = "SELECT * FROM users;"
    users = connector.read_query(select_query)
    for user in users:
        print(user)

    # Update data
    update_query = "UPDATE users SET role = 'Developer' WHERE name = 'Bob';"
    connector.execute_query(update_query)

    # Delete data
    delete_query = "DELETE FROM users WHERE name = 'Alice';"
    connector.execute_query(delete_query)
