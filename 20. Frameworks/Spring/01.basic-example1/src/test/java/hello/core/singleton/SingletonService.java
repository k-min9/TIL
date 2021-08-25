package hello.core.singleton;

//싱글톤 예시(테스트는 아님)
public class SingletonService {
    //static 영역에 미리 객체를 단 하나만 생성함, 생성되면서 단 한번 생성
    private static final SingletonService instance = new SingletonService();

    //접근은 public으로 열어서 이 메서드를 통해서만 조회
    public static SingletonService getInstance(){
        return instance;
    }

    //private 생성자 선언하면서 다른곳에서 못 만드는게 보장됨
    private SingletonService(){

    }
    
    public void logic(){
        System.out.println("싱글톤 객체 호출");
    }

}
