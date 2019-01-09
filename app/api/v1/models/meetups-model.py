"""
meetups model
"""
#import date
from datetime import datetime

#assign meetups to an empty list
meetups_rec = []

#create the meetup model class
class MeetupsModel:
    def __init__(self):
        self.db = meetups_rec

    def create_meetups(self, topic, happenningOn, location, images, tags):
        
        """
       Initialize the meetup class, with your variables at hand
        """
        payload = {

        "id" = len(MEETUPS_LEN)+,
        "topic" = topic
        "happeningOn" = happenningOn
        "location" = location
        "images" = images
        "tags" = tags
        "created_at" = datetime.now()
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