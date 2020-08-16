#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include "math_eq.h"
int tests_run = 0;
#define FAIL() printf("\nfailure in %s() line %d\n", __func__, __LINE__)
#define _assert(test) do { if (!(test)) { FAIL(); return 1; } } while(0)
#define _verify(test) do { int r=test(); tests_run++; if(r) return r; } while(0)

int test_sum(){
	_assert(sum(1,2) == 3);
	return 0;
}
int  test_diff(){
	_assert(diff(1,1) == 0);
	_assert(diff(2,1) == 1);
	_assert(diff(1,2) == 1);
	return 0;
}
int test_mdc(){
	_assert(mdc(12, 24) == 12);
	_assert(mdc(24, 12) == 12);
	return 0;
}
int all_tests(){
	_verify(test_sum);
	_verify(test_diff);
	_verify(test_mdc);
	return 0;	
}
 int main(){
 	int result = all_tests();
 	if(result == 0)
 		printf("PASSED\n");
 	printf("Tests run: %d\n", tests_run);

 	return result != 0;
 }