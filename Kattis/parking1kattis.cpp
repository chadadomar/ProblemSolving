#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,t,min,max;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>t;
		int T[t];
		cin>>T[0];
		min=T[0];max=T[0];
		for(int j=1;j<t;j++){
			cin>>T[i];
			if(T[i]>max){max=T[i];}
			if(T[i]<min){min=T[i];}
		}
		cout<<(max-min)*2<<endl;
	}
}
