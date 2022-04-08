#include<bits/stdc++.h>
using namespace std;

int main(){
	int L,x,k,index=0,denieded=0;
	cin>>L>>x;
	string s;
	for(int i=0;i<x;i++){
		cin>>s>>k;
		if(s=="leave"){
			index-=k;
		}
		else{
			if(k+index>L){denieded++;}
			else {index+=k;}
		}
		
	}
	cout<<denieded<<endl;
}
