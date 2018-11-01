import java.util.*;
import java.io.*;
class Codechef
{
    public static void main (String[] args) throws IOException
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine()); // t = number of test cases
        while(t-- >0)
        {
        int n=Integer.parseInt(br.readLine()); // n = number of months
        String s=(br.readLine()).replace(" " , ""); // chef paid 1000rs maintenance fees or not
        int a=0,ct=0;char ch;
        for(int i=0;i<s.length();i++)
        {
            ch=s.charAt(i);
            if(ch=='0') // fees not paid
                a++; // counter for fees not paid
            else if(ch=='1' && a>0) // fees paid
                ct++; // counter for fees paid
        }
        System.out.println(ct*100+a*1000+a*100); // total amount that has to be paid including fine
        }
    }
}
