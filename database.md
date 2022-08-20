A massive re-design for the database 


1. Remove entirely the idea of StudentProfile
2. Add a group permission instead to control the Account Model 
3. For the class section make it as a limit_choices_to 'is_student' : True
4. If possible create a custom manager that would execute a certain function that would set 'is_student' : True when a user is added to the model


Current Database Model 08/20/22 

1. Account - This is the main user model that inherits from the AbstractUser and with the extension of the following fields:
    1.1 is_enrolled - False by default
    1.2 is_student - False by default
    1.3 is_registrar - False by default
    1.4 is_teacher - False by default

2. StudentProfile - This is the StudentProfile where Students are added
    2.1 Section - This would be a reference (FK) to the Class_Section model
    2.2 User - This would be a reference (FK) to the Account model 

3. TeacherProfile - This is the same as StudentProfile but for the other group
    3.1 User - This would be a reference (FK) to the Account model 

4. Subject - This is the model to add subjects
    4.1 subject_name - This is a CharField used to define the name of the subject
    4.2 teacher - This would be a reference (M2M) to the TeacherProfile model

5. SubjectTeacher - This is a through model made possible by the Subject Model and the teaceher field. This model is used to associate a teacher to a subject.
    5.1 teacher - This would be a reference (FK) to the TeacherProfile model
    5.2 subject - This would be a reference (FK) to the Subject model
    5.3 semester - This is a field to determine the semester of the subject
    5.4 students - This would be a reference (M2M) to the StudentProfile model

6. StudentGrade - This is a through model made possible by the SubjectTeacher Model and the Students field
    6.1 subject_teacher - This would be a reference (FK) to the SubjectTeacher Model
    6.2 student - This would be a reference (FK) to the StudentProfile Model
    6.3 grade - An IntegerField to determine the grade for the subject

7. Class_Section - This represents the section that students would belong to
    7.1  section - A CharField to determine and describe the name of the section
    7.1 adviser - This would be a reference (FK) to the TeacherProfile model


===== Issues with the current database model =====
 
1. It is heavily reliant to the addition of the user using Django-Admin app. (Against "django-admin is not your application")
2. Unused links are being done (commonly with the students FK and subject FK)
3. Redundant design with StudentProfile and TeacherProfile 
4. The current model fields are relying on #3 to be functional such as the Class_Section and SubjectTeacher model
=======================END=========================
