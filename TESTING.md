# Wild Atlantic Way Testing

## Table of contents

- [Wild Atlantic Way Testing](#wild-atlantic-way-testing)
  - [Table of contents](#table-of-contents)
  - [Validator Testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
    - [Lighthouse](#lighthouse)
  - [Manual Testing](#manual-testing)
    - [Navbar and Footer (base.html)](#navbar-and-footer-basehtml)
      - [Sidebar](#sidebar)
      - [Pagination](#pagination)
      - [Post Detail Page (User signed in)](#post-detail-page-user-signed-in)
      - [Post Detail Page (User signed out)](#post-detail-page-user-signed-out)
      - [Register Page](#register-page)
      - [Login Page](#login-page)
      - [Logout Page](#logout-page)
      - [Create Post Page](#create-post-page)
      - [Update Post Page](#update-post-page)
      - [Delete post Page](#delete-post-page)
    - [About page (User signed out)](#about-page-user-signed-out)
    - [About page (User signed in)](#about-page-user-signed-in)
  - [Browser Testing](#browser-testing)
  - [Device Testing](#device-testing)
  - [Bugs](#bugs)

## Validator Testing

### HTML

Validator: [W3C Validator](https://validator.w3.org/)
**Home Page**
- ![Home page image](/static/images/testing/)

**Base Page**
- ![Home page image](/static/images/testing/)

**About Page**
- ![About page image](/static/images/testing/)
- 
**Categories Page**
- ![Categories page image](/static/images/testing/)

**Posts Page**
- ![Posts page image](/static/images/testing/)

**Sidebar Page**
- ![Sidebar page image](/static/images/testing/)

**Pagination Page**
- ![Pagination page image](/static/images/testing/)

**Register Page**
- ![Register page image](/static/images/testing/)

**Login Page**
- ![login page image](/static/images/testing/)

**Logout Page**
- ![Logout page image](/static/images/testing/)

**Create Post Page**
- ![Create post page image](/static/images/testing/)

**Update Post Page**
- ![Update post page image](/static/images/testing/)
- 
**Delete Post Page**
- ![Delete post page image](/static/images/testing/)


### CSS

Validator: [Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator)
 
- ![CSS validator image](/static/images/testing/)

### JavaScript

Validator: [JSHint Validator](https://jshint.com/).

- No errors were found when passing through the JSHint validator.
  
- ![JSHint validator](/static/images/testing/)

### Python

Validator: [CI Python Linter](https://pep8ci.herokuapp.com/).

Only files with custom-written Python code have been verified with the CI python Linter.

- ![JSHint validator](/static/images/testing/)

**admin.py**
- No errors found

**models.py**
- No errors found

**forms.py**
- No errors found
  
**views.py**
- No errors found

**waw_blog/urls.py**
- All clear, no errors found.

**wildatlanticway/urls.py**
- No errors found.

**settings.py**
- No errors found



### Lighthouse

**Base Page**
- ![Home page image](/static/images/testing/)

**Home Page**
- ![Home page image](/static/images/testing/)

**About Page**
- ![About page image](/static/images/testing/)

**Categories Page**
- ![Categories page image](/static/images/testing/)

**Posts Page**
- ![Posts page image](/static/images/testing/)

**Post detail Page**
- ![Post detail page image](/static/images/testing/)

**Header Page**
- ![Header page image](/static/images/testing/)

**Footer Page**
- ![Footer page image](/static/images/testing/)

**Sidebar Page**
- ![Sidebar page image](/static/images/testing/)
- 
**Pagination Page**
- ![Pagination page image](/static/images/testing/)

**Create Post Page**
- ![Create post page image](/static/images/testing/)

**Update Post Page**
- ![Update post page image](/static/images/testing/)
- 
**Delete Post Page**
- ![Delete post page image](/static/images/testing/)

**Register Page**
- ![Register page image](/static/images/testing/)

**Login Page**
- ![login page image](/static/images/testing/)
  
**Logout Page**
- ![Logout page image](/static/images/testing/)


## Manual Testing

### Navbar and Footer (base.html)
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Logo                  | Logo available to all users, when user clicks on logo they should be redirected to home page  | Click on logo | User is redirected to the home page      |    Pass  |
| Home                  | Home link available to all users, when user clicks on home they should be redirected to home page | Click on home | User is redirected to the home page      |   Pass   |
| About                  | About link available to all users, when user clicks on about they should be redirected to about page      | Click on about  | User is redirected to thr about page      |   Pass   |
| Register                  | Register link available to all signed out users, when user clicks on register they should be redirected to register page      | Click on register  | User is redirected to the register page      |   Pass   |
| Login                  | Login link available to all signed out users, when user clicks on login they should be redirected to login page      | Click on login  | User is redirected to the login page      |   Pass   |
| Logout                  | Logout link available to all signed in users, when user clicks on logout they should be redirected to logout page      | Click on logout  | User is redirected to the logout page      |   Pass   |
| Facebook link (icon)    | Facebook icon available to all users, when user clicks on icon it opens Facebook in a new tab | Click on Facebook icon  | User is redirected to Facebook website on a new tab  |   Pass   |
| Instagram link (icon)    | Instagram icon available to all users, when user clicks on icon it opens Instagram in a new tab | Click on Instagram icon  | User is redirected to Instagram website on a new tab  |   Pass   |
| Youtube link (icon)    | Youtube icon available to all users, when user clicks on icon it opens Youtube in a new tab | Click on Youtube icon  | User is redirected to Youtube website on a new tab  |   Pass   |
| Hamburger menu | Hamburger menu available to users on small screens  | Open site on mobile device  | Hamburger menu is present      |   Pass   |
| Hamburger menu | Hamburger menu can be toggled to open and closed position  | Toggle hamburger menu to open and closed  | Hamburger menu is responsive      |   Pass   |


#### Sidebar 
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|      Sidebar   |    Sidebar containing categories and popular posts is available to users on screens > 992px   |  Use Chrome developer tools to verify side bar is avaialbe on screens >= 992px and not on screens < 992px        |  side bar is avaialbe on screens >= 992px and not on screens < 992px       |  Pass         |
| Categories buttons           | When user clicks on a category they should be redirected to page with list of posts for selected category   | Click on category      | User is redirected to page with list of posts for selected category       | Pass|
| Clear filters         | When user clicks on "Clear Posts" they should be redirected to home page       | Click on "Clear Filter" | User is redirected to home page| Pass      |
| Popular post          | When user clicks on a post in the "Popular Post" list they should be redirected to the detailed view for the selected post | Click on one of the popular posts |User is redirected to post detail page for selected post | Pass|


#### Pagination
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|  Posts per page on home page      |  There should be 4 posts per page      |  Open home page and cound posts      |   There is 4 posts per page     |      Pass     |
| Next button | When user click on next button they are redirected to the next page| Click on "Next" button | User is redirected to the next page      | Pass|     
| Previous button | When user click on previous button they are redirected to the previous page| Click on "Previous" button | User is redirected to the previous page      | Pass|     
             

#### Post Detail Page (User signed in)
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Post detail page     | When the user clicks on the title of a post they should be redirected to the detailed view for the selected post       |   Click on title of a post     |    User is redirected to the detailed view for the selected post     |  Pass |
|    Post details     |  All details should be visible to all users - title, date, author, image, content, nummber of likes, number of comments, posted comments, additional information |   Click on a post     |    All details are present - title, date, author, image, content, nummber of likes, number of comments, posted comments, additional information   |     Pass      |
| Like post | The heart icon should be present and available to click, turns solid red when clicked and likes counter increments by 1      |  Click on heart icon      |    Heart icon goes solid red and likes counter increments by 1   |    Pass       |
| Un-like post | The heart icon should be solid red and and available to click, turns from solid red to normal icon when clicked and likes counter decrements by 1      |  Click on heart icon      |    Heart icon turns from solid red to normal icon when clicked and likes counter decrements by 1  |    Pass       |
|     Leave a comment     |   Comment form should be available and accept text, when user clicks "Submit" button the following message appears "Your comment is awaiting approval"     |  Type comment and click "Submit"     |    Comment can be submitted, and the following message appears    |   Pass        |
|   All-posts button      |   When  user click on "All Posts" it should redirect them to the home page     |  Click on "All Posts"      |   User is redirected to the home page     | Pass           |


#### Post Detail Page (User signed out)
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Post detail page     | When the user clicks on the title of a post they should be redirected to the detailed view for the selected post       |   Click on title of a post     |    User is redirected to the detailed view for the selected post     |  Pass |
|    Post details     |  All details should be visible to all users - title, date, author, image, content, nummber of likes, number of comments, posted comments, additional information |   Click on a post     |    All details are present - title, date, author, image, content, nummber of likes, number of comments, posted comments, additional information   |     Pass      |
| Like post | The heart icon should be present but not available to click   |  Click on heart icon      |    Heart icon does not change and likes counter does not increment   |      Pass     |
|     Leave a comment     |   Comment form should be present but does not accept text, the "Submit" button shuould not be present     |  Attempt to type in comment form    |    User can not type comment, and "Submit" button is not present |   Pass    |
|   All-posts button      |   When  user click on "All Posts" it should redirect them to the home page     |  Click on "All Posts"      |   User is redirected to the home page     | Pass           |


#### Register Page
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|    Submit signup form     |    Signup form can be submitted, A message indicating success should appear and disappear automatically after 3 seconds    |     Click sign up link in navbar, fill in fields and click "submit"   |  Signup form was submitted and message appears       |     Pass      |
|     Submit without filling out fields    |    The user should get an error message: "Please fill out this field"    |   Click "Sign-up" without filling in the mandadory fields      |  The following message appears  ![Register](/static/images/success-register.PNG)    |    Pass       |
|         |        |        |        |           |


#### Login Page
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|      Sign in    |  The user is signed in and redirected to the home page. A message indicating success should appear and disappear automatically after 3 seconds  |  Enter username and password      |   User is signed in and the following message appeared [Register](/static/images/success-register.PNG)      |      Pass     |
|    Sign In without filling in the mandadory fields      |   The user should get an error message: "Please fill out this field"       |  Click "Sign in" without filling in the mandadory fields       |   The following message appeared [Register](/static/images/success-register.PNG)     |       Pass    |


#### Logout Page
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|      Logout   |   The user is signed out and redirected to the home page. A message indicating success should appear and disappear automatically after 3 seconds      |  Click "Sign out"      |  The user is signed out and redirected to the home page. The following message appears [Register](/static/images/success-register.PNG)       |      Pass     |
  

#### Create Post Page
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|    Create post       |    Signed in user can create post. When user fills in fields and clicks "Create", a message appears "Your post is awaiting approval"    |  Fill in all fields and click "Create"      |   Message appears "Your post is awaiting approval" [Register](/static/images/success-register.PNG)       |     Pass       |
|    Incomplete form      |    The user should get an error message: "Please fill out this field"       |     Leave one field blank and click "Create"    |   The user gets an error message: "Please fill out this field"        |       Pass    |
|  Unique post title         |   The user should get an error message: "Post with this Title already exists"     |     Copy post title from post list page, fill out remaing fields and click "Create"   |   The follwoing message appears [Create post](/static/images/success-register.PNG)    |      Pass      |


####  Update Post Page
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|    Update own post     |  |  Click edit and update fields. Click "Update"       |    The success message appears [Update post](/static/images/success-post-updated.PNG)    | Pass



####  Delete post Page
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|     Delete own post   |    A signed in user can delete their own posts.     |   Click "Delete" on the home page, Post delete confirmation page opens, click "Delete"     |   Message appears "Your post was successfully deleted".      |   Pass        |
|     Go back     |   In the delete confirmation page, the user has the option to click on "Go back" to return to the home page, and not delte the post    |  Click "Delete" on the home page, Post delete confirmation page opens, click "Go back"      |    The user is returned to the home page and the post is not deleted    |    Pass       |


### About page (User signed out)
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|     Sign-in link       |   Sign in link is available and when user clicks "Sign in" they will be redirected to sign in page"     |   Open About page and click "Sign in"     |    User is redirected to sign in page    |     Pass
|     Register link       |   Register  link is available and when user clicks "Sign up" they will be redirected to sign up page"     |   Open About page and click "Sign up"     |    User is redirected to sign up page    |     Pass


### About page (User signed in)
| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|    Sign-in/Register links       |   Sign-in/Register links not present     |  Open about page and verify Sign-in/Register links not present     |   Sign-in/Register links not present     |   Pass        |




| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|         |        |        |        |           |


## Browser Testing

The project was tested extensively on Google Chrome, Microsoft Edge and Safari browsers, where no browser compatibility issues arose.

## Device Testing

The project was tested on a multiple devices: iPhone, android tablet, 14" laptop and 24" monitor. The website was responsive on all devices.


## Bugs

There are no known bugs in the current deployment of the site. A number of bugs were found and fixed during development. A summary of these bugs is provided below:

| Issue| Solution|Result|
|-----|--------|-------|
|    Create-post form allowed negative number for duration field      |     Update IntegerField to PositiveIntegerField in Post model                  |   Fixed   |
|   Comment count was incrementing for unapproved comments                |   Change "commented" to True in PostDetail post context                 |   Fixed        |      
|   Fix issue to prevent unregistered user directly accessing a page by the URL                |      Add LoginRequiredMixin to Post-Create, Post-Update and Post_Delete views               |       Fixed    |      
|    Post detail page was not accessible to logged ut user               |        Removed LoginRequiredMixin  from PostDEtail view           |     Fixed      |      
|        Delete-post success message was not appearing after post was deleted          |     Updated the delete method in the PostDelete view               | Fixed           |      
|  