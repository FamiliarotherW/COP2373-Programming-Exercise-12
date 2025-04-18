import numpy as np

def analyze_exam_grades(filename):
    """
    Loads student grades from a CSV file and analyzes the grades from each exam.

    Args:
        filename (str): The name of the CSV file.
    """
    try:
        # Load data from CSV file
        data = np.genfromtxt(filename, delimiter=',', skip_header=1)
        if data.size == 0:
            print("Error: CSV file is empty or contains no data.")
            return

        # Print the first few rows
        print("First 5 rows of the dataset:")
        if data.ndim > 1:
            print(data[:5, :])  # Print first 5 rows and all columns
        else:
            print(data[:5])

        # Get number of exams and students
        if data.ndim > 1:
            num_students, num_exams = data.shape
            num_exams -= 1  # Adjust for student ID column
        else:
            num_students = data.size
            num_exams = 1

        # Analyze each exam
        print("\n--- Exam Analysis ---")
        for i in range(1, num_exams + 1):
            if data.ndim > 1:
                exam_grades = data[:, i]
            else:
                exam_grades = data
            print(f"\nExam {i}:")
            print(f"  Mean: {np.mean(exam_grades):.2f}")
            print(f"  Median: {np.median(exam_grades):.2f}")
            print(f"  Standard Deviation: {np.std(exam_grades):.2f}")
            print(f"  Minimum: {np.min(exam_grades):.2f}")
            print(f"  Maximum: {np.max(exam_grades):.2f}")

            # Determine the number of students who passed and failed
            passing_students = np.sum(exam_grades >= 60)
            failing_students = np.sum(exam_grades < 60)
            print(f"  Passing Students: {passing_students}")
            print(f"  Failing Students: {failing_students}")

        # Analyze overall dataset
        print("\n--- Overall Analysis ---")
        if data.ndim > 1:
            all_grades = data[:, 1:].flatten()  # Get all grades, excluding student IDs
        else:
            all_grades = data
        print(f"  Mean Grade: {np.mean(all_grades):.2f}")
        print(f"  Median Grade: {np.median(all_grades):.2f}")
        print(f"  Standard Deviation: {np.std(all_grades):.2f}")
        print(f"  Minimum Grade: {np.min(all_grades):.2f}")
        print(f"  Maximum Grade: {np.max(all_grades):.2f}")

        # Calculate and print the overall passing percentage
        overall_passing_grades = np.sum(all_grades >= 60)
        overall_pass_percentage = (overall_passing_grades / len(all_grades)) * 100
        print(f"  Overall Pass Percentage: {overall_pass_percentage:.2f}%")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_file.csv' with the actual name of your CSV filename
    filename = 'your_file.csv'
    analyze_exam_grades(filename)

# Github: https://github.com/FamiliarotherW/COP2373-Programming-Exercise-12 