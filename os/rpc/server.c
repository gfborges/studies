#include <stdlib.h>
#include <rpc/rpc.h>
#include "calc.h"

int *soma_1_svc(in* nums, struct svc_req* arg) {
    static int res;
    res = nums->a + nums->b;
    return &res;
}

int* mult_1_svc(in* nums, struct svc_req* arg ) {
    static int res;
    res = nums->a * nums->b;
    return &res;
}

int* div_1_svc(in* nums, struct svc_req* arg ) {
    static int res;
    res = nums->a / nums->b;
    return &res;
}

int* max_1_svc(in* nums, struct svc_req* arg ) {
    static int res;
    res = (nums->a > nums->b) ? nums->a : nums->b;
    return &res;
}

int* min_1_svc(in* nums, struct svc_req* arg ) {
    static int res;
    res = (nums->a < nums->b) ? nums->a : nums->b;
    return &res;
}
