class ThreeStack:

    def __init__(self, cap=2):
        self.cap = cap
        arr_len = 3 * cap
        self.stacks = [None] * arr_len

        self.start = [0, arr_len//3, (2 * arr_len) // 3]
        self.end = [arr_len//3, (2 * arr_len) // 3, arr_len]


    def push(self, stack, val):
        st = self.start[stack]
        en = self.end[stack]

        if st == en:
            print("Stack is Full")
            return

        self.stacks[st] = val
        st += 1
        self.start[stack] = st


    def pop(self, stack):
        st = self.start[stack]
        en = self.end[stack]

        if en - st == self.cap:
            print("Stack is Empty")
            return

        st -= 1
        val = self.stacks[st]
        self.stacks[st] = None
        self.start[stack] = st

        return val


three_stack = ThreeStack()
three_stack.push(1, "a")
three_stack.push(1, "b")
three_stack.push(1, "c")
three_stack.push(1, "d")

val = three_stack.pop(1)
print(val)
val = three_stack.pop(1)
print(val)
val = three_stack.pop(1)
print(val)
val = three_stack.pop(1)
print(val)

val = three_stack.pop(0)
print(val)

