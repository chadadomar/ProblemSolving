#include <iostream>

using namespace std ;


int main(){
	int t ;
	cin>>t ;
	for (int u=0 ; u<t ; u++){
		int n,k;
		cin>>n>>k;
		float A[n][n];
		float s=1 ;
		for (int i=0 ; i<n ; i++){
			for (int j=0 ; j<n ; j++){
				cin>>A[i][j];
				if (i==k and j!=i){
					s*=A[i][j];
				}
			}
		}
		cout<<s;		
	}
	return 0 ;
	
	
}
