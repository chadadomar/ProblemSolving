#include<bits/stdc++.h>
using namespace std;

int lenth(string c){
	int m,Lenth=1,flag=1;
	m=c.size();
	for(int i=1;i<m;i++){
		for(int j=0;j<i;j++){
			if(c[j]==c[i]){
				flag=0;
				goto stop;
			}
		}
		stop:
		if(flag)Lenth++;
		flag=1;
	}
	return Lenth;
}

int main(){
	string s;
	cin>>s;
	cout<<lenth(s)<<endl;
}
