
    import java.util.Scanner;

class DispalyTime {
  public static void main(String[] args) {
    //System.out.println("Hello world!");
    Scanner input = new Scanner(System.in);
    //prompt the user for the input
    System.out.println("Enter an integer for the seconds");
    int seconds = input.nextInt();
    int minutes =seconds/60;
    int remainingSeconds = seconds%60;
    System.out.println(seconds+ " seconds is " + minutes + "minutes and " + remainingSeconds+ "seconds");

  }
}
