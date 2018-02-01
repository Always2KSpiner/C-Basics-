#include<iostream>
using namespace std;
class tess
{
int a,b;
public:
tess()
{
a=10;
b=50;
cout<<"CONSTRUCTOR CALLED(DEFAULT)";
}
tess(int s,int q)
{
a=s;
b=q;
cout<<"CONSTRUCTOR CALLED(PARAMETER)";
}
~tess()
{
cout<<"DESTRUCTOR CALLED";
}
};
int main()
{
tess a,b;
tess a();
{
tess b();
{
tess a(10,5);
tess b(6,4);
}
}
return 0;
}

