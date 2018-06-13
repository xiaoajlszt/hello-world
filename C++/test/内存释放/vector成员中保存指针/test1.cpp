#include <iostream>
#include "a.h"
using namespace std;

int main()
{
    A *a = new A();
    B b;
    //cout << sizeof(unsigned long) << endl;
    //cout << sizeof(a) << endl;

    b.AddA(a);

    //delete b.m_a[0]; 
    //b.m_a.clear();
    
    vector<A*>::iterator iter = b.m_a.begin();
    for(; iter != b.m_a.end(); ++iter)
    {
        A *ma = *iter;
        if(ma != NULL)
        {
            delete ma;
        }
    }
    
    return 0;
}
