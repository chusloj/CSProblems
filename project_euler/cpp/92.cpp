#include <iostream>

using namespace::std;

int next_chain(int num){
	int sum = 0;
	int digit;
	while(num > 0){
		digit = num % 10;
		sum += pow(digit, 2);
		num = floor(num/10);
	}

	return sum;
}


int find_termination(int start_num){
	int num = start_num;
	while((num != 1) && (num != 89)){ // using the correct "&&" operator made the program very fast
		num = next_chain(num);
	}

	return num;
}


int main(){
	int count_89 = 0;
	for(int num=1; num<10000000; num++){
		if(find_termination(num) == 89){
			count_89 += 1;
		}
	}

	cout << count_89;
}