class ChangeCalculator:
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    def calculateSmallestChange(self, total):
        change = []
        while total > 0:
            for coin in self.coins:
                if total - coin >= 0:
                    total = total - coin
                    change.append(coin)
                    break

        return change