'''
union find가 나온다구...? 진짜루?
'''
def find(parent, u):
	if u == parent[u]:
		return u
	parent[u] = find(parent, parent[u])
	return parent[u]

def merge(parent, u, v):
	u = find(parent, u)
	v = find(parent, v)
	if u == v:
		return True
	parent[max(u, v)] = min(u,v)
	return False

def solution(n, connections):
	answer = 0
	parent = list(range(n+1))
	for i, connection in enumerate(connections):
		if merge(parent, connection[0], connection[1]):
			answer = i + 1
			break
	return answer
