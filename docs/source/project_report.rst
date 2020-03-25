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
until current decades. Grimshaw et al. state that, despite billions of dollars each 
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

The third research toopic is to identify credible sources of health research data from the internet.
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

The literature review is presented in serveral subsections namely: the concept of digital preservation and 
institutional repositories; concepts and keywords used in disease categorization and metrics of reviewing health researches.

The concept of digital preservation and institutional repositories
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
repositories such as: institutional, discplinary, government and centralized repositories. The scope of 
this project focuses on institutional repositories which have several purposes - they support 
scholary communication and provide open access to articles, dissertations and research data and provide 
platforms for storing and preserving the digital master files created as a result of digitization projects.

Most IRs in Kenya are owned by universities. These include University of Nairobi, Kenyatta University, 
Jomo Kenyatta University of Agriculture and Technology, Moi University, Egerton University, Maseno University,
the Technical University of Kenya among other universities. Of all the universities in Kenya, UoN, KU, SU, PU,
JKUAT and DeKUT are some of the universities who've had their IRs listed in the worldwide directory of IRs. As 
such they provide a good candidates of research information to be utilised by this project. UoN, moreover, has 
the largest repository in terms of the total item count. Therefore, it provides adequate research information on
various topics include health research. Other universities IRs will work as supplimentary sources.

With the growth in digital preservation, comes the need to make use of all these information. There
has been many attempts and tools brought forward to help people utilize these information for better
decision making and living standards. Some of them include *data mining* and *natural language processing*. 
Data mining is defined as the practice of examining large pre-existing databases in order to generate new 
information. NaturalLanguage Processing is a subfield of linguistics, computer science, information engineering, 
and artificial intelligence concerned with the interactions between computers and human languages, in 
particular how to program computers to process and analyze large amounts of natural language data.

Concepts and keywords used in dieseases categorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

Metrics of reviewing health researches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Health Research Portal users have the ability to recommend and give review comment(s) on the relevance and
usability of a research paper. Most exert research reviewers usually have checklists that they review a 
papaer with. This same idea is used in the system to provide a scientific checklists for user to mark 
after recommending a research paper. The checklist used is adapted from Academic Medicine (2001). The paper
provides an extensive list of items to look at based on the research paper topics such as: Problem statement,
conceptual framework and research questions, references to the literature and documantation, relevance,
research design, instrumentation, data collection and quality control, population and sample, data analysis
and statistics, reporting of statistical analyses, presentation of results, discussion and conclusion,
title, authors and abstract, presnetation and documentation and scientific conduct.

SIMILAR WORK DONE BEFORE
~~~~~~~~~~~~~~~~~~~~~~~~
Some similar work done before include:

    #) WHO Global Observatory on Health R&D

       The WHO Global Observatory on Health R&D is a centralized and comprehensive source of 
       information and analyses on global health R&D activities for human dieseases.

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

       The system automates the process of retreiving health researches from various certified 
       repositories such as the University of Nairobi eRepository. It mines for the researches 
       that are then categorized based on the disease that is being researched on (e.g **Cancer**).

    #) Natural Language Processing.

       The text in a mined research is then processed to get similarities between the researched 
       and others that have been mined. With these similarities the researches are then grouped
       together. These grouping put similar information together making it easier for users to 
       use the information (e.g **under Cancer, research based on the *type of cancer* will be in 
       one group and research based on the *diagnosis of cancer* in another grouping**).

    #) Full Text Searching.

       To make it even more easier for users to get information, the system will involve a Full
       Text Search service to help get information faster in the mined researches.

    #) Reviewing

       The mined and processed researches will be ordered according to their relevance. Relevance 
       will be determined by the number of reviews a research gets form its users.


METHODOLOGY
===========

REQUIRMENTS ANALYSIS
~~~~~~~~~~~~~~~~~~~~
Requirements analysis involved the identification of potential system users, who include doctors,
lecturers and students from the School of Medicine actively involved in doing research in the healthcare 
field. There was **frequent communication** with the potential system users to determine the specific feature 
expectations. Requirements were also elicited from several documantation on **Knowledge Translation**.

*Alistair Cockburn's Use Case Template*

+--------------------------------------------------------------------------------------+
|USE CASE 1: GET RESEARCH INFORMATION                                                  |
|                                                                                      |
|A. CHARACTERISTIC INFORMATION                                                         |
|                                                                                      |
|       * **Goal in context:** User to get information from researches                 |
|       * **Actors:** System, Doctors, Researchers, Policy makers, Students            |
|       * **Scope:** Research done on Health.                                          |
|       * **Success condition:** User quickly gets useful research and reviews it      |
|                                                                                      |
|B. MAIN SUCCESS SCENARIO                                                              |
|                                                                                      |
|        #) User needs information from done researches                                |
|        #) User log-in the system and searches (e.g Malaria)                          |
|        #) System lists researches mined on malaria in well identified categories     |
|        #) User identifies a category and gets relevant research                      |
|        #) User then uses the obtained research                                       |
|        #) User reviews it (positively or negatively)                                 |
|                                                                                      |
|D. VARIATIONS                                                                         |
|                                                                                      |
|       #) User does not leave a review on a research                                  |
|                                                                                      |
|C. RELATED INFORMATION                                                                |
|                                                                                      |
|        #) * **Channel to actor:** Phone and Desktop                                  |
|        #) * **Priotiry:** Top                                                        |
+--------------------------------------------------------------------------------------+

SYSTEM DESIGN
~~~~~~~~~~~~~
System design for the project has been represented using **Data Flow Diagrams**.

.. figure:: Level0DFD.png
    :width: 200px
    :align: center
    :height: 200px
    :alt: Level 0 DFD
    :figclass: align-right

    *Automated Health Research Portal Level 0 DFD*

.. figure:: Level1DFD.png
    :width: 300px
    :align: center
    :height: 300px
    :alt: Level 1 DFD
    :figclass: align-left

    *Automated Health Research Portal Level 1 DFD*

.. figure:: dfd.png
    :width: 300px
    :align: center
    :height: 300px
    :alt: Level 1 DFD
    :figclass: align-left

    *Automated Health Research Portal database ERD*


References
==========
https://journals.lww.com/academicmedicine/Fulltext/2001/09000/APPENDIX_1__CHECKLIST_OF_REVIEW_CRITERIA.37.aspx
Digital repos - https://www.sciencedirect.com/topics/computer-science/digital-repository
IRs - https://www.researchgate.net/publication/327187267_Green_open_access_in_Kenya_a_review_of_the_content_policies_and_usage_of_institutional_repositories
ICD-10 - https://www.who.int/classifications/icd/en/