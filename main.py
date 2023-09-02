import Account_Book__ClassMade as ABCM


acc = ABCM.Account(1001, False, 62.79, "Rocket")

print(acc(), acc.summary(), acc.hash)
acc.__summary()