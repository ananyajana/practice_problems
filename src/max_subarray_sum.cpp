/*  Maximum subarray sum problem
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX	4

int main()
{
	int N, K, T;
	N = K = T = 0;
	char * arr = NULL;	// dynamic array to hold the array elements
	
	
    
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (char*)malloc(N * sizeof(char));
		if(NULL == arr){
			printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(int n = 0; n < N; ++n){
	   		scanf("%d ", &arr[n]); // scanning the elements of the array one by one
		
		}
		
		if(arr)
			free(arr);
	}
}
