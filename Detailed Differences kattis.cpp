#include <iostream>
#include <string.h>
using namespace std;


int main(){
	int a,j;
	cin>>a;
	string s,t;
	char c;
	for(int i=0;i<a;i++){
		cin>>s>>t;
		cout<<s<<endl;
		cout<<t<<endl;
		j=s.size();
		for(int i=0;i<j;i++){
			c=(s[i]==t[i])?'.':'*';
			cout<<c;
		}
		cout<<"\n"<<endl;
	
	}
}
