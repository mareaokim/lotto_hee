import java.io.*;

public class basic_logicaloperator {

    public static void main(String[] args)throws IOException{

        System.out.println("당신은 여성입니까?");
        System.out.println("Y 또는 N 을 입력하십시오.");

    BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));

    String str = br.readLine();
    char res = str.charAt(0);


    if(res == 'Y' || res == 'y') {

        System.out.println("당신은 상여자군요!");


    }else if (res == 'N' || res == 'n') {

        System.out.println("자댕이로군 재기해라");
    }
    else {
        System.out.println("Y 또는 N 을 입력하시오.");

    }

    }

}
