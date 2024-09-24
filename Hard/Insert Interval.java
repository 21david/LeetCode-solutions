// https://leetcode.com/problems/insert-interval/
// 4-3-2020

class Solution {
	public int[][] insert(int[][] intervals, int[] newInterval) {
		boolean[] overlaps = new boolean[intervals.length];
		boolean overlapped = false;

		// iterate through set of intervals, set corresponding element in boolean array to TRUE if elements overlap, FALSE if it doesn't
		for (int i = 0; i < intervals.length; i++)
		{
			if (newInterval[0] <= intervals[i][1] && newInterval[0] >= intervals[i][0]) // new interval starts somewhere in between current interval's range
			{
				overlaps[i] = true;
				overlapped = true;
			}
			else if (intervals[i][0] >= newInterval[0] && intervals[i][0] <= newInterval[1]) // current interval starts somewhere in between new interval's range
			{
				overlaps[i] = true;
				overlapped = true;
			}
		}
        
		ArrayList<int[]> newSet = new ArrayList<>();

		// if it never overlapped with anything
		if (overlapped == false)
		{
			int temp = intervals.length;

			for (int i = 0; i < intervals.length; i++)
			{
				if (intervals[i][0] > newInterval[0]) // break once it finds spot newInterval needs to be in
				{
					temp = i;
					break;
				}

				newSet.add(intervals[i]);
			}

			newSet.add(newInterval);

			for (int i = temp; i < intervals.length; i++)
			{
				newSet.add(intervals[i]);
			}

			return convert(newSet);
		}
        
		// iterate through boolean array
		int min = 0, max = 0;

		for (int i = 0; i < overlaps.length; i++)
		{
			if (!overlaps[i])
			{
				newSet.add(intervals[i]); // just add the interval unchanged
			}

			if (overlaps[i])
			{
				min = Math.min(intervals[i][0], newInterval[0]);
				max = 0;

				while (i < intervals.length - 1 && overlaps[i + 1])
					i++;

				max = Math.max(intervals[i][1], newInterval[1]);
				newSet.add(new int[] { min, max });
			}

		}

		return convert(newSet);
	}

	public int[][] convert(ArrayList<int[]> arrayList)
	{
		int[][] array = new int[arrayList.size()][];

		for (int i = 0; i < arrayList.size(); i++)
		{
			array[i] = arrayList.get(i);
		}

		return array;
	}
}
