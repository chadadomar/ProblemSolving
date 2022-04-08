#include<bits/stdc++.h>
using namespace std;

int main(){
	long int n,k,a;
	cin>>n>>k;
	vector <long int> v;
	
	for(int i=0;i<n;i++){
		cin>>a;
		v.push_back(a);
	}
	sort(v.begin(),v.end());
	if(k==0){
		if(v[0]==1) cout<<"-1";
		else cout<<"1";
	} 
	else{
		a=v[k-1];
		if(k==n) cout<<a;
		else{
			if(a==v[k]) cout<<"-1";
			else cout<<a;
		}
	}
	
}
