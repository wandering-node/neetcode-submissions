class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        flights = defaultdict(list)
        for src, dst in tickets:
            flights[src].append(dst)
           
        res = []
        def dfs(airport):

            while flights[airport]:
                new_dst = flights[airport].pop()
                dfs(new_dst)
            res.append(airport)
        dfs('JFK')
        return res[::-1]