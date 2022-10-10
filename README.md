# sparta_global_eng130

## Week 1

### Elevator pitch
- body language
  - smiling
  - confident
- no reading
- don't get caught up if you forget something
- include
  - who am i?
  - buzzwords
  - education
  - experience
  - why this role?

I'm Benedek Kovács, a junior DevOps engineer at Sparta Global. 
I started software development in high school, as I wanted to use my quantitative skills in real life.
For this reason I participated in startups, which made me very adaptable and provided me with years of coding experience, delving into various programming languages.
While studying and researching for my physics degree, I have gained exceptional problem-solving and critical thinking skills, which make me an extremely valueable member of many different types of teams.
I'm always looking to develop myself, which is why I took an online machine learning course during my 4th year of university. I'm currently working on completing a course about relational databases and SQL.
In my free time, I like to cook and I follow and watch Formula 1.

### Agile
- a mindset
- iterative, small iterations
- effective at cathcing mistakes early
![alt text](https://www.nvisia.com/hubfs/agile-methodology-chicago.png)

### Scrum
- a framework
- repeated feedback
- scrum team members: product owner, scrum master, scrum team (3-9 people)
- <a href="https://www.scrum.org/" title="Scrum website">Scrum Website</a>
![alt text](https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/2021-01/scrumorg-scrum-framework-3000.png)

### DevOps
- combined software development and operations
- shortens software development lifecycle
- DevOps engineer
  - works in the development and the operation teams as well
  - these teams are meant to be the same
  - understands both coding and operations
  - possesses both the hard and soft skills necessary
- business benefits: 
  - faster deployment
  - better scalability
  - faster response time
  - better documentation
  - better communication
![alt text](https://marvel-b1-cdn.bc0a.com/f00000000236551/dt-cdn.net/wp-content/uploads/2021/07/13429_ILL_DevOpsLoop.png)

### Python
- <a href="https://github.com/khanmaster/eng130_python" title="Installing Python">Installing Python</a>
- <a href="https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/" title="Add to the PATH on Windows 10">Add to the PATH on Windows 10</a>
- Installing PyCharm
- test by printing "Hello World!"

### Additional Stuff:
- markdown cheat sheets
  - basic: https://www.markdownguide.org/cheat-sheet/
  - extended: https://towardsdatascience.com/the-ultimate-markdown-cheat-sheet-3d3976b31a0#f407
- python libraries installed:
  - matplotlib
  - numpy
  - pandas
  - seaborn
  - tqdm
  - tensorflow
  - pytorch
  - scipy
  - spacepy
  - scikit-learn

## Week 2

### Python basics

#### Variables

```python
name = 'Benedek Kovács'
dob = 2000
```

#### Data types

int - integer number  
str - string, text  
char - single character  
float - real number  
boolean - true or False  

#### Input

```python
name = input()
print(name)
```
### Github setup

Make sure to replace arguments where needed:

- the main library
- the email address
- the public key name
- 

#### Generate SSH key

-enter [main library/.ssh] and generate SSH key (private and public)
```commandline
cd /c/Users/bened
cd .ssh
ssh-keygen -t rsa -b 4096 -C "kovacsbenedek4000@gmail.com"
```

####

- add SSH public key to Github account. read SSH key by copying the public key:  
```commandline
cat id_rsa.pub
```
- create repository on Github
- create README.md file in local folder
- prepare local folder to connect to repository and connect it to repository:
```commandline
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin "git@github.com:[username]/[repository].git"
```
- push local folder to repository:  
```commandline
git push -u origin main
```
