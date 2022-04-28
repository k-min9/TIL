import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * BOJ1300_Gd2_K번째수
 * 파라메트릭 문제네 이거
 */
public class BOJ1300_Gd2_K번째수 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());
		
		long lo = 1;
		long hi = K;
		
		while(lo < hi) {

			long mid = (lo + hi) / 2;	// 임의의 x(mid)를 중간 값으로 잡는다.
			long count = 0;
			
      // 식이 단순하니 별도 함수 분리 없음!
			for(int i = 1; i <= N; i++) {
				count += Math.min(mid / i, N);
			}
			
			if(K <= count) {
				hi = mid;
			}
			else {
				lo = mid + 1;
			}
		}
		
		System.out.println(lo);
	}
}
