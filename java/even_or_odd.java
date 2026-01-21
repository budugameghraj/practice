import java.util.Scanner;
public class even_or_odd {
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        System.out.println("Enter a number : ");
        int num = input.nextInt();
        if(num%2==0){
            System.out.println("It is an even number.");
        }else{
            System.out.println("It is an odd number.");
        }
    }
}
