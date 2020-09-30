# Project title
Gritter, a Grep-Team Twitter clone with enhancements.

# Team members' names
Jason Weidner, Aaron Shyuu, Michael Shippee, Francis Kim

# Vision statement
Gritter is a social media platform that focuses on user experience. Users will be able to share short posts with each other, as well as be able to share links to articles, blogs, and videos. Users can follow other users in order to automate and customize their feeds. Our streamlined platform allows for easier navigation and less clutter, giving every user the ability to get to what really matters - connecting and sharing with other users.

In the app users will be able to:
- Login to an account using a password that is encrypted
- Read a feed of public tweets
- Tweet to their own feed (which also adds content to the public feed)
- Browse the feeds of other users
- 'Follow' other users (i.e. generate a feed from content authored by users they are 'following') 
- 'Like' tweets (a binary on/off like button)
- Reply to tweets
- Retweet tweets by others (i.e. add another's tweet to their own feed)
- Edit their own tweets (not a feature currently available in real Twitter)
- Delete their own tweets
- Create a filter for content that is viewable in their feeds
- 'Mute' content either by keyword, tweet location, tweet author

Tweets will be limited to 240 characters in length.

We will seed our database with real Twitter data, which includes the metadata required for some of the filtering features we'd like to implement. If time permits we can use the Twitter API to get real-time data. If time does not permit we will use static Twitter data to seed the database. Such data is available through data science competition websites and/or faculty sites used for academic purposes.

# Motivation
Our motivation is to build a foundation for fleeting social media that can be filtered and edited in ways more useful to users. Currently users of real Twitter cannot edit their tweets, nor can they filter content based on keywords in combination with geotagging. By building our own Twitter-like application, we will have a foundation where we can extend functionality to include machine learning and natural language processing features to improve content management by the user rather than the platform.

Additionally, Gritter is a relatively simple app that will have features sophisticated enough to meet project objectives. It will require development of several different database tables, with relationships between each. It will have a backend and frontend, and lends itself to development using an agile approach, which is important to the team. 

Gritter is easy to explain to new users and developers examining project results. Furthermore, Gritter can be a good discussion point in technical interviews later on.

# Risks to project completion
- Accomodating the skillsets across the team
- Navigating large time zone differences
- Managing technical scope to be achievable
- Successful management and prioritization of backlog will be critical

# Risk Mitigations
## Managing technical scope to be achievable
- 3 week-long sprints with weekly standups to ensure progress on priority user stories without getting stalled with roadblocks.
- Use Trello to track stories and backlog. 
- Asychronous communication to facilitate team updates within each week.
- Keeping features simple enough to be useful to users but easy enough for development timeframes (i.e. filter content rather than sophisticated ML modelling)
- Simplify database data if time constraints require it (i.e. use static data rather than connecting to the Twitter API)

## Navigating large time zone differences
- Leverage Slack/email for asynchronous communication
- Plan meetings (Zoom) at mutually achievable time
- Use github to asynchronously managing the code base: https://github.com/jasonweidner/twitter_clone
- Two out of four team members are located in US time zone while two are located in Asia/Pacific region - may be possible to progress around the clock. 

## Accomodating the skillsets across the team
- Choose a technology stack that is as simple as possible but not simpler than what is needed (Flask vs Django/Rails/Springboot)
- Choose a technology stack that leverages the interests and existing skills of the team (Python vs Ruby/Java)
- Most members have limited experience in web development and using frameworks so class material is supplemented with self-learning.
- We discussed the possibility of a Covid-related app, but decided against it because of the challenges associated with data mining/scraping data from existing sources.
- Distribute user stories among team members according to their knowledge, skill and web development experience.

# Development method
We will use a Scrum process with 3 week sprints, with standups weekly. While 1 week between standups is a long time, we will be sure to communicate with one another asynchronously to overcome roadblocks. At the end of the sprint, we will review the progress for each sprint with a sprint retrospective to assess sprint sizing and story definitions going forward. These reviews may occur asynchronously to accomodate the global distribution of team members.

Work flow of our Agile Software Development Methodology:
1. Create our product backlog on Trello - Decide the features and assign points based on difficulty
2. Decide on the features for the sprint - Based on implementation difficulty, presentation and dependency
3. Work on the features decided - Everyone will work on a specfic task 
4. Demonstration and Testing - Demonstrating progression of features and running unit-tested functionalities
5. Sprint Retrospective and plan for following sprint - Analyze the completed sprint to improve the next one
6. Repeat steps 2 to 5 until completion

# Project Tracking Software 
We will be using Trello to track user stories, sprints and general progress visually. In the first meeting, we elected Aaron as the Scrum Master for backlog management. For version control, all code will be managed through a collaborative, public, github repo.

Components of our Trello board with Kanban Methodology:
- Story backlog including all the features and assigned points
- General progress - To do, doing, done
- Issues and blockages
