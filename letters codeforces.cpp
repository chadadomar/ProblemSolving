#include<bits/stdc++.h>
using namespace std;

int main(){
	long int n,m;
	cin>>n>>m;
	long long int  a[n+1]={},b[m]={};
	for(long int i=1;i<n+1;i++){
		cin>>a[i];
	}
	for(long  int i=0;i<m;i++){
		cin>>b[i];
	}
	long long int c=0;
	long int j=0;
	for(long  int i=0;i<m;i++){
		while(b[i]>c && j<n){
			j++;
			c+=a[j];
		}
		cout<<j<<' '<<fixed<<(long long int)b[i]+a[j]-c<<endl;
	}
}
