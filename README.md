
# Questioner Application [![Coverage Status](https://coveralls.io/repos/github/samwanjo41/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/samwanjo41/Questioner?branch=develop) [![Build Status](https://travis-ci.org/samwanjo41/Questioner.svg?branch=develop)](https://travis-ci.org/samwanjo41/Questioner) [![Maintainability](https://api.codeclimate.com/v1/badges/8eeb2e020595e3956cc7/maintainability)](https://codeclimate.com/github/samwanjo41/Questioner/maintainability)


Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

# Preriquisites

- Python 3.6.7
- Postman


# Installation
1. Clone this repository
    https://github.com/samwanjo41/Questioner.git

2. CD into the project folder on your machine
    $ cd Questioner

3. Create a virtual environment
    

4. Activate the virtual environment
    $ source env/bin/activate

5. Install the dependencies from the requirements file
    $ pip3 install -r requirements.txt
    $ pip3 install python-dotenv

6. Run the application
    python run.py

# Testing API endpoints
| Endpoint                                  | HTTP Verb | Functionality                 |
| ----------------------------------------- | -------| ----------------------------
| api/v1/meetups	                        | POST       | Create a meetup record  |
| api/v1/meetups/<meetup_id>	            | GET      | Fetch a specific meetup record  |
| api/v1/meetups/upcoming	                | GET      | Fetch a specific meetup record |
| api/v1/questions	                        | POST       | 	Create a question for a specific meetup  |
| api/v1/questions/<question_id>/upvote	    | PATCH      | Up-vote a specific question  |
| api/v1/questions/<question_id>/downvote   | PATCH     | Down-vote a specific question |
| api/v1/meetups/<meetip_id>/rsvps	         | POST       | Create a question for a specific meetup |

# Authors
    Samuel Wanjohi

# License
