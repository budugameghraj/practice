public class constructors {
    public static void main(String[] args) {
        class A{
            A(){
                System.out.println("A constructor.");
            }
        }
        class B extends A{
            B(){
                super();
                System.out.println("B constructor");
            }
        }
        B b= new B();
    }
}
