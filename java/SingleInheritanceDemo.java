public class SingleInheritanceDemo{
    public static void main(String[] args) {
        class animal{
            void eat(){
                System.out.println("Animal is eating");
            }
        }
        class dog extends animal{
            void bark(){
                System.out.println("The Dog is barking.");
            }
        }
        dog a=new dog();
        a.eat();
        a.bark();
    }
}