import java.util.Scanner;
public class Average{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float a=sc.nextFloat();
        float b=sc.nextFloat();
        double avg=(a+b);
        avg=avg/2;
        System.out.printf("%.4f",avg);

    }
}