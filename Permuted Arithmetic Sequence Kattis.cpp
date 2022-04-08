#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int t;
		long l;
		cin>>t;
		vector<long> T;
		for(int j=0;j<t;j++){
			cin>>l;
			T.push_back(l);	
		}
		long p;
		p=T[1]-T[0];
		int flag=1;
		for(int j=1;j<t-1;j++){
			if(T[j+1]-T[j]!=p){
				flag=0;
				break;
			}
		}
		if(flag==1){cout<<"arithmetic"<<endl;}
		else{
			sort(T.begin(),T.end()); 
			flag=1;
			p=T[1]-T[0];
			for(int j=1;j<t-1;j++){
				if(T[j+1]-T[j]!=p){
					flag=0;
					break;
				}
			}
			if(flag){cout<<"permuted arithmetic"<<endl;}
			else{cout<<"non-arithmetic"<<endl;}
		}
		
	}
}
