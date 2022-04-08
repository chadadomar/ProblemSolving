#include<bits/stdc++.h>
using namespace std;

int max(int a,int b,int c){
	int max;
	max=(a<b)?((b<c)?c:b):((a<c)?c:a);
	return max;
}

int min(int a,int b,int c){
	int min;
	min=(b<a)?((b<c)?b:c):((a<c)?a:c);
	return min;
}

int main(){
	int a,b,c,d,e,f;
	while(cin>>a>>b>>c){
		if(a==0 & b==0 & c==0){
			exit(0);
		}
		d=max(a,b,c);
		e=min(a,b,c);
		f=a+b+c-d-e;
		if(d*d==e*e+f*f){
			cout<<"right"<<endl;
		}
		else{
			cout<<"wrong"<<endl;
		}
		
	}
}
