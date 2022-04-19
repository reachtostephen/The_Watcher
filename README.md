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

    • Crawling Data using Scrapy
    • Setting the crawled data to a Database (.ipynb)

Stage1 --> Scrapy:

    • Data crawling code for stocks is in path watcher_crawl/watcher_crawl/spiders/watcher_spider.py
    • The crawled data is available in watcher.jl file
    • To run the watcher_spider file,
          change directory to the watcher_crawl using cd watcher_crawl and run scrapy crawl watcher_spider -O watcher.jl.
    • Now, watcher.jl should have all the crawled data.


    • Similarly We crawl the list of NSE companies.
    • The code for this NSE crawling is in path,
        ◦ utils/nse_crawl/nse_crawl/spiders/nse_spider.py
    • 	The crawled data for nse is available in nse.jl
    • To get the updated list, 
          change directory to the nse_crawl using cd utils/nse_crawl and scrapy crawl nse_spider -O nse.jl
    • Now, nse.jl should have the list of all NSE companies.



Stage2 --> ipynb notebooks:
		
    • ipynb notebooks were used for putting out data to a Mongo collections.
    • You should find 3 ipynb notebooks under path utils/ipynb_notebooks individually designated for its role with the collection in mongo.
    • company_stocks file meant to insert the stock details of sampled 5 companies, which saves its entries in 5 collections as 'income-annual', 'income-quaterly', 'ratios', 'cash-flow',,'balance-sheet’.
    • Similarly nse_companies file is used to insert the list of NSE companies and company_details used to lists the companies included for the stock data extraction.





          
	

			
    