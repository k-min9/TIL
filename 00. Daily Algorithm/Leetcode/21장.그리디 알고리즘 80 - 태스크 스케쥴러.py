# https://leetcode.com/problems/task-scheduler
# 풀이 X : https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation

import collections

def leastInterval(tasks, N):
        tasks_count = list(collections.Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        # 휴식시간이 발생할 경우, 멈출 수 없고, A _ _ 를 구성하는 내용물이 많지 않은 이상 이어진다.
        return max(len(tasks), (max_count-1)*(N+1)+max_count_tasks)

'''
알기 쉬운 단계별 설명
import collections 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:        
        
        # tasks = ["A","A","A","B","B","B"]
        # n = 2 
        
        counts = list(collections.Counter(tasks).values()) # [3,3]
        max_count = max(counts) # 3
        num_of_chars_with_max_count = counts.count(max_count) # 2, A and B
        
        num_of_chunks_with_idles = max_count-1 # 2  -> A  A  A

        # either a task will fill an empty place or the place stays idle, 
        # either way the chunk size stays the same  
        length_of_a_chunk_with_idle = n+1  # 3 -> A _ _ A _ _ A 

        # on the final chunk, there will only be most frequent letters 
        length_of_the_final_chunk = num_of_chars_with_max_count  # 2  

        length_of_all_chunks = (num_of_chunks_with_idles*length_of_a_chunk_with_idle) + length_of_the_final_chunk # 2*3 + 2 = 8 
        # -> A B _ A B _ A B 

        return max(len(tasks), length_of_all_chunks)
'''


print(leastInterval(["A","A","A","B","B","B","C","D","D"], 2))

# 그거랑 별개로 알고리즘 인터뷰의 우선순위 큐를 이용한 풀이도 아주 좋음
