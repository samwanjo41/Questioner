"""
meetups model
"""
# import date
from datetime import datetime

# assign meetups to an empty list
meetups_rec = []
rsvp = []
# create the meetup model class


class MeetupsModel():
    
    def __init__(self):
        self.db = meetups_rec

    def create_meetups(self, topic, happeningOn, location, images, tags):
        
        """
       Initialize the meetup class, with your variables at hand
        """
        payload = {
            "id": len(self.db) + 1,
            "topic": topic,
            "happeningOn": happeningOn,
            "location": location,
            "images": images,
            "tags": tags,
            "createdOn":  datetime.utcnow().isoformat()
        }
        self.db.append(payload)
        return payload

    def get_all_meetups(self):
        """Retrieves all  meetups"""
        return self.db

    def get_a_specific_meetup(self, id):
        """Retrieves a specific meetup"""
        meetup = [new_meetup for new_meetup in self.db
                  if new_meetup["id"] == id]
        return meetup

    def get_meetup_by_topic(topic):
        current_meetup = [meetup for meetup in meetups_rec if meetup["topic"] == topic]
        if current_meetup:
            return current_meetup
        else:
            return False

    def get_meetup_by_location(location):
        current_location = [location for location in meetups_rec if location["location"] == location]
       
        return current_location

    def get_meetup_by_date(happeningOn):
        current_date = [date for date in meetups_rec if date["happeningOn"] == happeningOn]
       
        return current_date


    def rsvp_for_meetup(self,meetup_id,topic,status,username):

        mitup = {
            "meetup_id":meetup_id,
            "topic":topic,
            "status": status,
            "user":username
        }
        rsvp.append(mitup)
        return mitup
     