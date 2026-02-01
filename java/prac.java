public class prac {
    public static void main(String[] args) {
        
        class A{
            int x =10;
        }
        class B extends A{
            int x = 30;
        }
        A a=new A();
        B b=new B();
        System.out.println(b.x);
    }
}
