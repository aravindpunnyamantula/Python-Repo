import java.util.Scanner;
public class HandShake{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int hs=((n-1)*n)/2;
        System.out.println(hs);
    }
}