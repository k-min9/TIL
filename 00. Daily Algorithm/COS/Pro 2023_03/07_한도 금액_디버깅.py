'''
1줄 고치기
excess >= money를 excess < money로... 
'''
def solution(cards, money):
    cards.sort()
    low = 0
    mid = None
    high = cards[len(cards) - 1]
    while low <= high:
        mid = (low + high) // 2
        excess = 0  
        for k in cards:
            if k > mid:
                excess += k - mid
        if excess < money: 
            high = mid - 1
        else:
            low = mid + 1
    return (high // 100) * 100
