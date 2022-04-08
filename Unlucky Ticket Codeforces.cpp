#include <iostream>
#include <string.h>
using namespace std;


int main(){
	int n,i;
	cin>>n;
	string s;
	cin>>s;
	if(s[0]<s[2*n-1]){
		for(i=1;i<n;i++){
			if(s[i]>=s[2*n-(i+1)]){
				cout<<"NO"<<endl;
				break;
			}
		}
		if(i==n){cout<<"YES"<<endl;}
		
	}
	else if(s[0]>s[2*n-1]){
		for(i=1;i<n;i++){
			if(s[i]<=s[2*n-(i+1)]){
				cout<<"NO"<<endl;
				break;
			}
		}
		if(i==n){cout<<"YES"<<endl;}
	}
	else{
		cout<<"NO"<<endl;
	}
}
