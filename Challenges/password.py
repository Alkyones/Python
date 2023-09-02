def check_password_strength(password):
    metRequirement = 0
    specChars = list('!@#$%^&*()-=_+[]{}|;:,.<>/?!@#$%^&*()-=_+[]{}|;:,.<>/?')
    if len(password) >= 8 : metRequirement += 1
    if any(ele.isupper() for ele in password): metRequirement += 1
    if any(ele.islower() for ele in password): metRequirement += 1
    if any(ele.isnumeric() for ele in password): metRequirement += 1
    for char in specChars:
        if char in password:
            metRequirement += 1
            break
    
    if metRequirement == 5:
        return "Strong password"
    
    if metRequirement >= 3 and len(password) >= 6:
        return "Moderate password"
    
    return "Weak password"
    
    


print(check_password_strength("Password123!"))  # Strong password.
print(check_password_strength("Abcd1234"))      # Moderate password.
print(check_password_strength("password"))       # Weak password.
