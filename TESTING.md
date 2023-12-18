# Wild Atlantic Way Testing

## Table of contents

- [Wild Atlantic Way Testing](#wild-atlantic-way-testing)
  - [Table of contents](#table-of-contents)
  - [Validator Testing](#validator-testing)
    - [HTML](#html)
      - [Home Page](#home-page)
      - [Base Page](#base-page)
      - [About Page](#about-page)
      - [Categories Page](#categories-page)
      - [Posts Page](#posts-page)
      - [Sidebar Page](#sidebar-page)
      - [Pagination Page](#pagination-page)
      - [Register Page](#register-page)
      - [Login Page](#login-page)
      - [Logout Page](#logout-page)
      - [Create Post Page](#create-post-page)
      - [Update Post Page](#update-post-page)
      - [Delete Post Page](#delete-post-page)
    - [CSS](#css)
    - [CSS](#css-1)
    - [JavaScript](#javascript)
    - [Python](#python)
      - [admin.py](#adminpy)
      - [models.py](#modelspy)
      - [forms.py](#formspy)
      - [views.py](#viewspy)
      - [waw\_blogg/urls.py](#waw_bloggurlspy)
      - [wildatlanticway/urls.py](#wildatlanticwayurlspy)
      - [settings.py](#settingspy)
    - [Lighthouse](#lighthouse)
      - [Base Page](#base-page-1)
      - [Home Page](#home-page-1)
      - [About Page](#about-page-1)
      - [Categories Page](#categories-page-1)
      - [Posts Page](#posts-page-1)
      - [Post detail Page](#post-detail-page)
      - [Header Page](#header-page)
      - [Footer Page](#footer-page)
      - [Sidebar Page](#sidebar-page-1)
      - [Pagination Page](#pagination-page-1)
      - [Create Post Page](#create-post-page-1)
      - [Update Post Page](#update-post-page-1)
      - [Delete Post Page](#delete-post-page-1)
      - [Register Page](#register-page-1)
      - [Login Page](#login-page-1)
      - [Logout Page](#logout-page-1)
  - [Manual Testing](#manual-testing)
    - [Base Page /  Header Page /  Footer Page / About page](#base-page---header-page---footer-page--about-page)
      - [Home Page / Sidebar Page / Categories Page](#home-page--sidebar-page--categories-page)
      - [Pagination Page](#pagination-page-2)
      - [Post Detail Page (User logged out)](#post-detail-page-user-logged-out)
      - [Register Page](#register-page-2)
      - [Login Page](#login-page-2)
      - [Post Detail Page (User Logged in)](#post-detail-page-user-logged-in)
      - [Create Post Page](#create-post-page-2)
      - [Update Post Page](#update-post-page-2)
      - [Delete post Page](#delete-post-page-2)
      - [Logout Page](#logout-page-2)
      - [Page](#page)
  - [Browser Testing](#browser-testing)
  - [Device Testing](#device-testing)
  - [Bugs](#bugs)

## Validator Testing

### HTML

Validator: [W3C Validator](https://validator.w3.org/)
    
#### Home Page
- ![Home page image](/static/images/testing/)

#### Base Page
- ![Home page image](/static/images/testing/)

#### About Page
- ![About page image](/static/images/testing/)

#### Categories Page
- ![Categories page image](/static/images/testing/)

#### Posts Page
- ![Posts page image](/static/images/testing/)

#### Sidebar Page
- ![Sidebar page image](/static/images/testing/)

#### Pagination Page
- ![Pagination page image](/static/images/testing/)

#### Register Page
- ![Register page image](/static/images/testing/)

#### Login Page
- ![login page image](/static/images/testing/)

#### Logout Page
- ![Logout page image](/static/images/testing/)

#### Create Post Page
- ![Create post page image](/static/images/testing/)

#### Update Post Page
- ![Update post page image](/static/images/testing/)

#### Delete Post Page
- ![Delete post page image](/static/images/testing/)


### CSS

Validator: [Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator)



### CSS

Validator: [Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator).
  
- ![CSS validator image](/static/images/testing/)

### JavaScript

Validator: [JSHint Validator](https://jshint.com/).

- No errors were found when passing through the JSHint validator.
  
- ![JSHint validator](/static/images/testing/)

### Python

Validator: [CI Python Linter](https://pep8ci.herokuapp.com/).

Only files with custom-written Python code have been verified with the CI python Linter.

- ![JSHint validator](/static/images/testing/)

#### admin.py
- No errors found

#### models.py
- No errors found

#### forms.py
- No errors found
  
#### views.py
- No errors found

#### waw_blogg/urls.py
- All clear, no errors found.

#### wildatlanticway/urls.py
- No errors found.

#### settings.py
- No errors found



### Lighthouse

#### Base Page
- ![Home page image](/static/images/testing/)

#### Home Page
- ![Home page image](/static/images/testing/)

#### About Page
- ![About page image](/static/images/testing/)

#### Categories Page
- ![Categories page image](/static/images/testing/)

#### Posts Page
- ![Posts page image](/static/images/testing/)

#### Post detail Page
- ![Post detail page image](/static/images/testing/)

#### Header Page
- ![Header page image](/static/images/testing/)

#### Footer Page
- ![Footer page image](/static/images/testing/)

#### Sidebar Page
- ![Sidebar page image](/static/images/testing/)

#### Pagination Page
- ![Pagination page image](/static/images/testing/)

#### Create Post Page
- ![Create post page image](/static/images/testing/)

#### Update Post Page
- ![Update post page image](/static/images/testing/)

#### Delete Post Page
- ![Delete post page image](/static/images/testing/)

#### Register Page
- ![Register page image](/static/images/testing/)

#### Login Page
- ![login page image](/static/images/testing/)

#### Logout Page
- ![Logout page image](/static/images/testing/)




## Manual Testing

### Base Page /  Header Page /  Footer Page / About page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Logo                  | Click      | Redirect to home                                                   | Pass      |
| Home                  | Click      | Redirect to home                                                   | Pass      |
| About                 | Click      | Open About page                                                    | Pass      |
| Register              | Click      | Open register page                                                 | Pass      |
| Login                 | Click      | Open Gallery page                                                  | Pass      |
| Logout                | Click      | Open logout page                                                   | Pass      |
| Facebook link         | Click      | Open in new page                                                   | Pass      |
| Instagram link        | Click      | Open in new page                                                   | Pass      |
| Youtube link          | Click      | Open in new page                                                   | Pass      |


#### Home Page / Sidebar Page / Categories Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Categories            | Click      | Redirect to page with list of posts for selected category          | Pass      |
| Clear filters         | Click      | Redirect to home page                                              | Pass      |
| Popular post          | Click      | Redirect to post detail page for selected post                     | Pass      |
| Individual post       | Click      | Redirect to post detail page for selected post                     | Pass      |

#### Pagination Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Posts per page        | Count      | Maximum of 4 posts per page                                        | Pass      |   
| Next button           | Click      | Redirect to next page                                              | Pass      |       
| Previous button       | Click      | Redirect to previous page                                          | Pass      |       


#### Post Detail Page (User logged out)
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Open post detail |  Logout out and open post | Click anywhere on post opens the post                      | Pass      |   
| Post details visible         | View post details     |All details visible - title, date, author, image, content, nummber of likes, number of comments, additional information, posted comments                                              | Pass      |   
|   Like post   |     Click on heart icon     |         Heard icon is not clickable, like count does not increment              | Pass      |   
|     Post comment |      Type comment in comment form    |      Unable to type in comment form                 | Pass      |   
|      |          |                       |      |   


#### Register Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|   Submit signup form   |   Click sign up button and fill in fields     |     The user is redirected to the home page                  | Pass      |  
|   Submit without filling in the mandadory fields   |    Click on the "Sign In" link in the navigation bar and then click the "Sign Up" button without filling in username, password or password(again) fields      |      The user should get an error message: "Please fill out this field"                 |      |   

#### Login Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|    Sign in  |        Enter username and password and click "Sign in"  |       The user is redirected to the home page                |  Pass    |
|   Sign In without filling in the mandadory fields   |   Click "sign in" without filling in the mandadory fields        |      The user should get an error message: "Please fill out this field"                    |   Pass   |


#### Post Detail Page (User Logged in)
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Leave a comment | Type comment and click "Submit"| Message appears "Your comment is awaiting approval" | Pass ![image]() |   
| Like post  | Click on heart icon | Heart icon goes solid red and likes counter increments by 1 | Pass |
| Unlike post| Click on heart icon | Heart icon returns to standard red icon and like counter decrements by 1 |  Pass  |   




#### Create Post Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Create post     |    Fill in all fields and click "Create"      |     Message appears "Your post is awaiting approval"                        |   Pass   |   
| Incomplete form  |       Leave one field blank and click "Create"   |          The user should get an error message: "Please fill out this field"               |   Pass   | 
| Unique post title     |   Copy post title from post list page       |        The user should get an error message: "Post with this Title already exists"          |  Pass    |   



####  Update Post Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|    Update post  | Update fields and click "Update         |      Message appears "Your post has been updated successfully"                      |  Pass    |   


####  Delete post Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|   Delete own post   |    Click "Delete" on post list page"      |        Post delete confirmation page opens with button to "Delete" and "Go back"              |  Pass    |   
|   Delete post|      Click "Delete" on delete confirmation page    |          Message appears "Your post was successfully deleted". Post is deleted from post list page               |  Pass    |   
|   Go back  |  Click "Go back" button       |    The user is redirected to the home page                   |  Pass    |   


#### Logout Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|   Logout   |     Click "Sign out"     |        The user is redirected to the home page               |    Pass  |   




####  Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|      |          |                       |      |   



## Browser Testing

The project was tested extensively on Google Chrome, microsoft Edge and Safari browsers, where no browser compatibility issues arose.

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