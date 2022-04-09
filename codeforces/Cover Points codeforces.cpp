#include<bits/stdc++.h>
using namespace std;

int main(){
	long int a,x,y,s=0;
	cin>>a;
	for(int i=0;i<a;i++){
		cin>>x>>y;
		s=(s>(x+y))?s:(x+y);
	}
	cout<<s;
}
