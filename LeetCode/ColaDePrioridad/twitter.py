from collections import defaultdict
import heapq
from typing import List
class Twitter:

    def __init__(self):
        self.contador_tweets = 0 # va hacia valores negativos , para hacer un maxheap a la hora de hacer el getNewsFeed
        self.tweets_por_usuario = defaultdict(list)
        self.seguidos_por_usuario = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_por_usuario[userId].append((self.contador_tweets, tweetId))
        self.contador_tweets -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        self.seguidos_por_usuario[userId].add(userId)

        for seguido in self.seguidos_por_usuario[userId]:
            for numero_tweet, tweet in self.tweets_por_usuario[seguido]:
                heapq.heappush(heap, (numero_tweet, tweet))

        result = []
        while heap and len(result) < 10:
            _, tweetId = heapq.heappop(heap)
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.seguidos_por_usuario[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.seguidos_por_usuario[followerId].discard(followeeId)


obj = Twitter()
# Usuario 1 publica un tweet
obj.postTweet(1, 101)
# Debee ver su propio tweet
print(obj.getNewsFeed(1))  # [101]
# Usuario 2 publica varios tweets
obj.postTweet(2, 201)
obj.postTweet(2, 202)
obj.postTweet(2, 203)
# Usuario 1 sigue a 2
obj.follow(1, 2)
# Debe ver los tweets de 1 y de 2 ordenados por fecha
print(obj.getNewsFeed(1))
# Usuario 1 deja de seguir a 2
obj.unfollow(1, 2)
# Solo ve los suyos
print(obj.getNewsFeed(1))

#[101]
#[203, 202, 201, 101]
#[101]
