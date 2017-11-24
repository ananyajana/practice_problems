/*  Reverse all subarrays of size K
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>


int main()
{
	int N, K, T, i, j, num, temp;
	N = K = T = i = j = num = 0;
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
	   		scanf("%d", &arr[i]); // scanning the elements of the arrival array one by one
		}
 		scanf("%d", &K); // scanning the size of the subarray
 		
		for(i = 0; i < N; i = i + K){	// scan every subarray of size K and revere it
			j = (i + K - 1)> (N - 1)? (N - 1) : (i + K - 1);
			num = (j - i + 1)/2;
			for(int k = 0; k < num; ++k){	//swapping the elements
				temp = arr[i + k];
				arr[i + k] = arr[j - k];
				arr[j - k] = temp;	
			}
		}
 

		
		//printf("\n");
			
		printf("\n");
		if(arr)
			free(arr);
	}
}
 