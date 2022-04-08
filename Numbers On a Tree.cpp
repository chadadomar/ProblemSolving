#include<bits/stdc++.h>
using namespace std;

int main()
{
	int h;
	string s;
	cin>>h>>s;
  	int k;
	k=s.size();
	//cout<<"h "<<h<<" string "<<s<<endl;
	long int position;
	if(s[0]=='L') position=0;
	else{
		position=1;
	} 
	//cout<<"k "<<k<<endl;
	if(k>1){
		//cout<<"in the case"<<endl;
		for(int i=1;i<k;i++){
			if(s[i]=='L') position=2*position;
			else{
				position=2*position+1;
			} 
		}
	}
	//cout<<"position is "<<position<<endl;
	cout<<pow(2,h+1)-pow(2,k)-position<<endl;
	/*string content;
  	string line;
	cout << "Please introduce a text. Enter an empty line to finish:\n";
	do {
		getline(cin,line);
	    content += line + '\n';
	} while (!line.empty());
	cout << "The text you introduced was:\n" << content;*/
	
}
