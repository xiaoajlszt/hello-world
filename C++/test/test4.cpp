#include <string.h>
#include <stdio.h>

class CA{
    public:
        virtual void eat(int a = 3)
        {
            printf("CA eat,");
            printf("%d,",a);
        }
//        virtual ~CA(){};
};

class CB:public CA{
    public:
        int a;

        virtual void eat(int a = 4)
        {
            printf("CB eat,");
            printf("%d,",a);
        }

        ~CB()
        {
            printf("Enter!");
        }
};

int main()
{
    CA *a = new CB();
    a->eat();

    delete a;
//CB *b = new CB();//    b->eat();

    return 0;
}
