INTRODUCTION
============

BACKGROUND
~~~~~~~~~~
Automated Health Research Portal, is a project that will be based on the 
concept of **Knowledge Translation**. The Canadian Institutes of Health Research 
(CIHR) in 2000, defined Knowledge Translation as:

    *[The] exchange, synthesis and ethically-sound application of knowledge—within 
    a complex system of interactions among researchers and users—to accelerate the 
    capture of the benefits of research for Canadians through improved health, more 
    effective services and products, and a strengthened health care system.*

Though the definition is focused on the Canadians, 
its concepts, models and applications can be applied in any other part of the world.

The origin of Knowledge Translation related activities dates back to the 1910s to 
address the underutilization of scientific findings in the health sector. 
Keeping up with information in real-time was one of the major issues that was being 
addressed. This underutilization of healthcare related research has remain unsolved 
until recent decades. Grimshaw et al. state that, despite billions of dollars each 
year spent in both public and private sectors on education and research in health and 
medicine, the healthcare system has failed to bring cost-effective services to a portion 
of those who need them. Grimshaw et al. hold the belief that people fail to benefit 
optimally from scientific and medical advances.

As a result of this, research has been done on how to improve the utilization of 
research and many tools have been put forward to do that. One of the proposed tools is 
Knowledge Translation. Knowledge Translation activities include: transferring of research 
findings to healthcare providers, such as doctors, who then apply the knowledge to 
healthcare consumers who are the patients. In a broader sense, this research finding can 
be used by policy makers to implement rational policies that have been backed by credible 
research.

Knowledge Translation has gained a lot of traction over the years. International organizations 
such as the World Health Organisation have encouraged and sponsored its implementation. 
In countries like Iran their Ministry of Health and Medical Education and major universities 
have taken up the challenge and supported any implementation put forward on Knowledge Translation.

**Take a look at the following scenarios:**

    #) It's a busy day in your office, and you are running behind schedule. Your patient with 
       arthritis of the knee greets you with a small stack of printouts from the Internet on 
       glucosamine. She wants to know whether taking this medicine would be beneficial.

    #) You're in the emergency department, managing a patient with unstable angina. 
       You wonder whether the current evidence would support combining a glycoprotein 
       IIb/IIIa inhibitor with low-molecular-weight heparin in this case.
       From the above scenarios we can conclude that it is important for doctors to 
       find reliable research that has been used, proven and reviewed by other doctors 
       in near real-time to help their patients.

This project is a technology-based implementation of the concepts of Knowledge Translation 
that will address the underutilization of the extensive and intensive research done in the 
health sector by mining health researches from a wide range of online sources, sorting them out
and put them in easily identifiable categories. I will be collaborating with Professor Peter Wagacha Waiganjo.


PROBLEM STATEMENT
~~~~~~~~~~~~~~~~~
Over the years, there has been an exponential growth in the number of research done in the 
healthcare sector. These research is extensive and intensive and is focused on the various 
fields and diseases in the industry. However, despite all the available research there has 
been major issues connected to the ineffective healthcare system such as:

    * Ineffective continuing education for health professionals.
    * Increasing complexity of medical procedures and treatments.
    * Inadequate application of evidence to case management.
    * Lack of adequate communication between researchers and policy makers.
    * Physicians are faced with a rapid and voluminous accumulation of new findings, 
      making it increasingly difficult to follow current knowledge and integrate it into practice.

OBJECTIVES
~~~~~~~~~~
This project’s objectives are based on two broad topics:

    #) RESEARCH OBJECTIVES

       * Research on the topic of Knowledge Translation.
       * Research on the application of knowledge based systems in the field of Knowledge Translation.
       * Research on credible sources of researches.
       * Research on how researches in the medical field are reviewed.

    #) SYSTEM DEVELOPMENT OBJECTIVES

       * To dig for the requirements and analyse them keenly.
       * To carry out system analysis and design activities 
       * using the various available tools such as Data Flow Diagrams.
       * To test, implement and document:

            * a relational database to store the information - Postgresql.
            * web scraper to automate the collection of researches - BeautifulSoup 
            * Full-Text Search to index the information for fast and accurate search results
            * a review mechanism for users to review information based on its usefulness and applicability.

.. raw:: latex

    \newpage

RESEARCH TOPICS
~~~~~~~~~~~~~~~
The first research topic will be on Knowledge Translation. This research will help understand the 
procedures followed in writing and publishing of research in the health sector that will be useful 
in designing the web scraper. Understanding in depth the concept, model and origin of Knowledge 
Translation will be one of the goals of this research. This will give a broader understanding of 
the concept and its barriers and the various solutions made over the years with regard to this topic. 
Moreover, knowledge in this field has over the years gotten attention by global organisations such as 
the World Health Organisation (WHO).

The second research topic will be on the application of knowledge based systems in Knowledge 
Translation. The research will be aimed at finding out if any, a knowledge-based system that has 
implemented this. The research will look at how best to store this knowledge taking into 
considerations the standards that have been set in this field. Identifying and learning the 
shortcomings of the said implementation and how best to overcome them and exploration on any other 
feasible implementation available will be part of the goals of this research.

The third research topic is to identify credible sources of health research data from the internet.
This will enable the project to fetch researches that are deemed relevant, useful and trusted by 
experts in the medical field.

The fourth, and last research topic is to understand how research reviewers review health publications
in order to create a smart review module for the users of this system. This involves looking at experts
checklists and integrating them with the system.

PROJECT JUSTIFICATION
~~~~~~~~~~~~~~~~~~~~~
The project will build a bridge the gap between researchers and users of these researches - medical practitioners, 
patients, researchers and policy makers. By translating knowledge and bringing it closer to them, 
they will be able to utilise the credible research available to improve the health care system and benefit all the players.


LITERATURE REVIEW
=================

The literature review is presented in several subsections namely: the concept of digital preservation and 
institutional repositories; concepts and keywords used in disease categorization and metrics of reviewing health researches.

THE CONCEPT OF DIGITAL PRESERVATION AND INSTITUTIONAL REPOSITORIES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Over the recent years the world has seen an increase in Digital Preservation. Digital preservation refers
to the overall approach to preserving information and appraisal of digital information over its entire
life cycle. There has been a growing awareness of the importance of digital preservation that has led
to the development of many approaches that deal with the said topic. Some examples of approaches
developed are migration and emulation. Migration is where by an object is transformed into widely
accessible representations. Emulation is where by a technical environment is created where objects can
be rendered or performed.Kenya, despite the many challenges in digital preservation, has made strides
towards the right direction with a lot of digital preservation present in most Kenyan universities.
 
Digital preservation leads to digital repositories. Digital repositories are information systems that
ingest, store, manage, preserve and provide access to digital content. There are several types of digital
repositories such as: institutional, disciplinary, government and centralized repositories. The scope of
this project focuses on institutional repositories which have several purposes - they support
scholarly communication and provide open access to articles, dissertations and research data and provide
platforms for storing and preserving the digital master files created as a result of digitization projects.
 
Most IRs in Kenya are owned by universities. These include University of Nairobi, Kenyatta University,
Jomo Kenyatta University of Agriculture and Technology, Moi University, Egerton University, Maseno University,
the Technical University of Kenya among other universities. Of all the universities in Kenya, UoN, KU, SU, PU,
JKUAT and DeKUT are some of the universities who've had their IRs listed in the worldwide directory of IRs. As
such they provide a good candidate of research information to be utilised by this project. UoN, moreover, has
the largest repository in terms of the total item count. Therefore, it provides adequate research information on
various topics include health research. Other universities IRs will work as supplementary sources.
 
With the growth in digital preservation, comes the need to make use of all this information. There
has been many attempts and tools brought forward to help people utilize these information for better
decision making and living standards. Some of them include *data mining* and *natural language processing*.
Data mining is defined as the practice of examining large pre-existing databases in order to generate new
information. NaturalLanguage Processing is a subfield of linguistics, computer science, information engineering,
and artificial intelligence concerned with the interactions between computers and human languages, in
in particular how to program computers to process and analyze large amounts of natural language data.
 
 
CONCEPTS AND KEYWORDS USED IN DISEASES CATEGORIZATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Researches have been categorized based on the diseases they address. These categories follow ICD-10 guidelines.
ICD is the foundation for the identification of health trends and statistics globally, and the international 
standard for reporting diseases and health conditions. It is the diagnostic classification standard for all 
clinical and research purposes. According to a history from the WHO the first international classification 
edition, known as the International List of Causes of Death, was adopted by the International Statistical 
Institute in 1893.

WHO was entrusted with the ICD at its creation in 1948 and published the 6th version, ICD-6, that incorporated 
morbidity for the first time. The WHO Nomenclature Regulations, adopted in 1967, stipulated that Member States 
use the most current ICD revision for mortality and morbidity statistics. The ICD has been revised and published 
in a series of editions to reflect advances in health and medical science over time.

ICD-10 was endorsed in May 1990 by the Forty-third World Health Assembly. It is cited in more than 20,000 scientific 
articles and used by more than 100 countries around the world. A version of ICD-11 was released on 18 June 2018 to allow 
Member States to prepare for implementation, including translating ICD into their national languages. ICD-11 will be 
submitted to the 144th Executive Board Meeting in January 2019 and the Seventy-second World Health Assembly in May 2019 
and, following endorsement, Member States will start reporting using ICD-11 on 1 January 2022. 

METRICS OF REVIEWING HEALTH RESEARCHES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Health Research Portal users have the ability to recommend and give review comment(s) on the relevance and
usability of a research paper. Most exert research reviewers usually have checklists that they review a
paper with. This same idea is used in the system to provide a scientific checklists for user to mark
after recommending a research paper. The checklist used is adapted from Academic Medicine (APPENDIX 1, 2001). The paper
provides an extensive list of items to look at based on the research paper topics such as: Problem statement,
conceptual framework and research questions, references to the literature and documentation, relevance,
research design, instrumentation, data collection and quality control, population and sample, data analysis
and statistics, reporting of statistical analyses, presentation of results, discussion and conclusion,
title, authors and abstract, presentation and documentation and scientific conduct.

SIMILAR WORK DONE BEFORE
~~~~~~~~~~~~~~~~~~~~~~~~
Some similar work done before include:

    #) WHO Global Observatory on Health R&D

       The WHO Global Observatory on Health R&D is a centralized and comprehensive source of 
       information and analyses on global health R&D activities for human diseases.

       It builds on existing data and reports from a wide range of data sources and gathers new 
       information (where needed and feasible) with the aim of enabling decisions on pritorites in R&D.

    #) IBM Watson

       Watson is a tool that brings AI tools and apps to your data wherever it resides. One of the 
       many things that it can do is to accelerate research and discovery. 

PROPOSED SYSTEM FOR DEVELOPMENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Automated Health Research Portal combines various tools in the field of Computer Science to help in
the utilization of digitally preserved information. The proposed system works in the realm of health
research, following the idea of Knowledge Translation.
 
The proposed system aggregates the following concepts:
 
   #) Data mining.
 
      The system automates the process of retrieving health research from various certified
      repositories such as the University of Nairobi eRepository. It mines for the research
      that are then categorized based on the disease that is being researched on (e.g **Cancer**).
 
   #) Natural Language Processing.
 
      The text in a mined research is then processed using the process of document classification
      to get similarities between the research and others that have been mined and categorized. 
      With these similarities the research are similar are then grouped together different from those
      that are different. These grouping put similar information together making it easier for users to
      use the information (e.g **under Cancer, research based on the *type of cancer* will be in
      one group and research based on the *diagnosis of cancer* in another grouping**).
 
   #) Full Text Searching.
 
      To make it even more easier for users to get information, the system will involve a Full
      Text Search service to help get information faster in the mined research.
 
   #) Reviewing
 
      The system will allow user interaction, that is, users of the system can recommend a research to other users.
      The mined and processed research will be ordered according to their relevance and the number. Relevance
      will be determined by the number of recommendations a research gets from its users. Moreover, users can
      start a discussion thread on a research and reply to discussions started by other users thus enabling 
      communication on the research results.
 

METHODOLOGY
===========

SYSTEM ANALYSIS
~~~~~~~~~~~~~~~

COLLECTION OF DATA
*******************
Target users identified for this project include but not limited to: healthcare staff such as
doctors and nurses, lecturers and students in healthcare related fields, researchers,
policy makers and other stakeholders. From the pool of target users, a small group of users
was identified which include needer groups and extreme users. Requirements were solicited
from the groups through the following methods:
 
**1. Frequent communications and informal interviews.**
Communications and interviews with the target users of the system provided very useful insights. It was evident that
due to the busy nature of their profession, they needed a fast and reliable way to access information
from research and publications. They also identified that one of their most preferred sources of information is from
the various university repositories. The proposed system would not only be efficient to them but would be a provide a good
knowledge base that would act as an enabler for their continuous learning.
 
**2. Online documentation**
The internet provides a very good source of data on any information. Data was collected from several online documentations
on the concepts of knowledge translation and its importance. Moreover, sentiments from comments from the internet community provided
insights on the existing gap between stakeholders in the healthcare industry and the access to health related researches and
publications.
 
**3. Existing systems**
The growing number of university repositories provided a lot of useful information. These repositories have a vast collection
of researches and publication which is useful, however, these repositories contain a lot of data, some of which may be outdated, thus
they have information overload. Secondly, they do not pay attention to the nitty gritties of categorizing a single research. It is
not uncommon to find a research about Typhoid under the Cancer category.
 
From the aforementioned sources, the requirements solicited helped identify the problems cause by the gap between healthcare shareholders
and the existing healthcare related researches that are being solved by the project which are:
 
   * Ineffective continuing education for health professionals.
   * Increasing complexity of medical procedures and treatments.
   * Inadequate application of evidence to case management.
   * Lack of adequate communication between researchers and policy makers.
   * Physicians are faced with a rapid and voluminous accumulation of new findings,
     making it increasingly difficult to follow current knowledge and integrate it into practice.
 

ANALYSIS OF COLLECTED DATA
***************************
The information collected has been analysed and interpreted resulting to use case diagrams.
The system actors include:
 
  * Sources of researches (repositories)
  * System users (Doctors, health researchers, health policy makers etc.)
 
The activities that are done to the sources of researches include:
 
  * Mining the research and publications data
  * Processing the collected researches using Natural Language Processing
  * Adding the processed researches to their respective smart categories
 
The activities that are done by the system user include:
 
  * Signing in/logging in to the system
  * Identification and selection of a research
  * Recommendation of a research
  * Starting a discussion on a research
  * Replying to a discussion started by another user

.. raw:: latex

    \newpage

**General Automated Health Research Portal Use Case Diagram**

.. image:: images/usecase.png
   :alt: Use case diagram
   :width: 500

*Figure 1: Automated Health Research Portal Usecase Diagram*

.. raw:: latex

    \newpage


FUNCTIONAL REQUIREMENTS
***********************
 
Functional requirements of the system include:
 
#) Scrape researches from repositories and organise them in categories based on ICD-10 classification
#) Allow users to discuss on scraped researches
#) Allow users to comment on other user's Discussions
#) Allow users to recommend and "unrecommend" a research
#) Order the scraped researches according to the number of recommends they get
#) User management
     - Registering new users
     - Password management
     - Sorting out researches recommended by a user
#) Search functionality to easily find a research
 
NON-FUNCTIONAL REQUIREMENTS
****************************
 
The system also provides non functional requirements such as:
 
#) Security - User data requested by the system should  be securely stored and should not be maliciously exposed.
#) Reliability - Users of the system should be able to rely on the information found in the system as it deals with the health sector where accuracy is very critical.
#) Availability - The system should be up and running when a user is in need of it.
#) Maintainability - The implementation of the system should make it easy for the developer or any other maintainer to maintain it with ease to ensure its efficiency.
#) Scalability - The system should be able to scale both horizontally and vertically with ease.
#) usability - Users should be able to intuitively use the system without any difficulties.
 

FEASIBILITY STUDY
*****************
**1. Technical feasibility**
Technical feasibility assesses the details of how a developer intends to use available materials and
determines whether the project can be implemented using the available technology. This project is technically
feasible as all the technology required to implement it are available. These technologies include; Laptop, Python/Django
Language, Postgresql, Github, CircleCI, Pytest, Google Cloud Platform etc. No hardware resources are needed for this project.
 
**2. Economic feasibility**
A system is considered to be economic feasible if the expected benefits accrued are greater than the
cost of undertaking the project. All the software used in developing this system is open source thus
no costs are incurred while using the. This makes the project economically feasible. Moreover, with access to fast and reliable
health related research then the benefits to the health sector are many.
 
**3. Resource feasibility**
All the resources used in this project were open source, thus there was no cost used by the resources in this project.
The project has resources feasibility.

.. raw:: latex

    \newpage

SYSTEM DESIGN
~~~~~~~~~~~~~

ARCHITECTURAL DESIGN
********************

The system uses a **client-server** architectural design. This design consists of two parties; 
a server and multiple clients. The server provides services to multiple client components. 
Clients request services from the server and the server provides relevant services to those clients. 

.. image:: images/client-server.jpeg
  :alt: client-server architectural design

*Figure 2: The application is hosted by Google Cloud servers from where it is accessible by multiple clients.*

LOGICAL DESIGN
**************

The logical design of the system is the abstract representation of the data flows(procedures),
inputs(sources), outputs(destinations) and data stores(database) of the system.

Data flow diagrams and Entity-Relationship diagrams have been used to represent the systems logical design.

E-R DIAGRAM
***********

.. image:: images/ERD.png
   :alt: ERD

*Figure 3: Automated Health Research Portal Entity Relationship Diagram*

.. raw:: latex

    \newpage

DATA FLOW DIAGRAMS
******************

.. image:: images/Context-level-DFD.png
   :alt: Context-Level-Diagram

*Figure 4: Automated Health Research Portal Context Level Diagram*

.. image:: images/level-1-DFD.png
   :alt: Level one context diagrams

*Figure 5: Automated Health Research Portal Level one Data Flow Diagram*

FLOWCHART
*********

.. image:: images/Flowchart.png
   :alt: Flowchart

*Figure 6: Automated Health Research Portal Flowchart*

.. raw:: latex

    \newpage

From the diagrams above, the system has the following inputs:

   * Research from repositories
   * Discussions on a research
   * Replies/comments to discussions
   * Recommends by users

The system output are:

   * Research processed and categorized according to ICD-10 classifications and ordered according to their number of recommends
   * Discussions and replies from the users
   * User recommendations


IMPLEMENTATION AND TESTING
==========================

DATABASE
~~~~~~~~
The system uses `PostgreSQL <https://www.postgresqltutorial.com/>`_ as its database. PostgreSQL is a powerful, open source object-relational database
system that uses and extends the SQL language combined with many features that safely store and scale the
most complicated data workloads. The move towards using PostgreSQL is that it supports many data types, it
ensures data integrity, reliability and disaster recovery, concurrency and security among others.
 
BACKEND
~~~~~~~
The backend has been implemented using Python and Django. The use of Python language to build the system
has been motivated by the widespread use of Python in Machine Learning. One of the core module of this project
is its **Natural Language Processing** module which has been purely written in Python using `NLTK <https://www.nltk.org/>`_
(Natural Language Processing ToolKit). As for Django, it provides a modern framework for perfectionists with deadlines.
 
The backend comprises of the following modules:
 
Web scraper
***********
This module does the actual data-mining of researches from their source repositories. It uses `BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_
and `Requests <https://requests.readthedocs.io/en/master/>`_ Python libraries.

.. raw:: latex

    \newpage

**Sample web scraping output**

.. code-block:: bash

   (venv) kentay@mathengekenneth:~/health_research_portal$ python manage.py scrape
   Impact Of Climate Extremes On Water Quality And Supply In Urban Informal Settlements 
   In Kenya: A Case Study Of Kisumu City 
   - http://erepository.uonbi.ac.ke/handle/11295/104937 
   successfully added in category malaria - malaria:water
   Statistical downscaling of future rainfall and temperature under different canesm2-RCP 
   model scenarios 
   - http://erepository.uonbi.ac.ke/handle/11295/104653 successfully added 
   in category malaria - malaria:climate
   Research already scraped
   "We don't want our clothes to smell smoke": changing malaria control practices 
   and opportunities for integrated community-based management in Baringo, Kenya. 
   - http://erepository.uonbi.ac.ke/handle/11295/103631 successfully added in 
   category malaria - malaria:control
   Sensitivity of vegetation to climate variability and its implications for 
   malaria risk in Baringo, Kenya 
   - http://erepository.uonbi.ac.ke/handle/11295/103625 successfully added in 
   category malaria - malaria:climate
   Molecular characterisation of microsporidia mb species and correlation with 
   plasmodium presence in anopheles mosquitoes in Mwea and Mbita, Kenya 
   - http://erepository.uonbi.ac.ke/handle/11295/104416 successfully added in 
   category malaria - malaria:plasmodium
   Research already scraped
   Assessment Of Results Based Management Practices In The Public Sector: Case 
   Study Of National Malaria Control Program In Kenya 
   - http://erepository.uonbi.ac.ke/handle/11295/105426 successfully added in 
   category malaria - malaria:control
   A Comparison of Different Parasitaemia Levels on Malaria Transmission Post-
   asexual Drug Treatment 
   - http://erepository.uonbi.ac.ke/handle/11295/105172 successfully added in 
   category malaria - malaria:treatment
   Research already scraped
   Research already scraped
   Successfully scraped. # Final output after scraping
   (venv) kentay@mathengekenneth:~/health_research_portal$

*Figure 7: Terminal output from the scraping process*

.. raw:: latex

    \newpage

Natural Language Processing
***************************
This module uses NLTK (Natural Language Toolkit) to process the research. Once the researches are scraped, BeautifulSoup is used again
to fetch the abstracts for each research. Text is obtained from the abstract page and  preprocessing is done
to it as demonstrated below.

**1. Obtaining the category of the research from its URL**
Example URL: "http://erepository.uonbi.ac.ke/discover?scope=%2F&query=tuberculosis&submit=&rpp=10&sort_by=dc.date.issued_dt&order=desc"

.. code-block:: bash

   Category: tuberculosis

*Figure 8: Getting the research category from its source URL.*

**1. Obtanining the text from the abstracts.**

.. code-block:: bash

   Assessment of tuberculosis diagnostic capacity in healthcare facilities in 
   Nairobi City County, Kenya\r\nBackground: Early diagnosis of
   Tuberculosis (TB) is an essential component of the World Health Organization’s 
   (WHO’s) end TB strategy. The Kenya Tuberculosis Prevalence Survey estab
   lished that TB prevalence in Kenya is higher than had been estimated and 
   that about half of those who fall ill with the disease each year are missed.
   This calls for early diagnosis of TB that can only be facilitated by a TB 
   laboratory that meets all the necessary requirements. The aim of the study was 
   to determine the tuberculosis diagnostic capacity of healthcare facility 
   laboratories in Nairobi City County.\r\nMethodology: A cross sectional stu
   dy was done in Nairobi City County in 2016....

   # Text has been truncated

*Figure 9: Abstract text.*

**2. Removing the stopwords such as "and"**

.. code-block:: bash

   {'over', 'no', 'o', 'theirs', 're', 'before', 'shan', 't', "wouldn't",
   'them', 'hadn', "won't", 'all', 'where', 'himself', 'aren', 'ours', 
   'hers', 'does', 'isn', 'be', 'not', 'own', 'again', 'or', 'when', 
   'same', 'in', "you'll", 'ain', 'was', 'with', 'you', 'will', "you'd",...}

   # Truncated stopwords from the abstract

*Figure 10: Removing the stop word*

**3. Tokenizing the abstract without stop words**

.. code-block:: bash

   ['.', 'Some', 'features', 'of', 'this', 'site', 'may', 'not', 'work', 
   'without', 'it', '.', 'Assessment', 'Of', 'Tuberculosis', 'Diagnostic', 
   'Capacity', 'In', 'Healthcare', 'Facilities', 'In', 'Nairobi', 'City', 
   'County', ',', 'Kenya', 'View/Open', 'Fulltext', '(', '2.119Mb', ')', 
   'Date', '2019',... ]

   # Truncated sample of the tokenized abstract

*Figure 11: Tokenizing the abstracts*

**4. Remove the punctuation marks and make all the words lowercase**

.. code-block:: bash

   ['some', 'features', 'of', 'this', 'site', 'may', 'not', 'work', 'without', 
   'it', 'assessment', 'of', 'tuberculosis', 'diagnostic',...]

*Figure 12: Removing punctuation marks*

**5. Count word frequency and get the most 10 words**

.. code-block:: bash

   [('tb', 32), ('diagnostic', 13), ('capacity', 11), ('lab', 10), 
   ('nairobi', 9), ('key', 6), ('assessment', 6), ('tuberculosis', 6), 
   ('county', 6), ('item', 6)]

*Figure 13: Counting the words frequencies*

**6. Find the intersect between a list of defined keywords and the most common words**

.. code-block:: bash

   'diagnostic'

*Figure 14: The intercept keyword between frequent keywords and predefined keywords*

**7 Create a dictionary of the research's category and keyword**
This dictionary is used to categorize the research in its respective category in the Frontend

.. code-block:: bash

   {tuberculosis: 'diagnostic'}

*Figure 15: Category-keyword dictionary*

 
Review
******
Research stored in the database are consequently displayed to the user who after critically going
through the research can initiate a discussion on it with other users in the system. Discussions recursively
has comments, that is other users can start a nested discussion based on another user's discussion. Discussions
and replies are stored in the following models:
 
 
Recommends
**********
When a user deems a scraped research useful and practical, they are provided with an option to
``Recommend`` the research to other users. Recommend/"Unrecommend" works similarly to "likes/unlikes" in social media
platforms with the research with the most recommendations sorted out to appear the first in the list.
 
 
FRONTEND
~~~~~~~~
The frontend has been implemented using Javascript, HTML5 and CSS3. The project is not "front-end heavy" since all
the processing and logic is handled in the powerful backend. The front-end is pluggable, that is the three languages
used can be switched with any other frontend language such as React with easy.

Sample frontend pages
*********************

**1. Landing Page**

.. image:: images/landing.png
   :alt: Landing page

*Figure 16: System's landing page*

**2. Research categories**

.. image:: images/categories.png
   :alt: Categories

*Figure 17: ICD-10 disease categories*

**3. Research sub-categories(keywords)**

.. image:: images/malaria.png
   :alt: Sub categories

*Figure 18: Disease research sub-categories*

**3. Research list**

.. image:: images/malaria_list.png
   :alt: List

*Figure 20: Sample list of scraped researches*

**4. Research details page**

.. image:: images/abs.png
   :alt: Details

.. image:: images/abs2.png
   :alt: Details

*Figure 21: Sample research details page*

**5. Discussions and Comments page**

.. image:: images/discussion.png
   :alt: Flowchart

*Figure 22: Discussionsand comments page*


CONSTRAINTS
~~~~~~~~~~~
The project has a data-mining module that has been implemented using a web scraper to find research form various
repositories. However, the scraper has the following constraints:
 
  #) The scraper requires access to scrape from an eRepository. This constraints to only fetching from the University of Nairobi's eRepository.
  #) Too many scraping pings may result in the scraper being blocked out temporarily from accessing the research.
  #) Full Text Searches such as ElasticSearch require powerful machine in which case the machine used to build this project crashed countless times.
  #) Privacy and ownership of data and legal implications that might occur during the mining of data.
 
TESTING
~~~~~~~
The project has been fully tested using `Pytest Framework <https://pytest-django.readthedocs.io/en/latest/>`_ and
`Model Bakery <https://model-bakery.readthedocs.io/en/latest/>`_ which creates smart fixtures for testing
in Django. Other tools used include: `Flake8 <https://flake8.pycqa.org/en/latest/>`_ that checks if the
code base complies to set python standards and `Tox <https://tox.readthedocs.io/en/latest/>`_ which
automates the whole testing process. The system has been unit-tested and integration-tested with a
test coverage of 100%. The system is fully backed by Continuous Integration. It has been integrated with
`CircleCI <https://circleci.com/>`_ that automates testing before the project is pushed to its version
control repository in `Github <https://github.com/>`_ and its deployment to its staging server in
**Google Cloud Platform**. 


**Test output:**

.. code-block:: bash

   (venv) kentay@mathengekenneth:~/health_research_portal$ pytest tests/researches/test_model.py::test_research_model
   ============================= test session starts ==============================
   platform linux -- Python 3.6.8, pytest-5.3.2, py-1.8.1, pluggy-0.13.1
   Django settings: config.settings (from ini file)
   rootdir: /home/kentay/health_research_portal, inifile: tox.ini
   plugins: cov-2.8.1, django-3.7.0, celery-4.4.2
   collected 1 item                                                               

   tests/researches/test_model.py .                                         [100%]

   ======================== 1 passed in 13.31s =====================================

*Figure 23: Sample terminal output for running test with pytest*

**CircleCI Test output:**

.. code-block:: bash

   #!/bin/bash -eo pipefail
   . venv/bin/activate
   tox -r

   ...
   py3 run-test: commands[0] | flake8 hrp/ tests/ # Runs flake8
   py3 run-test: commands[1] | coverage erase
   py3 run-test: commands[2] | pytest --cov=hrp/ # Runs the tests and their coverage
   ============================= test session starts ==============================
   platform linux -- Python 3.6.1, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
   cachedir: .tox/py3/.pytest_cache
   django: settings: config.settings (from ini)
   rootdir: /home/circleci/repo, inifile: tox.ini
   plugins: cov-2.8.1, django-3.9.0
   collected 23 items                                                             

   tests/researches/test_model.py ............                              [100%]
   tests/researches/test_views.py ...........                               [100%]

   ----------- coverage: platform linux, python 3.6.1-final-0 -----------
   Name                         Stmts   Miss Branch BrPart  Cover   Missing
   ------------------------------------------------------------------------
   hrp/researches/__init__.py       0      0      0      0   100%
   hrp/researches/filters.py        6      0      0      0   100%
   hrp/researches/forms.py         17      0      0      0   100%
   hrp/researches/models.py        50      0      0      0   100%
   hrp/researches/urls.py           4      0      0      0   100%
   hrp/researches/views.py        240     .0      4      0   100%
   ------------------------------------------------------------------------
   TOTAL                          317     .0      4      0   100%

   ======================= 23 passed in 1.80s =============================
   py3 run-test: commands[3] | coverage html
   ___________________________________ summary ____________________________________
   py3: commands succeeded
   congratulations :)

*Figure 24: Sample bash output for running tests in CircleCI*


DEPLOYMENT
~~~~~~~~~~
The project has been deployed to a staging server in **Google Cloud Platform** for user testing and supervisors demo. Further
considerations are being thought of to eventually push the project into production to be used with real users. The project in
the staging server can be accessed via: https://hrp.duckdns.org.
 
MAINTENANCE
~~~~~~~~~~~
 
The project has been written using **Robert C Martin** principles in his book **Clean Code** to make the process of debugging and
maintaining the code is easy. Bugs are addressed using Python's `PDB <https://docs.python.org/3/library/pdb.html>`_ debugging tool. Each class and function has constructively
written docstrings to clearly explain what the code does. New features identified have a process put into place before they
are integrated with the main code. Github provides an issue tracker that keeps a backlog of bug and enhancements that the
system requires.

DISCUSSION AND CONCLUSION
=========================

ACHIEVEMENT
~~~~~~~~~~~
The journey to doing this project has been an amazing one marked with several objectives and achievements met. Some of
the highlights include:
 
  * Getting an opportunity to put into practice most of the concepts, skills and technologies learnt during my attachment period.
  * Applying the knowledge obtained both in school and during my attachment to try and solve a real world problem.
  * Level up my knowledge in the field of Machine Learning and Data mining.
  * Successfully creating a fully functional system meeting all the objectives met during the project proposal.
  * Successfully worked with tools such as GIT, CircleCI, Google Cloud Platform, Sphinx to write this documentation and testing framework such as Pytest, which
    are relevant skills employed by several companies in their production code.
  * Successfully completing the project on time.
 
LIMITATIONS
~~~~~~~~~~~
Despite the success met along the way, there were several hurdles that were encountered. These hurdles include, but not limited to:
 
  * The uncertainties and hard times brought about by the Covid-19 pandemic
  * Information overload. With all the vast information online, finding quality and accurate information was a challenge
  * I worked the project on an old laptop, which over the months has needed several constant repairs
  * Financial challenges as some of the technologies intended to be used in this project required paid subscriptions such as the
    Google Cloud Platform.
  * Privacy and Ownership of data that I was mining. Some sites with relevant information needed access rights to be scrapped.
  * Most of the repositories interacted with were unstructured and trying to come up with a structure to scrape them was a bit challenging.
 
RECOMMENDTIONS
~~~~~~~~~~~~~~
The world of technology keep evolving, and even though this project uses the latest and trending technologies now, after some time
it will be passed by a future technology and trend. With that in mind, some of the recommendations include:
 
  * Evolving this web system into an Android and iOS application
  * The world of health researches is vast, thus more researches can be scraped to add to the count of the existing researches
  * The User Interface can have several more iterations to make it more user friend and follow the rules of UX
  * The Natural Language Processing logic can be enhanced more to increase its precision in categorizing researches
 
CONCLUSION
~~~~~~~~~~
In conclusion, this whole exercise has been very productive. The University should keep this going as the students get to apply
the knowledge gained since first year and the knowledge obtained from the attachment program. Morever, working hand-on on projects
solidifies the skills the one possesses. One is able to judge where they lie in the field of computer science. it gives once confidence
to face the real world as it helps us think of real world problem and how technology can be used to solve these problems. I am grateful
to the University, all me lecturers and my supervisor for giving me this opportunity and i am very confident in my project.


REFERENCES
==========

#) Academic Medicine, 2001. APPENDIX 1. [online] 76(9), p.959. Available at: 
   <https://journals.lww.com/academicmedicine/Fulltext/2001/09000/APPENDIX_1__CHECKLIST_OF_REVIEW_CRITERIA.37.aspx> 
   [Accessed 27 January 2020].

#) Xiew, I. and Matusiak, K., 2016. Digital Repository - An Overview | Sciencedirect Topics. [online] Sciencedirect.com. 
   Available at: <https://www.sciencedirect.com/topics/computer-science/digital-repository> 
   [Accessed 11 February 2020].

#) Chilimo, W., 2015. Green Open Access In Kenya : A Review Of The Content, Policies And Usage Of Institutional Repositories. 
   [online] ResearchGate. Available at: <https://www.researchgate.net/publication/327187267_Green_open_access_in_Kenya_a_review_of_the_content_policies_and_usage_of_institutional_repositories> 
   [Accessed 19 February 2020].

#) World Health Organization. 2018. International Classification Of Diseases, 11Th Revision (ICD-11). 
   [online] Available at: <https://www.who.int/classifications/icd/en/> [Accessed 15 March 2020].

#) Chiessi, L., 2018. Why Should I Use Postgresql As Database In My Startup/Company. [online] Medium. Available at: 
   <https://medium.com/we-build-state-of-the-art-software-creating/why-should-i-use-postgresql-as-database-in-my-startup-company-96de2fd375a9> 
   [Accessed 13 April 2020].

#) Knowledge translation. (2015, October 03) [online]. Available at: <https://www.who.int/ageing/projects/knowledge_translation/en/> [Accessed 16 March 2020] 

#) Platform, CHI KT., 19 Sept. 2018. What We Mean When We Say "Knowledge Translation". [online] Medium. Available at: 
   <https://medium.com/knowledgenudge/what-we-mean-when-we-say-knowledge-translation-1f81d57d5143.> [Accessed 18 March 2020]

#) Azimi, A., Fattahi, R. & Asadi-Lari, M., 2015. Knowledge translation status and barriers. Journal of the Medical Library Association : JMLA. Available at: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4404863/ [Accessed November 12, 2019].

#) Grimshaw, J., Eccles, M., Lavis, J., Hill, S. and Squires, J. (2012). [online] Implementation Science. Available at: https://implementationscience.biomedcentral.com/track/pdf/10.1186/1748-5908-7-50 [Accessed 18 Nov. 2019].

#) Ho, K. et al., 2003. Technology-enabled knowledge translation: building a framework for collaboration. CMAJ. Available at: https://www.cmaj.ca/content/168/6/710.short [Accessed November 12, 2019].

#) Anon, 2011. Knowledge Translation in Global Health. World Health Organization. Available at: https://www.who.int/bulletin/volumes/83/10/editorial21005html/en/ [Accessed November 13, 2019].

#) Ktdrr.org. (2005). What is Knowledge Translation?. [online] Available at: https://ktdrr.org/ktlibrary/articles_pubs/ncddrwork/focus/focus10/Focus10.pdf? [Accessed 14 Nov. 2019].

#) Moseti, I., Digital preservation and institutional repositories: case study of universities in Kenya. Journal of the South African Society of Archivists. Available at: https://www.ajol.info/index.php/jsasa/article/view/138434/128001 [Accessed November 18, 2019].


APPENDIX 1
==========

CODE SNIPPETS
~~~~~~~~~~~~~

BACKEND CODE SNIPPETS
*********************

**Web Scraper Code snippet:**

.. code-block:: python

   """Create the web scraper and NLP module."""
   ...
   import requests
   from bs4 import BeautifulSoup
   ...
   from hrp.common.util import KEYWORDS, URL_LIST
   from hrp.researches.models import Research

   def scraper():
      """Scrape certified repositories."""
      category_list = []
      for URL in URL_LIST:
         page = requests.get(URL)
         soup = BeautifulSoup(page.content, "html.parser")

         results = soup.find(id="main-container")
         researches = results.find_all(class_="col-sm-9 artifact-description")
         
         # Fetch the categories from the urls
         category = URL.split("&")[1]
         category_list.append(category)

         for item in category_list:
            category = item.split("=")[1]

         for research in researches:
            url = "http://erepository.uonbi.ac.ke" + research.find("a")["href"]
            title = research.find("h4").text
            ...

*Figure 25: Web scraper code snippet*

**Natural Language Processing Code snippet:**

.. code-block:: python

   """Create the web scraper and NLP module."""
   import nltk
   ...
   from nltk.corpus import stopwords
   from nltk.tokenize import word_tokenize

   from hrp.common.util import KEYWORDS, URL_LIST
   from hrp.researches.models import Research

   def scraper():
      """Scrape certified repositories."""
      category_list = []
      for URL in URL_LIST:
         ...

         for research in researches:
            url = "http://erepository.uonbi.ac.ke" + research.find("a")["href"]
            title = research.find("h4").text

            #  Convert the abstract page to text
            response = requests.get(url)
            text = BeautifulSoup(response.content, "html.parser")
            text = text.get_text()

            # Remove stop words like 'a' 'the' 'an'
            stop_words = set(stopwords.words("english"))
            word_tokens = word_tokenize(text)

            # Remove punctuations (noise) and lower the upper cases
            word_tokens = [
                  word.lower() for word in word_tokens if word.isalpha()
            ]

            filtered_text = [w for w in word_tokens if not w in stop_words]
            filtered_text = []

            for w in word_tokens:
                  if w not in stop_words:
                     filtered_text.append(w)

            # Count the most frequent words in the preprocessed text
            count_word_frequency = nltk.FreqDist(filtered_text)
            count_word_frequency = count_word_frequency.most_common(
                  10
            )  # Gets most frequent 10 words

            # Parse the most frequent words to get the key words (specified in __init__.py)
            get_keywords = [
                  [j for j in i if type(j) == str] for i in count_word_frequency
            ]  # Gets keywords as a list

            # Compares keywords gotten above with most_common words and find an intersect
            try:
                  keyword = [
                     _keyword
                     for _keyword in KEYWORDS
                     if _keyword in get_keywords
                  ]
                  keyword = ",".join(keyword[0])  # Gets the intersect
                  keyword = "{}:{}".format(category, keyword)

            except IndexError:
                  continue

            ...

*Figure 26: NLP code sample*

After successfully scraping and processing the a research, it then proceeds to be added in our database

**Database record creating Code snippet:**

.. code-block:: python

   ...
   try:
      Research.objects.create(
         url=url, title=title, category=category, keyword=keyword
      )
      print(
         "{} - {} successfully added in category {} - {}".format(
            title, url, category, keyword
         )
      )
   except:
         print("Research already scraped")

*Figure 27: Sample code to add a scrapped research to the database*

**Discussions Code Snippet**

.. code-block:: python

   class Discussion(models.Model):
      """Create discussions for a research."""

      research = models.ForeignKey(
         Research, on_delete=models.CASCADE, related_name="discussions"
      )
      created_by = models.ForeignKey(User, on_delete=models.CASCADE)
      created_on = models.DateTimeField(auto_now_add=True)
      discussion = models.TextField()

*Figure 28: Discussions module model code snippet*

**Replies to discussions Code Snippet**

.. code-block:: python

   class DiscussionReply(models.Model):
      """User can reply to a discussion."""

      discussion = models.ForeignKey(
         Discussion, on_delete=models.CASCADE, related_name="replies"
      )
      created_by = models.ForeignKey(User, on_delete=models.CASCADE)
      created_on = models.DateTimeField(auto_now_add=True)
      reply = models.TextField()

*Figure 29: Replies to discussions (comments) module model code snippet*


**Recommends code snippet:**

.. code-block:: python

   class Recommends(models.Model):
      """A research is ranked on its number of recommends."""

      research = models.ForeignKey(
         Research, on_delete=models.CASCADE, related_name="researches"
      )
      recommends = models.ManyToManyField(
         User, blank=True, related_name="recommends"
      )

*Figure 30: Recommendation module model code snippet*

.. raw:: latex

    \newpage

FRONTEND CODE SNIPPETS
**********************

**Landing Page Code Snippet**

.. code-block:: HTML

   {% extends 'base.html' %}
   {% load static %}

   {% block breadcrumbs %}
   <div class="jumbotron jumbotron-fluid">
   <div class="container">
      <h2>Health Research Portal</h2>
      <hr>
      <p class="lead text-muted">
         <smaller>
         Automated Health Research Portal is built upon three pillars:
         </smaller>
      </p>
      <br>
      <div class="row">
         <div class="col-4">
         <div class="card border-success mb-3" style="max-width: 18rem;">
            <div class="card-body text-success">
               <h5 class="card-title"><strong>Sourcing</strong></h5>
               <hr>
               <p class="card-text">We automate the process of looking for researches from the vast online space.</p>
            </div>
         </div>
         </div>

      ...

*Figure 31: Landing page HTML5 code snippet*

**Research Views Code Snippet**

.. code-block :: python

   class CancerTemplateView(TemplateView):
    """Cancer page template view."""

    template_name = "researches/cancer/cancer.html"

    def get_context_data(self, **kwargs):
        """Get template contexts."""
        context = super().get_context_data(**kwargs)
        context["diagnosis_count"] = Research.objects.filter(
            keyword="cancer:diagnosis"
        ).count()
        context["treatment_count"] = Research.objects.filter(
            keyword="cancer:treatment"
        ).count()
        context["location_count"] = Research.objects.filter(
            keyword="cancer:county"
        ).count()
        return context


   class CancerDiagnosisListView(ListView):
      """List view of researches."""

      queryset = (
         Research.objects.filter(keyword="cancer:diagnosis")
         .annotate(research_count=Count("researches__recommends"))
         .order_by("-research_count")
      )
      template_name = "researches/cancer/cancer_diagnosis.html"
      paginate_by = 10

      ...

*Figure 32: Sample research view code snippet*

**Review Views Code Snippet**

.. code-block :: python

   class ReviewCreateView(LoginRequiredMixin, CreateView):
    """Create a review for a recommended research."""

    model = Review
    template_name = "reviews.html"
    login_url = "login"
    redirect_field_name = "redirect_to"
    form_class = ReviewForm

    def form_valid(self, form):
        """Override form valid to add user and research."""
        form.instance.created_by = self.request.user
        form.instance.research_id = self.kwargs.get("pk")
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect the reviews page."""
        return reverse_lazy(
            "research:research-detail", kwargs={"pk": self.kwargs.get("pk")}
        )

    def get_context_data(self, **kwargs):
        """Get the research to be reviewed."""
        research = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        context["reviewed_research"] = Research.objects.get(pk=research)
        return context

      ...

*Figure 33: Sample review view code snippet*

**Sample URL Code Snippets**

.. code-block :: python

   """Researches app urls."""
   from django.urls import path

   from . import views

   app_name = "researches"
   urlpatterns = [
      path("", views.Index.as_view(), name="index",),
      path("signup/", views.SignUp.as_view(), name="signup"),
      path(
         "discussions/<int:pk>",
         views.DiscussionCreateView.as_view(),
         name="discussions",
      ),
      path(
         "discussions/replies_to_discussions/<int:pk>",
         views.DiscussionReplyCreateView.as_view(),
         name="replies_to_discussions",
      ),

      ...

*Figure 34: Sample url configuration code snippet that maps views to their models*


TESTS CODE SNIPPETS
*******************

**Sample test fixture code snippets:**

.. code-block:: python

   """Test fixtures."""
   import pytest
   from django.test import Client
   from model_bakery import baker

   from hrp.researches.models import Research

   pytestmark = pytest.mark.django_db

   ...

   @pytest.fixture
   def research():
      """Return a research."""
      return baker.make(
         Research,
         url="http://url-ya-testing-tu.com",
         title="Sample research title",
         scraped_date="2020-1-19",
         category="malaria",
         keyword="malaria:plasmodium",
      )

   # Test script

   """Test research models."""
   import pytest

   pytestmark = pytest.mark.django_db


   def test_research_model(research):
      """Test research."""
      assert research.url == "http://url-ya-testing-tu.com"
      assert research.title == "Sample research title"
      assert research.scraped_date == "2020-1-19"
      assert research.category == "malaria"
      assert research.keyword == "malaria:plasmodium"

*Figure 34: Sample test fixtures and test case code snippet*


PROJECT SCHEDULE
****************

.. image:: images/schedule.png
   :alt: Schedule

*Figure 35: Project proposed schedule*

PROJECT GANTT CHART
*******************

.. image:: images/gannt.png
   :alt: Schedule

*Figure 36: Project proposed Gantt Chart*