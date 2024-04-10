# Assuming database_configs is a dictionary containing configurations for different environments
database_configs = {
    "dev": {"dbname": "dev_db", "user": "dev_user", "password": "dev_password"},
    "uat": {"dbname": "uat_db", "user": "uat_user", "password": "uat_password"},
    "prod": {"dbname": "prod_db", "user": "prod_user", "password": "prod_password"}
}

# Iterating over each environment in the database_configs dictionary
for env, db_config in database_configs.items():
    print("Environment:", env)
    print("Database Configuration:", db_config)
