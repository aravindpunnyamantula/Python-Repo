import java.util.Scanner;

public class Water{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        int a=(x*y)/(x+y);
        System.out.printf("%d",a);
    }
}