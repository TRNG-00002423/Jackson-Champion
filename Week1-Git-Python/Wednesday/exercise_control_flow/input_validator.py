def validate_password(password):
    errors = []
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

        if char in "!@#$%^&*":
            has_special = True

    if not has_upper:
       errors.append("Password must contain at least one uppercase letter.")

    if not has_lower:
        errors.append("Password must contain at least one lowercase letter.")

    if not has_digit:
        errors.append("Password must contain at least one digit.")

    if not has_special:
        errors.append("Password must contain at least one special character.")

    if errors:
        return {"password": password, "valid": False, "errors": errors}

    return {"password": password, "valid": True, "errors": []}


print(f"\n{validate_password('Abc123!x')}")    # valid
print(f"\n{validate_password('abc')}")  # too short, no upper, no digit, no special
print(f"\n{validate_password('ABCDEFGH')}")    # no lower, no digit, no special
print(f"\n{validate_password('ABCDefgh1!')}")  # valid

print(f"\n{validate_password('Abc123!x')}")
