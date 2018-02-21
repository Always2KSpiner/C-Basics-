//Multiple Inheritance
#include<iostream>
using namespace std;
class A
{
public:
 int i=5;
};
class B
{
public :
int j=10;
};
class C : public A,public B
{
 public:
  int k=15;
  void display()
   {
    cout<<i<<endl<<j<<endl<<k<<endl;
   }
};
int main()
{
C l;
l.display();
return 0;
}
