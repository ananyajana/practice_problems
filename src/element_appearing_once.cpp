/*  Given a sorted array of integers, every element appears twice except for one. 
Find that single one in linear time complexity and without using extra memory.

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>



int main()
{
	int N, T, i, temp;
	N = T = i = 0;
	int *arr;	// dynamic array to hold the array elements, the highest elements to the left and right
	arr = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		
		if(!arr)
			exit(1);
				
		
		//scanning the array elements one by one
		for(i = 0; i < N; ++i)
			scanf("%d", &arr[i]);
		
		for(i = 0; i < N - 1; i += 2){
			if(((i % 2) == 0) && (arr[i] != arr[i + 1])){
				printf("%d\n", arr[i]);
				break;
			}
		}
		if(i == (N - 1))
			printf("%d\n", arr[i]);

		
		//freeing up the dynamically allocated memory
		if(arr)
			free(arr);		
	}
}
 