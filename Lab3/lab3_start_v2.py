#CS 2302
#Bradley Beltran
#Lab 3
#Instructor: Olac Fuentes
#Teaching Assistant: Jose Perez
#Instructional Assistant: David Dominguez

# You will need to install BeautifulSoup4
# Open "Anaconda Prompt" and run the command "conda install bs4"
# Anaconda Prompt is installed along with Spyder when Anaconda3 is installed
import bs4 as bs
import urllib.request

lowercase = ''.join(chr(i) for i in range(97,123)) + ' '     

def get_words(st):
    st = st.lower()
    st = st.replace('\r\n', ' ')
    st = ''.join( c for c in st if  c in lowercase)
    words = st.split()
    return words

# we input the book we want
def book_input():
    v = input("Choose among the following books: \n 1) The Call of the Wild \n 2) Dracula \n 3) The Adventures of Sherlock Holmes \n Selection: ")
    if int(v) > 3 or int(v) < 1:
        print("No book exist.")
        quit() 
    return int(v)-1
# save our book input
book_input = book_input()

# prints the book chosen 
def book_chosen():
    book_list = ['The Call of the Wild', 'Dracula', 'The Adventures of Sherlock Holmes']
    print(book_list[book_input] + " was chosen")
    return book_list[book_input]

# saves the book chosen
book_chosen=book_chosen()

# we pick the word
def word_pick():
    word_search = input("Enter a word to search: ")
    return word_search.lower()

# we save the book and a dictionaries for words and sentence
word_pick = word_pick()
D_word ={}
D_sentence ={}
countSent=0
        
if __name__ == "__main__":
    url_list = ['http://www.gutenberg.org/files/215/215-h/215-h.htm', 'http://www.gutenberg.org/files/345/345-h/345-h.htm', 'http://www.gutenberg.org/files/1661/1661-h/1661-h.htm']
    
    # Get the first URL from the list
    url = url_list[book_input]
    # These are the lists where we will store the words and sentences
    word_lists = []
    sentence_list = []
    
    # Read the raw HTML from the URL
    data = urllib.request.urlopen(url).read()
    
    # Use BeautifulSoup to parse the HTML and extract the text
    soup = bs.BeautifulSoup(data,'html.parser')
    
    # Go through all the paragraphs in the HTML
    for paragraph in soup.find_all('p'):
    	# Get the text inside that paragraph
        par  = paragraph.string
        # If the paragraph is not empty
        if par:
            # Replace newlines with spaces
            par = par.replace('\r\n', ' ')
            # Split the paragraph into sentences by splitting using periods
            sent = par.split('.')
            # For each sentence in the paragraph
            for s in sent:
                sentence_list.append(s+'.')         
                words = get_words(s)
                word_lists.append(words)
                
                # we save the words and sentices in a word dictionary
                for i in words:
                    if i in D_word:
                        D_word[i] += 1
                        D_sentence[i] += [countSent]
                    else:
                        D_word[i] = 1
                        D_sentence[i] = [countSent]
                countSent+=1
    
    # we print the word count and the first 10 sentences  
        
    if word_pick in D_word:
        print("The word "+word_pick+" appears in "+str(D_word[word_pick])+" sentences in "+ book_chosen)
        D_sentence_count=0
        for i in D_sentence[word_pick]:
            if D_sentence_count == 10:
                break
            print(sentence_list[i])
            D_sentence_count+=1
    elif not word_pick in D_word:
        print("The word "+word_pick+" does not appear in "+ book_chosen)
    
    # this is a loop so we can go through it as many times as the user wants
    TorF_continue = True  
    while TorF_continue is True:
        word_search = input("Do you wish to continue y/n? ")
        if word_search is 'n':
            break
        word_pick = input("Enter a word to search: ")
        if word_pick in D_word:
            print("The word "+word_pick+" appears in "+str(D_word[word_pick])+" sentences in "+ book_chosen)
            D_sentence_count=0
            for i in D_sentence[word_pick]:
                if D_sentence_count == 10:
                    break
                print(sentence_list[i])
                D_sentence_count+=1
        elif not word_pick in D_word:
            print("The word "+word_pick+" does not appear in "+ book_chosen)