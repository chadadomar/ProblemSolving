#include<bits/stdc++.h>
using namespace std;


int main(){
	int n,r,l;
	while(cin>>n){
		if(n==0)exit(0);
		else{
			int T[n];
			string s;
			for(int i=0;i<n;i++){
				cin>>T[i];
			}
			cin.ignore();
			getline(cin,s);
			l=s.size();
			r=l%n;
			if(r!=0){
				for(int i=0;i<n-r;i++)s+=" ";
				l+=n-r;
			}
			string code="";
			int q=l/n;
			for(int i=0;i<q;i++){
				for(int j=0;j<n;j++){
					code+=s[n*i+T[j]-1];
				}
			}
			cout<<"'"<<code<<"'"<<endl;
		}
	}
	
	
}
	
