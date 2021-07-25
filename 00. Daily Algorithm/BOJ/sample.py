from bisect import bisect_left,bisect, bisect_right

list = [50, 60, 70, 80, 90, 100]

idx = bisect_left(list,80)
print('idx', idx)
idx = bisect_right(list,80)
print('idx', idx)
idx = bisect(list,80)
print('idx', idx)

list.reverse()

# 함수 개조(Desc 개조)
def my_bisect_right(a, x, lo=0, hi=None):
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x >= a[mid]: hi = mid
        else: lo = mid+1
    return len(a) - lo

idx = my_bisect_right(list,80)
print('idx', idx)
idx = my_bisect_right(list,87)
print('idx', idx)


# 함수 개조(원본)
# def my_bisect_right(a, x, lo=0, hi=None):
#     hi = len(a)
#     while lo < hi:
#         mid = (lo+hi)//2
#         if x < a[mid]: hi = mid
#         else: lo = mid+1
#     return lo