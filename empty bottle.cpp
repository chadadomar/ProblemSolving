#include<bits/stdc++.h>
using namespace std;

int main(){
	int e,f,c;
	cin>>e>>f>>c;
	int q=0,r=0,s=0,tem;
	q=(e+f)/c;
	r=e+f-q*c;
	s+=q;
	//cout<<"q "<<q<<"r "<<r<<endl;
	while(q+r>=c){
		//cout<<"dkhalna"<<endl;
		tem=q+r;
		q=tem/c;
		r=tem-q*c;
		s+=q;
		//cout<<"2q "<<q<<"r "<<r<<endl;
	}
	cout<<s<<endl;
}
