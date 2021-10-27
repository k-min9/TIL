/**c++로 구현하는 union-find*/
#include <iostream>

using namespace std;
int n, m;
int parent[1000001];


int findParent(int a){
  if (a == parent[a]) return a;
  parent[a] = findParent(parent[a]);
  return parent[a];
}


void unionParent(int a, int b){
  a = findParent(a);
  b = findParent(b);

  if (b<a) parent[a] = b;
  else parent[b] = a;
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  // 집합 {0} ~ {n}, 쿼리 횟수 = m
  cin >> n >> m;
  for (int i = 1; i <= n; i++){
    parent[i] = i;
  }

  // 쿼리 (m 회)
  for (int i = 0; i < m; i++){
    int q, a, b;
    cin >> q >> a >> b;
    //union
    if (q == 0) unionParent(a, b);
    //find
    else{
      if (findParent(a) == findParent(b)) cout << "YES\n";
      else cout << "NO\n";
    }
  }
}