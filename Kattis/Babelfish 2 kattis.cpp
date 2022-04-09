#include<bits/stdc++.h>

using namespace std;


int main(){
	map<string,string> d;
	string line,a,b;
	while(getline(cin,line) && line != ""){
		stringstream s(line);
		s>>a;
		s>>b;
		d[b]=a;
	}
	while(cin>>b){
		a=d[b];
		cout<<(a==""? "eh":a)<<endl;
	}	

	/*a="err";
	b="rre";
	d[a]=b;
	cout<<d[a];*/
	
}
