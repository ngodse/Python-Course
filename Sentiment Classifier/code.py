punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
positive_words = []
with open("/Users/ngodse/eclipse-workspace/Neha/TestPy/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctutation(word):
    for c in word:
        if c in punctuation_chars:
            word.replace(c, "")
    return word 
def get_pos(sentence):
    sentence=sentence.lower()
    list_of_words=sentence.split()
    count=0
    for word in list_of_words:
        word=strip_punctutation(word)
        if word in positive_words:
            count+=1
    return count 
def get_neg(sentence):
    sentence=sentence.lower()
    list_of_words=sentence.split()
    count=0
    for word in list_of_words:
        word=strip_punctutation(word)
        if word in negative_words:
            count+=1
    return count 
result_file=open("output.csv","w")
result_file.write("Number_Of_Retweets, Number_of_Replies, Positive_Score, Negative_Score, Net_Score\n")
file=open("project_twitter_data.csv","r")
data=file.readlines()
for line in data[1:]:
    fullData=line.strip().split(",")
    text=fullData[0]
    retweets=fullData[1]
    replies=fullData[2]
    posScore=get_pos(text)
    negScore=get_neg(text)
    result_file.write(retweets+ ","+replies+","+str(posScore)+","+str(negScore)+","+str(posScore-negScore)+"\n")
result_file.close()
