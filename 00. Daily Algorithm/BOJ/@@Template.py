# 기본 전처리
import sys
input = sys.stdin.readline


# 시간 재기 (간략)
import time
t0 = time.time()
print("시간:", time.time()-t0)

# 시간 재기 (정확)
import timeit
t0 = timeit.default_timer()
print("시간:", timeit.default_timer()-t0)