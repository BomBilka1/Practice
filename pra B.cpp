#include <iostream>
#include <string>
#include <cmath>
 
using namespace std;
 
int main() {
 
    string an;
    string a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string fk, k;//= "SUPERDOG"
    string b;// b = "DONOTTOSAUNASOONAFTEREATING";
    string o;
    int s;// = 9,
    int i;
 
    cin >> b >> fk >> s;
 
    o = b;
    an = a;
    int t = 0;
 
    // удаление повторов в ключе
    for(int i = 0; i < fk.size(); i++) {
 
        bool repeat = false;
        for(int j = i - 1; j >= 0; j--) {
            if(fk[i] == fk[j]) {
                repeat = true;
            }
        }
        if(repeat == false) {
            k.insert(t, &fk[i], 1);
            t++;
        }
    }
 
    // вставка ключа в алфавит
    for(int i = 0; i < k.size(); i++) {
        if(s + i >= a.size()){
            an[s + i - (int)k.size()] = k[i];
        }
        else {
            an[s + i] = k[i];
        }
    }
 
    int j = s + k.size();
    bool not_repeat = true, two_step = false;
    int n = 0;
 
    int razmer = an.size();
 
 
    // создание алфавита
    for(int i = s + k.size();  i < razmer; i++) {
        bool c = true;
        while(c) {
            bool r = false;
            for(int j = 0; j < k.size(); j++) {
                if(a[n] == k[j]) {
                    r = true;
                }
            }
            if(r == false){
                an[i] = a[n];
                c = false;
            }
            n++;
        }
        if(i == razmer - 1 && two_step == false) {
            two_step = true;
            i = -1;
            razmer = s;
        }
    }
 
    // шифровка
    for(int i = 0; i < b.size(); i++) {
        for(int j = 0; j < a.size(); j++) {
            if(b[i] == a[j]){
                o[i] = an[j];
            }
        }
    }
 
    cout << o;
 
    return 0;
}
