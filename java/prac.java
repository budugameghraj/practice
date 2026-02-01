public class prac {
    public static void main(String[] args) {
        class A{
            int p =1000;
            int t=10;
            int r=3;
            double si{
                double x= (p*t*r)/100;
                System.out.println(x);
            }
        }
        class B extends A{
            int new_r=6;
            
        }
        A a=new A();
        B b=new B();
        System.out.println(b.x);
    }
}
