class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

required_length = 5
valid_domains = [".com", ".net", ".org", ".net"]

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < required_length:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email.split(".")[-1]

    if f".{domain}" not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print(f"Email is valid")

