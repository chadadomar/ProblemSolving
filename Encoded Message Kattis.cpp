#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	string c;
	for(int i=0;i<n;i++){
		string s="";
		cin>>c;
		int d,q;
		d=c.size();
		q=pow(d,0.5);
		for(int j=1;j<=q;j++){
			for(int i=1;i<=q;i++){
			s+=c[q*i-j];
			}
		}
		cout<<s<<endl;
		cout<<(float)5/6;
	}
}
