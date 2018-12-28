import java.util.Scanner;
import java.lang.Math.*;
import java.io.*;
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner sc=new Scanner (System.in);
	    long a[]=new long[2*1000001];
	    long sum[]=new long[1000001];
	    sum[0]=0;
	    sum[1]=2;
	    sum[2]=12;
	    sum[3]=36;
	    sum[4]=80;
	    sum[5]=141;
	    sum[6]=196;
	    sum[7]=249;
	    sum[8]=306;
	    sum[9]=373;
	    int s=0,p=11;
	    for(int i=0;i<=(2*1000000);i++)
	    {
	        if(i<=9)
	        {
	        if(i%2==0)
	            a[i]=i;
	        else
	            a[i]=-i;
	        }
	        else
	        {
	        a[i]=a[i/10]+a[i%10];
	        if(i>10)
	        s+=Math.abs(a[i]);
	        if(i%2==0&&i>18)
	        {
	            sum[i/2]=sum[(i/2)-1]+(2*s)-Math.abs(a[i]);
	            s-=Math.abs(a[p]);
	            p++;
	        }
	        }
	    }
	    long t=sc.nextLong(); // number of test cases
	    while(t-->0) 
	    {
	        int n=sc.nextInt();
	        System.out.println(sum[n]); // printing the answer
	    }
	}
}
