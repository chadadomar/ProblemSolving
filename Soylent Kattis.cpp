#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,c,d;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>c;
		d=(c/400==(float)c/400)? c/400:c/400+1;
		cout<<d<<endl;
	}
}
