class Solution:

    def __init__(self, w: List[int]):
        self.solution = w
        self.total = sum(w)
        for i in range(len(self.solution)):
            calc = self.solution[i] / self.total
            self.solution[i] = calc
    def pickIndex(self) -> int:

        indices = range(len(self.solution))

        random_index = random.choices(indices, weights=self.solution, k=1)[0]

        return random_index


        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()