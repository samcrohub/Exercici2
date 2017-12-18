import java.io.*;
 
public class CalculaRadi{
  public static void main(String[] args) throws IOException {
  
  float a;
  float b;
  float c;    
    System.out.println("Introduïu un nombre: ");
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    String linia = reader.readLine();
    System.out.println("Introduïu un nombre: ");
         BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    String linia = reader.readLine();
    
    a = Float.parseFloat(linia);
    b = Float.parseFloat(linia);
    
    System.out.println("A: "+a);
    System.out.println("B: "+b);
   
   c= Float.parseFloat(a);
   a= Float.parseFloat(b);
   b= Float.parseFloat(c);
   
    System.out.println("A: "+c);
    System.out.println("B: "+a);
    
    
    }
}
