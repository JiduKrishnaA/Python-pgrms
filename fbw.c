#include<stdio.h>
#include<stdlib.h>

int i;
void input(int *nb,int block[100],int *np,int process[100],int allocation[100])
{
printf("Enter the no of blocks : ");
scanf("%i",nb);
for(int i=0;i<*nb;i++){
printf("Enter size of block %i : ",i+1);
scanf("%i",&block[i]);
}
printf("Enter the no of process : ");
scanf("%i",np);
for(int i=0;i<*np;i++){
printf("Memory for process %i : ",i+1);
scanf("%i",&process[i]);
}
for(int i=0;i<*np;i++){
allocation [i]=-1;
}
}



void display(int np,int process[100],int allocation[100])
{
printf("Process id\tProcess size\tBlock no\n");
for(int i=0;i<np;i++){
printf("%d\t\t%d\t\t",i+1,process[i]);
if(allocation [i]==-1){
printf("Not Allocated \n");
}
else
{
printf("%i\n",allocation[i]+1);
}
}
}



void first(){
int nb,np,block[100],process[100],allocation[100];
input(&nb,block,&np,process,allocation);
for(int i=0;i<np;i++){
for(int j=0;j<nb;j++){
if(block[j]>=process[i]){
allocation[i]=j;
block[j]-=process[i];
printf("Process %i allocated in block %i\n",i+1,j+1);
break;
}
}
}
display(np,process,allocation);
}

void best(){
int nb,np,block[100],process[100],allocation[100];
input(&nb,block,&np,process,allocation);
for(int i=0;i<np;i++){
int min=1000;
int index=-1;
for(int j=0;j<nb;j++){
if(block[j]>=process[i]&&block[j]<min){
min=block[j];
index=j;
}
}
if(index!=-1){
allocation[i]=index;
block[index]-=process[i];
printf("Process %i allocated in block %i\n",i+1,index+1);
}
}
display(np,process,allocation);
}

void worst(){
int nb,np,block[100],process[100],allocation[100];
input(&nb,block,&np,process,allocation);
for(int i=0;i<np;i++){
int max=-1;
int index=-1;
for(int j=0;j<nb;j++){
if(block[j]>=process[i]&&block[j]>max){
max=block[j];
index=j;
}
}
if(index!=-1){
allocation[i]=index;
block[index]-=process[i];
printf("Process %i allocated in block %i\n",i+1,index+1);
}
}
display(np,process,allocation);
}






 int main(){
 printf("\n MENU\n1.First fit\n2.Best fit\n3.Worst fit\n4.Exit\n");
int ch;
do{
printf("\nEnter choice : ");
scanf("%i",&ch);
switch(ch){
case 1 :
first();

break;

case 2 :
best();
break;

case 3 :
worst();
break;


case 4 :
break;

default :
printf("wrong choice try again");
}
}while(ch!=4);

}
