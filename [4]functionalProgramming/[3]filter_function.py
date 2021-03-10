# -- Withdraw -->
bills = [200, 500, -150, -600, 1000]
def deposit(bill):
    return bill > 0

get_deposit = list(filter(deposit, bills))
print(get_deposit)


# -- Deposit -->
def withdraw(bill):
    return bill < 0

get_withdraw = list(filter(withdraw, bills))
print(get_withdraw) 