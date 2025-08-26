class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        ans = set()

        # Put phrases into an array of first_last_array (tuple, array), where tuple stores the
        # first and last word, and array stores the array of words in the phrase
        first_last_array = []
        for phrase in phrases:
            split = phrase.split()
            first_last_tup = (split[0], split[-1])
            first_last_array.append((first_last_tup, split))

        # For every pair of two phrases, check if they match (both orders), and create a new
        # phrase and add to the final answer set if so.
        M = len(first_last_array)
        for i in range(M):
            for j in range(M):
                if i == j:
                    continue
                
                i_item = first_last_array[i]
                j_item = first_last_array[j]

                # If last word of one phrase is the first word of another phrase
                if i_item[0][-1] == j_item[0][0]:
                    # Add the final phrase to the answer
                    final_phrase_arr = i_item[1][:-1]
                    final_phrase_arr.extend(j_item[1])
                    ans.add(' '.join(final_phrase_arr))

        return sorted(list(ans))
