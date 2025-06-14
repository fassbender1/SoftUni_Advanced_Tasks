class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

legal_age = 18
PIN, balance, age = map(int, input().split(", "))

while True:
    line = input().split("#")

    if line[0] == "End":
        break

    if line[0] == "Send Money":
        money, pin_code = int(line[1]), int(line[2])

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin_code != PIN:
            raise PINCodeError("Invalid PIN code")

        if age < legal_age:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money

        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    if line[0] == "Receive Money":
        money = int(line[1])

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        money_left = money * 0.5
        balance += money_left

        print(f"{money_left:.2f} money went straight into the bank account")










