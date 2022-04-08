#include<bits/stdc++.h>
using namespace std;

int fibonacci(int n){
	if(n==1){
		return 0;
	}
	else if(n==2){
		return 1;
	}
	else{
		int a=0,b=1,c;
		for(int i=2;i<n;i++){
			c=a+b;
			a=b;
			b=c;
		}
		return c;
	}	
}

int main(){
	int n,d,e;
	cin>>n;
	if(n==1){
		cout<<"0 1"<<endl;
	}
	else{
		d=fibonacci(n);
		e=fibonacci(n-1);
		cout<<d<<' '<<d+e<<endl;
	}

}
