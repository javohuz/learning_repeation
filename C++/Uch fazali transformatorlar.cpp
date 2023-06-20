#include <iostream> 
#include <math.h>
#include <cstdlib>
using namespace std;
int main()
    // UCH FAZALI TRANSFORMATORLAR BUYICHA MASALA 
    
{
	float Sn, U1n, U20, Uk, Pk, P0, i0 ; // bergan kattaliklar 
	float Uf, k, I1n, I10, cosf0, B, zk, rk, xk, r1, x1, r0, r2, x2, x0 , z0 , cosfk , sinfk ; // hisoblanadigan kattaliklar
 
    	cout<< " UCH FAZALI TRANSFORMATORLAR  " << endl;
		cout<< " masalarni ishlash uchun mo'ljallanga dastur " << endl ; 
  cout << "   " << endl ; 
		cout<< "                Suraladigan  malumotlarni kiritng " << endl ;
  cout << "   " << endl ; 
		cout<< "  Uch fazali trans..ning quvvati    (kBa)    ->  Sn=" ; cin>> Sn ; 
		cout<< " Birlamchi chulg'amning nominal kuchlanish   ->  U1n=" ; cin>> U1n ; 
		cout<< " Salt ishlashda ikkilamchai kuchlanishi      ->  U20=" ; cin>> U20 ; 
		cout<< " Qisqa tutashish kuchlanishi (%) da          ->  Uk=" ; cin>> Uk ; 
		cout<< " Qisqa tutashgandagi quvvati  -> Pk=" ; cin>> Pk ; 
		cout<< " Salt ishlashdagi quvvat      -> P0=" ; cin>> P0 ; 
		cout<< " Salt islash toki   (%) da    -> i0=" ; cin>> i0 ; 


  cout << "   " << endl ; 
  
		cout << "               NATIJALARNI KURISHINGIZ MUMKUN " << endl ;   	         
  cout << "   " << endl ; 
	
		Uf=U1n/1.73 ;                     cout<<" Faza kuchlanishi  ->  Uf=" << Uf << " (B)" << endl;  

			
	   	k=U1n/(1.73*U20) ;  			  cout<<"  Transformatsiya koyeffisenti   ->  k=" << k <<  " ()" << endl ;
  cout << "   " << endl ; 		
 
		I1n=Sn*1000/(1.73*U1n)  ;             cout<<" Birlamchi cho'lga'am nominla toki  ->  I1n=" << I1n <<  " (A)" << endl ;
  cout << "   " << endl ; 	
	
	    I10=i0*I1n/100 ;    		   	 cout<<" Salt ishlash toki       ->  I10=" << I10 <<  " (A)" << endl; 
  cout << "   " << endl ;  
  
  		cosf0=P0/(1.73*U1n*I10) ;         cout <<" Salt ishlashda quvvat koyeffisenti ->  cosf0=" << cosf0 <<  " ()" << endl;	    
 	            cout <<" Magnit isrofi burchagi  B=90-arc(cosf0)  formula orqali hisoblang" <<endl;    	
  				cout <<" dasturda arc(cosf0)ni ishlashning imkoni mavjud emas" <<endl;
  				
  cout << "   " << endl ; 	    
	    
	 	cout << "               Chulg'amlarning qarshiligi  " << endl ;   	         
  cout << "   " << endl ; 
  
     zk=Uk*U1n/(173*I1n);  	      cout <<"  ->  zk=" << zk << " (OM)" <<endl;
  cout << "   " << endl ; 
  
    	rk=Pk/(3*I1n*I1n);  	       cout <<"  ->  rk=" << rk << " (OM)" <<endl;
  cout << "   " << endl ; 
  
  		xk=sqrt(zk*zk-rk*rk);  	    cout <<"  ->  xk=" << xk << " (OM)" <<endl;
  cout << "   " << endl ; 
  
      	cosfk=rk/zk ;  	    cout <<"  ->  cosfk=" << cosfk << " ()" <<endl;
  cout << "   " << endl ; 
  
        sinfk=sqrt(1-cosfk*cosfk) ; 	    cout <<"  ->  sinfk=" << sinfk << " ()" <<endl;
  cout << "   " << endl ; 
  
  cout << "    Birlamchi va ikkilamchi chulg'amlarning keltirilgan qarshiliklari  " << endl ;   	         
  cout << "   " << endl ; 
  
     	r1=rk/2;  	 				 cout <<"  ->  r1=" << r1 << " (OM)" <<endl;
  cout << "   " << endl ; 
  
    	x1=xk/2;  					  cout <<"  ->  x1=" << x1 << " (OM)" <<endl;
  cout << "   " << endl ; 
  
    	r2=r1/(k*k);  				  cout <<"  ->  r2=" << r2 << " (OM)" <<endl;
  cout << "   " << endl ; 
  
    	x2=x1/(k*k);  	 			 cout <<"  ->  x2=" << x2 << " (OM)" <<endl;
  cout << "   " << endl ; 
  
    cout << "    Magnitlovchi tarmoq qarshiliklari , salt ishlash parametrlari  " << endl ;   	         
  cout << "   " << endl ;
  
      	z0=U1n/(1.73*I10);  	  cout <<"  ->  z0=" << z0 << " (OM)" <<endl;
  cout << "   " << endl ; 
  
        r0=P0/(3*I10*I10);  	  cout <<"  ->  r0=" << r0 << " (OM)" <<endl;
  cout << "   " << endl ;
   
    	x0=sqrt(z0*z0-r0*r0);  	  cout <<" ->  x0=" << x0 << " (OM)" <<endl;
  cout << "   " << endl ; 

   cout << "   Transformatorni tashqi haraktiri yani U2=f(beta) qurish uchun ikkilamchi    " << endl ; 
   cout << "   chulgam kuchlanishini kamaytrish uchun aniqlash kerak   " << endl ;   	         
   cout << "   " << endl ;
  	    
	    float Uka , Ukp , beta1=0.1 , beta2=0.2, beta3=0.4, beta4=0.6 ,beta5=0.8, beta6=1 , dU2  , cosf2=0.75 , sinf2=0.66 ;
	    
	    
		Uka=Uk*cosfk ;  	  cout <<"  ->  Uka=" << Uka << " (%)" <<endl;
  cout << "   " << endl ; 
  
  		Ukp=Uk*sinfk ;  	  cout <<"  ->  Ukp=" << Ukp << " (%)" <<endl;
  cout << "   " << endl ; 
	    
	    dU2=beta1*(Uka*cosf2+Ukp*sinf2) ;  	  cout <<" Beta =0,1 bulganda  ->  dU2=" << dU2 << " (%)" <<endl;
  cout << "   " << endl ; 
  
  	    dU2=beta2*(Uka*cosf2+Ukp*sinf2) ;  	  cout <<" Beta =0,2 bulganda  ->  dU2=" << dU2 << " (%)" <<endl;
  cout << "   " << endl ; 		
  
  	    dU2=beta3*(Uka*cosf2+Ukp*sinf2) ;  	  cout <<" Beta =0,4 bulganda  ->  dU2=" << dU2 << " (%)" <<endl;
  cout << "   " << endl ; 
  
  	    dU2=beta4*(Uka*cosf2+Ukp*sinf2) ;  	  cout <<" Beta =0,6 bulganda  ->  dU2=" << dU2 << " (%)" <<endl;
  cout << "   " << endl ; 
  
  	    dU2=beta5*(Uka*cosf2+Ukp*sinf2) ;  	  cout <<" Beta =0,8 bulganda  ->  dU2=" << dU2 << " (%)" <<endl;
  cout << "   " << endl ; 
  
    	dU2=beta6*(Uka*cosf2+Ukp*sinf2) ;  	  cout <<" Beta =1.0 bulganda  ->  dU2=" << dU2 << " (%)" <<endl;
  cout << "   " << endl ; 
        
	    
	     // RASHIDOV JAVOHIR 211 , M va R ,
	     
		system("pause");
		return 0 ;	
}
