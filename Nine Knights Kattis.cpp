#include<bits/stdc++.h>
using namespace std;

int main(){
	int T[5][5];
	string r;
	char s;
	int k=0;
	r="valid";
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			cin>>s;
			if(s=='k'){
				T[i][j]=1;
				k++;
			}
			else{
				T[i][j]=0;
			}
			
		}
	}
	if(k!=9){
		r="invalid";
		goto stop;
	}
	if(k==9){
		for(int i=0;i<5;i++){
			for(int j=0;j<5;j++){
				if(T[i][j]){
					if(i-2>=0){
						if(j-1>=0){
							if(T[i-2][j-1]){
								r="invalid";
								//cout<<"("<<i<<" "<<j<<") ; ("<<i-2<<" "<<j-1<<")"<<endl;
								goto stop;
							}
						}
						if(j+1<5){
							if(T[i-2][j+1]){
								r="invalid";
								//cout<<"("<<i<<" "<<j<<") ; ("<<i-2<<" "<<j+1<<")"<<endl;
								goto stop;
							}	
						}
					}
					if(i+2<5){
						if(j-1>=0){
							if(T[i+2][j-1]){
								r="invalid";
								//cout<<"("<<i<<" "<<j<<") ; ("<<i+2<<" "<<j-1<<")"<<endl;
								goto stop;
							}
						}
						if(j+1<5){
							if(T[i+2][j+1]){
								r="invalid";
								//cout<<"("<<i<<" "<<j<<") ; ("<<i+2<<" "<<j+1<<")"<<endl;
								goto stop;
							}	
						}
					}
					if(i-1>=0){
						if(j-2>=0){
							if(T[i-1][j-2]){
								r="invalid";
								//cout<<"("<<i<<" "<<j<<") ; ("<<i-1<<" "<<j-2<<")"<<endl;
								break;
							}
						}
						if(j+2<5){
							if(T[i-1][j+2]){
								r="invalid";
								//cout<<"("<<i<<" "<<j<<") ; ("<<i-1<<" "<<j+2<<")"<<endl;
								goto stop;
							}	
						}
					}
					if(i+1<5){
						if(j-2>=0){
							if(T[i+1][j-2]){
								r="invalid";
								//cout<<"("<<i<<" "<<j<<") ; ("<<i+1<<" "<<j-2<<")"<<endl;
								goto stop;
							}
						}
						if(j+2<5){
							if(T[i+1][j+2]){
								r="invalid";
								//cout<<"("<<i<<" "<<j<<") ; ("<<i+1<<" "<<j+2<<")"<<endl;
								goto stop;
							}	
						}
					}
				}
			}
		}
	}
	stop:
	cout<<r<<endl;
}
