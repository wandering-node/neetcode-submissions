class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = {
            "+": lambda b, a: int(b) + int(a),
            "-": lambda b, a: int(b) - int(a),
            "*": lambda b, a: int(b) * int(a),
            "/": lambda b, a: int(int(b) / int(a)),
        }
        for token in tokens:
            if token in ops:
                a = nums.pop()
                b = nums.pop()
                nums.append(ops[token](b, a))
            else:
                nums.append(token)
        return int(nums.pop())
