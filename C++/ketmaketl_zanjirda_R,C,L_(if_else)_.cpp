#include <iostream> 
#include <math.h>
#include<cstdlib>
using namespace std;
int main()
    // R,l,C ELEMENTLARI KETAM KET ULANFAN ZANJURDA UMUMIY QARSHILIK TOK KUCHI YOKI KUCHLANISHNI QIYMANITINI 
    // TOPISH UCHUN MULJALLANGAN DASTUR     Rashidov Javohir 211 , M va R ,
    
{
	float R , XL , XC, I, U ,Z , u, i ; 
 
 
    	cout<< "  R,l,C ELEMENTLARI KETAM KET ULANFAN ZANJURDA UMUMIY QARSHILIK \n TOK KUCHI YOKI KUCHLANISHNI QIYMANITINI \n TOPISH UCHUN MULJALLANGAN DASTUR  " << endl;


		cout<< " \n               Suraladigan  malumotlarni kiritng " << endl ;
		cout<< " \n Aktiv qarshilikni          -> R=" ; cin>> R ; 
		cout<< " Induktivlikdagi qarshilik  -> XL=" ; cin>> XL ; 
		cout<< " Sig'im qarshilik           -> XC=" ; cin>> XC ; 
		cout<< " Kuchlanish (agar bulmasa yani topilishi kk bulsa (U=0)) -> U=" ; cin>> U ; 
		cout<< " Tok kuchi  (agar bulmasa yani topilishi kk bulsa (I=0)) -> I=" ; cin>> I ; 
	
  
		cout << " \n              NATIJALARNI KURISHINGIZ MUMKUN " << endl ; 

	


		if(U==0)
			
			{
				if(XL==XC)
				
					{
				 		cout<<"\n Hozirgi holat rezonans yani XL=XC Z=R \n" ;
				 	}
				 
				Z=sqrt(R*R+(XL-XC)*(XL-XC)) ;        cout<<"\n  Zanjirning umumiy qarshilig -> Z=" << Z << " (OM)" << endl;
			
				u=I*Z ;    cout<<"\n Kuchlanishning qimati -> U=" << u << " (V)" << endl; 
			
			}
		
		
		else
	    
	    	{
	    		if(XL==XC)
				
					{
				 		cout<<"\n Hozirgi holat rezonans yani XL=XC Z=R \n" ;
				 	}
				 	
	    		Z=sqrt(R*R+(XL-XC)*(XL-XC)) ;                cout<<"\n Zanjirning umumiy qarshilig -> Z=" << Z << " (OM)" << endl;
	    	
				i=U/Z ;    cout<<"\n Tok kuchiningning qimati -> I=" << i << " (A)" << endl; 
			}
	    
	
	     //  Rashidov Javohir 211 , M va R ,
	     
		system("pause");
		return 0 ;	
}
