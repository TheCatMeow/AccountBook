from Crypto.Hash import SHA256


class Account:
    def __init__(self, timeStamp: int, isCost: bool, moneySpent: int | float, implementer: str) -> None:
        self.timeStamp = timeStamp
        self.isCost = isCost
        self.moneySpent = moneySpent
        self.implementer = implementer
        self.hashFun = SHA256.new()

        self.summary = 'ACCOUNT_START[' + str(timeStamp) + ', ' + str(
            int(isCost)) + ', ' + str(moneySpent) + ', ' + implementer + ']ACCOUNT_END'

        self.hashFun.update(bytes(self.summary, 'utf-8'))
        self.id = self.hashFun.hexdigest()

    def __call__(self) -> str:
        return self.summary

    def __hash__(self) -> hex:
        return hex(self.id)
