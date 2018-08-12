import java.util.*;
import java.io.*;
class Codechef
{
    public static void main (String[] args) throws IOException
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine());
        while(t-- >0)
        {
        String s=br.readLine();
        int a=0,b=0,c=0,j=0,k=0;char ch,p;
        for(int i=0;i<s.length();i++)
        {
            ch=s.charAt(i);
            if(ch=='A'){
                k=i;
                a++; }
            else if(ch=='B')
            {
                k=i;
                b++;}
            else if(ch=='.'&&(a>0||b>0)&&j<(s.length()+1))
            {
                j=i;
                p=s.charAt(j);   
                while (p=='.'&&j<(s.length()-1))
                {
                   c++;
                   p=s.charAt(++j);
                }
                if(p=='A'&&s.charAt(k)=='A')
                    a=a+c+1;
                else if(p=='B'&&s.charAt(k)=='B')
                    b=b+c+1;     
                else if(p=='A')
                a++;
                else if(p=='B')
                b++;
               c=0;
               k=j;
               i=j;
            }
        }
        System.out.println(a+" "+b);
        }
    }
}
