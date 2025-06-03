'''
After seeing hints 2-3 and skimming editorial
TC: O(N)
SC: O(1)
'''
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1: return False

        # Pass to check that all locked )s can be matched
        asterisks = opens = 0
        for char, lock in zip(s, locked):
            if lock == '0':
                asterisks += 1

            elif lock == '1':
                if char == ')':
                    if opens > 0:
                        opens -= 1
                    elif asterisks > 0:
                        asterisks -= 1
                    else:
                        # ')' that can't be matched with anything
                        return False

                elif char == '(':
                    opens += 1

        # Pass to check if all locked (s can be matched
        asterisks = opens = 0
        for char, lock in zip(s, locked):
            if lock == '0':
                if opens:
                    opens -= 1

            elif lock == '1':
                if char == ')':
                    if opens:
                        opens -= 1
                    elif asterisks:
                        asterisks -= 1

                elif char == '(':
                    opens += 1

        if opens:
            # Leftover locked (s that couldn't be closed by anything
            return False

        return asterisks % 2 == 0


'''
Test cases. *s represent unlocked characters:

(*)()*)(***)***(**(*)(******((**)*)**(*)
1011101100010001001011000000110010100101

*)*)**

*()*

*(*(**)*)*
((((()))))

()()(())

* ( * ) * ( * ( * ) * * * )
( ( ) ) ( ( ) ( ) ) ( ( ) )

* ( * ) * ( * ( ) * * )
( ( ) ) ( ( ( ( ) ) ) )

* ( * ) * ( * ( ) * ) *
( ( ) ) ( ( ( ( ) ) ) )

* ( * * ) ( * * ) *
( ( ( ) ) ( ( ) ) )

* * * * * )
( ( ( ) ) )

* ( * * * )

* * * * ( (

* * ( ( * ( ( * * ) ) * *
'''
