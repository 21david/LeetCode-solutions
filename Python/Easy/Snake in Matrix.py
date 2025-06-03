# https://leetcode.com/problems/snake-in-matrix

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r = 0
        c = 0

        for com in commands:
            match com:
                case 'UP':
                    r -=1
                case 'DOWN':
                    r += 1
                case 'RIGHT':
                    c += 1
                case 'LEFT':
                    c -= 1

        return r * n + c
