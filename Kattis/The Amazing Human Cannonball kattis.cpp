#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;


int main(){
    int n;
    cin>>n;
    int i;
    for(i=0;i<n;i++){
    	float v,o,x,h1,h2;
    	cin>>v>>o>>x>>h1>>h2;
    	float y,c;
    	c=cos(M_PI*o/180);
    	y=(x/c)*(sin(M_PI*o/180)-4.905*(x/(v*v*c)));
    	if(h1+1<y && y<h2-1){
    		cout<<"Safe"<<endl;
		}
		else{
			cout<<"Not Safe"<<endl;
		}
	}
}
