#include<bits/stdc++.h>
using namespace std;

int Occurence(string T[],int x,string c){
	int k=0;
	for(int i=0; i<x;i++){
		if(T[i]==c){
			k++;
		}
	}
	return k;
}

int main(){
	string S;
	cin>>S;
	int l,m,p=13,k=13,h=13,t=13;
	l=S.size();
	m=l/3;
	string T[m];
	for(int i=0; i<m;i++){
		T[i]=S.substr(3*i,3);
	}
	for(int i=0; i<m;i++){
		if(Occurence(T,m,T[i])>1){
			cout<<"GRESKA"<<endl;
			exit(0);
		}
		else{
			if(T[i][0]=='P')p--;
			else if (T[i][0]=='H')h--;
			else if (T[i][0]=='K')k--;
			else t--;
		}
	}
	cout<<p<<" "<<k<<" "<<h<<" "<<t<<endl;
}
