#include <iostream>
#include <cstring>
using namespace std;
int main(){
	char str[26];
	cin.getline(str, 26);
	char key[6];
	cin.getline(key, 6);
	
	int str_size = strlen(str);
	int key_size = strlen(key);
	
	
	//íà÷àëî 2
	
	char letters[] = " ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	int integer_str[str_size];
	int integer_key[key_size];
	for(int i=0; i<str_size; i++){
		for(int z=0; z<27; z++){
			if(str[i] == letters[z]){
				integer_str[i] = z;
			}
		}
	}
	
	//íà÷àëî 3
	
	for(int i=0; i<key_size; i++){
		for(int z=0; z<26; z++){
			if(key[i] == letters[z]){
				integer_key[i] = z;
			}
		}
	}
	
	//íà÷àëî 4
	
	int sum_array[str_size];
	for(int i=0; i<str_size; i++){
		sum_array[i] = (integer_key[i%5] + integer_str[i])% 27;
	}
	
	//íà÷àëî 5
	for(int i=0; i<str_size; i++){
		cout << letters[sum_array[i]];
	}
}
