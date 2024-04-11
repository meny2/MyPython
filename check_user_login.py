# user.py
from connect import connect_to_database

def check_user_login(username, password):
    # Connect to the database
    connection = connect_to_database()
    if connection:
        try:
            # Create a cursor object
            cursor = connection.cursor()

            # Execute SQL query to check user login
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password,))
            
            # Fetch the result
            user = cursor.fetchone()
            
            # Check if user exists
            if user:
                print("Login successful for user:", username)
                # Add code here to proceed after successful login
            else:
                print("Login failed for user:", username)

            # Close the cursor
            cursor.close()

        except psycopg2.Error as e:
            # Handle the database error
            print("Error querying the database:", e)

        finally:
            # Close the connection
            connection.close()
