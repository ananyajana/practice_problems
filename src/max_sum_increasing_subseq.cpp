/*  Maximum sum increasing subsequence
This has to be solved using dynamic programming.
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>


int main()
{
	int N, K, T, max, i, j;
	N = K = T = max = i = j = 0;
	int * arr = NULL;	// dynamic array to hold the array elements
	int * max_sum_incr_subsq;
	
	
    
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		max = i = j = 0;
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		max_sum_incr_subsq = (int*)malloc(N * sizeof(int));
		if((NULL == arr) || (NULL == max_sum_incr_subsq)){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &arr[i]); // scanning the elements of the array one by one
	   		max_sum_incr_subsq[i] = arr[i];
		}
		
		for(i = 1; i < N; ++i){
			for(j = 0; j < i; ++j){
				if((arr[i] > arr[j]) && (max_sum_incr_subsq[i] < max_sum_incr_subsq[j] + arr[j]))
					max_sum_incr_subsq[i] = max_sum_incr_subsq[j] + arr[j];
			}
		}
		
		for(i = 0; i < N; ++i){
			if(max < max_sum_incr_subsq[i])
				max = max_sum_incr_subsq[i];
		}
		printf("%d\n", max);
		if(arr)
			free(arr);
		if(max_sum_incr_subsq)
			free(max_sum_incr_subsq);
	}
}
 