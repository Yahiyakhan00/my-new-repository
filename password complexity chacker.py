def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in '!@#$%^&*()_+-=[]{};:\"|,.<>?/' for c in password):
        score += 1
    strength_levels = ['Very Weak', 'Weak', 'Moderate', 'Strong', 'Very Strong']
    return strength_levels[score]
