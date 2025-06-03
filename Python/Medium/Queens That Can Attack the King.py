'''
Brute force approach.
For each queen, use it's coordinates to check if it is in line with the king. O(1) to do this.
If it is, then move the piece in the directino of the king. If it runs into another queen, then
it can't hit the king. If it hits the king, we add its original position to the answer.

TC: O(Q)
SC: O(1)
Q = number of queens.
Assuming each searching operation (moving the queen up to 8 times) is O(1) since the board is 
always size 8, and assuming an 8x8 auxiliary board is O(1) space complexity.
It puts each queen and the king on the board, then it goes through each queen and checks whether 
it can hit the king or not, so O(Q) time complexity.
'''
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # Set up the board with queens and the king
        board = [[0] * 8 for _ in range(8)]
        for qR, qC in queens:
            board[qR][qC] = 'queen'
        
        kR, kC = king
        board[kR][kC] = 'king'

        ans = []

        # For each queen, check if it can directly hit the king
        for qR, qC in queens:
            # Make copies so we can use qR and qC as moving pointers to search
            qC_copy, qR_copy = qR, qC

            # Check vertical
            if qC == kC:
                # See if any other queen is blocking the path
                if qR > kR:
                    # Queen is below, go upward
                    while qR > 0:
                        qR -= 1
                        match board[qR][qC]:
                            case 'queen':
                                break
                            case 'king':
                                ans.append([qC_copy, qR_copy])
                else:
                    # Queen is above, go down
                    while qR < 7:
                        qR += 1
                        match board[qR][qC]:
                            case 'queen':
                                break
                            case 'king':
                                ans.append([qC_copy, qR_copy])
            
            # Check horizontal
            elif qR == kR:
                # See if any other queen is blocking the path
                if qC > kC:
                    # Queen is to the right, go left
                    while qC > 0:
                        qC -= 1
                        match board[qR][qC]:
                            case 'queen':
                                break
                            case 'king':
                                ans.append([qC_copy, qR_copy])
                else:
                    # Queen is to the left, go right
                    while qC < 7:
                        qC += 1
                        match board[qR][qC]:
                            case 'queen':
                                break
                            case 'king':
                                ans.append([qC_copy, qR_copy])

            # Check diagonals
            elif abs(kC - qC) == abs(kR - qR):
                if qR < kR and qC < kC:
                    # Search down-right
                    while qR < 7 and qC < 7:
                        qR += 1
                        qC += 1
                        match board[qR][qC]:
                            case 'queen':
                                break
                            case 'king':
                                ans.append([qC_copy, qR_copy])
                
                elif qR < kR and qC > kC:
                    # Search down-left
                    while qR < 7 and qC > 0:
                        qR += 1
                        qC -= 1
                        match board[qR][qC]:
                            case 'queen':
                                break
                            case 'king':
                                ans.append([qC_copy, qR_copy])

                elif qR > kR and qC < kC:
                    # Search up-right
                    while qR > 0 and qC < 7:
                        qR -= 1
                        qC += 1
                        match board[qR][qC]:
                            case 'queen':
                                break
                            case 'king':
                                ans.append([qC_copy, qR_copy])

                else:
                    # Search up-left
                    while qR > 0 and qC > 0:
                        qR -= 1
                        qC -= 1
                        match board[qR][qC]:
                            case 'queen':
                                break
                            case 'king':
                                ans.append([qC_copy, qR_copy])

        return ans
