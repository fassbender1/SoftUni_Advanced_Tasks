class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass


def special_chars(passwd, chars):
    only_digits = passwd.isdigit()
    only_chars = passwd.isalpha()
    only_specials = all(ch in chars for ch in passwd)
    return only_digits or only_chars or only_specials


passwd_length = 8
spec_chars = {"@", "*", "&", "%"}

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < passwd_length:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if special_chars(password, spec_chars):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in spec_chars for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

print("Password is valid")















