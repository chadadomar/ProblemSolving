#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,s,d,h=0,m=0;
	cin>>n>>s;
	int T[2*n]={};
	for(int i=0;i<n;i++){
		cin>>T[2*i]>>T[2*i+1];
	}
	int i;
	if(T[0]==0 && T[1]==0){
		for(i=0;i<n-1;i++){
			d=T[2*(i+1)]*60+T[2*(i+1)+1]-T[2*i]*60-T[2*i+1];
			if(d>=2*(s+1)){
				m=(T[2*i+1]+s+1)%60;
				h=T[2*i]+(int) (T[2*i+1]+s+1)/60;
				cout<<h<<" "<<m;
				//cout<<"case 1 1";
				exit(0);
			}
		}
		if(i==n-1){
			m=(T[2*n-1]+s+1)%60;
			h=T[2*(n-1)]+(int) (T[2*(n-1)+1]+s+1)/60;
			cout<<h<<" "<<m;
			//cout<<"case 2 2";
		}
	}
	else{
		d=T[0]*60+T[1];
		if(d>s){
			cout<<"0 0";
			exit(0);
		}
		else{
			for(i=0;i<n-1;i++){
			d=T[2*(i+1)]*60+T[2*(i+1)+1]-T[2*i]*60-T[2*i+1];
			if(d>=2*(s+1)){
				m=(T[2*i+1]+s+1)%60;
				h=T[2*i]+(int) (T[2*i+1]+s+1)/60;
				cout<<h<<" "<<m;
				//cout<<"case 2 1";
				exit(0);
				}
			}
			if(i==n-1){
				m=(T[2*(n-1)+1]+s+1)%60;
				h=T[2*(n-1)]+(int) (T[2*(n-1)+1]+s+1)/60;
				cout<<h<<" "<<m<<endl;
				//cout<<T[2*(i+1)]<<" "<<T[2*(i+1)+1]<<endl;
				//cout<<"case 2 2";
			}
			
		}
		
	}
	
}
