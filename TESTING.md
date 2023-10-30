<a name="top"></a>
### Yacht Club Testing file

[Back to README.md](<README.md>)

1. **user testing goals**
Testing User stories

#### Navigation and Authentication
1. [&check;] Navigation: As a user I can view a navbar from every page so that I can navigate easily between pages.

Acceptance Criteria
- [&check;] Have Search functionality to each page on the website
 - [&check;] Able to search using different keywords with different results showing with each search

2. [&check;] Authentication - Sign up: As a user I can create a new account so that I can access all the features for signed up users.

Acceptance Criteria
- [&check;] Sign up link visible on nav bar
- [&check;] user has functionality to sign up and create account
- [&check;] API updating with information

3. [&check;] Authentication - Sign in: As a user I can sign in to the app so that I can access functionality for logged in users.

Acceptance Criteria
- [&check;] Sign in link visible on Nav bar
- [&check;] User can sign in with a username and password
- [&check;] On sign in full website features are avaliable.

---
#### Trips
4. [&check;] Create Trips: As a user I can create a Trip / post so that I can share my images of a recent Yacht club trip!

Acceptance Criteria
- [&check;] A clear link on the navbar where the new trip can be added
- [&check;] A form where user is able to add new trip title/ pictures / description to website

5. [&check;] View a Trip: As a user I can view the details of a single trip picture so that I can learn more about it.

Acceptance Criteria
- [&check;] Able to view posted trip pictures.
- [&check;] functionality works to add pictures.

6. [&check;] Like a Trip: As a  user I can like a shared trip so that I can show my support for the trip that interest me.

Acceptance Criteria
- [&check;] Be able to like a trip picture

7. [&check;] Edit a Trip: As a users, i can edit a trip/ post title and description if i need to update a detail.

Acceptance Criteria
- [&check;] Ability to edit a trip picture
- [&check;] Ability to edit a trip description

8. [&check;] Delete a Trip: As a user I can delete a Trip / post so that no one can view the picture.

Acceptance Criteria
- [&check;] Able to delete trip pictures/ posts

9. [&check;] Search: As a user, I can search for specific trips/ users/ keywords, so that I can find specific details/ trips / user profiles I am most interested in.

Acceptance Criteria
- [&check;] users to successfully search.
 Able to create and view my created comment on the tripsearch function clear visible on website.

---

#### Comments
10. [&check;] Create a comment: As a logged in user I can add comments to a post so that I can share my thoughts about the trip.

Acceptance Criteria
- [&check;] Able to create and view my created comment on the trip

11. [&check;] View comments: As a user I can read comments on trips/ posts so that I can read what other users think about the trips/ posts.

Acceptance Criteria
- [&check;] able to view posted comments on a trip

12. [] Delete comments: As an owner of a comment I can delete my comment so that I can control removal of my comment from the application.

Acceptance Criteria
- [&check;]  to be able to clearly see the delete comment function
- ([x])  to be able to delete comment

13. [&check;] Edit a comment: As an owner of a comment I can edit my comment so that I can fix or update my existing comment
- [&check;] be able clearly see the functionality to edit my comments
- [&check;] to be able to edit my comment


---
#### The Profile Page

14. [&check;] Most followed profiles: As a user I can see a list of the most followed profiles so that I can see which profiles are popular

Acceptance Criteria
[&check;] Define the stats to show on the profile
[&check;] Ensure the stats are visible on the profile
[&check;] test the stats move.. ie when another profile is followed, followed + 1

15. [&check;] User profile - user stats: As a user I can view statistics about a specific user: bio, number of posts, follows and users followed so that I can learn more about them

Acceptance Criteria
[&check;] 

16. [&check;] Follow/Unfollow a user: As a logged in user I can follow and unfollow other users so that I can see and remove posts by specific users in my posts feed

Acceptance Criteria
[&check;] having ability to follow/ unfollow
[&check;] stats section changes

17. [&check;] As a user I can add a picture and bio so that i can tell people about my self and sailing likes

Acceptance Criteria
[&check;] be able to view the profile, profile avatar and bio

---

2. **Automated Testing**

In the building of the Yacht Club API, automated unit testing was completed on the trips app. This successfully tested.

1. list View:

```python
class TripListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='ben', password='pass')

    def test_can_list_trips(self):
        ben = User.objects.get(username='ben')
        Trip.objects.create(user=ben, trip_title='a trip')
        response = self.client.get('/trips/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_trip(self):
        self.client.login(username='ben', password='pass')
        response = self.client.post('/trips/', {'trip_title': 'a title'})
        count = Trip.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_in_user_cant_create_trip(self):
        response = self.client.post('/trips/', {'trip_title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

2. Trip Detail.

```python
class TripDetailViewTests(APITestCase):
    def setUp(self):
        ben = User.objects.create_user(username='ben', password='pass')
        ten = User.objects.create_user(username='ten', password='pass')
        Trip.objects.create(
            user=ben, trip_title='a title', description='bens content'
        )
        Trip.objects.create(
            user=ten, trip_title='the title', description='tens content'
        )

    def test_can_retrieve_trip_using_valid_id(self):
        response = self.client.get('/trips/1/')
        self.assertEqual(response.data['trip_title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_trip_using_invalid_id(self):
        response = self.client.get('/trip/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_trip(self):
        self.client.login(username='ben', password='pass')
        response = self.client.put('/trips/1/', {'trip_title': 'a new title'})
        trip = Trip.objects.filter(pk=1).first()
        self.assertEqual(trip.trip_title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_trip(self):
        self.client.login(username='ten', password='pass')
        response = self.client.put('/trips/1/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

```
- 
3. **Validation**

### Homepage

Due to lack of time limited amounts of code validator has been possible.

On the home page and trip validation page. No errors have been found.

- Homepage Html
- ![Screenshot](/frontend/src/assets/readme-images/validation/Homepage_html_validator.png)

- Homepage CSS
- ![Screenshot](/frontend/src/assets/readme-images/validation/css_homepage_validator.png)

- Trips Create HTML.
- ![Screenshot](/frontend/src/assets/readme-images/validation/trips_create_html_validator.png)


### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

| Desktop    | Display <1280px  | Display >1280px    |
|------------|------------------|--------------------|
| Render     |           x      |         x          |
| Images     |           x      |          x         |
| Links      |           x      |           x        |

### Browser Compatibility

Tested on google, ning and IOS - all loading successfully.


4. **Bug Tracking**

- Problem -Django object > is not JSON serializable
- Is it fixed [&check;]
- How? 
https://stackoverflow.com/questions/16790375/django-object-is-not-json-serializable

- Problem- Serializer not matching model exactly
- Is it fixed [&check;]
- How? 
https://stackoverflow.com/questions/49620189/django-core-exceptions-improperlyconfigured-field-name-id-is-not-valid-for-mo

- Problem -Problem with the serializers/ dot.notation - data not pulling through
- Is it fixed [&check;]
- How? 
https://chase-seibert.github.io/blog/2010/04/30/django-manytomany-error-cannot-resolve-keyword-xxx-into-a-field.html

- Problem -Refactoring code to ensure app talks to api
- Is it fixed [&check;]
- How? 
https://stackoverflow.com/questions/62776867/getting-status-400-bad-request-in-django-rest-framework-with-react

Refactoring code to ensure app talks to api

**Unfixed Bugs**
- React APP
1. Profile Avatar not show on Navbar or trips page. 
Fix suggested - defined as future feature
2. Comments app.
- Unable to delete.
Fix suggested - defined as future feature
3. username/ password functionality
Fix suggested - defined as future feature


[Back to README.md](<README.md>)