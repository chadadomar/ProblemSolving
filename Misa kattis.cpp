#include<bits/stdc++.h>
using namespace std;

int main(){
	//freopen("Untitled1.txt","r",stdin);
	int r,c;
	int l=0,L,m=0,M,k=0,temp,O=0;
	cin>>r>>c;
	string s;
	int T[r][c]={{0}};	
	int C[2*r*c];
	int K[2*r*c];
	for(int i=0;i<r;i++){
		cin>>s;
		for(int j=0;j<c;j++){
			if(s[j]=='.'){
				C[l]=i;
				C[l+1]=j;
				l+=2;
			}
			else{
				T[i][j]=1;
				K[m]=i;
				K[m+1]=j;
				m+=2;
			}
		}
	}
	/*//affichage des places vides
	cout<<endl<<"affichage des places vides"<<endl;
	for(int i=0;i<l/2;i++){
		cout<<"("<<C[2*i]<<","<<C[2*i+1]<<")  ";
	}
	//affichage des places occupées
	cout<<endl<<"affichage des places occupées"<<endl;
	for(int i=0;i<m/2;i++){
		cout<<"("<<K[2*i]<<","<<K[2*i+1]<<")  ";
	}*/

	//other people handshakes
	M=m/2;
	int v,w;
	for(int i=0;i<M;i++){
		temp=0;
		v=K[2*i];w=K[2*i+1];
		if(w>0){
			if(T[v][w-1]==1){	temp++;}
			if(v>0){	if(T[v-1][w-1]==1){	temp++;}}
			if(v<r-1){	if(T[v+1][w-1]==1){	temp++;}}
		}
		if(w<c-1){
			if(T[v][w+1]==1){	temp++;}
			if(v>0){	if(T[v-1][w+1]==1){		temp++;	}}
			if(v<r-1){	if(T[v+1][w+1]==1){		temp++;	}	}
		}
		if(v>0){		if(T[v-1][w]==1){	temp++;}	}
		if(v<r-1){	if(T[v+1][w]==1){		temp++;}	}
		O+=temp;
	}
	O=O/2;
	//cout<<"O is "<<O<<endl;
	//Mirko handshakes
	L=l/2;
	int p,q;
	for(int i=0;i<L;i++){
		temp=0;
		p=C[2*i];q=C[2*i+1];
		if(q>0){
			if(T[p][q-1]==1){	temp++;}
			if(p>0){	if(T[p-1][q-1]==1){	temp++;}}
			if(p<r-1){	if(T[p+1][q-1]==1){	temp++;}}
		}
		if(q<c-1){
			if(T[p][q+1]==1){	temp++;}
			if(p>0){	if(T[p-1][q+1]==1){		temp++;	}}
			if(p<r-1){	if(T[p+1][q+1]==1){		temp++;	}	}
		}
		if(p>0){		if(T[p-1][q]==1){	temp++;}	}
		if(p<r-1){	if(T[p+1][q]==1){		temp++;}	}
		k=(k>temp)?k:temp;
		}
	//cout<<"k is "<<k<<endl;

	cout<<k+O<<endl;
}
	
