/*  Minimum Platforms
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>


int main()
{
	int N, K, T, i, j;
	N = K = T = i = j = 0;
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
		
		for(i = N - 2; i >= 0; --i){	//start the search for leaders from the rightmost end of the array
		
		}
		
		
		if(arr)
			free(arr);
	}
}
 