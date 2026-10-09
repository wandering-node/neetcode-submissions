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

            if heap:
                freq = heapq.heappop(heap)
                if freq + 1 < 0:
                    q.append((time + n, freq + 1))

            while q and q[0][0] == time:
                # we pop tasks that are available next cycle back to heap
                _, freq = q.popleft()
                heapq.heappush(heap, freq)

        return time
