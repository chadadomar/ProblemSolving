#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	int b[n],sum=0,k=0,i=0;
	while(sum<1 && i<n){
		if(a[i]){
			b[k]=i;
			k++;
			sum+=f(float)a[i]/pow(2,i+1);
			i++;
		}
	}
	if(i==n && sum<1)cout<<"impossible"<<endl;
	else{
		for(int j=0;j<k;j++){
			//il me fallait encore savoire le petit/grand coté de chaque paper
		}
	}
}
