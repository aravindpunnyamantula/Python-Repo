import java.util.Scanner;
public class Temp{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int c=sc.nextInt();
        double f=c*9;
        f=f/5;
        f=f+32;
        System.out.printf("%.2f",f);
    }
}