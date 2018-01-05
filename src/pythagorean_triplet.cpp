/*  Pythagorean  triplet
Solution: We can pre-compute the squares and keep them sorted.
Then process that array to figure out whether a pytagorean triplet exsts.
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define PARENT(i)	((i - 1)/2)
#define LEFT(i)		(2*i + 1)
#define	RIGHT(i)	(2*i + 2)

void max_heapify(int a[], int i);
void build_max_heap(int a[]);
void heap_sort(int a[]);

//heap sz
int size, sz;


int main()
{
	int N, K, T, i, j, k, flag;
	N = K = T = i = j = k = 0;
	int *arr;	// dynamic array to hold the array elements
	arr = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		scanf("%d", &N); // scanning the number of elements in the array
		arr = (int*)malloc(N * sizeof(int));
		
		if(!arr)
			exit(1);

			
		for(i = 0; i < N; ++i){
			scanf("%d", &arr[i]);
			arr[i] = arr[i] * arr[i];
		}
		sz = size = N;
		//Soring the array using heapsort
		heap_sort(arr);
		
		flag = 0;
		
		//process the sorted array to check if a Pythaorean triplet exists: meeting the middle algorithm
		for(i = N - 1; i >= 2; --i){
			// arr[i] contains the prospective sum
			j = 0;
			k = i - 1;
			while(j < k){
				if(arr[j] + arr[k] == arr[i]){
					flag = 1;
					break;
				}
				else if (arr[j] + arr[k] < arr[i])
					++j;
				else
					--k;
			}
			if(flag)
				break;
		}
				
		
		if(flag)
			printf("Yes\n");
		else
			printf("No\n");
		
		if(arr)
			free(arr);
	}
}

void build_max_heap(int a[])
{
	int i;
	for(i = (sz - 1)/2; i >= 0; --i){
		//printf("i = %d\n", i);
		max_heapify(a, i);
	}	
}

void max_heapify(int a[], int i)
{
	int l, r, largest, temp;
	l = LEFT(i);
	r = RIGHT(i);

	//printf("%d %d\n", a[i], i);	
		
	if((l < sz) && (a[l] > a[i]))
		largest = l;
	else
		largest = i;
	if((r < sz) && ( a[r] > a[largest]))
		largest = r;
	if(largest != i){
		temp = a[largest];
		a[largest] = a[i];
		a[i] = temp;
		/*printf("hi\n");
		for(i = 0; i < size; ++i){
			printf("%d ", a[i]);
		}
		printf("\n");*/
		max_heapify(a, largest);
	}	
}

void heap_sort(int a[])
{
	int i, temp;
	
	build_max_heap(a);
	//printf("The heap is\n");
	/*for(i = 0; i < size; ++i){
		printf("%d ", a[i]);
	}
	printf("\n");*/
	
	//place the biggest element which is at the root, at the end of the array
	for(i = sz - 1; (i >= 1) && (sz > 1); --i){
		//printf("1.sz = %d, i = %d\n", sz, i);
		temp = a[0];
		a[0] = a[i];
		a[i] = temp;

		/*printf("hi1\n");
		for(i = 0; i < size; ++i){
			printf("%d ", a[i]);
		}
		printf("\n");*/
		//reduce the size of the heap as we removed the largest element
		--sz;
	
		//create a heap out of the remaining elements in the heap
		max_heapify(a, 0);
		//printf("2.sz = %d, i = %d\n", sz, i);
	}
}
 