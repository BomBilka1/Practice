    
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

void convert(const int num, string &snum){
	if (num%2==0)
		snum+="0";
	else snum+="1";
	if ((num/2)!=0) convert(num/2, snum);
	else return;
}

int main(){
	string snum;
	int number, help, sum;
	cin >> number;
	convert(number, snum);
	
	int max = -9000;
	sum = 0;
	
	int size = snum.size();
	int array[size], array2[size];;
	int counter = 0;
	
	
	for(int i=size-1; i>=0;i--){
	    array[counter] = int(snum[i])-48;   
	    counter++;
	    
	}
	counter = 0;
	for(int j=0; j<size; j++){
	
    	number = array[0];
    	for(int i = 0; i<size; i++){
    	    help = array[i];
    	    array[i] = array[i+1];
    	    array[i+1] = help;
    	}
    	
    	array[size-1] = number;
    	
    	for(int i = size-1; i>=0; i--){
    	    array2[i] = array[i]*pow(2,counter);
    	    counter++;
    	}
    	
    	
    	
    	for(int i = 0; i<size; i++){
    	    sum += array2[i];
    	}
    	
    	
    	if(max<sum){
    	    max = sum;   
    	}
    	sum = 0;
    	counter = 0;
    	
	}
	cout << max;
	
	
}
