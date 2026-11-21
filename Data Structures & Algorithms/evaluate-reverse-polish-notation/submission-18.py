class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = {
            "+": lambda n1, n2: int(n1) + int(n2),
            "-": lambda n1, n2: int(n1) - int(n2),
            "*": lambda n1, n2: int(n1) * int(n2),
            "/": lambda n1, n2: int(int(n1) / int(n2)),
        }
        for token in tokens:
            if token not in ops:
                nums.append(int(token))
            else:
                n2 = nums.pop()
                n1 = nums.pop()
                nums.append(ops[token](n1, n2))
        return nums.pop()