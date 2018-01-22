/*  Find the first element in the array where al left side elements are less 
than the element and all right side elements are greaterthan it.
Solution:Taking two auxiliay arrays left_max[] and right_min[]. 
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>



int main()
{
	int N, K, T, i, flag, elem;
	N = K = T = i = 0;
	long int *arr, *left_max, *right_min, min, max;	// dynamic array to hold the array elements, the highest elements to the left and right
	arr = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (long int*)malloc(N * sizeof(long int));
		left_max = (long int*)malloc(N * sizeof(long int));
		right_min = (long int*)malloc(N * sizeof(long int));
		
		
		if(!arr)
			exit(1);
				
		if(!left_max)
			exit(1);
			
		if(!right_min)
			exit(1);
		
		for(i = 0; i < N; ++i)
			scanf("%ld", &arr[i]);

		flag = 0;	//if flag is true then one such element is found
		//initializing the leftmost element in the left_max and the rightmost elemet in the right_min array with the array elements. 
		left_max[0] = arr[0];
		right_min[N - 1] =  arr[N - 1];
		
		//fill the left_max array. left_max[i] contains the maximum element seen between 0 - (i-1)th element
		for(i = 1; i < N; ++i){
			if(left_max[i - 1] < arr[i])
				left_max[i] = arr[i];
			else 
				left_max[i] = left_max[i - 1];
		}
		
		//fill the right_min array. right_min[i] contains the minimum element seen between  (i+1) and (N-1)th element
		for(i = N - 2; i >= 0; --i){
			if(right_min[i + 1] > arr[i])
				right_min[i] = arr[i];
			else
				right_min[i] = right_min[i + 1];
		}				
		
		/*printf("left	right\n");
		for(i = 0; i < N; ++i)
			printf("%ld	%ld\n", left_max[i], right_min[i]);
		*/
		
		//if the ith array element is >= left_max[i] and <= right_min[i], then the array element satifies our search 
		for(i = 1; i < N - 1; ++i){
			if((arr[i] >= left_max[i]) && (arr[i] <= right_min[i])){
				flag = 1;
				elem = arr[i];
				break;
			}
		}
		
		if(flag)
			printf("%d\n", elem);
		else
			printf("-1\n");
			
		//freeing up the dynamically allocated memory
		if(arr)
			free(arr);
			
		if(left_max)
			free(left_max);
		
		if(right_min)
			free(right_min);
	}
}
 