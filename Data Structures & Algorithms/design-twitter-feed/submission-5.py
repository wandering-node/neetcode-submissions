class Twitter:
    def __init__(self):
        self.followMap = collections.defaultdict(set)
        self.tweetMap = collections.defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set.union(self.followMap[userId], {userId})
        maxH = []
        for user in users:
            tweets = self.tweetMap[user]
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                maxH.append((-time, tweetId, user, idx))
        heapq.heapify(maxH)

        feeds = []
        while maxH and len(feeds) < 10:
            _, tweetId, user, idx = heapq.heappop(maxH)
            feeds.append(tweetId)
            if idx > 0:
                new_t, new_tweet = self.tweetMap[user][idx - 1]
                heapq.heappush(maxH, (-new_t, new_tweet, user, idx - 1))
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
