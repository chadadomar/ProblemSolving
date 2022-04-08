#include <iostream>
using namespace std;


int main() {
	int n;
  	cin>>n;
 	int c=1,k=0;
 	while(c<n){
      	c=c*2;
     	 k++;
  	}
 	if(c==n)cout<<n<<' '<<0;
  	else{
      	if(n%2==1)cout<<c<<' '<<k;
      	else{
      		int l=c,s=0,j=0;
      		while(s!=n){
      			j++;
      			s=s+l/2;
      			l=l/2;
			  }
			cout<<c<<' '<<j;
          
    	  }
 	 }
	return 0;
}
