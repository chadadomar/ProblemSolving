#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	float sum=0;
	for(int i=0; i<n;i++){
		float a,b,c;
		cin>>a>>b>>c;
		float x,d,p;
		x=sqrt(0.5*(a*a+b*b-c*c*0.5));
		float a2,c2;
		a2=x;c2=c/2;
		p=(a2+b+c2)/2;
		x=(float)4/x;
		d=(x*sqrt(p*(p-a2)*(p-b)*(p-c2)));
		sum+=d;
	}
	printf("%.5f",sum);
}
