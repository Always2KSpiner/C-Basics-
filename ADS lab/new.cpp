#include<iostream>
using namespace std;
class teacher;
class student
{
int rn=8;
int sap=7;
friend int show(student x,teacher y);
};
class teacher
{
int id=2;
int code=1;
friend int show(student x,teacher y);
};
int show(student x,teacher y)
{
cout<<"roll no. :"<<x.rn;
cout<<"SAP ID :"<<x.sap;
cout<<"Teacher ID :"<<y.id;
cout<<"Teacher code :"<<y.code;
return 0;
}
int main()
{
student a;
teacher b;
show(a,b);
return 0;
}
