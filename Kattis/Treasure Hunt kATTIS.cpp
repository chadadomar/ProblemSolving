#include<bits/stdc++.h>
using namespace std;

int main(){
	int r,c,index=0;
	cin>>r>>c;
	char t[r][c];
	string s;
	for(int i=0;i<r;i++){
		cin>>s;
		for(int j=0;j<c;j++){
			t[i][j]=s[j];
		}
	}
	int i=0,j=0,k=0;
	while(t[i][j]!='T'){
		if(t[i][j]=='N'){
			i-=1;
			if(i<0){
				cout<<"Out"<<endl;
				exit(0);
			}
			k++;
		}
		else if(t[i][j]=='S'){
			i+=1;
			if(i>r-1){
				cout<<"Out"<<endl;
				exit(0);
			}
			k++;
		}
		else if(t[i][j]=='W'){
			j-=1;
			if(j<0){
				cout<<"Out"<<endl;
				exit(0);
			}
			k++;
		}
		else{
			j+=1;
			if(j>c-1){
				cout<<"Out"<<endl;
				exit(0);
			}
			k++;
		}
		if(k>r*c){
			cout<<"Lost"<<endl;
			exit(0);
		}
	}
	cout<<k<<endl;
}
