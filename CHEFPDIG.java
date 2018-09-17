import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
	public static void main (String[] args) throws IOException
	{
	    Scanner sc=new Scanner(System.in);
	    int T=sc.nextInt();
	    for(int i=0;i<T;i++)
	    {
	        String n=sc.next();
	        char []ch=n.toCharArray();
	        int a[]=new int[10],c=0,ct=-1;
	        for(int j=0;j<10;j++)
            {
                for(int k=0;k<n.length();k++)
                {
                    if(j==(((int)ch[k])-48)&&(j>4||j<9))
                    {
                     c++;
                    }
                }
                a[j]=c;
                c=0;
            }
            for(int k=6;k<10;k++)
                {
                 if(a[k]!=0){
                     for(int j=0;j<10;j++)
                     {
                      if(a[j]!=0){
                          int p=k*10+j;
                        if(j==k&&a[k]>1){
                         if(p<91&&p>64)
                         {
                             System.out.print((char)p);
                             ct++;
                         }
                        }
                        else if(j!=k)
                        {
                            if(p<91&&p>64)
                            {
                                System.out.print((char)p);
                                ct++;
                            }   
                        }
                 }
                }
               }
            }
            if(ct<=-1)
            System.out.println();
            System.out.println();
	    }
	}
}
