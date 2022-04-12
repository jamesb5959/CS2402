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

if __name__ == "__main__":
    url_list = ['http://www.gutenberg.org/files/215/215-h/215-h.htm', 'http://www.gutenberg.org/files/345/345-h/345-h.htm', 'http://www.gutenberg.org/files/1661/1661-h/1661-h.htm']
    
    # Get the first URL from the list
    url = url_list[0]    
    
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
                
    
    print('This is the first sentence:')
    print(sentence_list[0])
    print('This is the first word list:')
    print(word_lists[0])
            
