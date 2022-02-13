
public class Strings {

    public static void main(String [] args) {
        
    String name= "Nasr Elzanaty Khalil";
    String myname = "NASR ELZANATY KHALIL";
    String Lname = "Omar Nasr";
    System.out.println(name.toLowerCase());
    System.out.println(name.toLowerCase());
    System.out.println(name.compareTo(Lname));
    System.out.println(name.compareToIgnoreCase(myname));
    System.out.println(name.contains("N"));
    System.out.println(name.concat(" "+ Lname));
    System.out.println(name.endsWith("l"));
    System.out.println(name.equalsIgnoreCase(myname));
    System.out.println(name.indexOf("N"));
    System.out.println(name.indexOf("l"));
    System.out.println(name.length());



}
}
