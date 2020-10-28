#include <stdio.h>

int fib(int n){

	int result;

	if(n <= 1){
        result = 1;
    }

    else {result = fib(n-1) + fib(n-2);}

    return result;
}

int sum_even_list(int upper_limit){

    int n = 0;
    int sum_list = 0;
    int result;

	while(fib(n) < upper_limit){

		result = fib(n);
		if(result % 2 == 0){sum_list += result;}
        n += 1;

    }

    return sum_list;
}


int main(){

    int final_result;
	final_result = sum_even_list(4000000);

    printf("The sum is: %d", final_result);

}