#include <iostream>
using namespace std;
template <class T>
T myMax(T x, T y)
{
   return (x*y);
}
 
int main()
{
  cout << myMax(3, 7) << endl;  
  cout << myMax(4.2, 7.7) << endl; 
  return 0;
}
