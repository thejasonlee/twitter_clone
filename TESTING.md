# Sign Up
### USER ACCEPTANCE TESTING

Use case name
Verify sign up with valid username, email, password and confirmation password

Description
Test the Gritter sign up page

Pre-conditions
User has valid username, email, password and confirmation password

Test steps
1. Navigate to sign up page
2. Click sign in button if already have an account, otherwise continue to next step
3. Provide valid username
4. Provide valid email
5. Provide valid password
6. Provide valid confirmation password
7. Click submit button

Expected result
User should be able to sign up

Actual result
User is redirected to the home page with successful registration

Status (Pass/Fail)
Pass

Notes
Validation conditions -&gt; No fields allowed to be left empty
username with a min of 5 characters and a max of 30 characters
email in a valid email form
password with a min of 5 characters and a max of 30 characters
password confirmation with a min of 5 characters and a max of 30 characters, must match password

Upon any failed validation conditions, the same page is rendered and corresponding error msgs are displayed


User Sample Test Run ->

Try => Username:
       Email: Aaron@gmail.com
       Password: hahawhat
       Password Confirmation: hahawhat
       * Should fail the username validation for being empty

Try => Username: Jon
       Email: jonnyboy@blue.net
       Password: as0
       Password Confirmation: as0
       * Should fail username and password validations, character lengths < 5

Try => Username: goodMorning
       Email: jonnyboy@blue.net
       Password: 1111111111222222222233333333330000000000
       Password Confirmation: 1111111111222222222233333333330000000000
       * Should fail password and confirmation validation, character lengths > 30

Try => Username: goodboy
       Email: a@a.a
       Password: imnotthere345
       Password Confirmation: iamhere123
       * Should fail the validation for non-match between password and password confirmation

Try => Username: whatisUp9
       Email: abc
       Password: eeeek
       Password Confirmation: eeeek
       * Should fail email validation

Try => Username: Aaron
       Email: AaronIsEvil@gmail.com
       Password: Unhappybaby
       Password Confirmation: Unhappybaby
       * Should pass the validations

Post-conditions
User is validated with sign up form and passes all requirements for registration.
User is added to the database and successfully registered as a user.
User has their password protected with a hash function for security.


### AUTOMATED TESTING
1. new User in db
	test: 

2. pw encrypted?
	test: 

3. validation for form inputs is working
 - username must be strings
 - username non-empty
 - password non-empty
 - pw has a length requirement

4. Partial form doesn't create new user

--------
# Signed-in
### USER ACCEPTANCE TESTING
Use case name
    Verify login with valid username and password
Description
    Test Gritter sign-in feature/page
Pre-conditions
    A user exists in the user table with a given username and password
Test steps
    1. Navigate to sign-in (https://gritter-3308.herokuapp.com/signin)
    2. Enter the correct username/password (test: fred/password )
    3. Click sign in button

Expected result
    "Welcome to the Gritter Homepage!". Successful sign-in will navigate a user to the Gritter homepage.
Actual result
    User is navigated to the homepage if credentials are correct.
Status (Pass/Fail)
    Pass
Notes
    Attempting to sign in with incorrect credentials will take user to a stub page.
Post-conditions
    Correct credentials give different behavior than incorrect credentials. 
    Querying database with proper credentials leads to a successful sign-in.
    After sign in, homepage will say "Hello, fred"

### AUTOMATED TESTING
 - navbar changes a bit
 - flash alert / sign-in message

1. un/pw that's in the db *can* sign-in

2. un/pw not in db *cannot* sign-in
 - redirected on failure to same page with flash

3. flash success on success

4. flash failure on failure

--------
# Create a Post
### USER ACCEPTANCE TESTING
Use case name
    Lorem ipsum
Description
    Lorem ipsum
Pre-conditions
    Lorem ipsum
Test steps
    1. Lorem ipsum
    2. Lorem ipsum

Expected result
    Lorem ipsum
Actual result
    Lorem ipsum
Status (Pass/Fail)
    Lorem ipsum
Notes
    Lorem ipsum
Post-conditions
    Lorem ipsum

### AUTOMATED TESTING

- need to be signed-in
- fill-in form, submit

1. new Post in the db

2. validation on Post form working
 - character limit restricts Post generation
 - empty post OK

3. Not signed-in can't access Post form (i.e. the route)
user = User.id(1) #Tommy

4. Sign-in *can* access Post form

--------
# 'Liking' a post
### USER ACCEPTANCE TESTING
- need to be signed-in
- can only like once
- liking is binary (1/0)

Use case name
    'Liking' a post
Description
    A user should be able to 'like' a tweet exactly once or not at all.
Pre-conditions
    User should be registerd and logged-in.
Test steps
    1. Find a post they would like to promote. 
    2. Click the 'like' button beneath the post, if it isn't liked already.

Expected result
    The 'like' button transitions from default to '+1', and the total number of likes increases by 1.
Actual result
    Lorem ipsum
Status (Pass/Fail)
    Lorem ipsum
Notes
    Lorem ipsum
Post-conditions
    Lorem ipsum

### AUTOMATED TESTING
1. User can 'like' a post.

2. User can unlike a post that's been liked.

3. Total number of likes reflects the likes from all users.

4. A post's like status can only be yes/no for a given user.

5. Non-signedin users cannot like a post.








