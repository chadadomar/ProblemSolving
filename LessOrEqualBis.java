import java.util.Arrays;
import java.util.Scanner;
public class LessOrEqualBis {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		String ss[] = s.split(" ");
		int n = Integer.parseInt(ss[0]);
		int k = Integer.parseInt(ss[1]);
		
		
		String seq = sc.nextLine();
		String seqq[] = seq.split(" ");
		
		int seqqq[] = new int[seqq.length];
		int i;
		for(i=0 ; i<seqq.length ; i++)
		{
			seqqq[i] = Integer.parseInt(seqq[i]);
		}
		
		Arrays.sort(seqqq);
		
		if(seqqq[k-1] == seqqq[k]) System.out.println("-1");
		else System.out.println(seqqq[k-1]+1);

	}

}
