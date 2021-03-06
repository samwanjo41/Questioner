from datetime import datetime

questions_list = []


class QuestionsModel(object):    
    def __init__(self):
        self.db = questions_list
    
    def create_questions(self, title, body, meetup_id, votes):
        payload = {

            "id": len(self.db) + 1,
            "createdOn": datetime.now(),
            "title": title,
            "body": body,
            "votes": votes,
            "meetup_id": meetup_id
           
        }

        self.db.append(payload)
        return payload

    def get_all_questions(self):
        """Retrieves all questions"""
        return self.db

    def get_a_specific_question(self, id):
        """Retrieves a specific question"""
        question = [new_quiz for new_quiz in questions_list
            if new_quiz["id"] == id]
        return question

    def upvote(self, question_id):
        """ Function to upvote question """
        for question in questions_list:
            if question['id'] == id:
                question['votes'] = question['votes']+1

            return question

    def downvote(self, question_id):
        """ Function to upvote question """
        for question in questions_list:
            if question['id'] == id:
                question['votes'] = question['votes']-1


            return question


    

