#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,a,b,s;
	cin>>n>>a>>b>>s;
	if(a*(n-1)+b<=s && s<=b*(n-1)+a) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;
}
