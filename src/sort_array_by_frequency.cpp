/*  Sorting Elements of an Array by Frequency

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define	SZ	61

int main()
{
	int N, T, i, j, unique_count, num, max, max_index, max_seen;
	N = T = i = unique_count = max = max_index = max_seen = 0;
	//int* arr;	// dynamic array to hold the elements
	int elem_count[SZ] = {0};	// array to hold the count of the elements.  Given, elements are in the range 1 to 60.
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		scanf("%d", &N);	//scanning the size of the array
		
		unique_count = max = max_index = max_seen = 0;
		
		for(i = 0; i < N; ++i){
			scanf("%d", &num);	//scanning the elements of the array
			//printf("%d ", num);
			//incrementing the count of the scanned element
			if(0 == elem_count[num])
				++unique_count;	// if the number is seen for the first time, increment the count of unique numbers seen till now
			++elem_count[num];
			
			if(num > max_seen)	// keep track of the maximum number seen so far, as we don't want to iterate over entire elem_count array
				max_seen = num;
		}

		
		//find the maximum frequency in the remaining elem_count array and print the index that many times, similar to counting sort and then put a zero
		// in that place and continue until we have found out all the maximums
		for(i = 0; i < unique_count; ++i){
			for(j = 0; j <= max_seen; ++j){
				if(elem_count[j] > max){
					max = elem_count[j];	// saving the maximum frequency
					max_index = j;		// saving the maximum frequency index		
				}
			}
			for(j = 0; j < max; ++j)
				printf("%d ", max_index);
			elem_count[max_index] = 0;	// clearing this element as we have already taken this into account
			max = max_index = 0;
		}
		printf("\n");
	}
}

