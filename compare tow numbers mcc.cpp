#include<bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
		long long int a,b,c,d;
		cin>>a>>b>>c>>d;
		long double s,u;
		s=(double)a/b+(double)c/d;
		u=(double)a*c/(b*d);
		//cout<<s<<" "<<u<<endl;
		if(s<u) cout<<"<"<<endl;
		else{
			if(s>u) cout<<">"<<endl;
			else cout<<"="<<endl;
		}
	}
}
