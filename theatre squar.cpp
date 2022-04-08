#include<bits/stdc++.h>
using namespace std;

int main(){
	long int n,m,a;
	cin>>n>>m>>a;
	double c,d;
	c=(double)(n)/(double)(a);
	d=(double)(m)/(double)(a);
	if (c==n/a){
		if(d==m/a){
			cout<<(n/a)*(m/a);
		}
		else{
			cout<<(n/a)*(1+m/a);
		}
	}
	else{
		if(d==m/a){
			cout<<(1+n/a)*(m/a);
		}
		else{
			cout<<(1+n/a)*(1+m/a);
		}
	}
}
