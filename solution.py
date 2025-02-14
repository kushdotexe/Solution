import pymysql

def validate_marks(marks, min_val, max_val):

    try:
        marks = float(marks)
        if min_val <= marks <= max_val:
            return marks
        else:
            print(f"Error: Marks must be between {min_val} and {max_val}.")
            return None
    except ValueError:
        print("Error: Invalid marks. Please enter a numeric value.")
        return None

def get_valid_input(prompt, min_val, max_val):

    while True:
        value = input(prompt)
        result = validate_marks(value, min_val, max_val)
        if result is not None:
            return result

def main():

    while True:
        try:
            n = int(input("How many candidates do you want to enter? "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Error: Please enter a valid number.")

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Kush123@',
        database='employeedb'
    )
    cursor = conn.cursor()

    for i in range(n):
        print(f"\nEntry {i+1}")
        student_name = input("Enter Student Name (Max 30 chars): ")[:30]
        college_name = input("Enter College Name (Max 50 chars): ")[:50]
        
        r1 = get_valid_input("Enter Round 1 Marks (0-10): ", 0, 10)
        r2 = get_valid_input("Enter Round 2 Marks (0-10): ", 0, 10)
        r3 = get_valid_input("Enter Round 3 Marks (0-10): ", 0, 10)
        tech = get_valid_input("Enter Technical Round Marks (0-20): ", 0, 20)

        cursor.execute(
            '''INSERT INTO CANDIDATES1 
            (StudentName, CollegeName, Round1Marks, Round2Marks, Round3Marks, TechnicalRoundMarks) 
            VALUES (%s, %s, %s, %s, %s, %s)''',
            (student_name, college_name, r1, r2, r3, tech)
        )
        conn.commit()

    cursor.execute("SET @rank := 0;")
    cursor.execute(
        "UPDATE CANDIDATES1 SET RankOfStudents = (@rank := @rank + 1) ORDER BY TotalMarks DESC"
    )
    conn.commit()

    print("\nCandidates sorted by rank:")
    cursor.execute("SELECT * FROM CANDIDATES1 ORDER BY RankOfStudents ASC")
    records = cursor.fetchall()
    for record in records:
        print(record)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()