/*  Leaders in the array
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>


int main()
{
	int N, K, T, last_leader_seen, i, j;
	N = K = T = last_leader_seen = i = j = 0;
	int * arr = NULL;	// dynamic array to hold the array elements
	int * leads = NULL;	// dynamic array to hold the array leaders
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		last_leader_seen = i = j = 0;
		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		leads = (int*)calloc(N, sizeof(int));	// We need the initial leads array to be cleared
		
		if((NULL == arr) ||(NULL == leads)){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &arr[i]); // scanning the elements of the array one by one
		}
		
		for(i = N; i > 0; --i){	//start the search for leaders from the rightmost end of the array

		}
		
		for(i = 0; i < N; ++i){
			
		}
		
		if(arr)
			free(arr);
	}
}
 