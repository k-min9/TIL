from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities)*5
        
    cnt = 0
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if cnt == cacheSize:
                cache.popleft()
                cache.append(city)
            else:
                cache.append(city)
                cnt += 1
            answer += 5          
    
    return answer