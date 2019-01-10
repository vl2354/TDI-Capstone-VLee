
# Capstone Project: Veronica Lee
***

### Agenda: 
1. Business objective
1. Data ingestion
1. Visualizations
1. Demonstration of at least one of the following:
   * Machine learning
   * Distributed computing
   * An interactive website
1. A deliverable



### 1. Business Objective: 

>The project should have a clear and demonstrable business objective.  This may be direct, building a product for consumers, or indirect, conducting analysis to improve the business of a company or government.  It should be clear who the user of the product is, and how they will gain a benefit from the product.

1. Objective:
     - Identify the risk appetite of CEO of the NYSE Public companies in given time frame, using **[Regulatory Focus theory](https://en.wikipedia.org/wiki/Regulatory_focus_theory)**.
     - Examine if CEO's risk appetite impacts on his/her company M&A activities in terms of (1) values of M&A (2) counts of M&A
     - _(tentative)_ Find how CEO's risk appetite-driven M&A activities impact on company values.  
     <br>
1. Audience: Business Exectuvies before M&A decisions <br>
<br>
1. Research Question/Hypothesis:
    - Does CEO's risk appetite impact on his/her M&A decision? 
    - If yes, how does the M&A decision impact on the firm-value? 



### 2. Data Ingestion: 

>The project should involve data processing beyond simply loading an existing data set.  This may involve gathering data through web scraping or API calls, combining and harmonizing data from multiple sources, or non-trivial processing of existing data sets.  Those projects using existing data sets should endeavour to find a unique perspective on that data.  The amount of data being processed is highly dependent on the project itself.  Many exemplary projects work with a gigabyte or more of data.

1. Data 1: Shareholder letters written by CEO 
   - Collect PDF/word version of Shareholder letters; 
   - Wrangle them into text/lists; 
   - Create a dictionary determining the risk appetite of the CEO by counting the promotion/prevention foci words used by CEO
   <br>
   <br>
2. Data 2: M&A data of the CEO's company _as an indepent variable_
   - Collect CEO's company's M&A activities by searching acquired company information in given time frame; 
   - Count M&A activities per company by year; 
   - Calculate M&A value (i.e., money spent for M&A activitieys) per company by year 
   <br>
   <br>
3. Data 3: Event Study _as a moderator variable_
   - [Fama&French three-factor model benchmark](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html#HistBenchmarks)
   <br>
   <br>
4. Data 4: CEO biographic data/stock option grant in RDMBS _as a control variable_ 

### 3. Visualizations: 

>The project should contain at least two distinct types of visualizations.  
Types of visualizations include line plots, scatter plots, maps, connection graphs, low-dimensional projections of data, and word clouds.  Distinct types of interactivity are also acceptable.  These may be produced with tools such as Matplotlib, Seaborn, Pandas, Bokeh, ggplot, D3.js, or others.

- Promotion/Prevention Foci Frequency [Reference:](https://github.com/JasonKessler/scattertext) ![plot](https://camo.githubusercontent.com/86c5fe96707b9e1dfc9618d2b04aca4df94b053d/68747470733a2f2f6a61736f6e6b6573736c65722e6769746875622e696f2f32303132636f6e76656e74696f6e73302e302e322e322e706e67)
- M&A value/count visualization 
- CEO's risk appetite visualization by sector [Reference](https://www.sciencedirect.com/science/article/pii/S2210670716301135)![plot2](https://ars.els-cdn.com/content/image/1-s2.0-S2210670716301135-gr7.jpg)
- Regression visualization



### 4. Data Science techniques

>* Machine Learning: The project should include the creation and use of one or more machine learning models.  The project must involve two or more of the following topics: regression, classification, unsupervised learning, cross validation, analysis of feature importance, anomaly or outlier detection, deep learning, ensemble models, feature engineering, time series analysis, and natural language processing.
>* Distributed Computing: The project should involve some distributed analysis of the data.  This may involve processing in MapReduce, Spark, or another framework on top of Hadoop.  Other frameworks may be approved at the instructors’ discretion.
>* Interactive Website: The project should result in a website that allows users to interact with the data.  This may be in the form of an interactive exploration of the data or customized recommendations or predictions for users.  This interactivity may be client-side, via Javascript, or server-side, via Flask or another web framework.


### 5. Deliverable: 

>A deliverable should describe the work performed on the capstone as well as its primary results.  This deliverable may take the form of (a portion of) a website, a Jupyter notebook, or some other type of document.  It should describe the tools used, the process of data ingestion and analysis, and the major results.  It should also include or link to the visualizations of point 3.  In-depth descriptions are not necessary, but the technical reader should be able to appreciate all of the steps involved.

