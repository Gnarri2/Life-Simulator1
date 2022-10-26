import os as _os

DEBUG = False

MALE_NAMES = open("assets/male_names.txt").read().splitlines()
FEMALE_NAMES = open("assets/female_names.txt").read().splitlines()
LAST_NAMES = open("assets/last_names.txt").read().splitlines()

SAVE_PATH = filename = _os.getcwd() + "/game_saves"  # + "/gamedata.pickle"

SALARY_TAX_BRACKETS = [
    [9950, 0.1],
    [40525, 0.12],
    [86375, 0.22],
    [164925, 0.24],
    [209425, 0.32],
    [523600, 0.35],
    0.37,
]

from src.lifesim_lib.translation import _

ILLNESSES_TRANSLATIONS = {
    "Depression": _("Depression"),
    "High Blood Pressure": _("High Blood Pressure"),
}

COMPLIMENTS = [
    _("a bubbly personality"),
    _("a champion"),
    _("a gem"),
    _("a genius"),
    _("a jewel"),
    _("a legend"),
    _("a player"),
    _("a revolutionary"),
    _("a smart cookie"),
    _("a treasure"),
    _("a winner"),
    _("a wizard"),
    _("a visionary"),
    _("adorable"),
    _("admirable"),
    _("an OG"),
    _("brave"),
    _("bright"),
    _("brilliant"),
    _("charming"),
    _("clever"),
    _("cool"),
    _("courageous"),
    _("delightful"),
    _("dope"),
    _("elite"),
    _("fascinating"),
    _("fearless"),
    _("fresh"),
    _("gorgeous"),
    _("golden"),
    _("groovy"),
    _("inspiring"),
    _("intelligent"),
    _("magnificent"),
    _("motivating"),
    _("neat"),
    _("nifty"),
    _("one-of-a-kind"),
    _("a perfect 10"),
    _("phenomenal"),
    _("rad"),
    _("smart"),
    _("spectatular"),
    _("stellar"),
    _("strong"),
    _("stunning"),
    _("stylish"),
    _("swell"),
    _("the best"),
    _("the greatest"),
    _("the life of the party"),
    _("unparalled"),
    _("wise"),
    _("wonderful"),
]

# Insults moved to the bottom


# Conversations section:
# This section is broken into basic conversation depths. It may be useful in future to e.g. not have a heart-to-heart with your {enemy}, {boss}, {whoever}.
# It might also be useful for age / job dependent topics, or to facilitate 'you spoke to your {relation} about which is better {movie} or {movie}' / 'you spoke with your {relation} about {sport} and how {team} will beat {team} this year'

# Casual chats, small-talk, etc. (can take words like 'chatted with your {relation} about' or 'talked about' prior to calling)
CHATS = [
    _("the hierarchy of licorice"),
    _("which is better, Star Wars or Star Trek"),
    _("which is better, Coke or Pepsi"),
    _("which is better, Lord of the Rings or Harry Potter"),
    _("who is better, the Red Sox or Yankees"),
    _("who will win the Monaco Grand Prix"),
    _("how it's illegal to masturbate in Indonesia"),
    _("whether you would rather live without music or television"),
    _("why mannequins have erect nipples"),
    _("Angleina Jolie's lips"),
]
CHATS_INFANT = [
	_("choo-choo trains, and then both made baby noises at each other"),
	_("why 'A' is for 'Apple'"),
	_("the fluffy pussy cat"),
	_("Thomas the Tank Engine"),
	_("Dinosaur Train"),
	_("Alphablocks"),
	_("Sesame street"),
	_("Mickey Mouse"),
	_("'O' is for 'Owl'"),
	_("'O' is for 'Octopus'"),
	_("'O' is for 'Orange'"),
    _("three blind mice"),
]
CHATS_CHILD = [
    _("which super power you would most like to have"),
    _("which super power they would most like to have"),
    _("what they want to be when they grow up"),
    _("how much you hate vegetables"),
    _("how scary the toilet is when it gets flushed"),
    _("why the sky is blue"),
    _("where water goes when the toilet gets flushed"),
    _("your favourite movie character"),
]
CHATS_TEEN = [
    _(""),
]
CHATS_ADULT = [
    _(""),
]
CHATS_CLASSMATES_PRIMARY = [
    _(""),
]
CHATS_CLASSMATES_SECONDARY = [
    _(""),
]
CHATS_CLASSMATES_TERTIARY = [
    _(""),
]
CHATS_CO_WORKERS = [
    _(""),
]


# Academic / debatable topics, topics that are contentious etc. (can take words like 'discussed' prior to calling)
DISCUSSIONS = [
    _("why cats are better than dogs"),
    _("why dogs are better than cats"),
    _("the Russia-Ukraine War"),
    _("High Fuel Prices"),
    _("the Metaverse"),
    _("the Economic crisis of Sri Lanka"),
    _("Moonlighting"),
    _("the Pros and Cons of working from home"),
    _("whether people should invest in cryptocurrency"),
    _("the Biomedical waste crisis"),
    _("the impact of 5G on the global economy"),
    _("how to prevent the next pandemic"),
    _("the impact of COVID-19 on the global economy"),
    _("the pros and cons of block chain technology"),
    _("the role of social media in international politics"),
    _("how to end the threat of nuclear war"),
    _("the impact of COVID-19 on the education sector"),
    _("Taliban rule in Afghanistan"),
    _("the rise of the gig economy"),
    _("the harms of passive smoking"),
    _("the advantages and disadvantages of having a credit card"),
    _("whether software should be free for everyone"),
    _("whether gambling should be allowed from the age of 16"),
    _("problems caused by the economic boycott in Cuba"),
    _("how international trade barriers work"),
    _("how the United Nations is based on diplomacy and strengthening relationships"),
    _("whether or not public schools are safe enough"),
    _("whether it is necessary to hold value in what you argue"),
    _("why drink driving is dangerous"),
    _("how India became such a large milk producer"),
    _("how to make money with recycling"),
    _("the decreasing productivity of the Japanese workforce"),
    _("a business model to help health-conscious customers"),
    _("what the best technologies are to safeguard the right of free speech on the internet"),
    _("what the best technologies are to safeguard the right of privacy on the internet"),
    _("how to check for the signs of burnout"),
    _("how to overcome the coal crisis in India"),
    _("the causes of bullying in schools"),
    _("why we should have a minimum wage"),
    _("whether universal basic income is a good idea"),
    _("the leadership changes needed in our country"),
    _("whether empowering women is the solution to violence against women"),
    _("the effects of communalism on social cohesion"),
    _("whether we're becoming too sensitive in society"),
    _("lessons for the world from the COVID-19 pandemic"),
    _("whether crime rates increase because of unemployment"),
    _("causes of poverty around the world"),
    _("the effects of the Internet of Things on our lives"),
    _("whether drug abuse is rampant among teenagers"),
    _("whether anemia effects urban society"),
    _("gender equality in the workplace"),
    _("whether the wealthy should be taxed more"),
    _("whether the poor should be given more assistance"),
    _("whether it is possible to maintain a work-life balance"),
    _("whether saying 'women make good managers' is sexist like saying 'asians are good at maths' is racist"),
    _("whether job creators are needed more than job seekers"),
    _("whether a borderless world is a myth or a reality"),
    _("what would happen if Bitcoin crashed to zero and whether it is possible"),
    _("business ethics in today's market compared with the past and the potential future"),
    _("whether patience is important in business and management"),
    _("whether the family-run business is relevant in today's market"),
    _("whether E-commerce discounts are harmful in the long run and is it the business or customer being harmed"),
    _("whether globalisation is an opportunity or a threat"),
    _("how markets are found and not created"),
    _("whether the world is ready for a cashless society"),
    _("whether physical infrastructure is the answer to social equality"),
    _("whether the public sector being a guarantor of job security is a myth"),
    _("whether a circular economy is key to sustainable development"),
    _("the contribution of the Indian IT industry to the US and global economy"),
    _("whether democracy is a hindrance to economic reforms in India"),
    _("the technology behind Zero Budget Natural Farming"),
    _("the effects of technological change on jobs"),
    _("whether pervasive technology is creating a generation of cyber zombies"),
    _("whether the IT industry will create more or less jobs in the future"),
    _("whether artificial intelligence can replace human intelligence"),
    _("the effects of big data on information privacy"),
    _("whether automation will create more or less jobs"),
    _("the benefits and challenges of data localisation"),
    _("whether artifical intelligence will change the future"),
    _("how technology can be used to tackle financial crimes"),
    _("whether polythene bags should be completely banned"),
    _("how to control air pollution levels"),
    _("whether green jobs are essential for sustainable development"),
    _("how to manage natural disasters"),
    _("how to manage financial disasters"),
    _("methods of disaster recovery"),
    _("the effects of Coronaviruses on the environment"),
    _("whether smart farming is the future of agriculture"),
    _("whether genetic engineering in agriculture is good or bad"),
    _("the effects of climate on the farming system and food supply"),
    _("whether automation in farming is good"),
    _("whether collective farming is a boon or a bane"),
    _("our views on natural versus factory farming"),
    _("our views on conventional farming and organic farming"),
    _("the role of women in agriculture"),
    _("whether agroforestry destroys the environment"),
    _("gay marriage and your views on it"),
    _("whether war is the best option to solve international disputes"),
    _("whether primary school children should be allowed to own mobile phones"),
    _("whether using animals for medical research should be allowed"),
    _("whether men and women will ever be equal, if they already are, and whether equality will last"),
    _("whether you can have a happy family life and a successful career at the same time"),
    _("whether marriage is an outdated institution"),
    _("whether citizens should be allowed to carry guns and other weapons"),
    _("whether the death penalty is acceptable for any reasons"),
    _("whether non-citizens and tourists should be allowed to vote in their country of residence"),
    _("whether sex education should be taught to children under 12"),
    _("whether or not women are paid the same as men"),
    _("whether bribery and corruption is acceptable in government"),
    _("whether bribery and corruption is acceptable in private business"),
    _("whether music that glorifies violence should be banned"),
    _("whether condoms should be distributed for free in primary schools"),
    _("whether nuclear weapons are necessary weapons"),
    _("whether teachers should be allowed to carry guns"),
    _("whether professional sports people earn too much money"),
    _("our views on whether or not beauty contests should be banned"),
    _("our views on whether or not cosmetic surgery should be outlawed"),
    _("our views on whether or not abortions are okay"),
    _("our views on whether or not social deprivation causes crime"),
    _("our views on whether or not military service should be compulsory"),
    _("our views on whether or not war is ever an option for solving international disputes"),
    _("our views on whether or not torture can be acceptable in some cases"),
    _("our views on whether or not curfews keep teens out of trouble"),
    _("our views on whether or not we're becoming too dependent on computers"),
    _("our views on whether or not smoking should be banned worldwide"),
    _("our views on whether or not it should be illegal to ride a bicycle without a helmet"),
    _("our views on whether or not single sex schools are bad for childhood development and lead to unhealthy views of the opposite sex"),
    _("our views on whether or not homework is harmful"),
    _("our views on whether or not the United Nations is a failed organisation"),
    _("our views on whether or not intelligence tests should be given before couples can have children"),
    _("our views on whether or not a woman's place is in the home"),
    _("our views on whether or not it's a man's world"),
    _("our views on whether or not money makes you happy"),
    _("our views on whether or not money can buy you happiness"),
    _("our views on whether or not the internet must be censored to protect society"),
    _( "our views on whether or not genetically modified foods have no ill health effects"),
    _("our views on whether a man should have a wife for the family and a paramour for pleasure"),
    _("our views on whether a woman should have a husband for the family and a paramour for pleasure"),
    _("our views on whether soft drugs should be legalised"),
    _("our views on whether or not electric cars help the environment"),
    _("our views on whether or not staying unmarried leads to a happier life"),
    _("our views on whether or not software piracy is a real crime"),
    _("our views on whether or not religion is needed"),
    _("our views on whether veganism is the key to solving climate change"),
    _("our views on whether the police force is institutionally racist"),
    _("our views on whether democracy must be imposed on nations"),
    _("our views on whether the war in Iraq was justified"),
    _("our views on whether your race affects your intelligence"),
    _("our views on whether your race affects your sporting ability"),
    _("our views on whether the world is over populated and steps must be taken to reduce births"),
    _("whether or not euthanasia should be illegal"),
    _("whether or not cloning is a valuable scientific pursuit"),
    _("whether obesity is a disease and not a lifestyle choice"),
    _("whether or not video games contribute to youth violence"),
    _("whether the drinking age should be lowered"),
    _("whether the drinking age should be raised"),
    _("whether the smoking age should be lowered"),
    _("whether the smoking age should be raised"),
    _("whether the age of consent should be lowered"),
    _("whether the age of consent should be raised"),
    _("whether the voting age should be lowered"),
    _("whether the voting age should be raised"),
    _("whether the driving age should be lowered"),
    _("whether the driving age should be raised"),
    _("whether the gambling age should be lowered"),
    _("whether the gambling age should be raised"),
    _("whether the military service age should be lowered"),
    _("whether the military service age should be raised"),
    _("whether drugs should be accepted in sports"),
    _("whether self driving cars are going to make our lives easier"),
    _("whether climate change exists"),
    _("whether carbohydrates are more damaging than fats"),
    _("whether terrorism can be justifed"),
    _("whether or not street prostitution should be illegal"),
    _("whether or not prostitution in a brothel should be illegal"),
    _("whether or not prostituting yourself in your own home should be illegal"),
    _("whether prisoners should be allowed to vote"),
    _("whether prenuptual agreements make families stronger"),
    _("whether corporal punishment should be allowed in schools"),
]
DISCUSSIONS_INFANT = [
    _(""),
]
DISCUSSIONS_CHILD = [
    _("if it is better to scrunch or fold"),
    _("if it is better to squat or sit"),
    _("if it is better to shower or bath"),
    _("if it is better to wipe from the front or back"),
    _("if it is better to "),
    _("your favourite movie character"),
    _("your imaginary friend"),
    _("your most prized posession"),
]
DISCUSSIONS_TEEN = [
    _(""),
]
# Important 'life' talks
TALKS = [
    _("not spending enough time with your family"),
]
TALKS_INFANT = [
    _("the importance of not sucking your thumb"),
]
TALKS_CHILD = [
    _("not drawing on the kitchen table"),
]
TALKS_TEEN = [
    _("the importance of cleaning up after yourself"),
]
TALKS_ADULT = [_("the importance of saving for retirement")]

# Emotionally sincere, serious, or personal conversations
HEART_TO_HEARTS = [
    _("the best gift you ever received"),
    _("your most bizarre pet peeves"),
    _("why you love your closest friends"),
    _("your favourite books to read at the beach"),
    _("your favourite foods to eat on a cold night"),
    _("your biggest turn offs in other people"),
    _("remembering the times when you've felt closest together"),
    _("what you would do if you knew you couldn't fail"),
    _("your favourite summertime memory"),
    _("something you've always wanted to try"),
    _("things you've always wanted to try"),
    _("a moment in history you would have liked to have been a part of"),
    _("how to manage money better"),
    _("where you would go if you could time travel"),
    _("what superpower you would have if you could have one"),
    _("what you're feeling thankful for today"),
    _("how much they mean to you"),
    _("something that you know you don't need but you're really grateful you have"),
    _("your fears of not accomplishing your New Year resolutions"),
    _("how silly New Year's resolutions are"),
    _("the best part of your day"),
]
HEART_TO_HEARTS_TEEN = [
    _("what happens when we die"),
]

# Celebrity list
# For use in situations like '{celebrity} followed you on instagram'; or "you were talking with your {relation} about {adam brody}'s {left ankle}"; "while you were working at {chicken shop} you noticed {seth rogan} stuck in traffic outside. You waved, {he} didn't wave back." etc
# Rough alphabetical order only so far

CELEBRITY_MALE_ACTOR = [
    _("Alex Pettyfer"),
    _("Ashton Kutcher"),
    _("Adam Brody"),
    _("Andrew Garfield"),
    _("Alexander Skarsgård"),
    _("Austin Nichols"),
    _("Allan Hyde"),
    _("Adam Garcia"),
    _("Arnold Schwarzenegger"),
    _("Ben McKenzie"),
    _("Bryan Greenberg"),
    _("Brad Pitt"),
    _("Bradley Cooper"),
    _("Channing Tatum"),
    _("Clive Owen"),
    _("Chace Crawford"),
    _("Cam Gigandet"),
    _("Chris Brown"),
    _("Chris Pine"),
    _("Chad Michael Murray"),
    _("Columbus Short"),
    _("Christian Bale"),
    _("Casey Affleck"),
    _("Cillian Murphy"),
    _("Daniel Craig"),
    _("David Beckham"),
    _("Ed Westwick"),
    _("Eric Bana"),
    _("Emile Hirsch"),
    _("Eric Dane"),
    _("Gerard Butler"),
    _("Garrett Hedlund"),
    _("Hayden Christensen"),
    _("Hugh Jackman"),
    _("Hugh Laurie"),
    _("Hugh Dancy"),
    _("Heath Ledger"),
    _("Ian Somerhalder"),
    _("James Lafferty"),
    _("James Marsden"),
    _("John Mayer"),
    _("Jude Law"),
    _("Jensen Ackles"),
    _("Jake Gyllenhaal"),
    _("Justin Chambers"),
    _("Jesse Metcalfe"),
    _("Justin Timberlake"),
    _("Javier Bardem"),
    _("Joe Manganiello"),
    _("Johnny Depp"),
    _("James Franco"),
    _("Jack O'Connell"),
    _("Kellan Lutz"),
    _("Josh Hartnett"),
    _("Jason Segel"),
    _("Jared Padalecki"),
    _("Joseph Gordon-Levitt"),
    _("Liam Hemsworth"),
    _("Leonardo DiCaprio"),
    _("Luke Pasqualino"),
    _("Milo Ventimiglia"),
    _("Mark Salling"),
    _("Matthew Goode"),
    _("Mads Mikkelsen"),
    _("Marshall Mathers"),
    _("Mekhi Phifer"),
    _("Matt Lanter"),
    _("Mike Vogel"),
    _("Nick Zano"),
    _("Orlando Bloom"),
    _("Patrick Swayze"),
    _("Penn Badgley"),
    _("Peter Facinelli"),
    _("Paul Walker"),
    _("Ryan Gosling"),
    _("Ryan Reynolds"),
    _("Robbie Jones"),
    _("Robert Pattinson"),
    _("Rick Malambri"),
    _("Ryan Kwanten"),
    _("Ryan Phillippe"),
    _("Rafi Gavron"),
    _("Sam Worthington"),
    _("Sean Faris"),
    _("Sylvester Stallone"),
    _("Seth Rogan"),
    _("Shia LaBeouf"),
    _("Stephen Colletti"),
    _("Shane West"),
    _("Simon Rex"),
    _("Taylor Lautner"),
    _("Tom Hardy"),
    _("Tupac Shakur"),
    _("Tristan Mack Wilds"),
    _("Timothy Olyphant"),
    _("Tom Welling"),
    _("Travis Barker"),
    _("Wentworth Miller"),
    _("Zac Efron"),
]
CELEBRITY_MALE_ATHLETE = [
    _("Arnold Schwarzenegger"),
    _("David Beckham"),
]
CELEBRITY_MALE_AUTHOR = [
    _("Joe Manganiello"),
]
CELEBRITY_MALE_BUSINESS = [
    _("Elon Musk"),
]
CELEBRITY_MALE_DANCER = [
    _("Justin Timberlake"),
]
CELEBRITY_MALE_DIRECTOR = [
    _("Joe Manganiello"),
]
CELEBRITY_MALE_FASHION_DESIGNER = [
    _("Michael Kors"),
    _("Tom Ford"),
]
CELEBRITY_MALE_MODEL = [
    _("David Gandy"),
    _("Sean O'Pry"),
]
CELEBRITY_MALE_MUSICIAN = [
    _("Eminem"),
    _("Jared Followill"),
    _("John Mayer"),
    _("Justin Timberlake"),
    _("Tupac Shakur"),
]
CELEBRITY_MALE_POLITICIAN = [
    _("Arnold Schwarzenegger"),
]
CELEBRITY_MALE_PORNSTAR = [
    _("James Deen"),
]
CELEBRITY_MALE_PRODUCER = [
    _("Arnold Schwarzenegger"),
    _("Brad Pitt"),
    _("Joe Manganiello"),
]
CELEBRITY_MALE_ROYAL = [
    _("Prince Carl Philip of Sweden, Duke of Värmland"),
]
CELBRITY_MALE_SCREENWRITER = [
    _("Sylvester Stallone"),
    _("Seth Rogan"),
]
CELEBRITY_MALE_SELF = [
    _("Arnold Schwarzenegger"),
]
CELEBRITY_MALE_SOCIAL_MEDIA = [
    _("Zach King"),
]
CELEBRITY_MALE_WRESTLER = [
    _("Randy Orton"),
]
CELEBRITY_MALE_WRITER = [
    _("Stan Lee"),
]

CELEBRITY_FEMALE_ACTOR = [
    _("Adriana Lima"),
    _("Aishwarya Rai Bachchan"),
    _("Alessandra Ambrosio"),
    _("Amber Heard"),
    _("Ana Beatriz Barros"),
    _("Anna Paquin"),
    _("AnnaSophia Robb"),
    _("Anne Vyalitsyna"),
    _("Angelina Jolie"),
    _("Ashley Benson"),
    _("Ashley Greene"),
    _("Bar Refaeli"),
    _("Behati Prinsloo"),
    _("Beyoncé Knowles"),
    _("Blake Lively"),
    _("Brooklyn Decker"),
    _("Candice Swanepoel"),
    _("Cassie Ventura"),
    _("Charlize Theron"),
    _("Cheryl Cole"),
    _("Chloë Grace Moretz"),
    _("Cindy Crawford"),
    _("Demi Lovato"),
    _("Denise Richards"),
    _("Diane Kruger"),
    _("Doutzen Kroes"),
    _("Elisha Cuthbert"),
    _("Emilia Clarke"),
    _("Emily Blunt"),
    _("Emma Stone"),
    _("Emma Watson"),
    _("Erin Heatherton"),
    _("Eva Green"),
    _("Eva Longoria"),
    _("Eva Mendes"),
    _("Freida Pinto"),
    _("Gisele Bündchen"),
    _("Hilary Duff"),
    _("Indiana Evans"),
    _("Irina Shayk"),
    _("Isabel Lucas"),
    _("Izabel Goulart"),
    _("Jenna Dewan"),
    _("Jennifer Lawrence"),
    _("Jessica Alba"),
    _("Jessica Biel"),
    _("Jordana Brewster"),
    _("Josie Maran"),
    _("Karolina Kurkova"),
    _("Kate Beckinsale"),
    _("Kate Upton"),
    _("Katie Holmes"),
    _("Keira Knightley"),
    _("Kelly Brook"),
    _("Kendall Jenner"),
    _("Kim Kardashian"),
    _("Kristen Stewart"),
    _("Kristin Kreuk"),
    _("Laetitia Casta"),
    _("Lauren Conrad"),
    _("Lily Aldridge"),
    _("Lucy Hale"),
    _("Marion Cotillard"),
    _("Nikki Reed"),
    _("Nina Dobrev"),
    _("Olivia Wilde"),
    _("Malin Akerman"),
    _("Marisa Miller"),
    _("Megan Fox"),
    _("Minka Kelly"),
    _("Mila Kunis"),
    _("Miranda Kerr"),
    _("Monica Bellucci"),
    _("Natalia Vodianova"),
    _("Natalie Portman"),
    _("Nicole Scherzinger"),
    _("Olivia Culpo"),
    _("Penélope Cruz"),
    _("Rachel Bilson"),
    _("Rachel McAdams"),
    _("Rachael Taylor"),
    _("Rachel Weisz"),
    _("Rihanna Fenty"),
    _("Roselyn Sanchez"),
    _("Rosie Huntington-Whiteley"),
    _("Salma Hayek"),
    _("Sara Carbonero"),
    _("Scarlett Johansson"),
    _("Selena Gomez"),
    _("Shanina Shaik"),
    _("Shay Mitchell"),
    _("Sienna Miller"),
    _("Sofía Vergara"),
    _("Stacy Keibler"),
    _("Tyra Banks"),
    _("Vanessa Hudgens"),
    _("Ximena Navarrete"),
    _("Zoe Saldana"),
]
CELEBRITY_FEMALE_ATHLETE = [
    _("Serena Williams"),
]
CELEBRITY_FEMALE_BUSINESS = [
    _("Sofía Vergara"),
]
CELEBRITY_FEMALE_CHEERLEADER = [
    _("Demi Lovato"),
    _("Stacy Keibler"),
]
CELEBRITY_FEMALE_DANCER = [
    _("Ashley Benson"),
    _("Cassie Ventura"),
    _("Jenna Dewan"),
    _("Roselyn Sanchez"),
    _("Stacy Keibler"),
]
CELEBRITY_FEMALE_FASHION_DESIGNER = [
    _("Kim Kardashian"),
    _("Rihanna Fenty"),
]
CELEBRITY_FEMALE_MODEL = [
    _("Adriana Lima"),
    _("Aishwarya Rai Bachchan"),
    _("Alessandra Ambrosio"),
    _("Ana Beatriz Barros"),
    _("Anne Vyalitsyna"),
    _("Bar Refaeli"),
    _("Behati Prinsloo"),
    _("Brooklyn Decker"),
    _("Candice Swanepoel"),
    _("Cassie Ventura"),
    _("Cindy Crawford"),
    _("Denise Richards"),
    _("Doutzen Kroes"),
    _("Elisha Cuthbert"),
    _("Eva Green"),
    _("Gisele Bündchen"),
    _("Irina Shayk"),
    _("Izabel Goulart"),
    _("Jenna Dewan"),
    _("Josie Maran"),
    _("Karolina Kurkova"),
    _("Kate Upton"),
    _("Kelly Brook"),
    _("Kendall Jenner"),
    _("Laetitia Casta"),
    _("Lily Aldridge"),
    _("Malin Akerman"),
    _("Marisa Miller"),
    _("Miranda Kerr"),
    _("Monica Bellucci"),
    _("Natalia Vodianova"),
    _("Olivia Culpo"),
    _("Rachael Taylor"),
    _("Roselyn Sanchez"),
    _("Rosie Huntington-Whiteley"),
    _("Shay Mitchell"),
    _("Sienna Miller"),
    _("Sofía Vergara"),
    _("Stacy Keibler"),
    _("Tyra Banks"),
    _("Ximena Navarrete"),
]
CELEBRITY_FEMALE_MUSICIAN = [
    _("Ashley Benson"),
    _("Beyoncé Knowles"),
    _("Cassie Ventura"),
    _("Cheryl Cole"),
    _("Demi Lovato"),
    _("Indiana Evans"),
    _("Minka Kelly"),
    _("Rihanna Fenty"),
    _("Roselyn Sanchez"),
    _("Selena Gomez"),
]
CELEBRITY_FEMALE_POLITICIAN = [
    _("Hillary Clinton"),
]
CELEBRITY_FEMALE_PORNSTAR = [
    _("Jenna Jameson"),
]
CELEBRITY_FEMALE_PRODUCER = [
    _("Charlize Theron"),
    _("Cindy Crawford"),
    _("Marion Cotillard"),
    _("Roselyn Sanchez"),
    _("Selena Gomez"),
    _("Tyra Banks"),
]
CELEBRITY_FEMALE_ROYAL = [
    _("Catherine Middleton, Princess of Wales"),
]
CELBRITY_FEMALE_SCREENWRITER = [
    _("Nikki Reed"),
]
CELEBRITY_FEMALE_SELF = [
    _("Catherine Middleton, Princess of Wales"),
    _("Natalia Vodianova"),
    _("Pippa Middleton"),
]
CELEBRITY_FEMALE_SOCIAL_MEDIA = [
    _("Olivia Culpo"),
]
CELEBRITY_FEMALE_WRESTLER = [
    _("Stacy Keibler"),
]
CELEBRITY_FEMALE_WRITER = [
    _("Kim Kardashian"),
    _("Roselyn Sanchez"),
    _("Shay Mitchell"),
    _("Tyra Banks"),
]


# List of Urban locations (a park, a bank etc.) called after 'to' or 'at' "we went to {urban_location}", "we spent time at {urban_location}"
# terms like 'downtown' arent in this list. you cant write 'spent time at downtown' over 'spent time downtown', or 'went to downtown' over 'went downtown'
# 'downtown' and other similar terms are in URBAN_DIRECTIONAL below

URBAN_LOCATION = [
	_("an abandoned building"),
	_("an abandoned factory"),
	_("an abandoned house"),
	_("an abandoned office building"),
	_("an abandoned school"),
	_("an airport"),
	_("an airfield"),
	_("an alleyway"),
	_("an ambulance station"),
	_("an apartment building"),
	_("an aquarium"),
	_("an arcade"),
	_("an art gallery"),
	_("an avenue"),
	_("a bakery"),
	_("a bank"),
	_("a bar"),
	_("a barber shop"),
	_("a beauty salon"),
	_("a bed & breakfast"),
	_("a bicycle rental stand"),
	_("a billboard"),
	_("a bookstore"),
	_("a boulevard"),
	_("a bowling alley"),
	_("a bridge"),
	_("a bus stop"),
	_("a butcher's shop"),
	_("a cafe"),
	_("a canal"),
	_("the central business district"),
	_("a church"),
	_("City Hall"),
	_("a clinic"),
	_("a coffee shop"),
	_("a college"),
	_("a community centre"),
	_("a community gardens"),
	_("a concert hall"),
	_("a condominium"),
	_("a construction site"),
	_("a convenience store"),
	_("a court"),
	_("a cycle highway"),
	_("a daycare centre"),
	_("a dentist"),
	_("a department store"),
	_("a dock"),
	_("the docks"),
	_("a doctor's office"),
	_("some drainage infrastructure"),
	_("a dry cleaner"),
	_("an embassy"),
	_("a factory"),
	_("a fire hydrant"),
	_("a fire station"),
	_("a flower shop"),
	_("a garbage facility"),
	_("a garden"),
	_("a gardens"),
	_("a government building"),
	_("a green-roof"),
	_("a grocery store"),
	_("a greengrocer"),
	_("a gym"),
	_("a gymnasium"),
	_("a harbour"),
	_("the harbour"),
	_("a highway"),
	_("a historical building"),
	_("a historical site"),
	_("a hospital"),
	_("a hotel"),
	_("a house"),
	_("a jail"),
	_("a karaoke bar"),
	_("a karaoke lounge"),
	_("a landmark"),
	_("a laundromat"),
	_("a library"),
	_("a linear park"),
	_("a market"),
	_("the markets"),
	_("a mixed-use building"),
	_("a mixed-use street"),
	_("a monument"),
	_("a movie theatre"),
	_("a museum"),
	_("a nature reserve"),
	_("a newspaper office"),
	_("some night architecture"),
	_("a nightclub"),
	_("a nursery school"),
	_("a nursing home"),
	_("an observatory"),
	_("an office building"),
	_("an opera house"),
	_("some outdoor seating"),
	_("an overpass"),
	_("a park"),
	_("a patisserie"),
	_("some pedestrian infrastructure"),
	_("a performance theatre"),
	_("a pharmacist"),
	_("a place of worship"),
	_("a play street"),
	_("a playground"),
	_("a police station"),
	_("a pond"),
	_("a port"),
	_("the port"),
	_("a post office"),
	_("a prison"),
	_("a product showroom"),
	_("a pub"),
	_("a public bath"),
	_("a public pool"),
	_("a public square"),
	_("a public toilet"),
	_("a radio station"),
	_("a railway line"),
	_("a railway station"),
	_("a recreation centre"),
	_("a recreation facility"),
	_("some remarkable architecture"),
	_("a restaurant"),
	_("a river"),
	_("a school"),
	_("the sewers"),
	_("a shopping centre"),
	_("a shopping mall"),
	_("a shop"),
	_("a skating rink"),
	_("a skyscraper"),
	_("a spa"),
	_("a sports facility"),
	_("a sports shop"),
	_("a sports stadium"),
	_("a sports store"),
	_("a stadium"),
	_("a stream"),
	_("a street"),
	_("some street art"),
	_("a street food vendor"),
	_("a street vendor"),
	_("a street light"),
	_("some street lights"),
	_("a strip of shops"),
	_("a subway station"),
	_("a swimming pool"),
	_("a synagogue"),
	_("a taxi stand"),
	_("a technology centre"),
	_("some tech infrastructure"),
	_("a television station"),
	_("a tennis court"),
	_("a temple"),
	_("a temple complex"),
	_("a theme park"),
	_("a tower"),
	_("a traffic light"),
	_("some traffic lights"),
	_("a train line"),
	_("a train station"),
	_("a tree"),
	_("some trees"),
	_("the underground"),
	_("an underpass"),
	_("a university"),
	_("an urban farm"),
	_("an urban forest"),
	_("a vending machine"),
	_("some vending machines"),
	_("a vertical park"),
	_("a visitor centre"),
	_("a void deck"),
	_("a water pipe"),
	_("some water pipes"),
	_("a water tower"),
	_("a waterfront"),
	_("the waterfront"),
	_("a waterfront tower"),
	_(""),
	_(""),
]

# List of urban story building directional movement terms.
# E.g. for 'we went {downtown} to {an urban forest}', or 'we spent time {across town} at {a void deck}

URBAN_DIRECTIONAL = [
	_("across the river"),
	_("across town"),
	_("downtown"),
	_("down the road"),
	_("over the road"),
	_("up the road"),
	_("up the street"),
	_(""),
]

# List of past tense urban movement terms
# Use for 'We {took the train} {downtown} to {an urban forest}

URBAN_MOVEMENT = [
	_("caught the bus"),
	_("hiked"),
	_("hitch-hiked"),
	_("jogged"),
	_("knocked about"),
	_("legged it"),
	_("meandered"),
	_("ran"),
	_("rode"),
	_("rowed a boat"),
	_("skated"),
	_("took a bus"),
	_("took a cab"),
	_("took a taxi"),
	_("took the train"),
	_("took a water taxi"),
	_("walked"),
	_("went jogging"),
]

# List of rural locations

RURAL_LOCATION = [
	_("a barn"),
	_("a country lane"),
	_("a dam"),
	_("a farm"),
	_("a field"),
	_("a fish farm"),
	_("a paddock"),
	_("a hay shed"),
	_("a windmill"),
]

# List of Natural locations (a mountain, a forest etc.)

NATURAL_LOCATION = [
	_("an alluvial fan"),
	_("an archipelago"),
	_("the archipelago"),
	_("an atoll"),
	_("a sand bar"),
	_("a barchan"),
	_("a basin"),
	_("the bay"),
	_("a coastal bay"),
	_("the bayside"),
	_("a beach"),
	_("the beach"),
	_("a butte"),
	_("the buttes"),
	_("a cape"),
	_("a canyon"),
	_("the canyon"),
	_("a cave"),
	_("the caves"),
	_("a channel"),
	_("a cliff"),
	_("the cliffs"),
	_("the coast"),
	_("a desert"),
	_("the desert"),
	_("a divide"),
	_("a dune"),
	_("a crescent dune"),
	_("a sand dune"),
	_("a geyser"),
	_("the geysers"),
	_("a glacier"),
	_("a gorge"),
	_("the gorge"),
	_("the grasslands"),
	_("the gulf"),
	_("a gully"),
	_("a dry gully"),
	_("a hill"),
	_("the hills"),
	_("an iceberg"),
	_("an ice sheet"),
	_("an inselberg"),
	_("an island"),
	_("the islands"),
	_("an isthmus"),
	_("a jungle"),
	_("the jungle"),
	_("a lagoon"),
	_("a moraine"),
	_("a mountain"),
	_("the mountains"),
	_("the base of a mountain"),
	_("the foot of a mountain"),
	_("a mountain peak"),
	_("a mountain range"),
	_("the mountain range"),
	_("the top of a mountain"),
	_("a fjord"),
	_("a forest"),
	_("the forest"),
	_("a deciduous forest"),
	_("a temperate forest"),
	_("a lake"),
	_("the lake"),
	_("the edge of a lake"),
	_("a salt lake"),
	_("the salt lakes"),
	_("a marsh"),
	_("the marshes"),
	_("a mesa"),
	_("the mouth of the river"),
	_("an oasis"),
	_("the ocean"),
	_("a salt pan"),
	_("a peninsula"),
	_("the peninsula"),
	_("a plain"),
	_("the plains"),
	_("a flood plain"),
	_("the flood plains"),
	_("a pediment"),
	_("the plateau"),
	_("a pond"),
	_("a prairie"),
	_("the quays"),
	_("a rainforest"),
	_("a subtropical rainforest"),
	_("a tropical rainforest"),
	_("a ravine"),
	_("the ravine"),
	_("a reef"),
	_("a coral reef"),
	_("the coral reef"),
	_("a river"),
	_("the river"),
	_("a river basin"),
	_("the river basin"),
	_("a river delta"),
	_("the river delta"),
	_("the source of a river"),
	_("a savanna"),
	_("the sea"),
	_("the seaside"),
	_("the shrublands"),
	_("the sound"),
	_("a coastal sound"),
	_("a steppe"),
	_("the steppes"),
	_("a strait"),
	_("a stream"),
	_("a swamp"),
	_("the swamp"),
	_("a tributary"),
	_("a tundra"),
	_("the tundra"),
	_("a valley"),
	_("a river valley"),
	_("a volcano"),
	_("an active volcano"),
	_("a dormant volcano"),
	_("an extinct volcano"),
	_("a wadi"),
	_("some wadis"),
	_("a waterfall"),
	_("the waterfalls"),
	_("a wetland"),
	_("the wetlands"),
	_("some yardangs"),
	_("some zeugens"),
]

# List of Environmental locations. E.g. 'You practiced writing a story, you chose comic sans and began with "It was {a dark and stormy night}', or "You {beat the meat} while thinking of {margaret thatcher} on {a hot sunny day}"

ENVIRONMENTAL_LOCATION = [
    _(""),
]

# Body parts for squabbles, fights etc.
# E.g. 'you squabbled with your {sibling} for not sharing {his_her} candy.' -> 'your {sibling} stormed you! {he_she} ripped your nipple.' 

BODYPART = [
    _("arm"),
    _("head"),
    _("leg"),
    _("foot"),
    _("knee"),
]

# Fighting words
# Same gist as above, e.g. for when you get attacked in a park and someone gouges your belly button or bites your pinky toe

ATTACK_WORD = [
	_("punched"),
	_("hit"),
	_("kicked"),
	_("attacked"),
	_("bit"),
]

# Insults: does what it says on the box. opposite list of compliments. (can be premised with 'called you {insults}')
INSULTS = [
    _("a dimwit"),
    _("a dork"),
    _("a douchebag"),
    _("a dummy"),
    _("a dunce"),
    _("a fatty"),
    _("a freak"),
    _("a goblin"),
    _("a jerk"),
    _("a jumpoff"),
    _("a lamebrain"),
    _("a loser"),
    _("a maniac"),
    _("a mouth-breather"),
    _("a pig"),
    _("a pumpkinhead"),
    _("a punk"),
    _("a scallywag"),
    _("a simpleton"),
    _("a snake"),
    _("a tool"),
    _("a tramp"),
    _("a triple-chin"),
    _("a twat"),
    _("a twit"),
    _("a villain"),
    _("a vulture"),
    _("a weasel"),
    _("an abomination to mankind"),
    _("an airhead"),
    _("an idiot"),
    _("an imbecile"),
    _("awful"),
    _("brainless"),
    _("careless"),
    _("dumb"),
    _("evil"),
    _("foolhardy"),
    _("mediocre at best"),
    _("mentally defective"),
    _("nasty"),
    _("obtuse"),
    _("psycho"),
    _("putrid"),
    _("skeezy"),
    _("stupid"),
    _("trashy"),
    _("weak"),
    _("weaksauce"),
]
