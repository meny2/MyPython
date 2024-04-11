import json
import psycopg2

def connect_to_database(config):
    try:
        connection = psycopg2.connect(
            dbname=config['dbname'],
            user=config['user'],
            password=config['password'],
            host=config['host'],
            port=config['port']
        )
        print(f"Connected to {config['name']} successfully!")
        return connection
    except psycopg2.Error as e:
        print(f"Unable to connect to {config['name']}: {e}")
        return None

# Read database configurations from JSON file
with open('config.json') as f:
    database_configs = json.load(f)
    
chosen_environment = database_configs['environment']

connection = {}
for env, db_config in database_configs.items():    
    if env == chosen_environment['name']:        
        connection = connect_to_database(db_config)
        break

cursor = connection.cursor()
cursor.execute("SELECT * FROM user_login;")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()
