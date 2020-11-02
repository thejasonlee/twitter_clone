
# Registration
### USER ACCEPTANCE TESTING
Use case name
    User creates account with username and password
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
1. 

2. Sign-in *can* access Post form








