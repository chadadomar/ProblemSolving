#include<bits/stdc++.h>
using namespace std;

int main(){
	long long  a,b,c;
	while(cin>>a>>b){
		if(a>b){
		c=a-b;
		}
		else{
			c=b-a;
		}
		cout<<c;
	}
}
