questions_list = []

class quiz(object):    
    def __init__(self):
        self.db = questions_list
    
    def create_questions(self, title, question, user, meetup):
        query = {

        "questionId" = len(self.db)+1
        "user" = user
        "meetup" = meetup
        "title" = title
        "question" = question
        }

        self.db.append(query)
            return query

    def get_all_questions(self):
        """Retrieves all questions"""
        return self.db

    def get_a_specific_question(self, id):
        """Retrieves a specific question"""
        question = [new_quiz for new_quiz in self.db
                  if new_quiz["id"] == id]
        return meetup

    