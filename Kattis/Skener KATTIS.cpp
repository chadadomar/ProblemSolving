#include <iostream>
#include <string.h>
using namespace std;


int main(){
	int r,c,z,y;
	cin>>r>>c>>z>>y;
	string s;
	for(int i=0;i<r;i++){
		cin>>s;
		for(int k=0;k<z;k++){
			for(int i=0;i<c;i++){
				for(int j=0;j<y;j++){
					cout<<s[i];
				}
			}
		cout<<endl;
		}
		
	}
}
