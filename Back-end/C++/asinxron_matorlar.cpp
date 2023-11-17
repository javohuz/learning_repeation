#include <iostream> 
#include <math.h>
#include<cstdlib>
using namespace std;
int main()
    // acinxron matorlar
    
{
	float Pn, Un, Sn, FIKn, cosfn, p, L , M , I , n0 ; 
	float P1n , Mn , Mmax, In , Iyu, Skr   ;
 
    	cout<< " Uch fazali kisqa tutashtirilgan asinxron mortor buyicha " << endl;
		cout<< " masalarni ishlash uchun mo'ljallanga dastur " << endl ; 
  cout << "   " << endl ; 
		cout<< "                Suraladigan  malumotlarni kiritng " << endl ;
  cout << "   " << endl ; 
		cout<< " Nominal quvvat       ->  Pn=" ; cin>> Pn ; 
		cout<< " Nominal kuchlanish   ->  Un=" ; cin>> Un ; 
		cout<< " Nominal sirpanish(%) -> Sn=" ; cin>> Sn ; 
		cout<< " Nominal foydali ish koyefsenti -> FIKn=" ; cin>> FIKn ; 
		cout<< " Nominal Quvvat koyefsenti   -> cosf=" ; cin>> cosfn ; 
		cout<< " Juft qutublar soni          -> p=" ; cin>> p ; 
		cout<< " O'ta yuklanish qobliyati    -> Mmax/Mn=" ; cin>> L ; 
		cout<< " Yurgizish momentini nominal momentga nisbati -> Myu/Mn=" ; cin>> M ; 
		cout<< " Yurgizish tokining nominal tokga nisbati   -> Iyu/In=" ; cin>> I ; 
		cout<< " Nominal aynalish chastotasi             ->   n0=" ; cin>> n0 ; 
  cout << "   " << endl ; 
  
		cout << "               NATIJALARNI KURISHINGIZ MUMKUN " << endl ; 
  cout << "   " << endl ; 
	
		P1n=Pn/FIKn ;                cout<<" Mator talab qiladigan quvvat ->  P1n=" << P1n << " (kBm)" << endl;  
  cout << "   " << endl ; 
			
	   	Mn=9550*(Pn/(n0*(1-Sn/100))) ;   cout<<" Matorning nominal qiymati    ->  Mn=" << Mn <<  " (Hm)" << endl ;
  cout << "   " << endl ; 		
 
		Mmax=Mn*L ;                  cout<<" Matorning maksimal qiymati   ->  Mmax=" << Mmax <<  " (Hm)" << endl ;
  cout << "   " << endl ; 	
	
	    In=P1n*1000/(1.73*Un*cosfn) ;     cout<<" Nominal tokning qiymati      ->  In=" << In <<  " (A)" << endl; 
  cout << "   " << endl ; 
  
  		Iyu=In*I ;                   cout <<" Yurgizish tokning qiymati    ->  Iyu=" << Iyu <<  " (A)" << endl;	    
  cout << "   " << endl ; 	  
   
   		Skr=Sn*(L+sqrt(L*L-1))/100;  	  cout <<" Kritik sirpanishning qiymati ->  Skr=" << Skr << " ()" <<endl;
  cout << "   " << endl ; 	    
	    
	    
	    
	     // RASHIDOV JAVOHIR 211 , M va R ,
	     
		system("pause");
		return 0 ;	
}
