#include<bits/stdc++.h>
using namespace std;

int main(){
	long int d,x;
	int n,move=0;
	cin>>n>>d;
	long int T[n];
	for(int i=0;i<n;i++){
		cin>>T[i];
	}
	for(int i=0;i<n-1;i++){
		if(T[i]>=T[i+1]){
			x=(int)((T[i]-T[i+1])/d)+1;
			T[i+1]+=d*x;
			move+=x;
		}
	}
	cout<<move<<endl;
}
