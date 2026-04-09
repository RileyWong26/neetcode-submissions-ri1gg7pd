class Tweet:
        def __init__(self, id: int, time: int, user: int):
            self.id = id
            self.time = time
            self.user = user

        def __lt__(self, other):
            # Min-heap based on time
            return self.time > other.time
class Twitter:
    def __init__(self):
        # Hold the tweets,
        self.tweets = []
        self.follows = {}
        self.time = 0

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, Tweet(tweetId, self.time, userId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        st = []
        res = []
        while len(self.tweets) != 0 and len(res) < 10:
            curr = heapq.heappop(self.tweets)
            # Push own tweets
            if curr.user == userId or (userId in self.follows and curr.user in self.follows[userId]):
                res.append(curr.id)
            st.append(curr)
        
        while len(st) > 0:
            heapq.heappush(self.tweets, st.pop())
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        # add the id to follower db if not already exists
        if followerId not in self.follows:
            self.follows[followerId] = set()
        
        # add to the list of followers
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Return early if not following anyone
        if followerId not in self.follows:
            return
        
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
            
