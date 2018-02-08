/*  Given an input stream of n integers the task is to insert integers to stream 
and print the kth largest element in the stream at each insertion.

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>



int main()
{
	int M, N, T, i, j, temp, occupied, temp1;
	N = T = i = 0;
	int *a1, *a2;	// dynamic array to hold the array elements, the highest elements to the left and right
	arr = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d %d", &M, &N); // scanning the number of elements in the array A1 and A2 respectively
		a1 = (int*)malloc(M * sizeof(int));
		a2 = (int*)malloc(N * sizeof(int));
		
		if((!a1) || (!a2))
			exit(1);
		
		for(i = 0; i < M; ++i){
	   		scanf("%d", &a1[i]); // scanning the elements of the arrival array one by one
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &a2[i]); // scanning the elements of the departure array one by one
		}	
		
		occupied = 0;
		for(i = 0; i < N; ++i){
			temp = a2[i];
			for(j = 0; j < M; ++j){
				if(temp == a1[j]){
					if(occupied != j){
						occupied += 1;
						temp1 = a1[j];
						a1[j] = a1[occupied];
						a1[occupied] = temp1;
					}
			}
			 
		}
		
		//freeing up the dynamically allocated memory
		if(a1)
			free(a1);
		if(a2)
			free(a2);		
	}
}
 