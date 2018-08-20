#include <iostream>
using namespace std;
template <int >
int myMax(int x, int y)
{
   return (x*y);
}
 
int main()
{
  cout << myMax(3, 7) << endl;  
  cout << myMax(4.2, 7.7) << endl; 
  return 0;
}
