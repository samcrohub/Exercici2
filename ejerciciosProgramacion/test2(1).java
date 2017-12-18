
import java.util.Scanner;

public class test2 {
	
	public static void main (String[] arg) {
			
		Scanner S = new Scanner(System.in);
		
		int edat,any;
		String nom="";
		boolean okey=true;
		
		System.out.printf("Introdueix el nom: ");
		nom = S.nextLine();
		
		System.out.printf("Introdueix la edat: ");
		edat = S.nextInt();
		
		System.out.printf("Introdueix l'any: ");
		any = S.nextInt();
		
		
		if (nom.isEmpty()) {
			System.out.printf("No has introduit un nom!\n");
			okey=false;
		}
		
		if (edat<0 || any<0) {
			System.out.printf("Edat o any son negatius!\n");
			okey=false;
		}
		
		if (edat>=any) {
			System.out.printf("No es possible tenir mes anys que l'any actual!\n");
			okey=false;
		} 
		
		if (okey==true) {
			int j = 0;
			for (int i=any-edat;i<any;i++) {
				if (j==0) {
					System.out.printf("El %d va neixer\n",i);
				} else {
					System.out.printf("El %d tenia %d anys\n",i,j);
				}
				j++;
			}
		}
		
		System.out.printf("Adeu %s!",nom);
		
	}

}
