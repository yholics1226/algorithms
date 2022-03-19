# [Maximum Frequency Stack] https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > len(self.stack):
            self.stack.append([val])
        else:
            self.stack[self.freq[val]-1].append(val)

    def pop(self) -> int:
        if len(self.stack[-1]) == 1:
            val = self.stack.pop()[0]
        else:
            val = self.stack[-1].pop()
        self.freq[val] -= 1
        if self.freq[val] == 0:
            del self.freq[val]
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
