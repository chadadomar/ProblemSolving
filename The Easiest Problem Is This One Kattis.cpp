#include<iostream>
#include<string.h>
using namespace std;

int SumDigits(long int N){
	int i,S=0;
	while(N){
			i=N-(N/10)*10;
			N=(N-i)/10;
			S+=i;
		}
	return S;
}

int main(){
	int p,S;
	long int N;
	while(cin>>N){
		if(N==0){
			exit(0);
		}
		p=11;
		S=SumDigits(N);
		while(SumDigits(N*p)!=S){
			p++;		
		}
		cout<<p<<endl;
	}
}
