#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    scanf("%d",&n);
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
    }
    int q=0,z=0,p=0;
    for(int i = 0; i < n; i++){
		if(arr[i]<0){
			q++;
		} 
    	if(arr[i]==0){z++;
		} 
        if(arr[i] > 0){ p++;
		}
    } 
    /*printf("%d\n",p);
    printf("%d\n",q);
    printf("%d\n",z);*/
    float a,b,c;
    a=(double) p/n;
    b=(double) q/n;
    c=(double) z/n;
    printf("%.6f\n",a);
    printf("%.6f\n",b);
    printf("%.6f\n",c);
    return 0;
}
