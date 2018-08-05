import java.util.*;
import java.lang.*;
import java.io.*;
class number
{
	public static void main (String[] args) throws java.lang.Exception
	{
	 BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	 int T=Integer.parseInt(br.readLine());
	 for (int i=1;i<=T;i++)
	 {
 	 String num=br.readLine();
	 int f=Character.getNumericValue(num.charAt(0));
	 int l=Character.getNumericValue(num.charAt(num.length()-1));
	 int sum=l+f;
	 System.out.println(sum);
	 }
	}
}