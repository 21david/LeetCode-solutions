class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        wdw = defaultdict(int)
        discarded = 0
        # first w arrivals
        for i in range(w):
            curr = arrivals[i]
            
            if wdw[curr] == m:
                # already at limit, discard
                arrivals[i] = 0
                discarded += 1
                continue
                
            # not at limit, include in window
            wdw[curr] += 1

        # the rest of the arrivals
        for i in range(w, len(arrivals)):
            # remove the leftmost item from window
            leftmost_idx = i - w
            leftmost = arrivals[leftmost_idx]
            if leftmost == 0:
                # this was discarded so no action needed
                pass
            else:
                wdw[leftmost] -= 1

            # process new arrival
            curr = arrivals[i]
            if wdw[curr] == m:
                # already at limit, discard
                arrivals[i] = 0
                discarded += 1
                continue
                
            # not at limit, include in window
            wdw[curr] += 1

        return discarded
