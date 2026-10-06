class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        # Available tasks, ordered by highest remaining count.
        available = [(-count, task) for task, count in counts.items()]
        heapq.heapify(available)

        # Entries: (ready_at, remaining_count, task)
        cooldown = collections.deque()

        time = 0

        while available or cooldown:
            time += 1

            # 1. Release tasks whose cooldown has ended.
            while cooldown and cooldown[0][0] <= time:
                ready_at, remaining, task = cooldown.popleft()
                heapq.heappush(available, (-remaining, task))

            # No available task means this cycle is idle.
            if not available:
                continue

            # 2. Run the most frequent available task once.
            negative_count, task = heapq.heappop(available)
            remaining = -negative_count - 1

            # 3. Start a new cooldown if this task must run again.
            if remaining > 0:
                ready_at = time + n + 1
                cooldown.append((ready_at, remaining, task))

        return time
