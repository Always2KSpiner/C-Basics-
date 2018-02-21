//Inheritance
#include<iostream>
using namespace std;
class A
{ 
public:
int c=6;
 int a=2,b=3;

 void display()
  {
   cout<<a<<endl<<b<<endl<<c<<endl;
  }

};
class B : public A
{ 
public:
 int k=10;
int j=1,i=7;
 void kdisplay()
  {
   cout<<k<<endl<<j<<endl<<i<<endl;
  }
};
int main()
{
 B l;
 cout<<l.j<<endl;
 cout<<l.c<<endl;
 l.display();
 l.kdisplay();
  return 0;
} 
