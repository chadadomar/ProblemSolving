#include<bits/stdc++.h>
using namespace std;

int main(){
    long long int n;
    while(cin>>n){
        if(n<=1){
            cout<<1<<endl;
        }
        else{
            double m=0;
            for(int i=2;i<=n;i++){
                m+=log10(i);
            }
            cout<<int(m)+1<<endl;
        }
    }
    //cout<<log10(12);
}
