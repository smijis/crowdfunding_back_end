# crowdfunding_back_end
A repo to contain my She Codes Crowdfunding back end project

# Crowdfunding Back End
Selina Shin

## Planning:
### Concept/Name
Fund-ED is an interactive online fundraising and learning platform designed to bring commerce and business studies to life for high school students. Students innovate their own business ideas and pitch them on the platform, while peers use virtual money to fund the ideas they believe in most. Classes can compete internally or enter termly and yearly national competitions with real prizes, creating an engaging, gamified learning experience. Aligned with the NSW Department of Education syllabus and HSC Commerce and Business Studies curriculum, Fund-ED builds foundational knowledge across consumer, financial, economic, and business topics, while developing essential research, problem-solving, and decision-making skills. Teachers can also reward positive behaviour and strong efforts in the classroom, or assessment results by allocating additional virtual funds, reinforcing responsible citizenship, personal finance, and real-world business thinking in a meaningful and motivating way.

### Intended Audience/User Stories
Fund-ED is designed for high school Commerce and Business Studies students and their teachers. Students use the platform to create and pitch business ideas and invest virtual money in ideas they support, learning real-world business and financial decision-making. Teachers use Fund-ED to support syllabus outcomes, run class competitions, reward positive behaviour or achievement with virtual funds, and engage students through interactive, curriculum-aligned learning.

### Front End Pages/Functionality
- Home / landing page
    - Overview of Fund-ED and how it works
    - Information about competitions and prizes
- Sign up / log in page
- Student Dashboard
    - Create and edit a business idea (product or service)
    - View available virtual funds
    - Browse and fund other students’ business ideas
    - Track funding received and competition rankings
    - Enter competition
- Teacher Dashboard
    - Create and manage classes
    - Allocate virtual funds to students as rewards
    - Monitor student participation and progress
    - Enter class into competition
- Business Idea Page
    - Display business descriptions, goals, and funding progress
    - Allow students to invest virtual money
    - Post emojis or likes (instead of comments)

### API Spec

| URL                    | HTTP Method | Purpose                            | Request Body                | Success Response Code | Authentication/Authorisation |
| /api/signup            | POST        | Create new student/teacher account | name, email, password, role | 201 Created           | none                         |
| /api/login             | POST        | Log a user into the system         | email, password             | 200 OK                | none                         |
| /api/student/dashboard | GET         | Retrieve student dashboard         | none                        | 200 OK                | authenticated student        |
| /api/teacher/dashboard | GET         | Retrieve teacher dashboard         | none                        | 200 OK                | authenticated teacher        |
| /api/business          | POST        | Create new business idea           | title, description, category| 201 Created           | authenticated student        |
| /api/business          | GET         | View all business ideas            | none                        | 200 OK                | authenticated user           |
| /api/business/{id}/fund| POST        | Fund a business idea               | amount                      | 200 OK                | authenticated student        |
| /api/teacher/class     | POST        | Create/manage a class              | class name, student list    | 201 Created           | authenticated teacher        |
| /api/teacher/funds     | POST        | Allocate funds to students         | student name, amount        | 200 OK                | authenticated teacher        |
| /api/competition/enter | POST        | Enter student/class in competition | student/class name          | 200 OK                | authenticated user           |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )