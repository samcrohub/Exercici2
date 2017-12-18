
import java.util.Scanner;

public class test1 {
	
	public static void main (String[] arg) {
		
		Scanner S = new Scanner(System.in);
		
		int num1, num2, suma=0;
		
		System.out.printf("Introdueix primer numero: ");
		num1 = S.nextInt();
		
		System.out.printf("Introdueix segon numero: ");
		num2 = S.nextInt();
		
		if (num2<num1) {
			System.out.printf("El segon numero no pot esser inferior al primer\n");
		} else if (num1==num2) {
			System.out.printf("%d\n",num1);
		} else {
			for (int i=num1;i<=num2; i++) {
				suma = suma + i;
			}
			
			System.out.printf("%d\n",suma);
		}
		
		
		
		
		
		
		
		
		
		
		
		
		S.close();
	}

}
