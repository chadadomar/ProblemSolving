#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,m,k,a=0,flag=0;
	cin>>n>>m>>k;
	int t[n];
	for(int i=0;i<n;i++){
		cin>>t[i];
		if (t[i]>m) a++;
		else{
			if(t[i]==m) flag=1;
		}
	}
	if(k==0){
		if(flag && a==0) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	else{
		if(a>k) cout<<"NO"<<endl;
		else cout<<"YES"<<endl;
	}
}
