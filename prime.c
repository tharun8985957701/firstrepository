/* #include<stdio.h>
int main(){
    int i,n,count=0;
    printf("enter any number: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        if(n%i==0){
            count=count+1 ;
        }
    }
    if(count==2)
        printf("the given number is prime");
    else 
        printf("given number is not prime");

//n/2
//(n)^1/2
//for composite number.the factor is prime is bw 1 to (n)^1/2
//there will be my phone number in any irrational number
}

#include<stdio.h>
int main(){
    int n,i,j,k,p,count,prime[50];
    printf("enter any number: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        count=0 ;
        for(j=1;j<=i;j++){
            if(i % j==0){
               count++ ;
        }
        } 
            if(count==2){
                //for(p=0;p<4;p++){
                 //   prime[p]=i ;
                //}
                printf("%d\n",i);
            }
       }
       //printf("the elements in the array are: ");
       //for(i=0;i<4;i++)
       //    printf("%d",prime[i]);
    }
 
*/

#include<stdio.h>
int main(){
    int prime[50],n,i,j,p,k=0,l=1,count;
    printf("enter number for getting prime numbers upto that: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        count=0 ;
        for(j=1;j<=i;j++){
           if(i % j==0){
              count++ ; 
           }  
        }
        if(count==2){
           prime[k]=i ;
           k++ ;
           l++ ;
        } 
}
for(i=0;i<l;i++){
    printf("%d ",prime[i]) ;
}
}
    
