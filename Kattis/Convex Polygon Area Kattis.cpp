#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,m;
	cin>>n;
	float d;
	for(int i=0; i<n;i++){
		d=0;
		cin>>m;
		short int t[m][2];
		for(int j=0; j<m;j++){
			cin>>t[j][0];
			cin>>t[j][1];
		}
		for(int j=0; j<m-1;j++){
			d+=t[j][0]*t[j+1][1]-t[j][1]*t[j+1][0];
		}
		d+=t[m-1][0]*t[0][1]-t[m-1][1]*t[0][0];
		d=abs(d)/2;
		cout<<d<<endl;
	}
}
