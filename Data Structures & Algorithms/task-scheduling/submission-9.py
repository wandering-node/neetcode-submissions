import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-val for _, val in counter.items()]
        heapq.heapify(heap)
        q = deque()

        time = 0
        while heap or q:
            time += 1

            # possible that when we loop through individual tasks in heap, time has already passed cooldown for many early stage tasks
            while q and q[0][0] <= time:
                _, freq = q.popleft()
                heapq.heappush(heap, freq)

            # enter the while loop give heap or q but if not heap means no available tasks enter heap now, all in cooldown, then we idle 
            if heap:
                freq = heapq.heappop(heap)
                if freq + 1 < 0:
                    q.append((time + n + 1, freq + 1))
        return time
            


