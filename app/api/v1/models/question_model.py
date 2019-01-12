from datetime import datetime

questions_list = []


class QuestionsModel(object):    
    def __init__(self):
        self.db = questions_list
    
    def create_questions(self, title, body, meetup, votes, createdBy):
        payload = {

            "id": len(self.db) + 1,
            "createdOn": datetime.now(),
            "createdBy": createdBy,
            "meetup": meetup,
            "title": title,
            "body": body,
            "votes": votes
        }

        self.db.append(payload)
        return payload

    def get_all_questions(self):
        """Retrieves all questions"""
        return self.db

    def get_a_specific_question(self, id):
        """Retrieves a specific question"""
        question = [new_quiz for new_quiz in self.db
            if new_quiz["id"] == id]
        return meetup

    