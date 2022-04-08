#include<bits/stdc++.h>
using namespace std;

int main(){
	int r,c;
	float d;
	cin>>r>>c;
	d=(float)(r-c)*(r-c)/(r*r);
	d=d*100;
	printf("%.8f",d);
}
