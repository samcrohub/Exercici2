import java.io.*;
 
 public class numero11{
   public static void main(String[] args) throws IOException {

System.out.println("Introdueix un número: ");
String linia = reader.readLine();

int num = Integer.parseInt(linia);

if (num<=0){

	System.out.print("Has d'introduir un número més gran que cero");

}
else{
	for (int i=1;i<=num;i++){
		for (int j=1;j<=i;i++){
			System.out.print("*"+"\t"); 
		System.out.print("");

			}
		}
	}
  }
}
