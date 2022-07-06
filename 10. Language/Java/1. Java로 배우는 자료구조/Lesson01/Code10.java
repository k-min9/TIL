/**
 * 1 ~ 100000 사이의 모든 소수들을 찾아서 출력하시오
 */
public class Code10 {
	public static void main(String[] args) {
		for (int n = 2; n < 100000; n++) {
			Boolean isPrime = true;
			for (int i = 2; i * i < n && isPrime; i++) {
				if (n % i == 0)
					isPrime = false;
			}

			if (isPrime)
				System.out.println(n);
		}

	}
}
