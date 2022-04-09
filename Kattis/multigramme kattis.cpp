#include<bits/stdc++.h>
using namespace std;

long int gcd(long int x1,long int x2){
	if(x2!=0){
		return gcd(x2,x1%x2);
	}
	else{
		return x1;
	}
	
}


int main(){
	string s;
	cin>>s;
	long int l,q;
	l=s.size();
	string n="";
	int flag;
	for(int i=0;i<l;i++){
		flag=1;
		for(int j=0;j<n.size();j++){
			if(s[i]==n[j]){
				flag=0;
				break;
			}
		}
		if(flag)n+=s[i];
	}
	q=n.size();
	long int t[q]={0};
	for(int i=0;i<q;i++){
		for(int j=0;j<l;j++){
			if(n[i]==s[j]){
				t[i]++;
			}
		}
	}
	long int g;
	g=t[0];
	for(int i=1;i<q;i++){
		g=gcd(t[i],g);
	}
	cout<<"gcd is "<<g<<endl;
	if(g==1){
		cout<<"-1"<<endl;
	}
	else{
		long int tst;
		for(tst=g;tst>1;tst--){
			if(l%tst==0){
				cout<<"test "<<tst<<endl;
				string b,c="";
				b=s.substr(0,l/tst);
				cout<<b<<endl;
				for(int i=0;i<tst;i++){
					c+=b;
				}
				cout<<"c is: "<<c<<endl;
				if(c==s){
					cout<<b<<endl;
					break;
				}
			}
		}
	}
}
