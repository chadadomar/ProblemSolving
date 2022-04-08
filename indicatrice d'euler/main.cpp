#include <bits/stdc++.h>

using namespace std;

int phi(long long int n){
    if(n==1) return 1;
    for(long long int d=2;d<=n;d++){
        if(n%(d*d)==0) return d*phi(n/d);
        else{
            if(n%d==0) return (d-1)*phi(n/d);
        }
    }
}



int main()
{
    long long int n;
    cin>>n;
    while(n){
        cout<<phi(n)<<endl;
        cin>>n;
    }
}
