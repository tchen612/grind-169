# https://leetcode.com/problems/implement-queue-using-stacks/
# Topic: Stack
# Difficulty: Easy

class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []
    
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def push(self, x: int) -> None:
        self.inStack.append(x)

    # Time Complexity: O(n) (Amortized is O(1), Worst-case is O(n))
    # Space Complexity: O(1)
    def pop(self) -> int:
        self.peek()
        return self.outStack.pop()

    # Time Complexity: O(n) (Amortized is O(1), Worst-case is O(n))
    # Space Complexity: O(1)
    def peek(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def empty(self) -> bool:
        return not self.inStack and not self.outStack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
