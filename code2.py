import java.util.Scanner;
public class Romeo{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        int z=sc.nextInt();
        x=5*x;
        y=10*y;
        z=(x+y)/z;
        System.out.printf("%d",z);

    }
}