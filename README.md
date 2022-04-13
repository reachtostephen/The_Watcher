Welcome to "The Watcher"

We help you analyse Stock Market data of various NSE(National Stock of India Ltd.) companies.


Setting up the Project:
	
    • Make sure that GIT is installed in the system.
    • Clone the project using git clone command
      git clone https://github.com/reachtostephen/the-watcher.git .
    • Open the project files in Pycharm (Preferred) / Any Editor
    • Install pip packages listed in requirements.in
      Use, pip install -r requirements.in.
    • To update with the secondary dependencies installed, Update it using 
      pip install -r requirements.txt. Now you should have all dependencies updated.
    • In-case any error faced in last step, please run pip-compile command,pip-compile --annotation-style=line --output-file=requirements.txt requirements.in. Now run pip install -r requirements.txt again.
    • Setup is done!!

Project Structure:

There were 2 stages

    • Crawling the list of NSE companies data and posting them in a collection.
    • Listing the performance of the stocks into individual collections. 

Stage1 -->  NSE Companies:

    • The code for this NSE crawling is in path,
        ◦ utils/nse_crawl/nse_crawl/spiders/nse_spider.py
    • 	The crawled data for nse should create a collection nse_companies under Database The-watcher
    • To have this collection and database, 
          change directory to the watcher_crawl using cd utils/nse_crawl and run scrapy crawl nse_spider


Stage2 -->  Stocks of companies:

    • The code for this NSE crawling is in path,
        ◦ utils/nse_crawl/nse_crawl/spiders/nse_spider.py
    • 	The crawled data for nse should create 6 collections under Database The-watcher
              -> 'income_annual'
              -> 'income_quaterly'
              -> 'ratios'
              -> 'cash_flow'
              -> 'balance_sheet'
              -> 'company_details'
    • To have this collection and database, 
          change directory to the watcher_crawl using cd watcher_crawl and run scrapy crawl watcher_spider



          
	

			
    