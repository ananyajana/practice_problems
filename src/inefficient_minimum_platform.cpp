/*  Minimum Platforms
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>


int main()
{
	int N, K, T, i, j, temp, max_j;
	N = K = T = i = j = 0;
	int * arr = NULL;	// dynamic array to hold the arrival times
	int * dep = NULL;	// dynamic array to hold the departure times
	int * platforms = NULL;
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		temp = max_j = 0;
		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		dep = (int*)malloc(N * sizeof(int));
		platforms = (int*)calloc(N, sizeof(int));
		
		if((NULL == arr) || (NULL == dep) || (NULL == platforms)){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &arr[i]); // scanning the elements of the arrival array one by one
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &dep[i]); // scanning the elements of the departure array one by one
		}
		
		// we need to sort the arrays according to the arrival time
		for(i = 0; i < N - 1; ++i){
			for(j = 0; j < (N - i -1); ++j){
				if(arr[j] > arr[j + 1]){
					temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
					
					temp = dep[j];
					dep[j] = dep[j + 1];
					dep[j + 1] = temp;
				}
			}
		}
		
		platforms[0] = dep[0];
		
		for(i = 1; i < N; ++i){
			for(j = 0; j <= i; ++j){
				if(arr[i] >= platforms[j]){
					platforms[j] = dep[i];
					//printf("i = %d, j = %d, platforms = %d\n",i, j, platforms[j]);
					if(j > max_j)
						max_j = j;
					break;
				}
			}
					
		}
		
		//printf("\n");
			
		printf("%d\n", (max_j + 1));
		if(arr)
			free(arr);
		if(dep)
			free(dep);
		if(platforms)
			free(platforms);
	}
}
 