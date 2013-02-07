import pycon.xmath as math
import pycon.bank as bank

print math.max(10, 5)
print math.sum(1, 2, 3, 4, 5)
print math.pi

acct = bank.Account('Justin', '123-4567', 1000)
acct.deposit(500)
acct.withdraw(200)
print acct