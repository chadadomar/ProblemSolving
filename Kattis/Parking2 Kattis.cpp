#include<bits/stdc++.h>
using namespace std;


int max(int a,int b,int c){
	int max;
	max=(a<b)?((b<c)?c:b):((a<c)?c:a);
	return max;
}

int min(int a,int b,int c){
	int min;
	min=(b<a)?((b<c)?b:c):((a<c)?a:c);
	return min;
}


int main(){
	int a,b,c,p=0;
	cin>>a>>b>>c;
	int x1,y1,x2,y2,x3,y3;
	cin>>x1>>y1>>x2>>y2>>x3>>y3;
	
	//les extremums
	int maxX,minX,maxY,minY;
	maxX=max(x1,x2,x3);
	minX=min(x1,x2,x3);
	maxY=max(y1,y2,y3);
	minY=min(y1,y2,y3);
	
	
	//valeurs intermediaires
	int Xint,Yint;
	Xint=x1+x2+x3-maxX-minX;
	Yint=y1+y2+y3-maxY-minY;
	
	
	if(maxX<=minY){
		p+=c*(minY-maxX)*3;
		p+=b*(maxX-Xint+Yint-minY)*2+a*(Xint-minX+maxY-Yint);
	}
	else{
		if(Yint<=maxX){
			if(minY<=Xint){
				p+=a*(y1+y2+y3-x1-x2-x3);
			}
			else{
				p+=a*(maxY-maxX);
				p+=b*(minY-Xint)*2+a*(Xint-minX+Yint-minY);
			}
		}
		else{
			if(minY<=Xint){
				p+=a*(minY-minX)+2*b*(Yint-maxX)+a*(maxY-Yint+maxX-Xint);
			}
			else{
				p+=a*(Xint-minX+maxY-Yint+maxX-minY)+2*b*(minY-Xint+Yint-maxX);
			}
		}
	}
	cout<<p<<endl;
	
}
