#include <bits/stdc++.h>

using namespace std;

int main()
{
    double p,s;
    cin>>p;
    s=(double)p*1000*5280/4854;
    cout<<fixed<<setprecision(4)<<s<<endl;
    if(s-floor(s)<=0.5)cout<<floor(s)<<endl;
    else cout<<floor(s)+1<<endl;
}
