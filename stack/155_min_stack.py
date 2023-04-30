"""
https://leetcode.com/problems/min-stack/description/

two stacks

else:

if element < min
push 2*element - min
min = element

pop popped_element < min
new_min 2*min - popped_element
return min

explanation on ipad

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('-inf')

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min = val
        else:
            if val > self.min:
                self.stack.append(val)
            else:
                push_val = 2 * val - self.min
                self.min = val
                self.stack.append(push_val)

    def pop(self) -> None:
        element = self.stack.pop()
        if element < self.min:
            a = self.min
            self.min = 2 * self.min - element
            return a

        return element

    def top(self) -> int:
        element = self.stack[-1]
        if element < self.min:
            return self.min

        return element

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()