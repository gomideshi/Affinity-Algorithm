import urllib
import mechanize
import re

#BROWSER AGENT SETTINGS
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-Agent', 'Chrome 3.2')]

#BROWSER DEBUG CODES - SET TRUE FOR ADDITIONAL INFO
browser.set_debug_http(False)
browser.set_debug_redirects(False)
browser.set_debug_responses(False)

#TITLE
print ' _    _  _____  ______ ___  _____ '
print '| |  | ||  ___||___  //   ||  _  |'
print '| |  | ||___ \    / // /| | \ V / '
print '| |/\| |    \ \  / // /_| | / _ \ '
print '\  /\  //\__/ /_/ / \___  || |_| |'
print ' \/  \/ \____/ \_/      |_/\_____/\n'

print '----------------------------> INFO'
print '* Quote Catcher'
print '* w5748\robotarmy\quotebank.txt' + '\n'

print '---------------------------> NOTES'
print '* SUPPORTED PLATFORMS:'
print '+ http://ThinkExist.com'
print '+ http://BrainyQuote.com'
print '+ http://GoodReads.com'
print '+ http://QuotesDaddy.com'
print '+ http://WorldOfQuotes.com' + '\n'

#LOOP
repeat = 'y'  
while repeat == 'y':

    #POINT BROWSER
    DIRECTORY = raw_input("ENTER DIRECTORY URL: ")
    browser.open(DIRECTORY)
    htmlback = browser.response().read()

    #URL DETECTION
    if 'thinkexist.com/quotations' in DIRECTORY:
        thinkexist_schema = re.compile(r'.html">(.*?)</a>&rdquo;')
        items=re.findall(thinkexist_schema,htmlback)

    if 'thinkexist.com/quotes' in DIRECTORY:
        thinkexist_schema = re.compile(r'&ldquo;(.*?)&rdquo;')
        items=re.findall(thinkexist_schema,htmlback)
        
    if 'brainyquote' in DIRECTORY:
        brainyquote_schema = re.compile(r'<span class="bqQuoteLink">.*">(.*?)</a></span><br>')
        items=re.findall(brainyquote_schema,htmlback)
        
    if 'goodreads' in DIRECTORY:
        goodreads_schema = re.compile(r'&ldquo;(.*?)&rdquo;')
        items=re.findall(goodreads_schema,htmlback)

    if 'quotesdaddy' in DIRECTORY:
        quotesdaddy_schema = re.compile(r'&ldquo;(.*?)&rdquo;')
        items=re.findall(quotesdaddy_schema,htmlback)

    if 'worldofquotes' in DIRECTORY:
        worldofquotes_schema = re.compile(r'<p itemprop="text">(.*?)</p>', re.DOTALL)
        items=re.findall(worldofquotes_schema,htmlback)
    
    #PURGE TERMS
    substitutions = [
        ('<i>', ''),
        ('</i>', ''),
        ('<em>', ''),
        ('</em>', ''),
        ('<br>', ''),
        ('<br/>', ''),
        ('<br />', ''),
        ('<bold>', ''),
        ('</bold>', ''),
        ('<strong>', ''),
        ('</strong>', '')]

    #WRITE OUT    
    for x in items:
        for search, replacement in substitutions:
            x=x.replace(search, replacement)
            x=x.strip()
        print 'MINED: ' + x + '\n'
        handle = open("quotebank.txt", "a")
        handle.write(x+"\n")
        handle.close()

    repeat = raw_input("NEW SCRAPE? y/n ")
    print '\n'
