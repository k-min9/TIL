/**
 * 최대공약수에서 최소공배수 나누고 그걸 곱으로 하는 짝 중에서 합이 가장 작고, 최대 공약수가 1인 것
*/
#include <iostream>
#include <stack>
 
using namespace std;

int gcd(int a, int b) {
	if (!b) return a;
	if (a > b) return gcd(b, a % b);
	return gcd(a, b % a);
}

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

	int a, b;
	int aa, bb;
  cin >> a >> b;
	b /= a;

	for(int i = 1; i * i <= b; i++)
		if (b % i == 0) {
			if (gcd(i, b / i) == 1) {
				aa = i, bb = b / i;
			}
		}

	cout << aa * a << " " << bb * a;
}