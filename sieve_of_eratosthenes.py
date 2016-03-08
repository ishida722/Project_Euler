class SieveOfEratosthenes:
    def __init__(self):
        self.maxNum = 0
        self.primes = []

    def SetMaxNum(self, num):
        self.maxNum = num

    def KnockOut(self):
        filterNum = self.findList[0]
        self.primes.append(filterNum)
        for i in self.findList:
            if i % filterNum == 0:
                self.findList.remove(i)

    def GenaratePrimes(self):
        self.findList = list(range(2, self.maxNum+1))
        while (self.findList[0] * self.findList[0]) <= self.maxNum:
            self.KnockOut()
        self.primes += self.findList
        return self.primes

if __name__ == '__main__':
    prime = SieveOfEratosthenes()
    prime.SetMaxNum(200)
    print(prime.GenaratePrimes())
