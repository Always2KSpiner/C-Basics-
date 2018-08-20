#include<iostream>
#include<fstream>
using namespace std;
class student
{
   int roll;
   char name[30];
   float marks;
public:
   void getData();
   void displayData();
};
 
void student :: getData() {
   cout << "\nEnter Roll No.- ";
   cin >> roll; 
   cin.ignore();
   cout << "\nEnter Name -";
   cin.getline(name, 30);
   cout << "\nEnter Marks- ";
   cin >> marks;
}
 
void student :: displayData() {
   cout << "\nRoll No. :: " << roll << endl;
   cout << "\nName :: " << name << endl;
   cout << "\nMarks :: " << marks << endl;
}
 
int main()
{
   student s[10]; 
   fstream file;
   int i;
 
   file.open("C:\\Users\\acer\\Documents\\file4.txt", ios :: out);
    cout << "\nWriting Student information to the file :- " << endl;
    cout << "\nEnter 10 students Details to the File :- " << endl;
 
   for (i = 0; i < 10; i++)
    {
      s[i].getData();
      file.write((char *)&s[i], sizeof(s[i]));
    }
 
   file.close(); 
 
   file.open("C:\\Users\\acer\\Documents\\file4.txt", ios :: in); 
   cout << "\nReading Student information to the file :- " << endl;
 
   for (i = 0; i < 10; i++)
    {
      file.read((char *)&s[i], sizeof(s[i]));
      s[i].displayData();
    }
 
   file.close(); 
 
   return 0;
}
