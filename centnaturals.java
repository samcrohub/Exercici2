import java.io.*;
 
public class centnaturals{
  public static void main(String[] args) throws IOException {

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    
    //Introducció de variables
    System.out.println("Introdueix un número: ");
    String nom = reader.readLine();
    
    System.out.println("Introdueix un altre número: ");
    String linia = reader.readLine();
    
    int numeroalto = Integer.parseInt(linia);
	int numerobajo = Integer.parseInt(nom);
	
	while numeroalto<numerobajo:
	
    for (int i=numerobajo;i<=numeroalto;i++){ 
      System.out.print(i+"\t");
    }


/*
    int i = 1;
    while (i <= numero) {
      System.out.print(nom+"\t");
      i++;
    }
*/
    }
}
