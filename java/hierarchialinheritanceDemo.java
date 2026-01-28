public class hierarchialinheritanceDemo {
    public static void main(String[] args){
        class course{
            void coursedetails(){
                System.out.println("Java");
            }
            void coursetimeline(){
                System.out.println("3 months");
            }
            }
        class student1 extends course{
            void stu_name(){
                System.out.println("Ram");
            }
            void stu_id(){
                System.out.println("1");
            }
        }
        class student2 extends course{
            void stu_name(){
                System.out.println("Mohith");
            }
            void stu_id(){
                System.out.println("2");
            }
        }
        class student3 extends course{
            void stu_name(){
                System.out.println("Karan");
            }
            void stu_id(){
                System.out.println("2");
            }
    }
    student1 a = new student1();
    student2 b = new student2();
    student3 c = new student3();
    a.stu_name();
    a.stu_id();
    a.coursedetails();
    b.stu_id();
    b.coursetimeline();
    c.stu_name();
    c.coursedetails();
    }
}

