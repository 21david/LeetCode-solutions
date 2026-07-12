class Solution {
    public int secondsBetweenTimes(String startTime, String endTime) {
        String[] sStr = startTime.split(":");
        int[] s = {
            Integer.parseInt(sStr[0]), 
            Integer.parseInt(sStr[1]), 
            Integer.parseInt(sStr[2])
        };

        String[] eStr = endTime.split(":");
        int[] e = {
            Integer.parseInt(eStr[0]), 
            Integer.parseInt(eStr[1]), 
            Integer.parseInt(eStr[2])
        };

        // Difference in hours converted to seconds, plus difference in minutes converted to seconds, plus difference in seconds
        return (e[0] - s[0]) * 60 * 60 
            + (e[1] - s[1]) * 60 
            + (e[2] - s[2]);
    }
}
