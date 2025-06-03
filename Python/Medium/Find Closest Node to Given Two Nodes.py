class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        set1 = set()
        set2 = set()

        q1 = deque([node1])
        q2 = deque([node2])

        n1_found = n2_found = False
        looped1 = looped2 = False

        while (q1 or q2) and not (looped1 and looped2):
            if q1 and not looped1:
                n1 = q1.popleft()
                if n1 != -1:
                    if (n1 in set2) or n1 == node2: n1_found = True
                    if (n1 in set1): looped1 = True
                    set1.add(n1)
                    if edges[n1] != -1: 
                        q1.append(edges[n1])
                    else:
                        looped1 = True

            if q2 and not looped2:
                n2 = q2.popleft()
                if n2 != -1:
                    if (n2 in set1) or n2 == node1: n2_found = True
                    if (n2 in set2): looped2 = True
                    set2.add(n2)
                    if edges[n2] != -1: 
                        q2.append(edges[n2])
                    else:
                        looped2 = True

            if n1_found and n2_found:
                return min(n1, n2)
            elif n1_found:
                return n1
            elif n2_found:
                return n2

        return -1

# Not my best algorithm nor problem-solving approach. Currently tired from a flipped sleep schedule - May 31 2025.
'''
Test cases:
[2,2,3,-1]
0
1
[1,2,-1]
0
2
[2,0,0]
2
0
[4,3,0,5,3,-1]
4
0
[5,4,5,4,3,6,-1]
0
1
[4,4,8,-1,9,8,4,4,1,1]
5
6
[51,-1,75,17,71,-1,52,15,58,44,16,22,47,4,60,71,32,10,84,-1,51,51,17,-1,15,51,32,53,83,83,47,-1,67,-1,47,6,46,77,9,-1,-1,61,11,54,6,15,7,37,8,0,9,81,30,49,38,-1,-1,22,68,48,-1,80,36,36,-1,22,52,48,82,27,68,10,56,84,32,49,75,57,77,50,36,9,61,0,49,0,16]
27
22
[-1,7,15,15,-1,4,16,2,16,7,11,6,10,4,9,1,14,-1]
1
6
'''
