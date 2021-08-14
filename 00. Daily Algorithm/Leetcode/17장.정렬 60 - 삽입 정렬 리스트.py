# https://leetcode.com/problems/insertion-sort-list
# 풀이 3 : 리스트 정렬 -> 함수 정렬 -> 리스트 정렬

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next
        
        # 정렬
        lst.sort()
        
        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

'''
아 삽입 정렬 아닙니다 이거
'''