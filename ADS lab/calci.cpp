#include<iostream>
using namespace std;
int main()
{
int a,b;
cout<<"Enter no.\n";
cin>>a;
cout<<"Enter no.\n";
cin>>b;
int c;
cout<<"Enter option\n";
cin>>c;
switch(c)
{
case 1: cout<<"SUM\n"<<a+b<<endl;
         break;
case 2: cout<<"DIFFERENCE\n"<<a-b<<endl;
         break;
case 3:cout<<"PRODUCT\n"<<a*b<<endl;
         break;
case 4:cout<<"DIVISION\n"<<a/b<<endl;
         break;
 default:cout<<"Enter valid choice \n";
}
return 0;
}
