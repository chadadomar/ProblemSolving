#include <iostream>
using namespace std;


int main(){
	int a,k,i;
	while(cin>>a){
		if(a==-1){
			exit(0);
		}
		int s,t,j;
		cin>>s>>t;
		j=t;
		k=s*t;
		for(i=1;i<a;i++){
			cin>>s>>t;
			k+=s*(t-j);
			j=t;
		}
		cout<<k<<" miles"<<endl;
		
	}
}
