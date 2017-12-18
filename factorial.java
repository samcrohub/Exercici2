import java.util.*;
import java.io.*;
 /*yyyyyyyy*/
public class factorial{
public static void main(String[] args)throws IOException{
int numero1;
String operacion;
int numero2;
int resultat;
String fin;
String linia;   
BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
fin="si";
while (fin.equals("si")){
System.out.print("Introdueix un numero: ");
linia = reader.readLine();
numero1 = Integer.parseInt(linia);
System.out.print("Introdueix una operació: ");
operacion= reader.readLine();
System.out.print("Introdueix un altre numero: ");
linia = reader.readLine();
numero2= Integer.parseInt(linia);
resultat=0;

	if (operacion.equals("+")) {
		resultat=numero1+numero2;
		System.out.print("resultat");
	}
	else if (operacion.equals("-")) {
		resultat=numero1-numero2;
	}
	else if (operacion.equals("*")) {
		resultat=numero1*numero2;
	}	  
	else if (operacion.equals("/")) {
		if (numero2==0){
	System.out.println ("Infinito");
	resultat=numero1/numero2;
	}}
	else if (numero2==0){
	System.out.println ("Infinito");
	}
	else {System.out.println("ERROR");} 
	System.out.println (resultat);
	System.out.print("Vols realitzar més càlculs? ");
	fin= reader.readLine();
}
	System.out.print("Adeu");
	
	 }
      }
   
