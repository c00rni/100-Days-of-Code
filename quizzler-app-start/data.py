from requests import get 

class QuestionGenerator:

    def __init__(self, categorie=18, number=10) -> None:
        self.setQuestion(categorie=categorie, number=number)

    def setQuestion(self, categorie=18, number=10):
        payload = {'amount': number, 'category': categorie, 'type': "boolean"}
        response = get(f"https://opentdb.com/api.php", params=payload)
        self._question_data = response.json()["results"]

    def getQuestions(self):
        return self._question_data
    