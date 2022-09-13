import java.util.*;

class Book {
	int price;
	String title;
	
	public Book(int price, String title) {
		this.price=price;
		this.title=title;
	}
}

/**
 * DFS
 */
public class BOJ16508_Sv3_전공책 {
	static ArrayList<Book> books = new ArrayList<>();
	static String str;
	static int[] count=new int[26];
	static int[] select=new int[26];
	static int n,min=Integer.MAX_VALUE;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

    // 입력 (만들단어, 책 수, 책 이름)
		str = sc.next();
		n = sc.nextInt();
		for(int i=0 ; i<n ; i++) {
			int price = sc.nextInt();
			String title = sc.next();
			
			books.add(new Book(price,title));
		}

    // 만들고 싶은 단어의 구성된 알파벳의 배열 값을 1로 변경
		for(int i=0;i < str.length();i++){
      count[str.charAt(i)-'A']++;
    }		
		
		dfs(0, 0);

		System.out.println(min == Integer.MAX_VALUE ? -1 : min);
    sc.close();
	}
	
	static void dfs(int depth, int total) {
		if(depth==n) {
			if(check())
				min=Math.min(total, min);
			return;
		}

    // depth번 탐색
		for(int i=0;i < books.get(depth).title.length();i++)
			select[books.get(depth).title.charAt(i)-'A']++;
		dfs(depth+1,total+books.get(depth).price);
		
		// depth번 탐색 안 함
		for(int i=0;i<books.get(depth).title.length();i++)
			select[books.get(depth).title.charAt(i)-'A']--;
		dfs(depth+1,total);

	}
	
	// 만들고 싶은 단어의 모든 알파벳이 나왔는지 확인하는 함수
	static boolean check() {
		for(int i=0;i<26;i++)
			if(count[i]>select[i])
				return false;
		return true;
	}
}