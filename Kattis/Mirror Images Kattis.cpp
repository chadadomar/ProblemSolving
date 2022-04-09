#include <iostream>
#include <string.h>
using namespace std;


int main(){
	int a;
	cin>>a;
	for(int i=0;i<a;i++){
		cout<<"Test "<<i+1<<endl;
		int l,c;
		cin>>l>>c;
		char T[l][c];
		for(int j=0;j<l;j++){
			for(int k=0;k<c;k++){
				cin>>T[j][k];
			}
		}
		for(int j=l-1;j>=0;j--){
			for(int k=c-1;k>=0;k--){
				cout<<T[j][k];
			}
			cout<<endl;
		}
	}
}
