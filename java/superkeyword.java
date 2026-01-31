public class superkeyword{
    public static void main(String[] args) {
        class Parent{
            int x=10;
        }
        class Child extends Parent{
            int x=30;
            void display(){
                System.out.println(x);
                System.out.println(super.x);
            }
        }
        Child obj = new Child();
        obj.display();
    }
}