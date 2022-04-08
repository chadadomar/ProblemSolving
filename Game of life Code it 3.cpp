#include<bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		int n;
		string s;
		cin>>n>>s;
		//string v=s;
		string u=s;
		for(int j=0;j<n;j++){
			//string u="";
			int l=0;
			while(l<u.size()){
				if(u[l]=='R'){
					u[l]="RB";
					l+=2;
				}
				else{
					u[l]="R";
					l++;
				}
			}
			//v=u;
		}
		cout<<u;
		/*int k=0,d;
		d=s.size();
		for(int j=0;j<v.size()-d+1;j++){
			if(v.substr(j,d)==s) k++;
		}
		cout<<k<<endl;*/
	}
}
