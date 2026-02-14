# crowdfunding_back_end

A repo to contain my She Codes Crowdfunding back end project

# Crowdfunding Back End

Selina Shin

## Planning:

### Concept/Name

![Community Change logo](/images/community_change_logo.png)

'Community Change' is a community-driven crowdfunding platform that allows people to create fundraisers for small, local improvement projects in their neighbourhood. Instead of waiting for council action, residents can raise money to directly support initiatives. Examples include filling in a pothole, covering graffiti with a mural, purchasing more books for the local library, running a school holiday program, and renovating the bathrooms at the local park.

(P.S. “Community Change” is a pun referring to both money and making a difference. In other words, it’s the positive change we can create together with our community's cash.)

### Intended Audience/User Stories

The intended audience for Community Change includes:

- Local residents and community groups who want to improve their suburb or neighbourhood but lack the time, resources, or influence to navigate council processes.
- Local residents and community groups looking to fund small-scale local projects (e.g. murals, youth programs, library resources).

User stories:

- "As a fundraiser creator, I want to create a fundraiser."
- "As a pledger, I want to view all fundraisers." 
- "As a user, I want to see all the pledges for a fundraiser." 
- "As a user, I want to see all the fundraisers I've created/all pledges I've made."
- "As a user, I want to see all the fundraisers another user has created."
- "As a fundraiser creator, I want to edit/close an existing fundraiser."
- "As a fundraiser creator, I want to delete a fundraiser if it has no pledges."
- "As a pledger, I want to fund a fundraiser." 
- "As a pledger, I want to edit a pledge."

### Front End Pages/Functionality

- Home Page
  - Overview of the platform and how it works
  - Featured or recent local fundraisers
  - Click to view details of a specific fundraiser
- Sign Up / Log In Page
  - Register as a community member
  - Log in to existing account
- User Dashboard
  - Create and edit local fundraisers
  - View fundraisers you have created
  - Track funding received on your fundraisers
  - View pledges you have made to other fundraisers
- Create Fundraiser Page
  - Form to create new fundraiser (login required)
- Browse Fundraisers Page
  - Browse active fundraisers (name and one line description)
  - Filter by location (e.g. suburb/council)
  - View funding progress for each fundraiser
  - View date created and deadline
- Fundraiser Page
  - Display fundraiser description, location, and goal
  - Show funding progress and deadline
  - Allow users to contribute funds (login required or will be directed to create an account)
  - View updates from the fundraiser creator
  - View comments made by pledgers
- Community Member's Fundraisers Page
  - Display all fundraisers created by that member
  - Option to view a fundraiser
  - Option to edit a fundraiser (for creator only)

### API Spec

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/ Authorisation |
|---|---|---|---|---|---|
| /api/signup/ | POST | Create new account | name, email, password | 201 Created | none |
| /api/login/ | POST | Log a user into the system | email, password | 200 OK | none |
| /api/fundraisers/ | GET | View all fundraisers | none | 200 OK | none |
| /api/fundraisers/ | POST | Create new fundraiser | title, image, description, location, goal amount, deadline, active | 201 Created | authenticated user |
| /api/fundraisers/:id/ | GET | View individual fundraiser and all pledges | none | 200 OK | none |
| /api/fundraisers/:id/ | PUT | Edit existing fundraiser | title, image, description, location, goal amount, deadline, active | 200 OK | authorised user |
| /api/pledges/| POST | Pledge fundraiser | fundraiser, amount, anonymous, comment | 201 Created | authenticated user |
| /api/pledges/:id/ | PUT | Edit pledge | anonymous, comment | 200 OK | authorised user |
| /api/users/:id/| GET | View all user's fundraisers | none | 200 OK | none |
| /api/users/:id/| GET | View all user's pledges | none | 200 OK | authorised user |

### DB Schema

![database schema diagram](/images/schema_database.png)

### Submission

- Link to the deployed project: https://crowdfunding-app-production-dc1723c10be4.herokuapp.com/fundraisers/
- A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
  - Create a user
  ![screenshot create a user](/images/POST_create_user.png)
  - Create a fundraiser
  ![screenshot create a fundraiser](/images/POST_create_fundraiser.png)
  - Create a pledge
  ![screenshot create a pledge](/images/POST_create_pledge.png)
- A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
  - Get all users
  ![screenshot of all users](/images/GET_all_users.png)
  - Get all fundraisers
  ![screenshot of all fundraisers](/images/GET_all_fundraisers.png)
- A screenshot of Insomnia, demonstrating a token being returned.
  ![screenshot generate token](/images/POST_generate_token.png)
- Step by step instructions for how to register a new user and create a new fundraiser (i.e. endpoints and body data).
  1. Register a new user 
    - endpoint: POST /users/
    - body data example:</br>
      ![body data example of creating a new user](/images/body_data_example_create_user.png)
  2. Create a new fundraiser
    - endpoint: POST /fundraisers/
    - body data example: </br>
      ![body data example of creating a new fundraiser](/images/body_data_example_create_fundraiser.png)
- Your refined API specification and Database Schema. (see above)