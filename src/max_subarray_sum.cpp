/*  Maximum subarray sum problem
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX	4

int main()
{
	int N, K, T, max_sum, temp, i, j, num_of_negatives, max_num;
	N = K = T = 0;
	int * arr = NULL;	// dynamic array to hold the array elements
	
	
    
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		max_sum = temp = i = j = num_of_negatives =0;
		max_num = -999999;
		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		if(NULL == arr){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(int n = 0; n < N; ++n){
	   		scanf("%d", &arr[n]); // scanning the elements of the array one by one
	   		if(arr[n] < 0)
	   			++num_of_negatives;	// this is to figure out how many negative numbers are present in the input
	   		if(max_num <  arr[n])		// if all the numbers in the input are negative, we would 
	   			max_num = arr[n];	// need to find the maximum among them, which will be the maximum sum
		}
		if(N == num_of_negatives){	// if all array entries are negative, output the largest among them
			printf("%d\n", max_num);
			continue;		
		}
		
		for(i = 0; i < N; ++i){	// max_sum has been initialized to 0, we start iterating over the numbers to
			//printf("1.temp = %d,max_sum = %d, i = %d\n", temp, max_sum, i); 
			for(j = i; j < N; ++j){		// find the sum of the array entries starting at index i and endng at endex j. temp holds this sum
				temp += arr[j];		
				if(temp > max_sum)	// if this sum is greater than max_sum then store this new sum in max sum
					max_sum = temp;
				else if(max_sum >= 0 && temp < 0 && j < N - 1){	//if the value in temp falls below 0, then we reposition the indices i and j, 
					i = j+1;
					temp = 0;	// we inaitialize the new sum to 0
					//printf("2.temp = %d,max_sum = %d\n", temp, max_sum);
					continue;
				}
				//printf("3.temp = %d,max_sum = %d, i = %d, j = %d\n", temp, max_sum, i, j);
			}
			
			if(j == N)
				break;
		}
		printf("%d\n", max_sum);	//this prints the maximum sum
		if(arr)
			free(arr);
	}
}
