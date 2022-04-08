import java.util.Scanner;
public class TalyaBis {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		
		String t = sc.nextLine();
		String tt[] = t.split(" ");
		int n = Integer.parseInt(tt[0]);
		int k = Integer.parseInt(tt[1]);
		
		
		
		int i;
		for(i=0 ; i<k ; i++)
		{
			if(n%10 == 0) n=n/10;
			else n=n-1;
					
		}
		System.out.println(n);
		

	}

}
