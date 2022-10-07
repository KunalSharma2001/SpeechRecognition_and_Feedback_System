# import library
import language_tool_python
import speech_recognition as sr

my_tool = language_tool_python.LanguageTool('en-US')


def convert_text_to_list(string):
    li = list(string.split(" "))
    return li


def check_grammar(my_text):
    my_matches = my_tool.check(my_text)
    myMistakes = []
    myCorrections = []
    startPositions = []
    endPositions = []

    # using the for-loop
    for rules in my_matches:
        if len(rules.replacements) > 0:
            startPositions.append(rules.offset)
            endPositions.append(rules.errorLength + rules.offset)
            myMistakes.append(my_text[rules.offset: rules.errorLength + rules.offset])
            myCorrections.append(rules.replacements[0])

        # creating new object
    my_NewText = list(my_text)

    # rewriting the correct passage
    for n in range(len(startPositions)):
        for i in range(len(my_text)):
            my_NewText[startPositions[n]] = myCorrections[n]
            if startPositions[n] < i < endPositions[n]:
                my_NewText[i] = ""

    my_NewText = "".join(my_NewText)

    # printing the text
    # print(my_NewText)
    return list(zip(myMistakes, myCorrections))



r = sr.Recognizer()

# recognizing the audio and converting it into the text using the SpeechRecognition Module
with sr.AudioFile('audio6.wav') as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
        # raising error if there is some problem in converting the speech
        print('Please record you voice again...')

filer_words = ["hello", "umm", "features"]
pauses = ["  ", "   ", "    ", "     ", "      ", "       "]
res = []
res1 = []

# putting the words that math the filler word list in the result list
for k in convert_text_to_list(text):
    if k in filer_words:
        res.append(k)


print([index for index, ele in enumerate(convert_text_to_list(text)) if ele == pauses])
print(res)
print(check_grammar(text))
# print(res1)
