class Solution {
    public int findContentChildren(int[] greed, int[] size) {
        Arrays.sort(greed);
        Arrays.sort(size);

        int G = greed.length, S = size.length;

        int count = 0;
        int j = 0;

        // For each kid, find the smallest cookie that will satisfy him/her (greedy)
        for(int i = 0; i < G; i++) {
            while(j < S && size[j] < greed[i])
                j++;

            if (j >= S)
                break;  // No suitable cookie found

            count++;
            j++;  // Move to next trainer to avoid reusing him
        }

        return count;
    }
}
