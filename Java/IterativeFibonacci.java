import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class IterativeFibonacci{
	static int range;
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		System.out.println("Enter range to print Fibonacci Series : ");
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		range = Integer.parseInt(reader.readLine());
		
		//Call to display FIbonacci series iteratively
		iterativeFibonacci(range);
	}
	
	public static void iterativeFibonacci(int range){		
	    int a=0,b=1,sum=0;
		System.out.print(0+" "+1);
		while((a+b)<=range){
			sum = a+b;
			a=b;
			b=sum;
			System.out.print(" "+ sum);
		}
	}
}