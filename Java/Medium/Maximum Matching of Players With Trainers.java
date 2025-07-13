class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);

        int P = players.length, T = trainers.length;

        int count = 0;
        int j = 0;

        // For each player, find the least capable trainer that can train him (greedy)
        for(int i = 0; i < P; i++) {
            while(j < T && trainers[j] < players[i])
                j++;

            if (j >= T)
                break;  // No suitable trainer found

            count++;
            j++;  // Move to next trainer to avoid reusing him
        }

        return count;
    }
}
