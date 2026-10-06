from collections import defaultdict



class Twitter:
    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # Include the user's own tweets as well as followed users.
        users = self.followMap[userId] | {userId}

        for uid in users:
            tweets = self.tweetMap[uid]
            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]
                heap.append((-time, tweetId, uid, index))

        heapq.heapify(heap)
        feed = []

        while heap and len(feed) < 10:
            _, tweetId, uid, index = heapq.heappop(heap)
            feed.append(tweetId)

            # Expose this author's next older tweet.
            if index > 0:
                index -= 1
                time, tweetId = self.tweetMap[uid][index]
                heapq.heappush(heap, (-time, tweetId, uid, index))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
