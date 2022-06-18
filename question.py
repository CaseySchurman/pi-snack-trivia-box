class Question:
    """
    Model class for questions we pull from opentdb.
    """
    
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer