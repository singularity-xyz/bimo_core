import pytest
from bimo_core import SEChain
from bimo_core import logging
from typing import Optional
from pydantic import BaseModel


# class Person(BaseModel):
#     person_name: str
#     person_height: int
#     person_hair_color: str
#     dog_breed: Optional[str]
#     dog_name: Optional[str]


# def test_extraction_simple():
#     chain = SEChain()

#     inp = """
#     Alex is 5 feet tall. Claudia is 1 feet taller than Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.
#     Alex's dog Frosty is a labrador and likes to play hide and seek.
#             """

#     response = chain.run(inp)

#     expected_response = [Person(person_name='Alex', person_height=5, person_hair_color='blonde', dog_breed='labrador', dog_name='Frosty'),
#                          Person(person_name='Claudia', person_height=6, person_hair_color='brunette', dog_breed=None, dog_name=None)]

#     # assert response == expected_response, f"Expected {expected_response}, but got {response}"
#     assert len(response) > 0, "Response is empty"

#     print()
#     print("Input:", inp)
#     print("Response:", [r.dict() for r in response])
#     # logging.info("Input: %s", inp)
#     # logging.info("Response: %s", [r.dict() for r in response])  # use .dict() to convert Pydantic models to dictionaries for logging

from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field

class Assignment(BaseModel):
    id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    due_date: Optional[str]
    weightage: Optional[float]

class Exam(BaseModel):
    id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    date: Optional[str]
    weightage: Optional[float]

class Syllabus(BaseModel):
    id: Optional[str]
    course_code: Optional[str]
    course_name: Optional[str]
    assignments: Optional[List[Assignment]] = []
    exams: Optional[List[Exam]] = []


def test_syllabus_extraction():
    chain = SEChain()

    inp = """
    ENST 100: Introduction to Environmental Studies
    Units: 4
    Fall 2020: Tuesdays/Thursdays 2:00-3:20pm
    Location: For Fall 2020, this course will be held online via
    Blackboard and Zoom.
    Instructor: Dr. Victoria Campbell-Arvai
    Office: tbd
    Online Office Hours: Mondays @ 1:00 pm & Thursdays @ 3:30pm,
    or by appointment.
    Contact Info: The best way to contact me is through email:
    vec@usc.edu (you can expect a response within 24 hours)
    Course Description
    This course will give you an overview of how the natural world works, the ways in which humans are
    perturbing the natural world, and the ways in which governments and society are (or are not) addressing
    environmental degradation
    Learning Objectives
    § Gain knowledge of the physical, chemical, and biological aspects of the environment.
    § Understand issues facing the environment from a scientific and social perspective.
    § Explore how environmental issues affect humans, from multiple perspectives.
    § Discuss solutions to environmental degradation through law, policy & markets, technology, and human
    behavior (both individual behavior and collective action).
    § Learning objectives in this course are aligned with those of the Environmental Studies Program:
    https://dornsife.usc.edu/environmental-studies/learning-objectives/
    Prerequisite(s): none
    Course Notes
    This course will use Blackboard for communication, information and submitting assignments. Lecture slides
    will be made available after the lecture is given. Additional readings may be assigned periodically
    throughout the semester, and these will be announced in class, posted on Blackboard, and an email
    reminder sent to the class. It is your responsibility to regularly check the course Blackboard site and your
    USC email for these course announcements. Let me know before the first lecture if you are having trouble
    accessing Blackboard and/or receiving course Announcements, but please check out the following
    information first: Blackboard Student Support https://studentblackboardhelp.usc.edu & the Blackboard
    Help Line (available 24/7/365) @ 213-740-5555, Option 2.
    Lectures, class discussions, and class activities will be held online using the Zoom meeting platform. Before
    the start of term, please make sure you have activated your USC-branded Zoom account, and that the most
    recent version of this app is downloaded and available on your computer or tablet. For more information
    and to get started with Zoom, visit: https://keepteaching.usc.edu/start-learning/,
    https://keepteaching.usc.edu/student-access-to-zoom/.
    Course Text & Readings
    G.T. Miller and S. Spoolman, 2016. Environmental Science 15th Edition. Delmar Cengage Learning.
    AVAILABLE FREE ONLINE through USC Libraries:
    § https://www-r2library-com.libproxy1.usc.edu/Resource/Title/1305090446
    § Use your Proxy or VPN to log into access this link
    AVAILABLE TO RENT, PURCHASE and AS AN eBOOK:
    § https://www.cengage.com/c/environmental-science-15e-miller/9781305090446/
    Other readings & resources, i.e., scientific articles, news stories, and web materials, videos will be
    assigned throughout the semester and links/PDFs made available on Blackboard.
    Page 2
    Communication and Contact
    Online office hours will be held on Mondays @ 1:00 pm & Thursdays @ 3:30pm, or by appointment. Email
    is the preferred way to reach me outside of class and office hours (please put the course number in the
    Subject line), and it is my policy to respond to emails within 24 hours (barring unforeseen circumstances).
    Please use your USC email when contacting me, I may not respond to emails sent from non-USC accounts.
    Course ‘Netiquette’. Please do:
    ▪ Log in to our class Zoom sessions using a computer or tablet. Logging in via a Smartphone is not
    recommended.
    ▪ Make sure your first name is displayed when you join the Zoom session.
    ▪ Contact the following for technical issues during the class
    o Blackboard Help Line (available 24/7/365) – 213-740-5555, Option 2;
    o Blackboard Support – blackboard@usc.edu;
    o Zoom Support – Contact ITS consult@usc.edu or 213-740-5555, Option 1
    ▪ Find a quiet and private place with minimal distractions from family, friends, pets, etc. from which to
    join the course.
    ▪ Mute your microphone when not speaking in class, and take care to avoid sounds and visual
    distractions in your background.
    ▪ Enable your webcam so you are visible to everyone in the course.
    ▪ Use Gallery View so that you can see and respond to other students in the class.
    ▪ Turn off and stow your phone during class time.
    ▪ Turn off other distractions, e.g., Email, Facebook, Instagram, Messenger/WhatsApp/other SMS,
    Pinterest, Snapchat, TikTok, Twitter, YouTube, etc., etc. etc. during class time.
    ▪ Use the internet for course-related searches as instructed by the instructor.
    ▪ Use the Zoom chat box during class time to communicate with me, the instructor, and with other
    students.
    ▪ Feel free to interrupt (using Zoom’s ‘Raise Hand’ feature) to ask a question verbally or via chat.
    As a general rule of thumb: Treat Blackboard and Zoom as you would any other in-person classroom or
    office hours. The online format does not lessen my expectations of what constitutes meaningful
    engagement and participation, appropriate communication/presentation and dedication to this class. Class
    participation and engagement (both synchronous –during class time and asynchronous—outside of class
    time) accounts for 10% of your grade!
    Exams
    There will be three (3) exams for this course: two Midterms and a Final exam. Exam questions will be
    drawn from course readings and lecture materials, and will include multiple choice, short answer, and essay
    questions. The exams will be timed and submitted via Resopondus on Blackboard. The first two exams will
    cover the lecture and reading material that precede them. The Final exam is cumulative (all material
    covered since the first day of class). If there is a conflict with an exam, or if you have DSP time extensions,
    or if you are in a very different time zone, you must email me (the instructor) 2 weeks in advance to see if
    alternative arrangements can be made (under reasonable circumstances). Make-up exams will be more
    difficult and will not be given except in extreme emergencies. If you have an emergency on exam day, you
    must get in touch with me before the exam. If a student misses an exam without an excused reason, they
    will receive a zero. During Fall 2020, you may use your notes during exams, but the exams will be timed, so
    will be best to study and not rely on your notes. Failure to comply with exam policies will automatically
    result in a grade of “0” for that particular exam.
    Assignments
    'Environment in the News' Discussion: We will start off each class with a brief (5 minute) discussion about
    a local, national, or global environmental news story. Each student will be required to participate and select
    Page 3
    a date to review and discuss a recent news article as well as your analysis on whether you believe the article
    was biased.
    Recognizing Bias in the News: The news article analysis is a ~2 page analysis of bias and truth in news
    articles pertaining to the topics we are covering in class. You will use a guide (given by the instructor) on
    how to look for bias and facts in the news, we will also discuss your analysis in class on the day each
    assignment is due.
    Endangered Species Research: The endangered species research assignment will involve researching an
    endangered species and its recovery plan and doing a write up of your research for use in an in-class
    discussion about choices in funding species recovery. Your research should cover the cause of your species
    endangerment, the details and cost of the recovery plan, the potential for recovery, and whether or not you
    think the cost is worth it. This research should be annotated with references for all information, and will be
    graded on the completeness of the content.
    Reflection: Thinking About Nature: For this assignment, students will read essays on nature from 4-5
    different authors and write a reflective response to the essay. These essays present perspectives on the
    relationship of the author with nature, and come from authors with diverse backgrounds. You will
    complete and submit three (3) of these assignments.
    Letter to a Decision-maker: You will write a ~2 page letter to a decision-maker (e.g., a member of federal,
    state, local or tribal government, a business leader, or a leader from a non-governmental organization)
    expressing your views on a particular environmental problem and how it should be solved. The letter will
    be formatted as a formal letter to this individual, and should be as persuasive as possible. You will provide
    evidence to express the importance of this issue, as well as how you propose it should be addressed. Extra
    credit will be given for actually sending your letter.
    Documentary Reflection: For this assignment, you will watch a documentary entitled “Oceans: The Mystery
    of the Missing Plastic” that details recent scientific research on the 'plastisphere': the nature, extent and
    fate of plastic pollution in the oceans. This will be accompanied by a set of questions to focus on in your
    reflection.
    Participation: You will be asked to read and engage with course readings and to constructively participate
    in class discussions and activities. What does it mean to engage? As part of your preparation for each topic
    you may be asked to think about real-world examples, reflect on the implications of these topics in your
    own daily life, and weigh the benefits, risks, and unintended consequences for society and the
    environment. You will be encouraged to speak and interact with your fellow students, share your own
    perspectives and experiences, and to complete the related "mini" activities.
    As a record of active participation and attendance, you will be asked to complete and submit ‘mini’ in-
    class work activities individually or in teams, e.g., collect some data, watch and reflect on a video or
    newspaper story, calculate your environmental footprint, participate in discussion, write a minute-paper,
    etc. These activities will help to illustrate key course concepts; some activities will help me (and you) to
    gauge your understanding of the topics as we progress through the course, and allow me to provide
    feedback. Sometimes, you may be asked to complete a work activity before the start of class (i.e., as
    preparation), during class, or for after class (as wrap-up and reflection). Your peers rely on you for your
    thoughtful and timely contributions to discussions and activities. I expect to learn a lot from you as well!
    In-class and outside-of-class work may be assigned at any point before or during the class. This will be
    announced in class and on BB. Participation credit will be given for thoughtful completion of this work. If
    you cannot make it to a particular class, you will need to let me know prior to the start of a class. If it is an
    excused absence, then I will provide you with an alternative way to obtain the associated in-class activity
    points outside of class.
    Full assignment & exam instructions will be posted to Blackboard and revisited throughout the term.
    Page 4
    Assignment Submission Policy
    Unless otherwise specified, all assignments are due by 5:00 pm California time via Blackboard Turnitin. The
    penalty for late submissions is 20% per day (or portion thereof). No make-up assignments will be allowed
    without explicit permission. If a you miss an assignment, you will receive a zero for that assignment.
    Instructions for all assignments will be posted to Blackboard (BB). Assignments will be graded and posted
    to Blackboard Gradebook within 7-14 days after the due date.
    Missed classes
    You are responsible for any material covered in class and related discussions, exercises and activities.
    Participation during regular class time is expected and encouraged.
    Technology:
    During class time, please refrain from accessing the internet and email for reasons other than those directly
    relevant to our class.
    Grading Timeline
    Exams and major assignments will be graded and returned within 7-14 days of the due date.
    Grading Breakdown
    Item Points % of grade
    Grading Scale
    Course final grades will be determined using the following scale:
    A 95-100
    A- 90-94
    B+ 87-89
    B 83-86
    B- 80-82
    C+ 77-79
    C 73-76
    C- 70-72
    D+ 67-69
    D 63-66
    D- 60-62
    F 59 and below
    Academic Conduct
    Plagiarism – presenting someone else’s ideas as your own, either verbatim or recast in your own words – is
    a serious academic offense with serious consequences. Please familiarize yourself with the discussion of
    plagiarism in SCampus in Part B, Section 11, “Behavior Violating University Standards”
    https://policy.usc.edu/scampus-part-b/ (scroll down to find Section 11). Other forms of academic
    dishonesty are equally unacceptable. See additional information in SCampus and university policies on
    scientific misconduct, https://policy.usc.edu/scientific-misconduct/. Any submitted work with evidence of
    plagiarism or other forms of academic misconduct, whether by accident or on purpose, will receive a grade
    of zero (0). Cases of academic misconduct may also be referred for further review and disciplinary action.
    Midterm 1 75 15.0%
    Midterm 2 75 15.0%
    Final Exam 150 30.0%
    Recognizing bias in the news 10 2.0%
    News Discussion/Presentation 15 3.0%
    Endangered species research 50 10.0%
    Documentary Reflection 30 6.0%
    Letter to a decision-maker 30 6.0%
    Reflection on Nature (5 pts X 3) 15 3.0%
    Participation 50 10.0%
    Page 5
    Course Schedule:
    Topics/Daily Activities Readings Deliverables
    Aug. 18 Introductions and Introduction
    to the Course Syllabus, Chapter 1 Getting to know you survey &
    Icebreaker Activity & Discussion
    Aug. 20
    What is science? Measures of
    Env health and understanding
    data.
    Chapter 1, Chapter 2 (Section 2.1),
    BB Readings
    Signup for 'Environment in the News'
    Discussion
    Aug. 25 Energy, Matter & Earth Systems Chapter 2, BB Readings
    Aug. 27 Ecosystem Ecology Chapter 3, BB Readings Recognizing Bias in the News
    Sept. 1 Climate and Biomes Chapter 7, BB Readings
    Sept. 3 Population and Community
    Ecology Chapter 5, BB Readings Proposal for your Endangered Species
    Research
    Sept. 8 Genetics and Evolution Chapter 4, BB Readings Reflection on Nature I
    Sept. 10 Biodiversity Chapter 4, BB Readings
    Sept. 15 MIDTERM 1: Lectures and readings August 18-September 10
    (inclusive) MIDTERM 1
    Sept. 17 Human Population Growth and
    Demographics Chapter 6, BB Readings
    Sept. 22 Conservation and Endangered
    Species Chapter 8, BB Readings Endangered Species Research
    Sept. 24 Terrestrial Resources Chapter 9, BB Readings
    Sept. 29 Freshwater and Marine
    Resources Chapter 11, BB Readings
    Oct. 1 Agriculture and Food Systems Chapter 10, BB Readings Reflection on Nature II
    Oct. 6 Geology and Mineral Resources Chapter 12, BB Readings
    Oct. 8 Nonrenewable Energy Chapter 13, BB Readings Proposal for your Letter to a Decision-maker
    Oct. 13 MIDTERM 2: Lectures and readings September 17-October 8
    (inclusive) MIDTERM 2
    Oct. 15 Renewable & Alternative Energy Chapter 13, BB Readings
    Oct. 20 Environmental Hazards &
    Human Health Chapter 14, BB Readings
    Oct. 22 Air Pollution and Solutions Chapter 15, BB Readings Letter to a Decision-maker
    Oct. 27 Water Pollution: PPCP and CoEC
    oh my! Chapter 11, BB Readings
    Oct. 29 Solid Waste and Solutions Chapter 16, BB Readings
    Nov. 3 Marine Plastic Pollution BB Readings, Documentary Documentary Reflection
    Nov. 5 Climate Change Chapter 15, BB Readings
    Nov. 10 Climate Change and Solutions BB Readings Reflection on Nature III
    Nov. 12 Environmental Justice Chapter 17, BB Readings
    FINAL
    EXAM
    Final exams will be held November 17-24. Refer to the final exam schedule in the USC Schedule of Classes at
    https://classes.usc.edu/term-20203/finals/
    Page 6
    Our Course Code of Conduct 1 :
    1. Share responsibility for including all voices in the conversation. If you tend to have a lot to say, make
    sure you leave sufficient space to hear from others. If you tend to stay quiet in group discussions,
    challenge yourself to contribute so others can learn from you.
    2. Listen respectfully. Don’t interrupt, turn to technology, or engage in private conversations while others
    are speaking. Use attentive, courteous body language. Comments that you make (whether asking for
    clarification, sharing critiques, or expanding on a point) should reflect that you have paid attention to
    the previous speakers’ comments.
    3. Be open to changing your perspectives based on what you learn from others. Try to explore new
    ideas and possibilities. Think critically about the factors that have shaped your perspectives. Seriously
    consider points-of-view that differ from your current thinking.
    4. When you disagree with your peers, challenge or critique the idea, not the person.
    5. Support your statements. Use evidence and provide a rationale (preferably from the material we are
    covering in class) for your points.
    6. Understand that we are bound to make mistakes in this space, as anyone does when approaching
    complex tasks or learning new skills. Strive to see your mistakes and others’ as valuable elements of the
    learning process.
    7. Understand that your words have effects on others. Speak with care. If you learn that something
    you’ve said was experienced as disrespectful or marginalizing, listen carefully and try to understand
    that perspective. Learn how you can do better in the future.
    8. Take care when generalizing about groups of people, whether you belong to that group or not.
    Consider who might feel excluded or devalued when you offer a broad characterization of a group. Do
    not ask others to speak on behalf of a group you perceive them to represent.
    9. Take pair work or small group work seriously. Remember that your peers’ learning is partly dependent
    upon your engagement.
    10. Understand that others will come to these discussions with different experiences from yours. Be
    careful about assumptions and generalizations you make based only on your own experience. Be open
    to hearing and learning from other perspectives.
    11. Make an effort to get to know other students. Introduce yourself to your peers during group
    discussion and class activities. Refer to your classmates by name and be attentive when they are
    speaking.
    12. Understand that there are different approaches to solving problems. If you are uncertain about
    someone else’s approach, ask a question to explore areas of uncertainty. Listen respectfully to how and
    why the approach could work.
    1 Adapted from the University of Michigan Center for Research on Learning and Teaching (CRLT) Discussion
    Guidelines: http://www.crlt.umich.edu/examples-discussion-guidelines
            """

    response = chain.run(inp)

    # assert response == expected_response, f"Expected {expected_response}, but got {response}"
    assert len(response) > 0, "Response is empty"

    print()
    # print("Input:", inp)
    print("Response:", response[0].json(indent=4))
    # logging.info("Input: %s", inp)
    # logging.info("Response: %s", [r.dict() for r in response])  # use .dict() to convert Pydantic models to dictionaries for logging
