from student import Student

if __name__ == "__main__":
    s = Student(
        name="Lahiru Weerasingha",
        person_id="199831400505",
        email="COMScDS252P-014@student.nibm.lk",
        phone="0712345678",
        student_id="COMScDS252P-014",
        major="MSc Data Science",
        enrollment_date="2026-02-23",
    )

    # Enroll courses
    s.enroll_course("CS101")
    s.enroll_course("DS102")

    # Add grades
    s.add_grade("CS101", 3.8)
    s.add_grade("DS102", 3.6)

    print(s.get_info())