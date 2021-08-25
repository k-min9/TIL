
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = N*(N-1)*(N-2)//6 - 