#include <vector>
#include <memory>
using namespace std;

class A
{
private:
    int a;
    int b;

public:
    A() = default;
    ~A() = default;

    int show_a() {return a;}

};

class B
{
public:
    vector<A*> m_a;
public:
    B() = default;
    ~B() = default;
    size_t size() {return m_a.size();}
    void AddA(A *a) {m_a.push_back(a);};
};
