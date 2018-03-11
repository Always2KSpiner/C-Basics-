#include <iostream>
using namespace std;
 
// One function works for all data types.  This would work
// even for user defined types if operator '>' is overloaded
template <class T>
T myMax(T x, T y)
{
   return (x > y)? x: y;
}
 
int main()
{
  cout << myMax(3, 7) << endl;  // Call myMax for int
  cout << myMax(3.0, 7.0) << endl; // call myMax for double
  cout << myMax('g', 'e') << endl;   // call myMax for char
 
  return 0;
}
