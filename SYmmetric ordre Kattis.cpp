#include <iostream>
#include <string.h>
using namespace std;


int main(){
	int a,k;
	k=1;
	while(cin>>a){
		if(a==0){
			exit(0);
		}
		cout<<"SET "<<k<<endl;
		k++;
		int i;
		string t[a];
		for(i=0;i<a;i++){
			cin>>t[i];
		}
		for(i=0;i<a;i+=2){
			cout<<t[i]<<endl;
		}
		i=int(a/2)-1;
		while(2*i+1>0){
			cout<<t[2*i+1]<<endl;
			i--;
		}
	}
}
