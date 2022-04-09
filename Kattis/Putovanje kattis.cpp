#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	long int c;
	cin>>n>>c;
	int t[n+1]={0};
	for(int i=0;i<n;i++){
		cin>>t[i];
	}
	long int sum=0;
	int step=0;
	for(int i=0;i<n;i++){
		int j=i+1,k=0;
		if(t[i]<=c){
			k=1;
			long int sum=t[i];
			while(sum<=c and j<n+1){
				sum+=t[j];
				j++;
				k++;	
			}
			//cout<<"i="<<i<<", k="<<k<<" old step is "<<step;
			step=(step>k-1)?step:k-1;
			//cout<<" new step is "<<step<<endl;
		}
	}
	cout<<step<<endl;
}
