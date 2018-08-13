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
        int n=Integer.parseInt(br.readLine());
        String s=(br.readLine()).replace(" " , "");
        int a=0,ct=0;char ch;
        for(int i=0;i<s.length();i++)
        {
            ch=s.charAt(i);
            if(ch=='0')
                a++; 
            else if(ch=='1' && a>0)
            ct++;
        }
        System.out.println(ct*100+a*1000+a*100);
        }
    }
}
