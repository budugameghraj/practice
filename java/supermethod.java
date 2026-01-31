public class supermethod {
    public static void main(String[] args) {
        class Parent{
            void display(){
                System.out.println("parent class method");
            }
        }
        class Child extends Parent{
            void display(){
                super.display();
                System.out.println("child class method");
            }
        }
        Child obj=new Child();
        obj.display();
    }
}