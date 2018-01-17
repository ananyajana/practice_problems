/*  Stock buy and sell
Solution: find all non-overlapping contiguous increasing subsequences
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>



int main()
{
int N, K, T, i, j, start, end, start_flag, end_flag;
	N = K = T = i = j = start = end = 0;
	int *arr;	// dynamic array to hold the array elements, the highest elements to the left and right
	arr = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		
		if(!arr)
			exit(1);

		for(i = 0; i < N; ++i)
			scanf("%d", &arr[i]);
		
		start = end = -1;
		start_flag = end_flag = 0;
		
		for(i = 0; i < (N - 1); ++i){
			while((arr[i] >= arr[i + 1]) && (i < N - 1))
				++i;
			if(i != N - 1){
				start = i;
				//printf("start = %d\n", start);
			}
			else
				break;
				
			while((arr[i] < arr[i+1]) && (i <= N - 1) && (start != -1))
				++i;
			if(i <= N - 1){
				end = i;
				printf("(%d %d) ", start, end);
			}
		}
		printf("\n");
		
		if(arr)
			free(arr);
	}
}
 