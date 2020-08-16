#include <limits.h>
#include <stdio.h>
#include "math_eq.h"

int sum(int x, int y){
	return x+y;
}

void swap(int *x, int *y){
	int t =*x;
	*x = *y;
	*y =t;
}

int diff(int x, int y){
	if(y<=x)
		return x-y;
	return y-x;
}

int mdc(int x, int y){
	if(!y)
		return 0;
	while(y){
		int t = x;
		x = y;
		y= t%y;
	}
	return x;
}