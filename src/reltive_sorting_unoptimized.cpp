/*  Sort an array according to the order defined by another array

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int a[], int n);

int main()
{
	int M, N, T, i, j, k, l, temp, occupied, temp1;
	N = T = i = 0;
	int *a1, *a2, *a1_sorted, *temp_sorted;	// dynamic array to hold the array elements, the highest elements to the left and right
	a1 = a2 = a1_sorted = temp_sorted = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d %d", &M, &N); // scanning the number of elements in the array A1 and A2 respectively
		a1 = (int*)malloc(M * sizeof(int));
		a2 = (int*)malloc(N * sizeof(int));
		a1_sorted = (int*)malloc(M * sizeof(int));	// contains the relatively sorted array
		temp_sorted = (int*)malloc((M - N) * sizeof(int)); // contains the elements present in a1 but not in a2. This array is used for sorting.
		
		if((!a1) || (!a2))
			exit(1);
		
		for(i = 0; i < M; ++i){
	   		scanf("%d", &a1[i]); // scanning the elements of the arrival array one by one
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &a2[i]); // scanning the elements of the departure array one by one
		}	
		
		/*occupied = 0;
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
			 
		}*/
		
		// if the element is present in both a1 and a2, then copy it to a1_sorted, and put a 0 in place of that element in a1
		k = 0;
		for(i = 0; i < N; ++i){
			for(j = 0; j < M; ++j){
				if(a2[i] == a1[j]){
					a1_sorted[k++] = a2[i];
					a1[j] = 0;
				}
			}
		}
		
		// copy the remaining elements of a1 into temp_sorted
		l = 0;
		for(j = 0; j < M; ++j){
			if(a1[j] != 0)
				temp_sorted[l++] = a1[j];
		}
		
		//sort the temprary array
		insertion_sort(temp_sorted, l);
		
		//place the elements from temp_sorted into a1_sorted
		for(j = 0; j < l; ++j){
			a1_sorted[k++] = temp_sorted[j];
		}
		
		for(j = 0; j < M; ++j){
			printf("%d ", a1_sorted[j]);
		}
		printf("\n");
		
		//freeing up the dynamically allocated memory
		if(a1)
			free(a1);
		if(a2)
			free(a2);
		if(a1_sorted)
			free(a1_sorted);
		if(temp_sorted)
			free(temp_sorted);		
	}
}


void insertion_sort(int a[], int n)
{
	int i, j, key;

	for(j = 1; j < n; ++j){
		key = a[j];
		i = j - 1;
		while(i >= 0 && a[i] > key){
			a[i + 1] = a[i];
			i = i - 1;
		}
		a[i + 1] = key;
	}
}

 