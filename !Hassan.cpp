#include <bits/stdc++.h>

using namespace std ;

typedef long long ll;

int main(){
	freopen("!Hassan.txt","r",stdin);
	
	ll x,y,n;
	scanf("%lld %lld %lld",&n,&x,&y);
	
	ll l,r,duration,computers;
	cout<<x<<" "<<y<<" "<<n<<" "<<endl;
	cout<<endl<<endl;
	
	l=n*x*y/(x+y); // left value
	r=min(x,y)*n ; // right value that assure the n computers will be fixed
	cout<<r<<endl;
	ll ans=r;
	printf("%lld\n",ans);
	while(l<r){
		duration = (r+l)/2 ;
		computers = duration / x + duration /y ;
		printf("%lld ",duration);
		
		if (computers >= n){
			ans = duration ;
			r = duration -1;
			printf("True\n");
		}else{
			l = duration+1;
			printf("False\n");
		}
	}
	printf("%lld",ans);
}
