from random import seed
from random import randint
topic = input("Please enter you essay topic here (please use progressive tense + noun, for example: drinking water, doing homework, etc.) ==> ")
times = 0

print(topic + "_________________________________________________________________________________________________________________")
quotes = ["\"To be or not to be.\" ",
          "\"If life were predictable it would cease to be life, and be without flavor.\" that is what Eleanor Roosevelt said. ",
          "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.\" said Oprah Winfrey. " ,
          "\"I sometimes would say Life is a wonder.\" -- John Cena, ",
          "\"Don't judge each day by the harvest you reap but by the seeds that you plant.\"",
          "\"You will face many defeats in life, but never let yourself be defeated.\" -Maya Angelou,",
          "\"Never let the fear of striking out keep you from playing the game.\" -Babe Ruth,",
          "\"Life is either a daring adventure or nothing at all.\" -Helen Keller,",
          "\"Many of life's failures are people who did not realize how close they were to success when they gave up.\" -Thomas A. Edison,",
          "\"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.\" -Dr. Seuss,",
          "\"Life itself is the most wonderful fairy tale.\" -Hans Christian Andersen",
          "\"Life is ours to be spent, not to be saved.\" -D. H. Lawrence",
          "\"In three words I can sum up everything I've learned about life: it goes on.\" -Robert Frost,",
          "\"Love the life you live. Live the life you love.\" -Bob Marley,",
          "\"Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.\"― Albert Einstein,",
          "\"So many books, so little time.\"― Frank Zappa,",
          "\"Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.\"― Bernard M. Baruch,",
          "\"You only live once, but if you do it right, once is enough.\"― Mae West,",
          "\"No one can make you feel inferior without your consent.\"― Eleanor Roosevelt, ",
          "\"I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel,” ",
          "\"A friend is someone who knows all about you and still loves you.\"― Elbert Hubbard, ",



]
#21 starters
starters = ["Ancient philosophers believe ",
            "Amazingly, ",
            "Surprisingly, "
            "According to my observation, ",
            "I strongly believe that ",
            "Contrary to common belief, ",
            "Now, ",
            "Unbelievably, ",
            "Today, ",
            "Overall, ",
            "By defult, ",
            "By the time this essay is published, ",
            "I think, ",
            "Many others also see ",
            "Although readers like you don't know, ",
            "My rivals think, ",
            "Most think, ",
            "Many think, ",
            "Studies show that the rich often think, ",
            "Research shows that the poor think, ",
            "The homeless protestors state, ",
            "Negotiations about " + topic + " were rejected, ",
            "Many others like the majority hold the opinion:  ",
]
#21 semistarters
semistarters = ["",
                "",
                "",
                "",
                "",
                "",
                "",
                "though that's what it apears to be like, it turns out that ",
                "though, ",
                "as it turns out, ",
                "which also enforces the idea that ",
                "many factors determine that, ",
                "for these reasons it occurs to me that,",
                "it's possible that ",
                "like many thought, ",
                "some imagined ",
                "if we analyze both recent history and reliable studies done on " + topic + " and the people involved in achieving it, ",
                topic + " is probably more interesting than you think. So, ",
                "many negative effects of " + topic + " were investigated by both modern and past philosophers. Some think that ",
                "for many years the pros and cons of " + topic + " were discussed, however, today, the attention is shifted so that ",
                "the possibility of " + topic + " being a paradox made it clear how ",
                "last week global institutions dedicated to settle the debate over the positives and negatives on " + topic + " has withdrawn due to insufficient funding. This unfortunate turn really shows ",
                "intellectuals eventually gave up on this topic. Why do people give up on " + topic + " so easily? perhaps now ",
                "political powers were involved in the world wide discussion about " + topic + ", yet none has won the hearts of the crowd. Quite possibly now ",
                "it is very cool to notice that ",
                "perhaps it's smart to see that ",
                "it is lucky if you witness how ",
                "we might have to settle for the explanation that ",
]
#there are so far 21 conjunctions
conjunctions = ["so ",
                "but also ",
                "that means ",
                "because ",
                "that's basically saying  ",
                "but ",
                "and ",
                "of course it means ",
                "which probably indicates ",
                "this quote tells us ",
                "obviously the message of this quote was ",
                "but after doing some digging on this topic, I realized this trying to say that ",
                "unfortunately this didn't get the attention it deserved but now we know it is trying to say ",
                "so it's possible that this was a warning about how likely that ",
                "thus we know that ",
                "from this we know it is apparent that ",
                "this tells us that sometimes it\'s important to beware that ",
                "can you believe it? Even people like them realized the importance to prove that ",
                "shocking, right? No one knew how powerful those words are, even today. On the brightside, we now care about analyzing the fact that ",
                "maybe they were trying to inform people that ",
                "unbelievably no one believed it until recently when ",
                ","
                ","
                ","
                ","
                ","
]


ideas = ["it is very urgent to solve the problem of ",
         "it requires lots of effort in the researching of ",
         "it is not  pointless to investigate ",
         "many facilities are also wondering if it is possible to prove the practicallity of ",
         "this discussion itself might be changing the very definition of ",
         "the very idea of " + topic + " is dangerous. We need to think over the decision of ",
         "modern researchers have wondered why the idea of " + topic + " has only shown in the recent years. They also wonder the very purpose of ",
         "it is important to put " + topic + " into the curriculum for highschool students for them to realise the signifigance of ",
         "the reason of " + topic + " being so facinating is actually because of the origin of the phrase: ",
         "atleast we still have the freedom to discuss about ",
         "many places do not have the freedom of discussing about ",
         "eventually we will all die from wars on ",
         "the false information related to " + topic + " is like drugs and religion. That's why we should stay way from ",
         "some day, humanity will go extinct because of ",
         "even ordinary people should carefully think about ",
         "poor people will die first from conflicts formed because of the political inaction on ",
         "we need to solving before it is to late the problem of ",
         "the death of pop culture is related to ",
         "the extinction of animals is the result of ",
         "the shortage of food can be attributed to ",
         "the epidemic of coronavirus can actually be linked to ",
         "it is time we face our bad decisions and make better ones because of ",


         ]

quote_start = ["it is infact appropriate to bring in a quote: ",
               "it is a good decision to showcase how what this person said about " + topic + " is infact very true: ",
               "it is a  good action to examine quotes about " + topic + " like this one: ",
               "it is obvious that to answer all the questions about " + topic + " a good quote is: ",
               "it is nice to know if the wise had said something like this: ",
               "the smart ones had repeatedly mentioned things like, ",
               "this quote really suites the question of " + topic + ": ",
               "only a few can think about things like this such as, ",
               "it is important to use a good quote:",
               "it is only beneficial if this essay use an appropriate quote: ",
               "a quote like this one should be used, ",
               "quotes like this deserve recognition under these circumstances, ",
               "here is a quote, ",
               "this good quote goes, ",
               "it is normal to feel the need to reflect on this quote, ",
               "it is relevant to here quote: ",
               "it\'s beneficial to society if we beware of this quote: ",
               "it is funny if this esssy does not quote: ",
               "famous quotes are necessary to gain understanding, ",
               "this quote reflects on the brutal reality, ",
               "we need to face exactly what this quote describes, ",
               "this quote answers, ",
               "no one ever doubted this quote, ",
               "this questions what is " + topic + " if it is not the state it is currently in and also what is " + topic + " if it is exactly the state it is in currently. "



]
conclusions = ["With all that being said, we need to think philosophically. Historically, philosophy encompassed any body of knowledge. From the time of Ancient Greek philosopher Aristotle to the 19th century, natural philosophy encompassed astronomy, medicine, and physics.",
               "Traditionally, the term philosophy referred to any body of knowledge. In this sense, philosophy is closely related to religion, mathematics, natural science, education and politics.",
               "Answering the very question of " + topic + " might require the deployment of Moral philosophy (ethics, from êthika, literally, having to do with character, disposition, manners). It was the study of goodness, right and wrong, justice and virtue.",
               "Does this question help progress the field of philosophy? Many philosophical debates that began in ancient times are still debated today. Colin McGinn and others claim that no philosophical progress has occurred during that interval.",
               "Coming up with a response to the question of " + topic + " requires us to understand what a question exactly is. A question is an utterance which typically functions as a request for information, which is expected to be provided in the form of an answer.  ",
               "What is the cost of solving the questions of " + topic + "? We need to understand ethics to decide. Ethics or moral philosophy is a branch of philosophy that involves systematizing, defending, and recommending concepts of right and wrong conduct.",
               "We need statistically reliable data to decide if the answers are right. But what consitutes reliability? Reliability in statistics and psychometrics is the overall consistency of a measure. A measure is said to have a high reliability if it produces similar results under consistent conditions." ,
               "Someone even wrote a poem dedicated to solving the question of " + topic + ": roses are red, violets are blue, " + topic + " is interesting, so are you.",
               "Further analysis is required to conclude " + topic + ". But what is an analysis? Analysis is the process of breaking a complex topic or substance into smaller parts in order to gain a better understanding of it. The technique has been applied in the study of mathematics and logic since before Aristotle (384–322 B.C.), though analysis as a formal concept is a relatively recent development.",
               "According to popular opinion, we need to consider the financial practicality of " + topic + ". But that means this essay will also need to investigate the very own definition of practicality. According to my own research, practcality is the quality or state of being practical. ",
               "To come up with a satisfactory answer, we need to examine the purpose of this essay. What is an essay? An essay is, generally, a piece of writing that gives the author's own argument — but the definition is vague, overlapping with those of a paper, an article, a pamphlet, and a short story. ",
               "Society need to better define what " + topic + " really is. So, we need to define what a good definition really is. A definition is a statement of the meaning of a term (a word, phrase, or other set of symbols). Definitions can be classified into two large categories, intensional definitions (which try to give the sense of a term) and extensional definitions (which try to list the objects that a term describes). ",
               "In a way, the discusion on " + topic + " is starting an intellectual revolution. How so? Well, we need to fully comprehend that revolutions can acually be slow but sweeping transformations of the entire society that take several generations to bring about (such as changes in religion). ",
               "Can humans come up with a universal and global solution to all the questions about " + topic + "? Maybe not, but atleast we can partially maximize our benefits. ",
               "Nevertheless, we still need to educate people om how urgent it is to solve the question of " + topic + ". But first, what dictates urgency? According to personal experiance, urgency is importance requiring swift action.",
               "Many people of old age deeply regret not taking time to think about " + topic + " when they were young. It is important for us to not make that same mistake. ",
               "Some researchers state that plagerism on this topic is justified because of how common this question is, it is impossible to come up with unique and original responses. ",
               "Oh, " + topic + " , so many has tried to solve your mystery, but none had succeeded. What a shame. ",
               "The internet has also been a popular arena for the debate over the justification for " + topic + ". So, we should also consider what justification really means. I will mention it later in the essay. ",
               "With all the things listed above, we also need to tackle this question from a different angle. ",
               "Not only that, other people have been agreeing. ",

]







while True:
    if times < 20:
        print(starters[randint(0,20)] + semistarters[randint(0,25)] +"\n"+ quote_start[randint(0,22)]  + quotes[randint(0,19)] + "\n" + conjunctions[randint(0,20)] + ideas[randint(0,21)] + topic + ".\n" + conclusions[randint(0,19)])
        times = times + 1







