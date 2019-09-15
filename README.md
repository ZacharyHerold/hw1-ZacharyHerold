# Fall 2019 DATA622.001/002 Homework #1

1) Assigned on August 30, 2019
2) Due on September 15, 2019 11:59 PM EST
3) 17 points possible, worth 17% of your final grade

Python Coding (7 points)
Please write python programs for the following two questions.
1. Write a Python Program to Find the Second Samllest Number in a List?
2. Two words are anagrams of each other if they contain the same number of characters and the same characters. Please write a function to test if two words are anagrams. e.g. cautioned is an anagram for education.

Submission Instructions:

.py or jupyter notebook submission would work.

Data Science Working Environment: Docker & Anaconda (10 points)

1. Read this article on Python environment and Anaconda. https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c
2. Read these articles on Docker. https://www.dataquest.io/blog/docker-data-science/; https://becominghuman.ai/docker-for-data-science-part-1-dd41e5ef1d80
3. Write a short paragraph (around ~200 words total) on the following topics:

the role "environment" plays in a data scientist's workflow (the readings from #1 & #2 will cover this)

the difference between Docker & Anaconda, and why some data 
science teams prefer to use the two together (you will need to do more 
research on this outside of the articles listed above)
the role "environment" plays in a data scientist's workflow 

---------------------------------------------------------------------------------------------
Response:

Development and run-time environments for a data scientist include the software stack employed in the development of some analytic product. The end product, or application, has a collection of dependencies of the software versions and programs which are required for it to run. No matter the workflow phase (be it the employment of extensive ETL processes, techniques from statistics, information access, machine learning, artificial intelligence, and graph analytics), these dependencies accrue, which determine the "environment".

Containerization tools such as Docker allow internal or external users to overcome the problems that occur when their supporting software environments are not identical by bundling an application and all its dependencies into a single object. Comparable to lightweight versions of virtual machines, developers can assemble and users can run programs and executables in Docker containers across Windows and Linux operation systems. 

Anaconda is a distribution of Python that has its own virtual environment system called conda. Conda is a package and environment management system for installing and switching between multiple versions of software packages and their dependencies at the command-line level, and it supports languages other than Python. However, where Conda and Docker are different is that Dockers is designed to package multiple dependencies into a single object or image, which are easily distributed to collaborators and bundled into applications. Because the Anaconda distribution includes hundreds of useful packages for data science, it may be useful for data scientists to use Anaconda images for their projects. 
