'''
TC: O(N log N)
SC: only dependent on sorting algorithm, so O(N) or O(logN) I believe
'''
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        L = len(skill)
        l = L//2 - 1
        r = L//2

        team_skill = skill[l] + skill[r]
        total_chem = skill[l] * skill[r]
        l -= 1
        r += 1
        while r < L:
            if skill[l] + skill[r] != team_skill:
                return -1
            else:
                total_chem += skill[l] * skill[r]
                l -= 1
                r += 1

        return total_chem
        
'''
Test case
[8,14,5,1,7,6,9,10]
'''


'''
TC: O(N)
SC: O(N)
'''
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Find target team skill
        team_skill = sum(skill) / (len(skill) // 2)

        # If not an integer, no solution
        if team_skill % 1 != 0:
            return -1

        team_skill = int(team_skill)

        # Try to form teams using team_skill
        total_chem = 0
        seen = defaultdict(int)

        for person in skill:
            needed = team_skill - person
            if seen[needed] > 0:
                seen[needed] -= 1  # Form a team
                total_chem += person * needed
            else:
                seen[person] += 1

        if any(seen.values()):
            # At least 1 person couldn't fit into a team
            return -1
        else:
            return total_chem

        
