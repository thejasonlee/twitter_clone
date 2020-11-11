### Team name: Grep
### Project Title: Gritter
### Members: Aaron Shyuu, Francis Kim, Jason Weidner, Michael Shippee
### github repo: https://github.com/jasonweidner/twitter_clone
### steps for automated tests: run test.py from within .../twitter_clone/ subdirectory.

#### Note to Instr. Knox: There are details about automated testing within the UAT#1 section.

--------

## UAT #1: Sign Up

#### Use case name<br>
Verify sign up with valid username, email, password and confirmation password

#### Description<br>
Test the Gritter sign up page

#### Pre-conditions<br>
User has valid username, email, password and confirmation password

#### Test steps
1. Navigate to sign up page
2. Click sign in button if already have an account, otherwise continue to next step
3. Provide valid username
4. Provide valid email
5. Provide valid password
6. Provide valid confirmation password
7. Click submit button

#### Expected result<br>
User should be able to sign up

#### Actual result<br>
User is redirected to the home page with successful registration

#### Status (Pass/Fail)<br>
Pass

#### Notes<br>
Validation conditions => <br>No fields allowed to be left empty<br>
username with a min of 5 characters and a max of 30 characters<br>
email in a valid email form<br>
password with a min of 5 characters and a max of 30 characters<br>
password confirmation with a min of 5 characters and a max of 30 characters, must match password

(Given any failed validation conditions, the same page is rendered and corresponding error msgs are displayed)

#### User Sample Test Run ->

Try => <br>Username:<br>
       Email: Aaron@gmail.com<br>
       Password: hahawhat<br>
       Password Confirmation: hahawhat<br>
       * Should fail the username validation for being empty

Try => <br>Username: Jon<br>
       Email: jonnyboy@blue.net<br>
       Password: as0<br>
       Password Confirmation: as0<br>
       * Should fail username and password validations, character lengths < 5

Try => <br>Username: goodMorning<br>
       Email: jonnyboy@blue.net<br>
       Password: 1111111111222222222233333333330000000000<br>
       Password Confirmation: 1111111111222222222233333333330000000000<br>
       * Should fail password and confirmation validation, character lengths > 30

Try => <br>Username: goodboy<br>
       Email: a@a.a<br>
       Password: imnotthere345<br>
       Password Confirmation: iamhere123<br>
       * Should fail the validation for non-match between password and password confirmation

Try => <br>Username: whatisUp9<br>
       Email: abc<br>
       Password: eeeek<br>
       Password Confirmation: eeeek<br>
       * Should fail email validation

Try => <br>Username: Aaron<br>
       Email: AaronIsEvil@gmail.com<br>
       Password: Unhappybaby<br>
       Password Confirmation: Unhappybaby<br>
       * Should pass the validations

#### Post-conditions<br>
User is validated with sign up form and passes all requirements for registration.<br>
User is added to the database and successfully registered as a user.<br>
User has their password protected with a hash function for security.<br>
<br>

### AUTOMATED TESTING
1. Validation for sign up form inputs
 - all fields must be non-empty
 - username, password and email must be strings
 - username, password and password confirmation must satisfy character length between 5 and 30 inclusive
 - email must satisfy email form
 - password must match password confirmation

2. Partial form doesn't create new user

3. New user added in db

4. User password is encrypted with hash function

--------

## UAT #2: Signed-In

#### Use case name
Verify login with valid username and password

#### Description
Test Gritter sign-in feature/page
    
#### Pre-conditions
A user exists in the user table with a given username and password\

#### Test steps
1. Navigate to sign-in (https://gritter-3308.herokuapp.com/signin)\
2. Enter the correct username/password (test: fred/password )\
3. Click sign in button -> should see homepage with "hello, fred" at bottom\
4. Navigate back to sign-in
5. Enter incorrect username/password (test: fred/wrongpassword)\
6. Should be taken back to sign in page. This indicates signin was not successful.\

#### Expected result
"Welcome to the Gritter Homepage!". Successful sign-in will navigate a user to the Gritter homepage.\
An incorrect username/password will direct the user back to the Signin page. \

#### Actual result
User is navigated to the homepage if credentials are correct.\

#### Status (Pass/Fail)
Pass

#### Notes
Attempting to sign in with incorrect credentials will take user back to the signin page.\

#### Post-conditions
Correct credentials give different behavior than incorrect credentials. \
Querying database with proper credentials leads to a successful sign-in.\
After sign in, homepage will say "Hello, (user)"

--------

## UAT #3: 'Likes', en masse

#### Use case name
A developer needs to be able to generate many 'likes' easily for testing logic and UI.

#### Description
A developer should be able to generate 'likes' on existing posts, en masse, with a couple of clicks.
This would help the developer and developer team be able to visualise and test the logic related to post likes.

#### Pre-conditions
This is intermediary functionality only for use during app development. It would be inappropriate to have this functinality available for non-developers in a public-facing app ready for production.

#### Test steps
1. Navigate a web browser to https://gritter-3308.herokuapp.com/likes
2. Click the 'Delete likes' button to delete all 'likes' currently in the database.
3. Click the 'Generate likes' button to generate 'likes' for posts (and users) currently in the database.

#### Expected result
Clicking 'Delete likes' should:
 - reload the https://gritter-3308.herokuapp.com/likes page (after removing all likes from the database, which won't be visible to the user).
 - When reloaded, an orange flash message should appear indicating the user deleted the likes. 
 - Also, no likes should be listed on the page (as they've been deleted)
 - Additionally, the same posts should remain when the page reloads even though likes are now gone.
 - The posts listed on the page should remain if the page is refreshed. 
 - Also, the flash message should be dismissible (by clicking the 'x' on the right)
 Clicking 'Generate likes' should:
 - reload the https://gritter-3308.herokuapp.com/likes page
 - When reloaded, a green flash message should appear indicating the user has created new likes. 
 - Also, the new likes should be listed on the page (as they've been added to the database)
 - Additionally, the same posts should remain when the page reloads as they have not been modified during like creation.
 - The posts and likes listed on the page should remain if the page is refreshed. 
 - Also, the flash message should be dismissible (by clicking the 'x' on the right)
The logic automating 'like' creation, identifies every post and every user, and 50% of the time has a user like a post. So like totals per post should reflect this logic.

#### Actual result
The page behaves as expected.

#### Status (Pass/Fail)
Pass

#### Notes
This functionality will be moved to testing features later, as the app progresses. Currently the app is in a developer-only state.

#### Post-conditions
N/A








