def check_password_stregth(password):
    score = 0           
    # check if password contains at least one 10
    if len(password) >=10:
        score += 2

    # check if the password contains at least one number
    if any(char.isdigit() for char in password):
        score += 2

    # check if the password contains at least  one uppercase letter
    if any(char.isupper() for char in password):
        score =+ 2

    # check if the password contains at least one lowercase letter
    if any(char.islower() for char in password):
        score += 2

    # check if the password contains at least one special character 
    special_character = "!@#$%^&*()_+-=<>?/"
    if any( char in special_character for char in password):
        score += 2

    #Determine the Strength based on the score
    if score <= 4:
        strength = "Weak"
    elif score <= 7:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score
# Ask the user for a passwod 
password = input("Enter your password: ")

# check the password strength
strength, score = check_password_stregth(password)

# print the result
print(f"Password Strength: {strength}, (Score: {strength}/10)")

# save the result to a file 
with open("password_results.txt", "a") as file:
    file.write(f"Password: {password}, Strength: {strength},Score: {score}/10\n")

# Ask for feedback
feedback = input("How was this tool? Leave feedback: ")

# Save feedbackto a file
with open("feedback.txt", "a") as feedback_file:
    feedback_file.write(f"Feedback: {feedback}\n")

print("Thank you for your feedback!")