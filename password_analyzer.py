def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Passsword too short" 
    # Check if the Password contains atleast one number
    if not any(char.isdigit() for char in password): 
        return "Weak: Password Must Contain  at least number"   
    # check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak: Password Must Contain at least one uppercase letter"
     # check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak: Password Must Contain at least one lowercase letter"
     # check if the password contains at least one special character 
    special_character = "!@#$%^&*()_+-=/.,<>?{}|"
    if not any(char in special_character for char in password):
        return "Weak: Password Must Contain at least one special chaacter"
    
    # if all checks pass 
    return "Password length is okay"
# Ask the user for a password 
password = input ("Enter your password: ")
    
# Print the result of the password check 
print(check_password_strength(password))
