#include<bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		int N;
		cin>>N;
		int d[N];
		for(int j=0;j<N;j++){
			cin>>d[j];
		}
		for(int c=0;c<N-1;c++){
			int k=0,b=c+1;
			while(d[c]>d[b] && b<N){
				k++;
				b++;
			}
			cout<<k<<" ";	
		}
		cout<<"0"<<endl;
	}
}
