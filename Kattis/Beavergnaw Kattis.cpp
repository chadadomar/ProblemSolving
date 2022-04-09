#include<bits/stdc++.h>
using namespace std;


int main(){
	long int D,V;
	cin>>D>>V;
	while(D!=0 && V!=0){
		printf("%.7f",pow(D*D*D-6*V/M_PI,(float)1/3));
		cout<<endl;
		cin>>D>>V;
	}
}
