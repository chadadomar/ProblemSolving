#include<bits/stdc++.h>

using namespace std;


long long int gcd(long long int x1,long long int x2){
    if (x2==0)return x1;
    else return gcd(x2,x1%x2);

}

int main(){
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        long long int n;
        cin>>n;
        int l;
        cin>>l;
        vector <long long int> c;
        vector <long long int> p;
        vector <long long int> w;
        for(int j=0; j<l;j++){
            long long int e;
            cin>>e;
            c.push_back(e);
        }
        long long int u;
        u=gcd(c[0],c[1]);
        p.push_back(c[0]/u);
        p.push_back(u);
        for(int j=1;j<l;j++){
            p.push_back(c[j]/u);
            u=c[j]/u;
        }
        vector<long long int>::iterator it;
        for(int j=0;j<l+1;j++){
            it =find(w.begin(), w.end(), p[j]);
            if (it == w.end()){
                w.push_back(p[j]);
            }
        }
        sort(w.begin(),w.end());
        map<long long int, char>D;
        for(int j=0;j<26;j++){
            D[w[j]]=(char)(j+65);
        }
        cout<<"Case #"<<(i+1)<<": ";
        for(int j=0;j<l+1;j++){
            cout<<D[p[j]];
        }
        cout<<endl;
    }
}
