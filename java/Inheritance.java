class A{
            int i,j;
            void showij(){
                System.out.println("i and j "+i+""+j);
            }
        }
class B extends A{
            int k;
            void showk(){
                System.out.println("k : "+ k);
            }
        }
public class Inheritance{
    public static void main(String[] args) {
        A SuperObj=new A();
        B SubObj=new B();
        SuperObj.i=90;
        SuperObj.j=70;
        SuperObj.showij();
        SubObj.i=60;
        SubObj.j=78;
        SubObj.k=40;
        SubObj.showij();
        SubObj.showk();
    }
}



