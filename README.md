<a name="top"></a>

# Milestone project 5 Frontend

--- 
**Live Website**

---
### Am i response image

--- 
### Project purpose and description

**Yacht Club** is a website for a fictional yatch club based in the UK. 

[Wikipedia](https://www.wikipedia.org/) defines the purpose of a "yacht club is to celebrate boaters and the sport of yacht racing, sailing, and cruising. What Is A Yacht Club? A yacht club is a social membership sports club for boaters."

The Yacht Club website has been created as 5th Portfolio project for the Code Institutes fullstack developer program. 

The website goal is to allow users to view and share pictures of trips taken and future trips with the Yatch club.  

The website is designed as a browser-based interface to enable;
- users to create, read, comment and vote on shared content.
- content to be searched and catergorised.
- search results can be filtered on username, popularity, date created, title, content keywords and category. 

The project is built using React, JSX, (HTML, Javascript and CSS), specific frameworks and libraries (detailed in a below section) and connected to a separate backend API (also built for this course).

---

### Site Owner's goal

My family are keen sailers and belong to sailing club that allows them to sail with friends all around the UK and Northern Europe. At the minute the only place they can share their pictures is Facebook. I wanted to create a place where they could share their pictures, memories and feedback on old trips.

---
### Site User's goal

- To create a website for club members to share their trip pictures to club members. 
- To allow the club to show pictures of the previous adventures the members have been on. 

---
### User Stories

The below user stories have been defined for the project.

#### Navigation 
- [] Navigation: As a user I can view a navbar from every page so that I can navigate easily between pages.
- [] Routing: As a user I can navigate through pages quickly so that I can view content seamlessly without page refresh

#### Authentication and account creation
- [] Authentication - Sign up: As a user I can create a new account so that I can access all the features for signed up users.
- [] Authentication - Sign in: As a user I can sign in to the app so that I can access functionality for logged in users.
- [] Authentication - Logged in Status: As a user I can tell if I am logged in or not so that I can log in if I need to.
- [] Authentication - Refreshing access tokens: As a user I can maintain my logged-in status until I choose to log out.
- [] Avatar: As a user I can view user's avatars so that I can easily identify other website users.


#### Trips
- [] Create Trips: As a user I can create a Trip / post so that I can share my images of a recent Yacht club trip!
- [] View a Trip: As a user I can view the details of a single trip picture so that I can learn more about it.
- [] Like a Trip: As a  user I can like a shared trip so that I can show my support for the trip that interest me.
- [] Edit a Trip: As a users, i can edit a trip/ post title and description if i need to update a detail.
- [] Delete a Trip: As a user I can delete a Trip / post so that no one can view the picture.
- [] Search: As a user, I can search for specific trips/ users/ keywords, so that I can find specific details/ trips / user profiles I am most interested in.

#### The Trips Page
- [] View most recent Trips: As a user I can view all the most recent Trips, the most recently created shown first so that I am up to date with the newest content.
- [] Liked trips: As a logged in user I can view the trips I liked so that I can find the trips I enjoy the most
- [] Followed users: As a logged in user I can view content filtered by users I follow so that I can keep up to date with content.

#### Comments
- [] Create a comment: As a logged in user I can add comments to a post so that I can share my thoughts about the trip.
- [] View comments: As a user I can read comments on trips/ posts so that I can read what other users think about the trips/ posts.
- [] Delete comments: As an owner of a comment I can delete my comment so that I can control removal of my comment from the application
- [] Edit a comment: As an owner of a comment I can edit my comment so that I can fix or update my existing comment

#### The Profile Page
- [] Profile page: As a user I can view other users profiles so that I can see their posts and learn more about them
- [] Most followed profiles: As a user I can see a list of the most followed profiles so that I can see which profiles are popular
- [] User profile - user stats: As a user I can view statistics about a specific user: bio, number of posts, follows and users followed so that I can learn more about them
- [] Follow/Unfollow a user: As a logged in user I can follow and unfollow other users so that I can see and remove posts by specific users in my posts feed
- [] View all trips created by a specific user: As a user I can view all the trips created by a specific user so that I can catch up on their created trips, or decide I want to follow them
- [] Edit profile: As a logged in user I can edit my profile so that I can change my profile picture and bio
- [] Update username and password: As a logged in user I can update my username and password so that I can change my display name and keep my profile secure

---
### Structure

#### Wireframes

##### HomePage
![Screenshot](/readme-images/home-page.png)

##### Profile Page
![Screenshot](/readme-images/profile-page.png)

##### Sign In
![Screenshot](/readme-images/sign-in.png)

##### Sign Up
![Screenshot](/readme-images/sign-up.png)

##### Trip Detail
![Screenshot](/readme-images/trip-detail.png)

---

#### Database Schema

![Screenshot](/readme-images/yacht_club_database_scheme.png)

----
##### Data Model

1. **Profile model**

| Name            | Database Key    | Field Type    | Validation |
| --------------- | --------------- | ------------- | ---------- |
| Owner           | owner           | OneToOneField | User, on_delete=models.CASCADE,related_name='user_profile'    |
| Avatar          | avatar          | ImageField    | upload_to='images/', default='../profilepicture>', blank=True     |
| Display_name    | display_name    | Charfield     | max_length=25, null=True, blank=True, related_name='user_profile'     |
| Birth_date      | birth_date      | DateField     | null=True, blank=True     |
| Bio             | bio             | TextField     | max_length=100, null=True, blank=True     |
| Created_at      | created_at      | DateTimeField | auto_now_add=True     |
| updated_at      | updated_at      | DateTimeField | auto_now=True     |

2 **User model**
| Name            | Database Key    | Field Type    | Validation |
| --------------- | --------------- | ------------- | ---------- |
| User.username   | user.username   | ForeignKey    | User, on_delete=models.CASCADE    |
| User.password   | user.password   | Charfield     | max_length=30, unique=True, blank=False   |

3. **Comment model**

| Name            | Database Key    | Field Type    | Validation |
| --------------- | --------------- | ------------- | ---------- |
| Owner_following | owner_following | ForeignKey    | User, related_name=’author’, on_delete=models.CASCADE     |
| Trip            | trip            | ForeignKey    | to=Trip, on_delete=models.CASCADE, related_name='trip_comments'     |
| Comment         | comment         | ForeignKey    | to=Trip, on_delete=models.CASCADE, related_name=’trip_comments’   |
| Created_at      | created_at      | DateTimeField | auto_now_add=True   |
| Updated_at      | updated_at      | DateTimeField | auto_now=True   |


4. **Followers model**

| Name            | Database Key    | Field Type    | Validation |
| --------------- | --------------- | ------------- | ---------- |
| Owner_following | owner_following | ForeignKey    | User, related_name='following', on_delete=models.CASCADE  |
| Followed        | followed        | ForeignKey    | User, related_name='followed', on_delete = models.CASCADE |
| Created_at      | created_at      | DateTimeField | auto_now_add=True |

5 **Trip model**

```Python
TRIP_CATEGORIES = (
    ("1", "Fleet"),
    ("2", "Racing"),
    ("3", "Parasailing"),
    ("4", "eSailing"),
    ("5", "Offshore"),
    ("6", "Cruising"),
    ("7", "Radio"),
)
```
| Name            | Database Key    | Field Type    | Validation |
| --------------- | --------------- | ------------- | ---------- |
| Owner           | owner           | ForeignKey    | to=User, on_delete=models.CASCADE, related_name='Trip_post’   |
| Trip_title      | trip_title      | Charfield     | max_length=30, unique=True, blank=False  |
| Description     | description     | TextField     | max_length=100, blank=True,related_name='Trip_post’   |
| Image           | image           | ImageField    | trip_image, folder = trips, null = True, blank = True     |
| Category        | category        | CharField     | max_length=255, blank=False, choices=trip_categories, default='Sightseeing'   |
| Trip_location   | trip_location   | CharField     | max_length=255, blank=False   |
| Created_at      | created_at      | DateTimeField | auto_now_add=True     |
| Updated_at      | updated_at      | DateTimeField | auto_now=True     |

6 **Like model**

| Name            | Database Key    | Field Type    | Validation |
| --------------- | --------------- | ------------- | ---------- |
| Owner           | owner           | ForeignKey    | to=User, on_delete=models.CASCADE, related_name='initiated_like_request_events'   |
| Trip            | trip            | ForeignKey    | Trip, on_delete=models.CASCADE, related_name=likes    |
| Created_at      | created_at      | DateTimeField | auto_now_add=True     |
| Updated_at      | updated_at      | DateTimeField | auto_now=True     |


---
### Design Choices

#### Colour Scheme

The colour scheme chosen for the website is light colours with stong links to summer and sailing. They provide strong contrasts which will make the information clear and easy to read for the user.
![Screenshot](/readme-images/palette.png)

---
#### Fonts and Typography

- Ruda font used on site, fall back font is sans-serif. Example of Ruda font from.
![Screenshot](/readme-images/ruda_font.png)

---
#### Agile Project Management

To manage and track the development process GitHub projects has been used.

For each User Story a GitHub Issue was created, which was then allocated to a milestone (Epic). 

With in each User Story the acceptance criteria has been defined to make it clear when the User Story has been completed. 

The acceptance criteria are further broken down into tasks to facilitate the User Story's execution. 

The issues were closed when the work is completed.

### Features

1 **Navbar**
2 **Sign up**
3 **Sign in**
4 **Feed**
5 **Add Trip**
6 **Trip Detail**
7 **Edit trip**
8 **Delete Trip**
9 **Profile**
10 **Follow/ Followed**
11 **Comments**
12 **Categories**
13 **Footer**
**Future Features**


---
### Technologies Used

### Languages

- HTML / JSX (JavaScript XML)
- CSS
- Python
- Javascript
---
### Frameworks

- [Django](https://www.djangoproject.com/): A high-level Python web framework used for building the Yacht Club API.
- [React](https://react.dev/): A JavaScript library for building user interfaces. It is commonly used for creating dynamic and interactive components in web applications.
---
### Database

- ElephantSQL: ElephantSQL is a PostgreSQL database as a service. It is used as the database for the Yacht Club project, providing a reliable and scalable storage solution for the application's data.

---

### Tools

- [GitHub](https://github.com/): A web-based hosting service for version control repositories for storing and managing the project's source code.
- [Gitpod Repository](https://gitpod.io/): An online integrated development environment (IDE) used for developing and testing the Yacht Club project.
- [Heroku](https://dashboard.heroku.com/apps): A cloud platform that enables deployment and hosting of web applications. Heroku was used for deploying the Yacht Club project to a live server.
- [Balsamiq](https://balsamiq.com/): A wireframing tool for creating mockups and prototypes of the Yacht Club website.
- [DrawSQL](https://drawsql.app/) - software is a platform used to create, visualize and collaborate on your database entity relationship diagrams
- [Google Fonts](https://fonts.google.com/): An open-source fonts used for typography on the Yacht Club website.
- [Font Awesome](https://fontawesome.com/): A library of free  icons to the Yacht Club website.
- [logo.com](logo.com): used to create the business logo.
- [Wikipedia](https://www.wikipedia.org/) - used for the description of a yacht club.
- [Cloudinary](https://cloudinary.com/): A cloud-based media management platform used for storing and serving images in the Yacht Club project.
- [freepik.com](https://www.freepik.com/): Website with Millions of Free Graphic Resources

---
### Testing

please see testing.md when created for:

1. **manual testing**
2. **user testing goals**
3. **automated testing**
unit testing
4. **Validation**
w3c
js bin
ci linter - python
i am responsive
lighthouse report
browser testing
5. **Bug Tracking**

---

### Deployment

#### Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

#### Create the Heroku App

1. Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.

2. On your Heroku dashboard, click the button labelled New in the top right corner and from the drop-down menu select Create new app.

3. Enter a unique and meaningful app name** and choose the region which is best suited to your location.
- Click on the Create app button.

4. Select Deploy from the tabs at the top of the app page.

5. Select Connect to GitHub from the deployment methods. 

6. Search for the repository to connect to by name.

7. Click Connect. Your app should now be connected to your GitHub account.

 8. Select Enable Automatic Deploys for automatic deployments.

- If you would like to deploy manually, select Deploy Branch. If you manually deploy, you will need to re-deploy each time the repository is updated.

- For the first time deploying to Heroku, you may have to deploy manually but if you select automatic deploys it will update from then onwards.

14. Click View to view the deployed site.

--- 

#### Forking the GitHub Repository

By forking the GitHub Repository you can make a copy of the original repository. You can view and/or make changes without affecting the original repository by using the following steps...

**1.** Log in to GitHub and locate the [GitHub Repository](https://github.com/) you would like to fork.

**2.** At the top of the Repository, just above the Tabs, locate the Fork Button and you should now have a copy of the repository in your account.

--- 

#### Cloning this repository

**1.** Log in to GitHub and locate the [GitHub Repository](https://github.com/).

**2.** On the repository main page, click the drop-down menu called Code.

**3.** To clone the repository using HTTPS, copy the link.

**4.** Open Git Bash

**5.** Change the current working directory to the location where you want the cloned directory to be made.

**6.** Type git clone, and then paste the URL you copied in Step 3.

**7.** Press Enter. Your local clone will be created.


--- 

### Credits