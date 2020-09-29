# Project title
Gritter, a Grep-Team Twitter clone with enhancements.

# Team members' names
Jason Weidner, Aaron Shyuu, Michael Shippee, Francis Kim

# Vision statement
We aim to build a simple Twitter clone called Gritter.

In the app users will be able to:
- login to an account using a password that is encrypted
- read a feed of public tweets
- tweet to their own feed (which also adds content to the public feed)
- browse the feeds of other users
- 'follow' other users (i.e. generate a feed from content authored by users they are 'following') 
- 'like' tweets (a binary on/off like button)
- reply to tweets
- retweet tweets by others (i.e. add another's tweet to their own feed)
- edit their own tweets (not a feature currently available in real Twitter)
- delete their own tweets
- create a filter for content that is viewable in their feeds
- will 'mute' content either by keyword, tweet location, tweet author

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

## Accomodating the skills across the team
- Choose a technology stack that is as simple as possible but not simpler than what is needed (Flask vs Django/Rails/Springboot)
- Choose a technology stack that leverages the interests and existing skills of the team (Python vs Ruby/Java)
- Choose a project concept that is as simple as possible but not simpler than what is needed to meet project objectives
- We discussed the possibility of a Covid-related app, but decided against it because of the challenges associated with data mining/scraping data from existing sources.
- Distribute user stories among team members according to their knowledge, skill and previous experience.

# Development method
We will use a Scrum process with 3 week sprints, with standups weekly. While 1 week between standups is a long time, we will be sure to communicate with one another asynchronously to overcome roadblocks. At the end of the sprint we will review the progress for each sprint with a sprint retrospective, even if briefly, to assess sprint sizing and story definitions going forward. These reviews may occur asynchronously to accomodate the global distribution of team members.

# Project Tracking Software 
We will be using Trello to track stories, sprints and a story backlog. In the first meeting, we elected Aaron as the Scrum Master for backlog management. All code will be managed through a collaborative, public, github repo.
