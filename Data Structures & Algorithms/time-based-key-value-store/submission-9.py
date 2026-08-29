class TimeMap:

    def __init__(self):
        self.info = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.info:
            self.info[key][0].append(timestamp)
            self.info[key][1].append(value)
        else:
            self.info[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.info or self.info[key][0][0] > timestamp:
            return ""

        if timestamp >= self.info[key][0][-1]:
            return self.info[key][1][-1]
        
        l = 0
        r = len(self.info[key][0]) - 1
        res = ''
        while l <= r:
            mid = (l + r) // 2
            if  self.info[key][0][mid] > timestamp:
                r = mid - 1
            else:
                res = self.info[key][1][mid]
                l = mid + 1
        return res
            
