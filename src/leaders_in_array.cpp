/*  Leaders in the array
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>


int main()
{
	int N, K, T, max, i, j;
	N = K = T = max = i = j = 0;
	int * arr = NULL;	// dynamic array to hold the array elements
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		
		if(NULL == arr){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &arr[i]); // scanning the elements of the array one by one
		}
		
		for(i = 1; i < N; ++i){

		}
		
		for(i = 0; i < N; ++i){
			
		}
		
		if(arr)
			free(arr);
	}
}
 