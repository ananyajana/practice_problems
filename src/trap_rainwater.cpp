/*  Trapping rain water
Solution(from geeksforgeeks): Find out the highest bars on the 
left and right sides and then compute the amount of water between
them and the ends.
Preprocessing: store the highest element bar on the left and right for
every array element

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>



int main()
{
	int N, K, T, i, water;
	N = K = T = i = 0;
	int *arr, *left, *right;	// dynamic array to hold the array elements, the highest elements to the left and right
	arr = left = right = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		left = (int*)malloc(N * sizeof(int));
		right = (int*)malloc(N * sizeof(int));
		
		if(!arr)
			exit(1);
		if(!left)
			exit(1);
		if(!right)
			exit(1);
			
		for(i = 0; i < N; ++i)
			scanf("%d", &arr[i]);
		
		water = 0;
		left[0] = arr[0];
		for (i = 1; i < N; i++)
       			left[i] = (left[i-1] > arr[i]) ? left[i-1]:arr[i];
		
		right[N - 1] = arr[N - 1];
		for (i = N-2; i >= 0; i--)
       			right[i] = (right[i+1] > arr[i]) ? right[i+1]:arr[i];
       		
       		// Calculate the accumulated water element by element
    		// consider the amount of water on i'th bar, the
    		// amount of water accumulated on this particular
    		// bar will be equal to min(left[i], right[i]) - arr[i] .
    		for (int i = 0; i < N; i++)
       			water += ((left[i] < right[i]) ? left[i]:right[i]) - arr[i];
		
		printf("%d\n", water);
		
		
		if(arr)
			free(arr);
		if(left)
			free(left);
		if(right)
			free(right);
	}
}
 