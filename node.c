#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int key;
    struct node *prev_hash;

} node;


node *head=NULL;

node* search(node* const head,int key){

    node *head_func=head;


while (1){
    if (key!=head_func->key) head_func=head_func->prev_hash;
    else {

        int counter=0;
        node *head_func_2=head;
        while(1){
            counter=counter+1;


            if (head_func_2->prev_hash==NULL) break;

            else head_func_2=head_func_2->prev_hash;
               
                }

            // printf("Counter : %d \n",counter);
       
        head_func_2=head;

        while(1){
            
            counter-=1;

            if (head_func_2->prev_hash==head_func) break;

            
            head_func_2=head_func_2->prev_hash;
            
                

        }

        

        printf(" Value : %d\nBlock No. %d\n",key,counter);

        return head_func;

    }



}
    
}



void insert_at_begin(int new_key){

node *head_func=head;
node *temp=(node*) malloc(sizeof(node));

temp->key=new_key;

temp->prev_hash=NULL;

while (1){
    if(head_func->prev_hash==NULL) {head_func->prev_hash=temp;
    break;
    }
    else head_func=head_func->prev_hash;
}



}

void delete_node(int key){
    node *head_func=head;
    node *ptr=search(head,key);
    
    if (head_func->key==key){
       
        head=head->prev_hash;
        free(head_func);
        return ;
    }
    while(1){
      
        if(head_func->prev_hash->key==key) {
             
        head_func->prev_hash=head_func->prev_hash->prev_hash;
        
        break;
        }
        else {
        head_func=head_func->prev_hash;
        
        }
    }

    free(ptr);

}



void insert_at_end(int key){
    node *temp=(node*) malloc(sizeof(node));
    temp->key=key;
    temp->prev_hash=head;
    head=temp;
}





void insert_after(int new_key,int after_value,node* const head){

    node *head_func=head;
    node *temp=(node*) malloc(sizeof(node));
 

    temp->prev_hash=search(head,after_value);
    temp->key=new_key;


    while(1){
        if(head_func->prev_hash->key==after_value) {head_func->prev_hash=temp;
        break;
        }
        else head_func=head_func->prev_hash;
    }



}



int main(void){


int keys[10];

for(int i=0;i<10;i++) *(keys+i)=i+1;

for(int i=0;i<10;i++){

node *temp=(node*) malloc(sizeof(node));

temp->key=keys[i];
temp->prev_hash=head;
head=temp;

}


// Head is the last node of the link list

printf("%d \n",head->key);
printf("Address of head : %p \n",head->prev_hash);
printf("%d\n",(head->prev_hash)->key);
printf("%d\n",(head->prev_hash)->prev_hash->key);

// In search function we need to provide head and the key value the node holds in the link list as parameters and return the address of the node containing the value

printf("%d \n",search(head,5)->key);
// This search function also prints the block number of the node


// Here 11 is the new value that has to be added after value 8 in link list

insert_after(11,8,head);

// This will add 11 after 8 in link list and this can be checked

printf("%d\n",(head->prev_hash)->key);//9
printf("Placed after 8 : %d\n",(head->prev_hash)->prev_hash->key); //11 placed after 8

insert_at_end(12);

// This will add node will key as 12 at the end of the link list

printf("%d \n",head->key);//12

// As head represents the last block of the node and from here it can be verified


printf("%d\n",(head->prev_hash)->key);//10

insert_at_begin(0);

// This will add 0 at the begining of the link list



delete_node(10);

// This will delete the node with value 10



insert_at_end(13);

// This will add a node at the end of the link list with key 13

printf("%d \n",head->prev_hash->key);
printf("%d \n",head->prev_hash->prev_hash->key);
printf("%d \n",head->prev_hash->prev_hash->prev_hash->prev_hash->key);



// Checking all the nodes

printf("Checking the nodes\n");

node* func_tr=head;
int num_blocks=0;

while (1){

    printf("Value : %d      \n",func_tr->key);
    num_blocks+=1;
    if (func_tr->prev_hash==NULL) {
        printf("The Number of Blocks is %d",num_blocks);
        break;
        }
    else {
        
        func_tr=func_tr->prev_hash;
    }



}



return 0;
}