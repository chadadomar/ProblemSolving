#include<bits/stdc++.h>
using namespace std;

int main()
{
	map<string,string> m;
	string c,s;
	cin>>c>>s;
	while(c.size()!=0){
		cin>>s;
		m[s]=c;
		cin>>c;
	}
	cin>>c;
	while(cin>>c){
		cout<<m[c]<<endl;
		cin>>c;
	}
}
