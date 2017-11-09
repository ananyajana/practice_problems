/*  Subarray with given sum
Similar to maximum sub-array problem with a small difference.
Let i, j denote the left and right(respectively) index of 
the subarray which has sum S. We start calculating the 
subarray sum from leftmost index and continue doing so
until our sum becomes either equal to or greater than S.
If equal, we print out the indices. Else if it is greater
than S, we subtract arr[i] from our sum and increment i.
We continue doing this until our sum is <= S. If < S, then
we increment jand start adding arr[j] and perform the same 
check i.e. whether current sum is >= S.
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX	4

int main()
{
	int N, S, T, temp, start, end, i, j;
	N = S = T = 0;
	int * arr = NULL;	// dynamic array to hold the array elements
	
	
    
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){

		temp = 0;
		start = -1;	// this holds the starting index of the subarray whose sum equals S
		end = -1;	// this holds the ending index of the subarray whose sum equals S
		
		scanf("%d", &N); // scanning the number of elements in the array
		scanf("%d", &S); // scanning the sum
		
		arr = (int*)malloc(N * sizeof(int));
		if(NULL == arr){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(int n = 0; n < N; ++n){
	   		scanf("%d", &arr[n]); // scanning the elements of the array one by one
		}
		
		for(i = 0; i < N; ++i){
			for(j = i; j < N; ++j){		// find the sum of the array entries starting at index i and endng at endex j. temp holds this sum
				temp += arr[j];
				if(temp == S){	// we have found the subarray whose sum is S, print the indices i+1, j+1
					start = i + 1;
					end = j + 1;
				}
				else if(temp > S){	// if this sum is greater than S, then we need to decrease the sum, starting from the element arr[i]
					while((i <= j) && (temp > S)){
						temp = temp - arr[i++];
					}
					if(temp == S){
						start = i + 1;
						end = j + 1;
					}
					else if(i > j)
						temp = 0;
				}	
			}
			
			if(j == N)
				break;
		}
		printf("%d %d\n", start, end);	//this prints the maximum sum
		if(arr)
			free(arr);
	}
}
