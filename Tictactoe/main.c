#include<stdio.h>
#include<stdbool.h>

char board[9] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
int winning_combinations[][3] = {
    {0, 1, 2},// top Rows
    {3, 4, 5},// middle 
    {6, 7, 8},//bottom
    {0, 3, 6},// left columns
    {1, 4, 7},// middle
    {2, 5, 8},// right 
    {0, 4, 8},// left-right Digonals
    {2, 4, 6} // right-left 
};

void print_board();
bool move(int x , int player);
bool is_winner(int player);
int take_input(int player);

int main(){
    int inp;
    int player;
    print_board();
    for(int i = 1 ; i <= 9 ; i++){
        if (i % 2 != 0){
            player = 1;
            do {
                inp = take_input(1);
            }while(inp < 1 || inp > 9 || board[inp - 1] != ' ');
        }

        else{
            player = 2;
            do {
                inp = take_input(2);
            }while(inp < 1 || inp > 9 || board[inp -1] != ' ');
        }
        
        move(inp , player);
        print_board();

        if (is_winner(1)){
            printf("Player 1 is winner...\n");
            return 1;
        }
        
        if(is_winner(2)){
            printf("Player 2 is winner...\n");
            return 1;
        }
    }

    printf("Match is draw between player 1 and player 2\n");
    return 0;
}


void print_board(){
    for(int i = 1 ; i <= 9 ; i++){
        printf("| %c ",board[i - 1]);
        if (i % 3 == 0){
            printf("|\n\n");
        }
    }
}

bool move(int x , int  player){
    if(player == 1){
        if (board[x -1] == ' '){
            board[x-1] = 'X';
        }
        else{
            return false;
        }
    }
    else{
        if(board[x - 1] == ' '){
            board[x -1] = 'O';
        }
        else{
            return false;
        }
    }
    return true;
}

bool is_winner(int  player){
    char str_player = (player == 1) ? 'X' : 'O';
    for(int i = 0 ; i < 8 ; i++ ){
        int count = 0;
        for(int j = 0 ; j < 3 ; j++){
            if (board[winning_combinations[i][j]] == str_player){
                count++;
            }
        }
        if (count == 3){
            return true;
        }
    }
    return false;
}

int take_input(int player){
    int pos;
    printf("Enter the position player %d: \n",player);
    scanf("%d",&pos);
    return pos;
}