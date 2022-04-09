#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,k,s,r,u;
	cin>>n>>k;
	r=k;
	int i;
	for(i=0;i<k;i++){
		cin>>s;
		if(s==0){
			 r=i;
			 break;
		}
	}
	while(i<n && s!=0){
		cin>>u;
		if(u==s) r++;
		else break;
		i++;
	}
	cout<<r;
}
