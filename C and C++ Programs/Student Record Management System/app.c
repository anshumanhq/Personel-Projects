#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

struct Student {
    int roll;
    char name[50];
    int marks[3];
    float percentage;
};

struct Student students[MAX];
int count = 0;   // current number of students

void addStudent();
void displayAll();
void searchStudent();
void updateStudent();
void deleteStudent();
void saveToFile();
void loadFromFile();

int main() {
    loadFromFile();
    int choice;
    do {
        printf("\n=== Student Record Management ===\n");
        printf("1. Add Student\n");
        printf("2. View All\n");
        printf("3. Search\n");
        printf("4. Update\n");
        printf("5. Delete\n");
        printf("6. Save & Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        switch(choice) {
            case 1: addStudent(); break;
            case 2: displayAll(); break;
            case 3: searchStudent(); break;
            case 4: updateStudent(); break;
            case 5: deleteStudent(); break;
            case 6: saveToFile(); printf("Exiting...\n"); break;
            default: printf("Invalid choice!\n");
        }
    } while(choice != 6);
    return 0;
}
