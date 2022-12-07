class Solution:
    def reverseOnlyLetters(self, letters: str) -> str:
        alphabets = []
        for letter in letters:
            if letter.isalpha():
                alphabets.append(letter)
        # ab-cd => abcd


        new = []
        for idx in range(len(letters)):
            if letters[idx].isalpha():
                new.append(alphabets.pop())
            else:
                new.append(letters[idx])

        return "".join(new)
