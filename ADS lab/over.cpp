#include<iostream>
using namespace std;
int sum(int f,int s)
{
cout<<f+s<<endl;
}
int sum(double f,double g)
{
cout<<f+g<<endl;
}
int main()
{
sum(4,6);
sum(2.9,2.8);
return 0;
}
