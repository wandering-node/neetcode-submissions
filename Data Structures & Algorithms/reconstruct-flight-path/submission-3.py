class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        ticket_plan = defaultdict(list)
        for src, dst in tickets:
            ticket_plan[src].append(dst)
        res = []
        
        def dfs(airport):

            while ticket_plan[airport]:
                next_airport = ticket_plan[airport].pop()
                dfs(next_airport)
            res.append(airport)
        dfs('JFK')
        return res[::-1]