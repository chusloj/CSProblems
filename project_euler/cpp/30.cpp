#include <iostream>

using namespace::std;


int get_digit_sum(int num){
	int digit_sum = 0;
	int rem;
	while(num > 0){
		rem = num % 10;
		digit_sum += pow(rem, 5);
		num = floor(num/10);
	}

	return digit_sum;

}



int main(){
	int total_sum = 0;
	for(int i=10; i <= 6 * pow(9,5); i++){
		if(i == get_digit_sum(i)){
			total_sum += i;
		}
	}

	cout << total_sum;
	return 0;
}