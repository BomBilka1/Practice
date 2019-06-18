#include <iostream>
#include <string.h>

using namespace std;

int main(void) {
    int a = 0, res = 0;
    char str[17] = {'\0'}, max_str[17] = {'\0'}, temp = '\0';
    int len = 0;
    int i = 0, j = 0;

    scanf("%d", &a);
    itoa(a, str, 2);

    for (len = strlen(str), i = 0; i < len; i++) {
        if (strcmp(str, max_str) > 0)
            strcpy(max_str, str);
        temp = str[0];
        for (j = 1; j < len; j++)
            str[j-1] = str[j];
        str[len-1] = temp;
    }

    for (j = 0; j < len; j++)
        res = res * 2 + (max_str[j] - '0');
    printf("%d\n", res);
    return 0;
}
