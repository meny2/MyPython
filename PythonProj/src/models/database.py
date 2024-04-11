import psycopg2

def connect_to_database():
    try:
        # Return connection object without establishing the connection
        connection = psycopg2.connect(
            dbname="postgres",
            user="admin",
            password="adminpwd",
            host="localhost",
            port="5432"
        )
        print("Database connection object created successfully!")
        return connection

    except psycopg2.Error as e:
        # Handle the database connection error
        print("Error creating database connection object:", e)
        return None
    