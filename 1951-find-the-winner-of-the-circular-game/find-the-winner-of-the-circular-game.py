class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = deque()
        for i in range(1, n+1):
            friends.append(i)

        while len(friends) > 1:
            for i in range(k-1):
                friends.append(friends.popleft())
            friends.popleft()

        return friends[0]
            

        