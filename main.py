class TinkerTailor:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.tinker = []
        for x in range(1, self.n + 1):
            self.tinker.append(x)

    def tinker_main(self):
        k = self.k - 1
        count = k

        if self.k > self.n:
            print('Please add less than', self.n, 'syllables and restart!')
        else:
            print('The players: ', self.tinker)

            while len(self.tinker) > 1:
                self.tinker.pop(count)
                count = (count + k) % len(self.tinker)
            print('No. ', self.tinker[0], ' have won!')

if __name__ == '__main__':
    tinker_test = TinkerTailor(5, 3)
    tinker_test.tinker_main()