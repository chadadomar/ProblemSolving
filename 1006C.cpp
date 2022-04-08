#include <bits/stdc++.h>
using namespace std ;

typedef long long ll;

int main(){
	ios_base::sync_with_stdio(0); cin.tie(NULL);
	freopen("1006C_in.txt","r",stdin);
	int n;
	cin>>n;
	vector<ll> d(n);
	ll som=0;
	for(int i = 0;i<n;i++){
		cin>>d[i];
		som += d[i];
	} 
	ll a=-1,b=n; // 0->a  a->b  b-> n-1  
	ll sum1=0,sum3=0;
	ll sum1_=sum1,sum3_=sum3;
	cout<<sum1<<endl;
	while ( a< b-1 ){
			cout<<sum1<<" ("<<a<<","<<b<<")" << endl;
			if ( sum1_ < sum3_){
				a++;
				sum1_+=d[a];
			}
			else{
				b--;
				sum3_+=d[b];
			}
			
			if (sum1_ == sum3_){
				sum1=sum1_;
				sum3=sum3_;
			}
	}
	cout<<sum1<<" ("<<a<<","<<b<<")" << endl;
}
