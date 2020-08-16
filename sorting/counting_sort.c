#include <stdio.h>
const int max = 100;
const int range  = 10;

void print_arr(int *arr, int size){
	for(int i=0; i<size; i++){
		if(i > 0)
			printf(" ");
		printf("%d", arr[i]);
	}
	printf("\n");
}

void copy_to(int * from, int *to,const int size){
	for(int i=0; i<size; i++)
		to[i] = from[i];
}

void count_sort(int * arr, int size){
	int count[10]= {0};
	int copy[max];
	for(int i=0; i<size; i++)
		count[arr[i]]++;
	for(int i=1; i<10; i++)
		count[i] += count[i-1];
	for(int i=0; i<size; i++){
		copy[ --count[arr[i]] ]= arr[i];
	}
	copy_to(copy, arr,size);
}

void input(int * arr, int * size){
	scanf("%d", size);
	for(int i=0; i<(*size);i++)
		scanf("%d",&arr[i]);
}

int main(){
	int arr[max],size;
	input(arr, &size);
	count_sort(arr, size);
	print_arr(arr, size);

	return 0;
}
