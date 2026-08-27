#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100
#define FILENAME "students.dat"

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

// Add a new student
void addStudent() {
    if (count >= MAX) {
        printf("Cannot add more students. Limit reached.\n");
        return;
    }

    struct Student newStudent;
    int i;

    printf("Enter roll number: ");
    scanf("%d", &newStudent.roll);

    // Check for duplicate roll
    for (i = 0; i < count; i++) {
        if (students[i].roll == newStudent.roll) {
            printf("Student with roll %d already exists.\n", newStudent.roll);
            return;
        }
    }

    printf("Enter name: ");
    scanf(" %[^\n]", newStudent.name);  // reads string with spaces

    printf("Enter marks in three subjects: ");
    for (i = 0; i < 3; i++) {
        scanf("%d", &newStudent.marks[i]);
    }

    // Calculate percentage
    int total = 0;
    for (i = 0; i < 3; i++) {
        total += newStudent.marks[i];
    }
    newStudent.percentage = (float)total / 3.0;

    // Add to array
    students[count++] = newStudent;
    printf("Student added successfully.\n");
}

// Display all students
void displayAll() {
    if (count == 0) {
        printf("No student records found.\n");
        return;
    }

    printf("\n--- Student Records ---\n");
    printf("Roll\tName\t\tMarks (1,2,3)\tPercentage\n");
    for (int i = 0; i < count; i++) {
        printf("%d\t%s\t\t%d, %d, %d\t%.2f%%\n",
               students[i].roll,
               students[i].name,
               students[i].marks[0],
               students[i].marks[1],
               students[i].marks[2],
               students[i].percentage);
    }
}

// Search by roll number
void searchStudent() {
    if (count == 0) {
        printf("No student records found.\n");
        return;
    }

    int roll;
    printf("Enter roll number to search: ");
    scanf("%d", &roll);

    for (int i = 0; i < count; i++) {
        if (students[i].roll == roll) {
            printf("\nStudent found:\n");
            printf("Roll: %d\n", students[i].roll);
            printf("Name: %s\n", students[i].name);
            printf("Marks: %d, %d, %d\n", students[i].marks[0], students[i].marks[1], students[i].marks[2]);
            printf("Percentage: %.2f%%\n", students[i].percentage);
            return;
        }
    }
    printf("Student with roll %d not found.\n", roll);
}

// Update student details by roll
void updateStudent() {
    if (count == 0) {
        printf("No student records found.\n");
        return;
    }

    int roll;
    printf("Enter roll number to update: ");
    scanf("%d", &roll);

    for (int i = 0; i < count; i++) {
        if (students[i].roll == roll) {
            printf("Current details:\n");
            printf("Name: %s\n", students[i].name);
            printf("Marks: %d, %d, %d\n", students[i].marks[0], students[i].marks[1], students[i].marks[2]);

            printf("Enter new name: ");
            scanf(" %[^\n]", students[i].name);

            printf("Enter new marks in three subjects: ");
            for (int j = 0; j < 3; j++) {
                scanf("%d", &students[i].marks[j]);
            }

            // Recalculate percentage
            int total = 0;
            for (int j = 0; j < 3; j++) {
                total += students[i].marks[j];
            }
            students[i].percentage = (float)total / 3.0;

            printf("Student record updated successfully.\n");
            return;
        }
    }
    printf("Student with roll %d not found.\n", roll);
}

// Delete student by roll
void deleteStudent() {
    if (count == 0) {
        printf("No student records found.\n");
        return;
    }

    int roll;
    printf("Enter roll number to delete: ");
    scanf("%d", &roll);

    int found = 0;
    for (int i = 0; i < count; i++) {
        if (students[i].roll == roll) {
            found = 1;
            // Shift all elements after i one position left
            for (int j = i; j < count - 1; j++) {
                students[j] = students[j + 1];
            }
            count--;
            printf("Student with roll %d deleted successfully.\n", roll);
            return;
        }
    }
    if (!found) {
        printf("Student with roll %d not found.\n", roll);
    }
}

// Save all records to binary file
void saveToFile() {
    FILE *file = fopen(FILENAME, "wb");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return;
    }

    // Write the count first, then the array of students
    fwrite(&count, sizeof(int), 1, file);
    fwrite(students, sizeof(struct Student), count, file);

    fclose(file);
    printf("Data saved successfully.\n");
}

// Load records from binary file
void loadFromFile() {
    FILE *file = fopen(FILENAME, "rb");
    if (file == NULL) {
        // No existing file, start fresh
        return;
    }

    // Read the count
    fread(&count, sizeof(int), 1, file);
    // Read the students
    fread(students, sizeof(struct Student), count, file);

    fclose(file);
    printf("Data loaded successfully. %d records found.\n", count);
}
