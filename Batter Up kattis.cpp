#include<bits/stdc++.h>
using namespace std;

int main(){
	int a,n=0,sum=0;
	short int b;
	cin>>a;
	for(int i=0;i<a;i++){
		cin>>b;;
		if(b!=-1){
			n++;
			sum+=b;
		}
	}
	float c;
	c=(float)sum/n;
	cout<<c;
	
}
