#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	int n, m;
	cin>>n>>m;
	int a[n]={0} ;
	for (int i=0; i<m; i++)
	{
		int l,r;
		cin>>l>>r;
		for(int j=l-1; j<r; j++)
			a[j]++;				
	}	
	vector<int> v(a,a+n);
	sort(v.begin(),v.end());
	int q;
	cin>>q;
	for (int i=0; i<q; i++)
	{
	    vector<int>::iterator low,up;
		int k;
		cin>>k;
		low=lower_bound(v.begin(),v.end(),k);
		up=upper_bound(v.begin(),v.end(),k);
		cout<<(v.end()-low)<<"\n";
	}
	return(0);
}
