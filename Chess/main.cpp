#include <bits/stdc++.h>

using namespace std;

struct point{
    int x;
    int y;
};

bool check(int x,int y){
    return (0<x<9 && 0<y<9 );
}


int main()
{
    int n;
    cin>>n;
    for(int h=0;h<n;h++){
        char a,b;
        int x,y,u,v;
        cin>>a>>y>>b>>v;
        x=a-'A'+1;
        u=b-'A'+1;

        //identical points
        if(x==u && y==v){
            cout<<"0 "<<a<<" "<<y<<endl;
            continue;
        }
        point p1={x,y};
        point p2={u,v};

        //moves vector of p1
        vector<point> v1;

        //moves vector of p1
        vector<point> v2;


        for(int i=0;i<9;i++){
                if (check(p1.x+i,p1.y+i)) v1.push_back({p1.x+i,p1.y+i});
                if (check(p1.x+i,p1.y-i)) v1.push_back({p1.x+i,p1.y-i});
                if (check(p1.x-i,p1.y+i)) v1.push_back({p1.x-i,p1.y+i});
                if (check(p1.x-i,p1.y-i)) v1.push_back({p1.x-i,p1.y-i});
        }
        bool finish= false;
        for(int i=0;i<v1.size();i++){
            if(v1[i].x==p2.x && v1[i].y==p2.y){
                cout<<"1 "<<a<<" "<<y<<" "<<b<<" "<<v<<endl;
                finish= true;
            }
        }
        if(finish) continue;

        for(int i=1;i<9;i++){
                if (check(p2.x+i,p1.y+i)) v2.push_back({p2.x+i,p2.y+i});
                if (check(p2.x+i,p1.y-i)) v2.push_back({p2.x+i,p2.y-i});
                if (check(p2.x-i,p1.y+i)) v2.push_back({p2.x-i,p2.y+i});
                if (check(p2.x-i,p1.y-i)) v2.push_back({p2.x-i,p2.y-i});
        }
        int intersect=-1;
        for(int i=0;i<v1.size();i++){
            for(int j=0;j<v2.size();j++){
                if(v1[i].x==v2[j].x && v1[i].y==v2[j].y){
                    intersect=j;
                }
            }
        }

        if(intersect==-1){
            cout<<"Impossible"<<endl;
            continue;
        }
        char e;
        e=(char) v2[intersect].x-1+'A';
        cout<<"2 "<<a<<" "<<y<<" "<<e<<" "<<v2[intersect].y<<" "<<b<<" "<<v<<endl;
    }
}
