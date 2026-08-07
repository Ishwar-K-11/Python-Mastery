# we will leran to create a custom exception


class InsufficientFundError(Exception):
    pass


def Withdraw_amount(balance, withdraw):
    if withdraw > balance:
        raise InsufficientFundError("Not enough Balance")
    print(f"Total Balance: {balance}")


try:
    Withdraw_amount(10000, 12000)

except InsufficientFundError as e:
    print(f"Error:{e}")

    print(f"Error Type: {type(e).__name__}")

except Exception as e:
    print(f"Error Type: {type(e).__name__}")
