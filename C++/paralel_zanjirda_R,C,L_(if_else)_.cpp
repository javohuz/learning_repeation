#include <iostream> 
#include <math.h>
#include<cstdlib>
using namespace std;
int main()
    // R,l,C ELEMENTLARI PARALEL ULANGAN ZANJURDA UMUMIY QARSHILIK TOK KUCHI YOKI KUCHLANISHNI QIYMANITINI 
    // TOPISH UCHUN MULJALLANGAN DASTUR  
{
	float R , XL , XC, I, U ,Z , u, i, r, l, c , Y; 
 
 
    	cout<< "  R,l,C ELEMENTLARI PARALEL ULANFAN ZANJURDA UMUMIY QARSHILIK \n TOK KUCHI YOKI KUCHLANISHNI QIYMANITINI \n TOPISH UCHUN MULJALLANGAN DASTUR  " << endl;


		cout<< " \n               Suraladigan  malumotlarni kiritng " << endl ;
		cout<< " \n Aktiv qarshilikni          -> R=" ; cin>> r ; 
		cout<< " Induktivlikdagi qarshilik  -> XL=" ; cin>> l ; 
		cout<< " Sig'im qarshilik           -> XC=" ; cin>> c ; 
		cout<< " Kuchlanish (agar bulmasa yani topilishi kk bulsa (U=0)) -> U=" ; cin>> U ; 
		cout<< " Tok kuchi  (agar bulmasa yani topilishi kk bulsa (I=0)) -> I=" ; cin>> I ; 
	
  
		cout << " \n              NATIJALARNI KURISHINGIZ MUMKUN " << endl ; 

	R=1/r; XL=1/l; XC=1/c;


		if(U==0)
			
			{
				if(XL==XC)
				
					{
				 		cout<<"\n  Hozirgi holat rezonans yani bl=bc Y=b \n" ;
				 	}
				 
				Y=sqrt(R*R+(XL-XC)*(XL-XC)) ; Z=1/Y;       cout<<"\n  Zanjirning umumiy qarshilig -> Z=" << Z << " (OM)" << endl;
														   cout<<"\n  Zanjirning umumiy utkazuvchanligi -> Y=" << Y << " (sim)" << endl;
				u=I*Z ;    cout<<"\n  Kuchlanishning qimati -> U=" << u << " (V)\n" << endl; 
			
			}
		
		
		else if (I==0)
	    
	    	{
	    		if(XL==XC)
				
					{
				 		cout<<"\n  Hozirgi holat rezonans yani bl=bc Y=b  \n" ;
				 	}
				 	
	    		Y=sqrt(R*R+(XL-XC)*(XL-XC)) ; Z=1/Y;       cout<<"\n  Zanjirning umumiy qarshilig -> Z=" << Z << " (OM)" << endl;
														   cout<<"\n  Zanjirning umumiy utkazuvchanligi -> Y=" << Y << " (sim) " << endl;
	    	
				i=U/Z ;    cout<<"\n  Tok kuchiningning qimati -> I=" << i << " (A)\n" << endl; 
			}
	    
		else 
		
			{
				
				cout<<"   Xato Malumotlar kiritildi tekshirib boshidan kiritnig  \n   kuchlanish yoki tok kuchi lardan biri aniqlanishi kerak (U=0 or I=0)\n " ;
				
			}
	     //  JAVOHIR RASHIDOV 211 , M va R ,
	     
		system("pause");
		return 0 ;	
}
