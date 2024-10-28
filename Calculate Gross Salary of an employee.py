import java.util.Scanner;
public class Gross{
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        float salary=sc.nextFloat();
        float hra=sc.nextFloat();
        float da=sc.nextFloat();

        float pf=(salary*12)/100;
        float Gsalary=salary+hra+da+pf;

        System.out.printf("%.2f\n",pf);
        System.out.printf("%.2f",Gsalary);



    }
}