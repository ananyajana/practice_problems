/*  Maximum subarray sum problem
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX	4

int main()
{
	int N, K, T, max_sum, temp, i, j;
	N = K = T = max_sum = temp = i = j = 0;
	int * arr = NULL;	// dynamic array to hold the array elements
	
	
    
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		if(NULL == arr){
			printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(int n = 0; n < N; ++n){
	   		scanf("%d", &arr[n]); // scanning the elements of the array one by one
		}
		max_sum = arr[0];
		for(i = 0; i < N; ++i){
		printf("1.temp = %d,max_sum = %d, i = %d\n", temp, max_sum, i);
			for(j = i; j < N; ++j){
				temp += arr[j];
				if(temp > max_sum)
					max_sum = temp;
				else if(max_sum > 0 && temp < 0 && j < N - 1){
					i = j+1;
					temp = 0;
					printf("2.temp = %d,max_sum = %d\n", temp, max_sum);
					continue;
				}
				printf("3.temp = %d,max_sum = %d, i = %d, j = %d\n", temp, max_sum, i, j);
			}
			
			if(j == N)
				break;
		}
		printf("max_sum = %d\n", max_sum);
		if(arr)
			free(arr);
	}
}
