import re

def is_valid_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Match the email address with the pattern
    if re.match(pattern, email):
        print('email T : ',email)
        return True
    else:        
        print('email F : ',email)
        return False