class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # Package into tuples and sort by time
        tuples = sorted([*zip(username, website, timestamp)], key = lambda x: x[-1])
        # print(tuples)
        visited = defaultdict(list)

        for name, web, time in tuples:
            visited[name].append(web)

        # print(visited)

        # For each person's ordered list of website visits
        # Do triple nested loop to get all patterns of length 3 (all ordered combinations of length 3)
        # For each of those, add to the new dictionary and increase count by 1, representing this person
        patterns = defaultdict(int)
        answers = []  # answers with same x, real answer is lexicographically smallest
        curr_max = 0

        for person, webs in visited.items():
            seen = set()
            W = len(webs)
            for i in range(W-2):
                for j in range(i+1, W-1):
                    for k in range(j+1, W):
                        pattern = (webs[i],webs[j],webs[k])
                        if pattern not in seen:
                            # If this pattern hasnt been done by this person, include this person in the count
                            patterns[pattern] += 1

                            # If a new max is hit, reset answers
                            if patterns[pattern] > curr_max:
                                curr_max = patterns[pattern]
                                answers = [pattern]
                            elif patterns[pattern] == curr_max:
                                answers.append(pattern)

                        seen.add(pattern)

        # print(dict(patterns))

        # Find lexicographically smallest tuple in answers
        smallest = answers[0]
        for i in range(1, len(answers)):
            if answers[i] < smallest:
                smallest = answers[i]

        return smallest

# Solved after seeing 3 hints
