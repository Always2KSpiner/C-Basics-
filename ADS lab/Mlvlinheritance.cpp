//Multilevel Inheritance
#include<iostream>
using namespace std;
class A
{
public:
 int i=136;
};
class B : public A
{
public : 
int j=112;
};
class C : public B
{
 public:
  int k=185;
  void display()
   {
    cout<<i<<endl<<j<<endl<<k<<endl;
   }
};
int main()
{
C obj;
obj.display();
return 0;
}
