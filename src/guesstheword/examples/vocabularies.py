import random
from guesstheword.vocabularies import VocabularyBase


class RandomVocabulary(VocabularyBase):
    """
    Vocabulary example.
    Choose random word from choices.

    """
    CHOICES = (
        ('consider', 'Deem to be'),
        ('minute', 'Infinitely or immeasurably small'),
        ('evident', 'Clearly revealed to the mind or the senses or judgment'),
        ('commit', 'Perform an act, usually with a negative connotation'),
        ('issue', 'Some situation or event that is thought about'),
        ('establish', 'Set up or found'),
    )

    def get_word_and_hint(self):
        return random.choice(self.CHOICES)
