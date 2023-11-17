#include <iostream>
#include <math.h>
using namespace std; 
int main()
{

	float R1 , R2 , R3 , E1 , E2 ;
	float I11 , U1ab , I12 , I13 , I22 , U2ab , I21 , I23 , I1 , I2 , I3 ;

cout<<" \n R qarhsilik va EYUK E ning \t qiymatini kiriting" << endl;

	cout<< "R1=";   cin>> R1; 
	cout<< "R2=";   cin>> R2; 
	cout<< "R3=";   cin>> R3; 
	cout<< "E1=";   cin>> E1; 
	cout<< "E2=";   cin>> E2; 

I11=E1/(R1+(R2*R3)/(R2+R3)) ;	U1ab=I11*((R2*R3)/(R2+R3));

I12=U1ab/R2;		I13=U1ab/R3;

I22=E2/(R2+(R1*R3)/(R1+R3));	U2ab=I22*((R1*R3)/(R1+R3));

I21=U2ab/R1;	I23=U2ab/R3;

I1=fabs(I11-I21);		cout<< "I1=" << I1 << " (A)"  <<endl ;

I2=fabs(I12-I22); 		cout<< "I2=" << I2 << " (A)" <<endl;

I3=fabs(I13+I23);		cout<< "I3=" << I3 << " (A)" <<endl;

return 0;
}

// RASHIDOV JAVOHIR



