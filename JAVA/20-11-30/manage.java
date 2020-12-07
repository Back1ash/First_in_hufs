import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import sun.security.util.Length;

public class manage {
    public static void add(List list) {
        list.add(input_S());
    }

    public static void del(List list) {

    }

    public static void view_all(List list) {
        len(list);
    }

    public static void replace(List list) {

    }

    public static void search(List list) {

    }
    public static String input_S(){
        Scanner sc = new Scanner(System.in);
        String qwe = sc.nextLine();
        sc.close();
        return qwe;
    }

    public static int input_I(){
        Scanner sc = new Scanner(System.in);
        int qwe = sc.nextInt();
        sc.close();
        return qwe;
    }

    public static int user_chat() {
        boolean flag = true;
        int user_input = 0;
        Scanner sc = new Scanner(System.in);

        System.out.println(" -----  학생 관리 프로그램 -----");
        System.out.println("1. 목록 추가");
        System.out.println("2. 목록 편집(대체)");
        System.out.println("3. 목록 삭제");
        System.out.println("4. 목록 검색");
        System.out.println("5. 목록 전체 보기");
        System.out.println("6. 프로그램 종료");

        while (flag) {
            System.out.print("동작할 기능에 맞는 숫자를 입력하세요 : ");
            user_input = sc.nextInt();
            if (user_input == 1 | user_input == 2 | user_input == 3 | user_input == 4 | user_input == 5
                    | user_input == 6)
                break;
            else
                continue;
        }
        sc.close();
        return user_input;

    }

    public static void main(List args) {
        List list = new ArrayList();
        int a;

        while (true) {
            a = user_chat();
            switch (a) {
                case 1:
                    add(list);
                    break;

                case 2:
                    replace(list);
                    break;

                case 3:
                    del(list);
                    break;

                case 4:
                    search(list);
                    break;

                case 5:
                    view_all(list);
                    break;

                case 6:
                    System.exit(0);
                    break;

            default:
                break;
        }
    }
}}
