class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_heap = [(-val, key) for key, val in counter.items()]
        heapq.heapify(max_heap)
        queue = collections.deque([])
        time = 0
        while max_heap or queue:
            time += 1

            # If nothing is available, skip idle cycles.
            if not max_heap:
                time = max(time, queue[0][2])

            # Release all tasks whose cooldown has finished.
            while queue and queue[0][2] <= time:
                freq, task, _ = queue.popleft()
                heapq.heappush(max_heap, (freq, task))

            # Execute one available task.
            freq, task = heapq.heappop(max_heap)
            freq += 1

            # Every execution must start a new cooldown.
            if freq:
                queue.append((freq, task, time + n + 1))

        return time
