# crowdfunding_back_end

A repo to contain my She Codes Crowdfunding back end project

# Crowdfunding Back End

Selina Shin

## Planning:

### Concept/Name

'Community Change' is a community-driven crowdfunding platform that allows people to create fundraisers for small, local improvement projects in their neighbourhood. Instead of waiting for council action, residents can raise money to directly support initiatives. Examples include filling in a pothole, covering graffiti with a mural, purchasing more books for the local library, running a school holiday program, and renovating the bathrooms at the local park.

### Intended Audience/User Stories

The intended audience for Community Change includes:

- Local residents and community groups who want to improve their suburb or neighbourhood but lack the time, resources, or influence to navigate council processes.
- Local residents and community groups looking to fund small-scale local projects (e.g. murals, youth programs, library resources).

User stories:

- "As a fundraiser creator, I want to create a fundraiser." -> Endpoint: POST/fundraisers/
- "As a fundraiser creator, I want to see all the pledges for my fundraiser." -> Endpoint: GET/fundraisers/<id>/pledges/
- "As a fundraiser creator, I want to see all the fundraisers I've created." + "As a community member, I want to view all the fundraisers by a fundraiser creator." -> Endpoint: GET/users/<id>/fundraisers
- "As a fundraiser creator, I want to edit an existing fundraiser." -> Endpoint: PUT/fundraisers/<id>/
- "As a fundraiser creator, I want to close an existing fundraiser." +
  "As a fundraiser creator, I want to close a fundraiser when goal as been reached." -> Endpoint: PATCH/fundraisers/<id>/
- "As a community member, I want to view all fundraisers." -> Endpoint: GET/fundraisers/
- "As a community member, I want to view a fundraiser's details." -> Endpoint: GET/fundraisers/<id>/
- "As a community member, I want to fund a fundraiser." -> Endpoint: POST/fundraisers/<id>/pledges/
- "As a community member, I want to see all my pledges." -> Endpoint: GET/users/<id>/pledges

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
  - View contributions you have made to other fundraisers
- Create Fundraiser Page
  - Form to create new fundraiser (login required)
- Browse Fundraisers Page
  - Browse active fundraisers (name and one line description)
  - Filter by suburb/council
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

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| /api/signup | POST | Create new account | name, email, password | 201 Created | none |
| /api/login | POST | Log a user into the system | email, password | 200 OK | none |
| /api/dashboard | GET | Retrieve dashboard | none | 200 OK | authenticated user |
| /api/users | GET | Retrieve all users | none | 200 OK | none |
| /api/fundraisers | GET | View all fundraisers | none | 200 OK | none |
| /api/fundraisers | POST | Create new fundraiser | title, description, funding goal, suburb/location, deadline| 201 Created | authenticated user |
| /api/fundraisers/{id} | GET | View individual fundraiser | title, description, funding goal, amount raised, location, deadline, creator | 200 OK | none |
| /api/fundraisers/{id}/pledge| POST | Pledge fundraiser | amount | 201 Created | authenticated user |

### DB Schema

![database schema diagram](schema_database.png)
