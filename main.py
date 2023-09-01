import Account_Book__ClassMade as ABCM


acc1 = ABCM.Account(1101, False, 128.66, 'Rocket')
acc2 = ABCM.Account(1101, False, 128.66, 'Rocket')
acc3 = ABCM.Account(1101, False, 128.67, 'Rocket')
print(acc1.id, '\n', hash(acc2()), '\n', acc3())
