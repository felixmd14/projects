def get_initial(name, force_uppercase = True, force_lowercase = True):
    if force_uppercase:
        initial = name[0:1].upper()
    elif force_lowercase:
        initial = name[0:1].lower()
    else:
        initial = name[0:1]
    return initial

fname = input('Please enter your first name: ')
lname = input('Please enter your last name: ')

print(f'Hi, {fname.capitalize()}, your initials are: {get_initial(force_uppercase = True, name = fname)}{get_initial(force_uppercase = False, name = lname)}.')