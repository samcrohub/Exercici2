import java.io.*;
 
 public class exercici2bis{
   public static void main(String[] args) throws IOException {
  
  
  
  double a;
  double b;
  double c;
  double d;
  
   String linia;   

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    System.out.print("Segundos: ");
    
    linia = reader.readLine();
    a = Integer.parseInt(linia);
   
               
             
   b= (a/3600.0);
   c=(a-(b*3600.0))/60.0; 
   d=a-((b*3600.0)+(c*60.0));
       b=(float(a/3600))
c=float((a-(b*3600))/60)
d=a-((b*3600)+(c*60))  
    
      
    //System.out.println("HORA:"+Math.round(b)+" MINUTOS:"+Math.round(c,1)+" SEGUNDOS"+Math.round(d));
System.out.println("HORA:"+b+" MINUTOS:"+c+" SEGUNDOS"+d);

    
    
    }

}
