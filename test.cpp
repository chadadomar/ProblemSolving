#include <bits/stdc++.h>
using namespace std;


vector<string> trans(string s){
	vector<string> t;
	t.push_back("");
	int i,j=0;
	for(i=0;i<s.size();i++){
		if(s[i]==' '){
			t.push_back("");
			j++;
		}
		else{
			t[j]=t[j]+s[i];
		}
	}
	t.push_back(" ");
	return t;
}


int main(){
	freopen("Untitled1.txt","r",stdin);
	string s;
	getline(cin,s);
	vector<string> t;
	t=trans(s);
	for(int i=0;t[i]!=" ";i++){
		cout<<t[i]<<endl;
	}
}
