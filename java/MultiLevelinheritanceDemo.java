public class MultiLevelinheritanceDemo {
    public static void main(String[] args){
        class GrandParent{
            void house(){
                System.out.println("Grandparent has a house");
            }
        }
        class Parent extends GrandParent{
            void Business(){
                System.out.println("Parent has a business");
            }
        }
        class child extends Parent{
            void education(){
                System.out.println("Computers.");
            }
        }
        child a= new child();
        a.house();
        a.Business();
        a.education();

    }
}
