import java.util.Scanner;

public class manage {
    public void add(String[] list) {
        
    }
    public void del(String[] list) {
        
    }
    public void view_all(String[] list) {
        
    }
    public void replace(String[] list) {
        
    }
    public void search(String[] list) {
        
    }
    public int user_chat() {
        boolean flag = true;
        int user_input;
        System.out.println(" -----  학생 관리 프로그램 -----");
        System.out.println("1. 목록 추가");
        System.out.println("2. 목록 편집(대체)");
        System.out.println("3. 목록 삭제");
        System.out.println("4. 목록 검색");
        System.out.println("5. 목록 전체 보기");
        System.out.println("6. 프로그램 종료");

        while (flag){
            Scanner sc = new Scanner(System.in);
            System.out.println("동작할 기능에 맞는 숫자를 입력하세요 : ");
            user_input = sc.nextInt();
            if (user_input == 6) System.exit(0);
            else return user_input;

    }
    public static void main(String[] args) {
        String[] list = new String[100];
        
        int a = user_chat();

        }
    }
}
