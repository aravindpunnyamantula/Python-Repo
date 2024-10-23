import java.util.Scanner;

public class SecondsToHms{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int hrs=n/3600;
        int min=(n%3600)/60;
        int sec=n%60;
        System.out.print("H:M:S-"+hrs+":"+min+":"+sec);
    }
}