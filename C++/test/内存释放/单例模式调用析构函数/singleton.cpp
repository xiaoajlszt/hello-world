#include "singleton.h"
#include <iostream>
using namespace std;

SingletonA* SingletonA::_instance = 0;
SingletonA::CGarbo SingletonA::Garbo;

SingletonA::SingletonA()
{
    cout << "Enter SingletonA construction" <<endl;
}

SingletonA::~SingletonA()
{
    cout << "Enter SingletonA distruction" <<endl;
}

SingletonA* SingletonA::Instance()
{
    if(0 == _instance)
    {
        _instance = new SingletonA();
    }

    return _instance;
}

int main()
{
    SingletonA *sgn = SingletonA::Instance();
    return 0;
}
