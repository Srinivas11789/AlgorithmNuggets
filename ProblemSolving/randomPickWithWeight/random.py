# Logic 1: create dictionaries ( be space lenient ) and calculate the probability as you pick values and asses what to send next - 22% faster
class Solution:

    def __init__(self, w: List[int]):
        self.weights = {} # to access the weights
        self.log = {} # to know what we have picked before
        self.total_sent = 0
        self.max_weight = 0
        self.high_candidate = 0
        self.n = sum(w)
        self.len = len(w)
        self.w = w
        for i in range(len(w)):
            self.weights[i] = w[i]/self.n
            if self.weights[i] > self.max_weight:
                self.max_weight = self.weights[i]
                self.high_candidate = i
            self.log[i] = 0

    def pickIndex(self) -> int:
        #print(self.total_sent, self.len//2, self.weights)
        if self.total_sent <= self.len//2:
            self.total_sent += 1 
            return self.high_candidate
        for k, v in self.log.items():
            #print(k, v, k/self.total_sent, self.weights[k])
            if v/self.total_sent <= self.weights[k]:
                self.total_sent += 1
                self.log[k] += 1
                return k
        return -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
