import java.util.*;
import java.io.*;

public class exercici1{
public static void main(String[] args)throws IOException{
int numero1;
String operacion;
int numero2;
int resultat;
String linia;   
BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
System.out.print("Introdueix un numero: ");
linia = reader.readLine();
numero1 = Integer.parseInt(linia);
System.out.print("Introdueix una operació: ");
operacion= reader.readLine();
System.out.print("Introdueix un altre numero: ");
linia = reader.readLine();
numero2= Integer.parseInt(linia);
resultat=0;

switch (operacion){
	case "+":
		resultat=numero1+numero2;
		break;
	case "-":
		resultat=numero1-numero2;
		break;
	case "*":
		resultat=numero1*numero2;
		break;
	case "/":
		if (numero2==0){
			System.out.println ("Infinito");
			resultat=numero1/numero2;
		}else if (numero2==0){
			System.out.println ("Infinito");
		}else {System.out.println("ERROR");} 
		
		break;

	default:
		System.out.println ("No contemplem aquesta operació");
		break;


}  System.out.println (resultat);

     }
      }
