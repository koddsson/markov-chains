import sys
import random


class MarkovChain:
    def __init__(self, filename):
        # Let's build our chain.
        self.data = dict()
        with open(filename, 'r') as f:
            cleaned_string = (f.read().replace('\r\n', ' ').replace(',', '')
                              .replace(';', ''))
            words = cleaned_string.split(' ')

            for idx in range(0, len(words)):
                try:
                    key = words[idx] + ' ' + words[idx+1]
                except IndexError as e:
                    break
                try:
                    third_word = words[idx+2]
                except IndexError as e:
                    third_word = []
                if key in self.data:
                    self.data[key].append(third_word)
                else:
                    self.data[key] = [third_word]

    def getRandomSentance(self):
        random_key = random.choice(self.data.keys())
        random_value = self.data[random_key]
        current_key = random_key

        s = [current_key]

        while(current_key in self.data):
            random_value = random.choice(self.data[current_key])
            s.append(random_value)
            if len(random_value) == 0:
                break
            current_key = current_key.split(' ')[1] + ' ' + random_value
        return ''.join(map(lambda x: str(x) + ' ', s))

if __name__ == '__main__':
    filename = sys.argv[1]
    markovChain = MarkovChain(filename)
    print markovChain.getRandomSentance()
