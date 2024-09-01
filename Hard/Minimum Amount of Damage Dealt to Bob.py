# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob
# See my solution article for an explanation:
# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/solutions/5717483/python-simple-heap-sorting-thorough-explanation-and-commented-code-beats-100/

'''
Heap solution
TC: O(NlogN)
SC: O(N)
'''
from heapq import heapify, heappop
class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)

        # Calculate in how many hits each enemy will die - O(N) time, O(N) space.
        hits_to_kill = []
        for i in range(n):
            # Divide enemy's health by Bob's power to get its number of hits before death.
            # Taking the ceiling will give us the exact number of hits to fully kill the enemy.
            num_hits = int(ceil(health[i] / power))
            hits_to_kill.append(num_hits)

        # Calculate the ratio of (damage) to (hits to kill) for each enemy and store it in this array
        # along with its damage and number of hits to kill it for later use - O(N) time, O(N) space.
        enemy_infos = []
        for i in range(n):
            # The negative sign is added to simulate a max heap in Python
            ratio = -(damage[i] / hits_to_kill[i])
            enemy_infos.append((ratio, damage[i], hits_to_kill[i]))

        heapify(enemy_infos)  # O(N) time

        # This is the damage all monsters will deal on Bob every second.
        total_enemy_damage_per_sec = sum(damage)  # O(N) time

        # Damage dealt to Bob will be stored here.
        answer = 0

        # Simulate the entire battle, calculating total damage dealt to Bob. O(N log N) time.
        while enemy_infos:
            # Grab enemy with highest ratio.
            best_enemy_to_kill = heappop(enemy_infos)  # O(log N) time

            ratio, enemy_power, hits_needed = best_enemy_to_kill

            # Calculate damage dealt to Bob by all enemies during all hits to the current enemy before it dies.
            answer += (total_enemy_damage_per_sec * hits_needed)

            # Now that this monster is dead, subtract its power from the total enemy damage being dealt per second.
            total_enemy_damage_per_sec -= enemy_power

        return answer


'''
Sorting solution. Same overall approach.
TC: O(NlogN)
SC: O(N)
'''
class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(health)

        # Calculate hits to kill
        hits_to_kill = []
        for i in range(n):
            num_hits = int(ceil(health[i] / power))
            hits_to_kill.append(num_hits)

        # Calculate ratios
        enemy_infos = []
        for i in range(n):
            ratio = (damage[i] / hits_to_kill[i])
            enemy_infos.append((ratio, damage[i], hits_to_kill[i]))

        # Sort only by ratio, descending
        enemy_infos.sort(key=lambda e: e[0], reverse=True)

        # Simulate entire battle
        total_enemy_damage_per_sec = sum(damage)
        answer = 0
        for ratio, enemy_power, hits_needed in enemy_infos:
            answer += (total_enemy_damage_per_sec * hits_needed)
            total_enemy_damage_per_sec -= enemy_power

        return answer
