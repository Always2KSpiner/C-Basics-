#include<iostream>
using namespace std;
class consti
{
 public:
int a,b;
consti()
{
a=10;
b=50;
cout<<"CONSTRUCTOR CALLED(DEFAULT)\n";
cout<<a<<endl<<b<<endl;
}
consti(int s,int q)
{
a=s;
b=q;
cout<<"CONSTRUCTOR CALLED(PARAMETER)\n";
cout<<a<<endl<<b<<endl;
}
consti(consti &l)
{
cout<<"CONSTRUCTOR CALLED(COPY)\n";
}
~consti()
{
cout<<"DESTRUCTOR CALLED\n";
}
};
int main()
{
consti a,b;
{
consti a(10,5);
}
{
consti b(a);
}
return 0;
}

