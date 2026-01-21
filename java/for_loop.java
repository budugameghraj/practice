import java.util.Scanner;
public class for_loop{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int num = input.nextInt();
        int i;
        for(i=1;i<=num;i++){
            System.out.println(i);
        }
    }
}