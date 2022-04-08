#include<bits/stdc++.h>
using namespace std;

int main(){
	long int n,r;
	cin>>n;
	r=n%3;
	if(r==2){
		cout<<n-3<<" 2 1";
	}
	else{
		cout<<n-2<<" 1 1";
	}
}
