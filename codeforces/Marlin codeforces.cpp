#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n,k;
	cin>>n>>k;
	if(k<2*(n-2))
	{
		cout<<"YES"<<endl;
		for(int i=0;i<n;i++)cout<<". ";
		cout<<endl<<". ";;
		if(k>n-2){
			for(int i=0;i<n-2;i++)cout<<"# ";
			cout<<". "<<endl<<". ";
			for(int i=0;i<k-n+2;i++)cout<<"# ";
			for(int i=0;i<2*(n-2)-k+1;i++)cout<<". ";
			cout<<endl;
			for(int i=0;i<n;i++)cout<<". ";
		}
		else{
			for(int i=0;i<k;i++)cout<<"# ";
			for(int i=0;i<n-k-1;i++)cout<<". ";
			cout<<endl;
			for(int i=0;i<n;i++)cout<<". ";
			cout<<endl;
			for(int i=0;i<n;i++)cout<<". ";
		}
		
	}
	else{
		cout<<"NO";
	}
}
