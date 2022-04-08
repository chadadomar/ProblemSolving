#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c,d;
    cin>>a>>b>>c;
    d=(b-a<=c-b)?c-b-1:b-a-1;
    cout<<d<<endl;
}
