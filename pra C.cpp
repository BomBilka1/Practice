#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int len, i, j, t=0, x;
    char a[81];
    cin>>a;
    len=(int)strlen(a);
    for(i=0; i<len; i++)
    {
        x=0;
        while(a[i]>='0' && a[i]<='9')
        {
            x*=10;
            x+=(int)(a[i++]-'0');
        }
        if(x==0)
        {
            cout<<a[i];
            t++;
            if(t%40==0)
                cout<<"\n";
        }
        else
        {
            for(j=0; j<x; j++)
            {
                cout<<a[i];
                t++;
                if(t%40==0)
                    cout<<"\n";
            }
        }
    }
    return 0;
}
