#include<bits/stdc++.h>
using namespace std;

long int gcd(long int a, long int b) 
{ 
    if (a == 0) 
        return b; 
    return gcd(b % a, a); 
} 
  
 
long int findGCD(long int arr[], int n) 
{ 
    long int result = arr[0]; 
    for (int i = 1; i < n; i++) 
        result = gcd(arr[i], result); 
  
    return result; 
} 


int main(){
	int n;
	cin>>n;
	long int t[n];
	for(int i=0;i<n;i++){
		cin>>t[i];
	}
	int q,flag=1;
	q=n/2;
	long int o[q];
	for(int i=0;i<q;i++){
		o[i]=(t[i]>t[n-1-i])?t[i]-t[n-1-i]:t[n-1-i]-t[i];
		if(o[i]) flag=0;
	}
	if(flag) cout<<-1<<endl;
	else{
		cout<<findGCD(o, q)<<endl;
	}
}
