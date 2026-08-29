class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.tweets.get(userId):
            self.tweets[userId] = []
        self.count -= 1
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        recent = []

        if userId not in self.followers:
            self.followers[userId] = set()
        self.followers[userId].add(userId)

        for follower in self.followers[userId]:
            if follower in self.tweets:
                index = len(self.tweets[follower]) - 1
                count, tweetId = self.tweets[follower][index]
                recent.append([count, tweetId, follower, index - 1])
        heapq.heapify(recent)
        while recent and len(res) < 10:
           count, tweetId, followerId, index = heapq.heappop(recent)
           res.append(tweetId)
           if index >= 0:
                count, tweetId = self.tweets[followerId][index]
                heapq.heappush(recent, [count, tweetId, followerId, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.followers.get(followerId):
            self.followers[followerId] = set()

        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

