# https://leetcode.com/problems/top-k-frequent-elements
# 풀이 1: counter를 이용한 음수 순 추출

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    
    # 힙에 음수 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
        
    # 여기서 most_common 쓰면 필요없지 않나
    answer = list()
    
    for _ in range(k):
        answer.append(heapq.heappop(freqs_heap)[1])
        
    return answer