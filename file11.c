#include <stdio.h>
#include <string.h>


void sort(int num_words,int max_size,char words[][max_size+1]){

    

    for (int i=0;i<num_words-1;i++){
        if(strcmp(words[i+1],words[i])<0){
            char temp[max_size+1];
            strcpy(temp,words[i+1]);
            strcpy(words[i+1],words[i]);
            strcpy(words[i],temp);

        }
    }

    

}


void disp_length(int num_words,int max_size,char words[][max_size+1]){
    int range_1=2,range_2=5,range_3=10;
    int num1=0,num2=0,num3=0,num4=0;
    for(int i=0;i<num_words;i++){
        int word_length=0;
        for(int j=0;j<max_size;j++){
            if(words[i][j]!='\0') word_length++;
            else break;
        }

        if(word_length>range_3) num4++;
        else if(word_length>range_2) num3++;
        else if(word_length>range_1) num2++;
        else num1++;
    }


    printf("Word length Range 1-2 : %d\nWord length Range 3-5 : %d\nWord length Range 6-10 : %d\nWord length Range greater than 10 : %d\n",num1,num2,num3,num4);
    
}


int main(){


    int m,n;

    printf("Enter the Number of words and Maximum length of the word : \n");
    scanf("%d%d",&m,&n);
    char words_list[m][n+1];
    printf("Enter the %d Number of Words separated with space : ",m);
    for(int i=0;i<m;i++){
        char word[n+1];
        scanf("%s",word);
        strcpy(words_list[i],word);
    }
    
    sort(m,n,words_list);



    printf("Sorted Lexographically List : \n");
     for(int i=0;i<m;i++){
       
        printf("%s ",words_list[i]);
       
    }
    printf("\n");

    disp_length(m,n,words_list);

    return 0;
}