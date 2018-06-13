#ifndef _SINGLETON_H_
#define _SINGLETON_H_

#include <iostream>
using namespace std;

class SingletonA
{
public:
    int a = 10;
    int b = 20;
    static SingletonA* Instance();

protected:
    SingletonA();
    ~SingletonA();

private:
    static SingletonA* _instance;

    class CGarbo
    {
    public:
        CGarbo()
        {
            cout << "Enter CGarbo construction" <<endl;
        }

        ~CGarbo()
        {
            cout << "Enter CGarbo destruction" <<endl;

            if(NULL !=_instance)
            {
                delete _instance;
                _instance = NULL;
            }
        }
    };
    static CGarbo Garbo;
};

#endif
