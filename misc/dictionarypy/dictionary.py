import webbrowser as chrome
word = input('Find: ')

def look_up_word(word):
  url = "https://www.google.com.tr/search?q={}".format(word)
  chrome.open(url)
