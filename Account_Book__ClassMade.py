from Crypto.Hash import SHA3_256, SHA3_512

class Account:
    def __init__(self, timeStamp: int, isCost: bool, moneySpent: float, implementer: str, lastAccoutId: bytes) -> None:
        self.timeStamp = timeStamp
        self.isCost = isCost
        self.moneySpent = moneySpent
        self.implementer = implementer
        self.__lastAccoutId = lastAccoutId
        self.__hashFun = SHA3_512.new()
        self.id = SHA3_256.new().update(bytes(str(self.timeStamp) + str(self.implementer), 'utf-8')).digest()

        self.__summary = 'ACCOUNT_START[' + str(timeStamp) + ', ' + str(
            int(isCost)) + ', ' + str(moneySpent) + ', ' + implementer + ', ' + lastAccoutId + ']ACCOUNT_END'

        self.__hashFun.update(bytes(self.__summary, 'utf-8'))
        self.__hash = self.__hashFun.hexdigest()

    def __call__(self) -> bytes:
        """
            return the id of this account
        """
        return self.id

    def summary(self) -> str:
        """
            return the summary of this account
        """
        return self.__summary

    def hash(self) -> str:
        """
            return the hash value of this account
        """
        return self.__hash
