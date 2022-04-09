#include<bits/stdc++.h>
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
	freopen("Hay Points.txt","r",stdin);
	int n,m;
	cin>>n>>m;
	vector<string> S;
	string help;
	vector<long int> y;
	for(int i=0;i<n;i++){
		cin>>help;
		S.push_back(help);
		cin>>y[i];
	}
	int k;
	string s;
	for(int i=0;i<m;i++){
		vector<string> t;
		k=0;
		cin.ignore();
		getline(cin,s);
		while(s!="."){
			t=trans(s);
			vector<string>::iterator it;
			for(int i=0;t[i]!=" ";i++){
				/*it=find(S.begin(), S.end(), t[i]);
				if(it!= S.end()){
					k+=y[it - S.begin() ];*/
				cout<<t[i]<<endl;
				}
			cin.ignore();
			getline(cin,s);
			cout<<s[1]<<endl;
		}
		//cout<<k<<endl;
	}
}
