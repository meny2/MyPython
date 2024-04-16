import psycopg2
import configparser


def environment():
    config = configparser.ConfigParser()
    config.read('config/connect_db.ini')
    if config.has_section('environment'):
        env=config.get('environment', 'env')
        print("Found ["+env+"] section in connect.ini")
        host, database, user, password = config.get(env, 'host'), config.get(env, 'database'), config.get(env, 'user'), config.get(env, 'password')
        return host, database, user, password
    else:
        print("Did not find [environment] section in connect.ini")
        return None    
   
def connect_to_database():
    result = environment()
    if result is not None:   
        host, database, user, password = result     
        try:
            connection = psycopg2.connect(host=host, database=database, user=user, password=password)
            print("Connected to PostgreSQL database")
            return connection
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            return None

def verify_user_login(connection, username, password):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE (username = %s OR email = %s) AND password = %s", (username, username, password))
        user = cursor.fetchone()
        if user:
            print("User login successful")
            return True
        else:
            print("Invalid username or password")
            return False
    except (Exception, psycopg2.Error) as error:
        print("Error while verifying user login", error)
        return False
    finally:
        if connection:
            cursor.close()

def verify_email(connection, email):
    emaildb = ""
    print('email',email)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s ", (email,))
        user = cursor.fetchone()        
        if user:           
            return user[3]
        else:            
            return ""
    except (Exception, psycopg2.Error) as error:
        print("Error while verifying email", error)
        return ""
    finally:
        if connection:
            cursor.close()

def update_password(connection, username, new_password):
    try:       
        cursor = connection.cursor()        
        # Execute the update query
        cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_password, username))
        
        # Commit the transaction
        connection.commit()
        
        print("Password updated successfully.")
        
    except (Exception, psycopg2.Error) as error:
        # Rollback the transaction in case of error
        if connection:
            connection.rollback()
        print("Error:", error)
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def insert_user(connection, username, email, password):
    try:       
        cursor = connection.cursor()   

        # Call the PostgreSQL function
        cursor.callproc('get_current_timestamp')
        # Fetch the timestamp returned by the function
        timestamp = cursor.fetchone()[0]

        # SQL INSERT statement to add the account to the users table
        sql = "INSERT INTO users (username, password, email, created_on) VALUES (%s, %s, %s, %s)"
        values = (username, password, email, timestamp)

        # Execute the update query
        cursor.execute(sql, values)
        
        # Commit the transaction
        connection.commit()
        
        print("Insert successfully.")
        
    except (Exception, psycopg2.Error) as error:
        # Rollback the transaction in case of error
        if connection:
            connection.rollback()
        print("Error:", error)
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()