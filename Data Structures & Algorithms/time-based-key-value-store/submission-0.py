class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.info = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.info:
            self.info[key][0].append(value)
            self.info[key][1].append(timestamp)
        else:
            self.info[key] = [[value], [timestamp]]
        # print(self.info)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.info:
            return ''
        values, timestamps = self.info[key][0], self.info[key][1]
        if timestamps[0] > timestamp:
            return ''
        elif timestamps[-1] < timestamp:
            return values[-1]

        l = 0
        r = len(timestamps) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamps[mid] == timestamp:
                return values[mid]
            elif timestamps[mid] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return values[r]
                

 