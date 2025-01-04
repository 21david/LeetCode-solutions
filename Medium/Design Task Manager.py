'''
January 4 2025 morning contest question 2.
I came close to a solution (659/662 passed).
I fixed it after seeing another solution.
'''
from heapq import heapify, heappop as pop, heappush as push
class TaskManager:
    # O(N)
    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.tasks = {}

        for user_id, task_id, priority in tasks:
            self.heap.append([-priority, -task_id, user_id])
            self.tasks[task_id] = [user_id, priority]

        heapify(self.heap)

    # O(log N)
    def add(self, userId: int, taskId: int, priority: int) -> None:
        push(self.heap, [-priority, -taskId, userId])
        self.tasks[taskId] = [userId, priority]
      
    # O(log N)
    def edit(self, task_id: int, new_priority: int) -> None:
        user_id, priority = self.tasks[task_id]
        self.add(user_id, task_id, new_priority)
        
    # O(1)
    def rmv(self, task_id: int) -> None:
        del self.tasks[task_id]

    # O(NlogN) in the worst case, but O(logN) on average due to amortization
    def execTop(self) -> int:
        while self.heap:
            priority, task_id, user_id = pop(self.heap)

            if -task_id not in self.tasks:
                # This task got deleted at some point, move on to next task
                continue
            
            curr_task_user, curr_task_pr = self.tasks[-task_id]

            if (curr_task_user, curr_task_pr) != (user_id, -priority):
                # This task was edited and these are old values, move on to next task
                continue
                
            # Remove from the map to prevent interfering with future calls
            del self.tasks[-task_id]

            # If we found correct up-to-date values for the current task, return its user
            return user_id

        # If heap is empty, there are no tasks to execute
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
