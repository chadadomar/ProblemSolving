#include <bits/stdc++.h>

using namespace std;

int main()
{
    int d;
	cin>>d;
	float r;
	r=(float)log(d)/log(2);
	if(r==int(r)) cout<<int(r)+1<<endl;
	else cout<<int(r)+2<<endl;
}
