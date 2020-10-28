#include <iostream>

using namespace::std;

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

	cout << "The sum is: " << sum_even_list(4000000);

}