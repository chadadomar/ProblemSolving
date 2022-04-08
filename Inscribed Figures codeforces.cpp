#include <bits/stdc++.h>
using namespace std ;

int main(){
	int n;
	cin>>n;
	int T[n];
	for(int i=0;i<n;i++){
		cin>>T[i];
	}
	long int sum=0;
	for(int i=0;i<n-1;i++){
		if(T[i]+T[i+1]==5){
			cout<<"Infinite"<<endl;
			exit(0);
		}
		else sum+=T[i]+T[i+1];
	}
	cout<<"Finite"<<endl;
	for(int i=0;i<n-2;i++){
		if (T[i]==3 && T[i+1]==1 && T[i+2]==2) sum--;
	}
	cout<<sum<<endl;
}
