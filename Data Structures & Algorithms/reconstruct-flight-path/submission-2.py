class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []

        def dfs(airport):
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)
            res.append(airport)

        dfs("JFK")
        return res[::-1]
