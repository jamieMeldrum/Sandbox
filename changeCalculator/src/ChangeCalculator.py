class ChangeCalculator:
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    def calculateSmallestChange(self, total):

        if (total < 0):
            raise ValueError("Total must be 0 or greater")

        if (total > 4999):
            raise ValueError("Total must not be greater than 4999")

        change = []
        while total > 0:
            for coin in self.coins:
                if total - coin >= 0:
                    total = total - coin
                    change.append(coin)
                    break

        return change