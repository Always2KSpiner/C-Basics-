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
cout<<"HAHAHA!!!\n";
}
tess(int s,int q)
{
a=s;
b=q;
cout<<"BAAM BAAM!!!\n";
}
tess(int s,int q)
{
a=s;
b=q;
cout<<"BAAM BAAM!!!\n";
}
~tess()
{
cout<<"BOOOOM!!!!!!!\n";
}
};
int main()
{
tess a,b;
a=tess();
{
b=tess();
{
a=tess(10,5);
b=tess(6,4);
}
}
cout<<"FIREWORKS ARE OVER\n";
return 0;
}

