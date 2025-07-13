class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        count = 0
        j = 0  # pointer for trainer array
        # For each player, find the least capable trainer that can train him (greedy)
        for i in range(len(players)):
            while j < len(trainers) and trainers[j] < players[i]:
                j += 1

            if j >= len(trainers):
                break  # No suitable trainer found

            
            count += 1
            j += 1  # Move to next trainer to avoid reusing him

        return count
