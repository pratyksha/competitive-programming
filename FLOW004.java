import java.util.*;
import java.lang.*;
import java.io.*;
class number
{
	public static void main (String[] args) throws java.lang.Exception
	{
	 BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	 int T=Integer.parseInt(br.readLine()); // number of test cases
	 for (int i=1;i<=T;i++)
	 {
 	 String num=br.readLine(); // integer n
	 int f=Character.getNumericValue(num.charAt(0)); // first digit
	 int l=Character.getNumericValue(num.charAt(num.length()-1)); // last digit
	 int sum=l+f;
	 System.out.println(sum); // output sum of last and first digit
	 }
	}
}
