//#include <stdio.h>
//#include <stdbool.h>

/*int main(){

    //int y = 321;

    //int age = 21;
    //double scale = 3.60000000000000000;
    //char grade = 'C';
    //char name[] = "Bro"; //series of characters
    //printf("%0.15lf\n", scale); - Long Float, retains more values with precision
    //bool e = true;  //Include stdbool.h for it to run
    //printf("%d\n", e);
    //char f = 120;
    //printf("%c\n", f);

    //float item1 = 5.00;
    //float item2 = 7.50;
    //float item3 = 10.00;
    
    // format specifier % = defines and formats a type of data to be displayed
    //printf("Item 1 Costs $%.2f\n", item1); //.2 after % indicates how # of place holders
    //printf("Item 2 costs $%8.2f\n", item2); //The 8 goes and places spaces before presentting
    //printf("Item 3 costs $%.2f\n", item3);

    //constant = fixed value that cannot be changed in any process during program execution
    //const float PI = 3.14159;
    //pi = 1231.2312; //Is not represented in the final code and runs error
    //printf("%f", PI);

    //int x = 4;
    //int y = 7;
    //float z= x / (double) y; //by preceeding with denotion, it helps with adding more decimal holders
    //int z = x % y;
    //printf("%d", z);


    // augmented assinment operators = Changes statements from assigned values and plugging them back in for a new statement
    //int x = 10;
    //x%=2;
    //printf("%d", x);



        return 0;
} */

//#include <stdio.h>
//#include <string.h>

/*int main(){

    char name[25]; //bytes
    int age;
    
    printf("\nWhat's your name?");
    fgets(name,  25, stdin); //Goes and allows for first and last name up to 25 char.
    //scanf("%s", &name); //Only includes characters and not white spaces(spaces between characters)
    name[strlen(name)-1] = '\0';  //Advanced for now, but joins second question correctly formatted
    
    printf("\nHow old are you?");
    scanf("%d", &age);  // & places the address of the operator, scanf reads and outputs from stdin(keyboard)
    
    printf("\nHello %s, how are you?", name);
    printf("\nYou are %d years old", age);
    
    return 0; //All of this is done in terminal using user interface

}*/

/*#include <stdio.h>
#include <math.h> //must be included to be able to access far more eg. floor, pow, round, ceil...)

int main(){

double A = sqrt(9);

printf("\n%lf", A);

    return 0;
}*/

#include <stdio.h>

int main(){

const double PI = 3.14159;
double radius;
double circumference;
double area;

printf("\nEnter radius of a circle: ");
scanf("%lf", &radius);

circumference = 2 * PI * radius;
area = PI * radius * radius;

printf("Circumference: %lf", circumference);
printf("\nArea: %lf", area);

    return 0;
}


#include <stdio.h>

int main(){






    return 0;
}

