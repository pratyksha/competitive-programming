import java.util.*;
import java.lang.*;
import java.io.*;
import java.lang.Math.*;
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int t=Integer.parseInt(br.readLine()); // number of test cases 
		while(t-->0)
		{
		    String s[]=(br.readLine()).split(" ");
            int n=Integer.parseInt(s[0]);
            int m=Integer.parseInt(s[1]);
		    String a[]=new String[n];
		    String b[]=new String[n];
		    String c[]=new String[n];
		    String st="",st2="";
		    int cost1=0,cost2=0;
		    for(int i=0;i<n;i++)
		    {
		        a[i]=br.readLine();
		        for(int j=0;j<m;j++)
		        {
		            if(i%2==0)
		            {
		                if(j%2==0)
		                {
		                    st=st+'R';
		                    st2=st2+'G';
		                }
		                else
		                {
		                    st=st+'G';
		                    st2=st2+'R';
		                }
		            }
		            else
		            {
		             
		                if(j%2!=0)
		                {
		                    st=st+'R';
		                    st2=st2+'G';
		                }
		                else
		                {
		                    st=st+'G';
		                    st2=st2+'R';
		                }   
		            }
		        }
		        b[i]=st;
		        c[i]=st2;
		        st=st2="";
		    }
		    for(int i=0;i<n;i++)
		    {
		        for(int j=0;j<m;j++)
		        {
		            char ac=a[i].charAt(j);
		            char bc=b[i].charAt(j);
		            char cc=c[i].charAt(j);
		            if(ac!=bc&&ac=='G')
		                cost1+=3;
		            else if(ac!=bc&&ac=='R')
		                cost1+=5;
		            if(ac!=cc&&ac=='G')
		                cost2+=3;
		            else if(ac!=cc&&ac=='R')
		                cost2+=5;
		        }
		    }
		    System.out.println(Math.min(cost1,cost2));
		}
	}
}
