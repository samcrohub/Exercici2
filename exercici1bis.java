import java.io.*;
 
 public class exercici1bis{
   public static void main(String[] args) throws IOException {
  
  float a;
  float b;
  String linia;   

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    System.out.println("Introduïu un nombre: ");
    
    linia = reader.readLine();
    a = Float.parseFloat(linia);
    
    System.out.println("Introduïu otro nombre: ");
    
    linia = reader.readLine();
    b = Float.parseFloat(linia);
    
    System.out.println("A: "+a);
    System.out.println("B: "+b);
   
    c=a+b

    System.out.println("A: "+c);
    System.out.println("B: "+b);
    
    
    }
}
