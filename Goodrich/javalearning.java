import java.util.Scanner; // loads Scanner definition for our use

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter your age in years: ");
    double age = input.nextDouble();
    System.out.print("Enter your maximum heart rate: ");
    double rate = input.nextDouble();
    double fb = (rate-age)*0.65;
    System.out.println("Your ideal fat-burning heart rate is "+fb);
    System.out.print("Enter an interger value: ");
    int timepass = input.nextInt();
    System.out.println("The integer value is: "+timepass);
  }
}
