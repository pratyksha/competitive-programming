/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt (br.readLine());
		while(t>0)
		{
		String s=br.readLine(), st ="";
		//System.out.println(s);
		s=s+" ";
		int flag=0;
		for(int i=0;i<s.length();i++)
		{ 
		    
		    if(s.charAt(i)!=' ')
		        st+=s.charAt(i);
		    else
		    {
		        //System.out.println(st);
		        if(st.equals("not"))
		        {
		        flag++;
		        break;
		        }
		        st="";
		    }
		}
		if(flag==0)
		System.out.println("regularly fancy");
		else
		System.out.println("Real Fancy");
		t -= 1;
		}
		
	}
}
