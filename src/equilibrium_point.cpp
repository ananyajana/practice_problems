/*  Equilibrium point. 
Logic: At the time of input we calculate the sum of all
elements of the array. Later we iterate from the beginning
of the array to the N-1 element to see whether the sum of 
elements till i matches the sum of the remaining elements
after i+1.
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX	4

int main()
{
	int N, T, eq_point, sum_before, sum_after, total, i;
	N = T = total = i = 0;
	eq_point = -1;
	int * arr = NULL;	// dynamic array to hold the array elements
	
	
    
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		sum_before = sum_after = total = 0;
		eq_point = -1;
		
		scanf("%d", &N); // scanning the number of elements in the array
		
		arr = (int*)malloc(N * sizeof(int));
		if(NULL == arr){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		
		for(i = 0; i < N; ++i){
	   		scanf("%d", &arr[i]); // scanning the elements of the array one by one
	   		total += arr[i];
		}
		
		if(1 == N){	// if there is only one element, the that is the equilibrium point, there is no  need to scan the element in this case.
			eq_point = 1;	// but still we would as this is a set of test inputs and not scanning an input would mess the inputs
		}
		
		for(i = 0; i < (N - 1); ++i){
			sum_before += arr[i];
			sum_after = total - (arr[i+1] + sum_before); 	//the i+1 th element is the equlibrium element if sum till i the element
			if(sum_before == sum_after){			//matches the sum of remaining elements after i+1
				eq_point = i+1+1;
				break;
			}
		}
		
		printf("%d\n", eq_point); 
		if(arr)
			free(arr);
	}
}
