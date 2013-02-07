def max(a, b):
    return a if a > b else b
    
def min(a, b):
    return a if a < b else b
    
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
    
pi = 3.141592653589793
e = 2.718281828459045

def account(name, number, balance):
    return {'name': name, 'number': number, 'balance': balance}

def deposit(acct, amount):
    if amount <= 0:
        raise ValueError('amount must be positive')
    acct['balance'] += amount
       
def withdraw(acct, amount):
    if amount > acct['balance']:
        raise RuntimeError('balance not enough')
    acct['balance'] -= amount

def to_str(acct):
    return 'Account:' + str(acct)

print max(10, 5)
print sum(1, 2, 3, 4, 5)
print pi

acct = account('Justin', '123-4567', 1000)
deposit(acct, 500)
withdraw(acct, 200)
print to_str(acct)