/*  Leaders in the array
If an element is bigger than the element to its right and also 
bigger than the last leader seen, then it is a leader
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
		leads = (int*)malloc(N* sizeof(int));	// We need the initial leads array to be cleared
		
		if((NULL == arr) ||(NULL == leads)){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &arr[i]); // scanning the elements of the array one by one
	   		leads[i] = -99999;
		}
		
		last_leader_seen = leads[N -1] = arr[N - 1];	// the rightmost element is always a leader
		for(i = N - 2; i >= 0; --i){	//start the search for leaders from the rightmost end of the array
			if((arr[i] > arr[i + 1]) && (arr[i] > last_leader_seen)){	
				leads[i] = arr[i];
				last_leader_seen = arr[i];
			}
		}
		
		for(i = 0; i < N; ++i){
			if(-99999 != leads[i])
				printf("%d ", leads[i]);	// print out the leaders
		}
		printf("\n");
		if(arr)
			free(arr);
		if(leads)
			free(leads);
	}
}
 