public class AdvanceMultinheritanceDemo {
    public static void main(String[] args) {
        class Loan{
            double p = 10_000;
            double r = 8.0;
            int t = 10;
            double calculateInterest(){
                return ((p*t*r)/100);
            }
        }
        class HomeLoan extends Loan{
            double extra_r=1.5;
            double new_rate=extra_r+r;
            double calculate_new_Interest(){
                return ((p*t*new_rate)/100);
            }
        }
        
    }
}
