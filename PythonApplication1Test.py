"""
1. Describe project 2.Use open to open .txt file and store it as a string variable 3.create set, starting index, start char, end char
4. for loop to iterate through .txt file, use enumerate to find char and index 5. create dictionary to story key:value pairs for
words to replace 6. use for loop to ask user for replacement words 7.use for loop to replace all words 8. print the .txt file
"""

"""
In the <adjective1>land of <place>, a <animal> was feeling <emotion>. The <animal> lost its <object>.

Suddenly, a <character> appeared. "I will help you find your <object>,' they said.

Together, they journeyed through <terrain> and faced the <weather_condition>. Finally, they found
the <object> in a <place2>. The <animal> was so <emotion2> and thanked the <character>. They lived <adverb> ever after.
"""

#1. Description: Madlibs generator takes a .txt file and replaces specific keywords to any keyword of the users input

#2. Openu sing open and store it in string variable
with open("story.txt") as f:
    story = f.read()
    
#3.Create set, starting index, starting char and ending char
words = set()
starting_index = -1
target_start = "<"
target_end = ">"

#4. Use for loop and enumerate to take out index and char
for i, char in enumerate(story):
    #find starting char and index
    if char == target_start:
        starting_index = i
    #find end
    if char == target_end and i != starting_index:
        #store the word in a variable
        word = story[starting_index: i +1]
        words.add(word)
        starting_index = -1
        
#5. create dictionary for key-value pairs in order to replace words
answers = {}

#6. Use for loop to ask user to input words as replacement
for word in words:
    #ask user for replacement
    answer = input("Please enter a replacement for " + word + ":")
    answers[word] = answer
    
#7. Replace all words with user input
for word in words:
    story = story.replace(word,answers[word])
    
#8. Print
print(story)
    
        
        
        
