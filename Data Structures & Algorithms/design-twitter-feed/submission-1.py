class Twitter:

    def __init__(self):
        self.tweetMap = {} #userId: (count, tweetId)
        self.followMap = {} #userId: set() - followerId
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = [(self.count, tweetId)]
        else:
            self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []

        if userId in self.tweetMap:
            for tweet in self.tweetMap[userId]:
                heapq.heappush_max(maxHeap, tweet)
        
        if userId in self.followMap:
            for followee in self.followMap[userId]: #gives set
                # CRITICAL: Don't add own tweets again if following self
                if followee == userId:
                    continue

                for tweet in self.tweetMap[followee]:
                    heapq.heappush_max(maxHeap, tweet)
        
        while maxHeap and len(res) < 10:
            count, tweet = heapq.heappop_max(maxHeap)
            res.append(tweet)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set([followeeId])
        else:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            # if followeeId in set
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)
        
