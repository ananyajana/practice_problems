/*  Minimum Platforms
Need to find the number of maximum overlapping intervals
Using bubble sort takes too much time.So replacing with merge sort.
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
 
    /* create temp arrays */
    int L[n1], R[n2];
 
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];
 
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    /* Copy the remaining elements of L[], if there
       are any */
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    /* Copy the remaining elements of R[], if there
       are any */
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 
/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l+(r-l)/2;
 
        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
 
        merge(arr, l, m, r);
    }
}


int main()
{
	int N, K, T, i, j, temp, max, plat_needed;
	N = K = T = i = j = 0;
	int * arr = NULL;	// dynamic array to hold the arrival times
	int * dep = NULL;	// dynamic array to hold the departure times
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		dep = (int*)malloc(N * sizeof(int));
		
		if((NULL == arr) || (NULL == dep)){
			//printf("couldn't allocate space! Exiting\n");
			exit(1);
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &arr[i]); // scanning the elements of the arrival array one by one
		}
		for(i = 0; i < N; ++i){
	   		scanf("%d", &dep[i]); // scanning the elements of the departure array one by one
		}
		
		/*// sorting the arrival array
		for(i = 0; i < N - 1; ++i){
			for(j = 0; j < (N - i -1); ++j){
				if(arr[j] > arr[j + 1]){
					temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
			}
		}
		// sorting the departure array
		for(i = 0; i < N - 1; ++i){
			for(j = 0; j < (N - i -1); ++j){
				if(dep[j] > dep[j + 1]){
					temp = dep[j];
					dep[j] = dep[j + 1];
					dep[j + 1] = temp;
				}
			}
		}*/
		mergeSort(arr, 0, (N - 1));
		mergeSort(dep, 0, (N - 1));
		
		plat_needed = max = 1;
		i = 1, j = 0;
 
		// Similar to merge in merge sort to process all events in sorted order
		while (i < N && j < N){
      		// If next event in sorted order is arrival, increment count of platforms needed
      			if (arr[i] < dep[j]){
				plat_needed++;
				i++;
				if (plat_needed > max)  // Update result if needed
					max = plat_needed;
			}
			else{ // Else decrement count of platforms needed
				plat_needed--;
				j++;
			}
		}

		
		//printf("\n");
			
		printf("%d\n", max);
		if(arr)
			free(arr);
		if(dep)
			free(dep);
	}
}
 