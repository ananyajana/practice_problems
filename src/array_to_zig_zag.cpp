/*  Convert an array into zig-zag fashion

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>



int main()
{
	int N, T, i, flag, temp;
	N = T = i = 0;
	int *arr;	// dynamic array to hold the array elements, the highest elements to the left and right
	arr = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		flag = 0;
		
		if(!arr)
			exit(1);
				
		
		//scanning the array elements one by one
		for(i = 0; i < N; ++i)
			scanf("%d", &arr[i]);
		
		for(i = 0; i < (N - 1); ++i){
			if(0 == flag){
				if(arr[i] > arr[i + 1]){
					temp = arr[i];
					arr[i] = arr[i + 1]; 
					arr[i + 1]= temp;
				}
				flag = 1;
			}
			else{
				if(arr[i] < arr[i + 1]){
					temp = arr[i];
					arr[i] = arr[i + 1]; 
					arr[i + 1]= temp;
				}
				flag = 0;
			}
		}
		
		for(i = 0; i < N; ++i)
			printf("%d ", arr[i]);
		printf("\n");
		
		//freeing up the dynamically allocated memory
		if(arr)
			free(arr);
			
	}
}
 