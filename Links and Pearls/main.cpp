#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin>>s;
    int a,b=0,c;
    a=s.size();
    for(int i=0;i<a;i++){
        if(s[i]=='o')b++;
    }
    if(b==0)cout<<"YES";
    else{
        c=a-b;
        if(c%b==0)cout<<"YES";
        else cout<<"NO";
    }

}
