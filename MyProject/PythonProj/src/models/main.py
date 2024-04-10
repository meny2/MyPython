from database import connect_to_database
from check_login import check_user_login

# Establish database connection
connection = connect_to_database()

# Call function to check user login
if connection:
    check_user_login(connection, "admin", "adminpwd")