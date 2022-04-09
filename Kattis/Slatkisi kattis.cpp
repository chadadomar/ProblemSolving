#include<bits/stdc++.h>
using namespace std;

int main(){
	long int c,h,d;
	int k;
	cin>>c>>k;
	h=pow(10,k);
	d=c-(c/h)*h;
	if(d>=(float)h/2){
		cout<<c-d+h<<endl;
	}
	else{
		cout<<c-d<<endl;
	}
}
