(function () {

	var wrapper = $('.wrapper'),
	front = $('#front'),
	designandbuild = $('#designandbuild'),
	roboficial = $('#roboficial'),
	initiatives = $('#initiatives'),
	programmersinc = $('#programmersinc'),
	electrify = $('#electrify'),
	elixir = $('#elixir'),
	matka = $('#matka'),
	cubing = $('#cubing'),
	bitsmun = $('#bitsmun'),
	specials = $('#specials'),
	corporate = $('#corporate')
	event1 = $('.event1'),
	event2 = $('.event2'),
	event3 = $('.event3'),
	event4 = $('.event4'),
	event5 = $('.event5'),
	event6 = $('.event6'),
	event7 = $('.event7'),
	event8 = $('.event8'),
	event9 = $('.event9'),
	event10 = $('.event10'),
	event11 = $('.event11'),
	subevent_wrapper = $('ul.sub-events'),
	subevent = $('ul.sub-events li');

	var contentObject = {
		designandbuild: {
			burnout: "BURNOUT is an RC car-racing event. The teams are required to fabricate a remote controlled vehicle that is powered by an Internal Combustion(IC) Engine for propulsion capable of racing on an off-road dirt track paved by a varied range of obstacles. Here, both speed and control are important as the track has biting turns, cross bumps and rough covers.",
			trailblazers: "Trailblazers is an RC plane flying competition open for all aerodynamics lovers which will test their designing and flying skills. Participants have to design and make a fast, light, wireless remote controlled aircraft (using electric motors only), which can complete the mentioned task while having a maximum payload fraction in the least possible time before landing in the specified zone.",
			mortarkombat: "Design and build a spud gun to compete in different challenges, adhering to the rules and regulations of the game.",
			contraption: "You are required to create an imaginative and innovative sequence of energy conversions, such that once you provide an initial energy to the setup, the contraption continues to fulfill the final compulsory task, followed by an infinite assortment of steps.",
			cration: "Participants will be required to design a dam, on a half-completed terrain. A 3D model file of the riverbank at the site of the dam will be given, and the participant will have to construct the dam on it without making much changes to the given river bank model."
		},
		roboficial: {
			robokombat: "Design a wired/wireless, manually controlled robot, which is capable of fighting one-on-one in a battle with other bots.",
			robokick: "The main focus of the RoboKick competitions is the game of soccer, where the research goals concern cooperative multi-robot and multi-agent systems in dynamic adversarial environments. Design a manually controlled robot wired or wireless that can push the ball in the opposite team’s goal post and prevent opposite team from pushing the ball in their goal post.",
			robosumo: "A manually controlled robot wired or wireless has to either push other robot out of arena or make it immobile. Robots can have pushing, toppling and braking mechanisms.",
			roborace: "Construct a robot which out runs all other robots to win the race. Manually controlled robot capable to sustaining over different terrain & unseen hurdles robot win most cumulative points wins.",
			linefollowingbot: "Make wireless robot that will follow black line on a white background as quickly as possible. There can be unexpected obstacles on the arena but only the fastest robots will proceed to the next round."
		},

		initiatives: {
			principleventure: "Principle Venture during Quark 2017 provides you a platform to attempt and come up with a technological resolution for the impediments that society faces. Your aim is to employ technology to provide economically feasible solutions to create a platform for entrepreneurship for rural women. ",
			mygreenidea: "Ideas are abound when you have the conviction to bring about a change around you. Want to reduce your carbon footprint? Concerned about the quality of water you drink? Wish to know how things can be recycled often counterintuitively? My Green Idea provides you a platform to challenge your intellect. Research, build and come up with ideas that can potentially save the world and become a superhero!",
			smartcitiessmartsolutions: "\"If we had recognized urbanization as an opportunity 25 years ago, we could have been at par with the developed world today. But better late than never,\" This event requires one to come up with such solutions that make Indian cities smarter and provide a sustainable and decent quality of life to its citizens. Idea can be any that incorporate aids like governance, technology, energy, healthcare infrastructure etc. for fuss free smarter way of living.",
			designfordisaster: "The aim of the competition is to provide preventive measures to mitigate the effects of the disaster by reducing the impact of it or coming up with techniques to ensure maximum safety when it actually strikes.",
			injustice: "This event consists of a debate round (Team Event) and a group discussion round to come up with solutions on the major social problems faced by our nation based on certain cases of the Indian Judiciary."
		},

		programmersinc: {
			reversecoding:"This event will push your logical, deductive and mathematical skills to the limits. Be the Bond of programming and figure out what is the hidden source code for a given application by testing different inputs and analyzing the output.",
			crypticenigma: "Do you like breaking codes and solving ciphers? Would you like the chance to use your mathematical and programming skills to win some great prizes? Then the Cryptic Enigma Challenge is for you! This is an interesting contest in the area of Cryptography. The participants shall use their deducing skills, cryptography and programming skills to decrypt a set of messages provided.",
			bitsctf: "The game consists of a series of challenges where participants must reverse engineer, break, hack, decrypt, or do whatever it takes to solve them. The challenges are all set up with the intent of being hacked; making it a great way to get some hands-on experience. The objective of the game is for to gain as many points as possible by solving these challenges.",
			codejam: "Do you believe not just in writing code but making it more efficient? If yes, this event is for you. Quark present to you a competitive programming event. Rack your brains to solve puzzles and real world problems. Compete with people all across the nation and show off your programming skills.",
			hackathon:"Hackathon is a one of it’s kind event in Quark 2017, It involves the particpants spending extensive time over a problem statement, with the quest of bring out the most innovative ideas of an app or web development. The theme would be provided on spot and the contestants would be given the freedom to choose whatever they wish to build, as long as it is related to the main theme.",
			codeoshuffle: "This is a competitive programming contest with a twist. The team will be allotted 4 different questions on 4 different terminals initially, the terminals will be rotated periodically. The teams would be given a bug solving type common question , i.e. the code will have syntax errors, runtime errors and logical errors and the team will to change the code accordingly and another competitive coding question to solve."
		},

		electrify: {
			digilogica: "Do you think that Digital Design is just a boring course just about gates and logic? Well you’re in for a huge surprise! Welcome to the vast world of digital logic! Get ready to go beyond with counters, multiplexers, flip flops, encoders, decoders and much more and be prepared to be challenged at a whole new level! This event will have questions on topics ranging from digital logic circuits and minimization.",
			arduinoopen: "This event is a battle of skill and technicality between teams who are expected to solve simple to complex problem statements based on their pre-existing knowledge of Arduino and its interfacing.",
			analogtussle: "Enough of being Digitized, Think you know all about Analog?  Well then, take this test and find out. The event will test a broad base of techniques used in designing analog circuits.",
			matmania: "The 4th generation Programming language and Interactive environment ‘MATLAB’ hackathon in QUARK 2017! This event will test the general knowledge of MATLAB, covering syntax, features and data types. The event will have rounds based on a simulation of a system in SIMULINK based on basic Signal Processing and Image Segmentation. ",
			embition: "Embition will put to test your creativity and technical skills. It includes solving complex problems using Arduino and other electronic components, creating and implementing algorithms and integrating it with electronics."
		},

		elixir: {
			quarknationalquiz: "A quiz based on Science, Technology and Business.",
			carpedictum: "Consist of number of literary events.",
			ganimatoonics: "This quiz will be based on Ganimatoonics i.e. Games (not limited to just video games), Anime, Cartoons and Comics over the years. Anything related to these domains can be asked in the quiz.",
			themaydaymystery: "Behind every air crash, there lies a sequence of critical events that decide the fate of the aircraft. Come try your luck in air crash investigation! This event will be a test of your analytical and deductive skills more than knowledge of aircraft and its systems.",
			edorado: "The event is online and will consist of a series of pictorial questions, with the first person to correctly answer all questions declared as the winner.",
			numb3rs: "A competition where the participants will be able to test their aptitude and logical reasoning skills. We guarantee you a few puzzling, numbing and frustrating hours of fun and mind-gasmic problem solving.",
			celesticon: "The quiz will be based on astronomy and astrophysics. We help you explore the dormant side of your curiosity, invoking which, will help you ponder over ultimate questions of universe."
		},

		specials: {
			openshowcase: "Open Showcase during Quark is a platform where you get to promulgate your projects and models, and make your amazing skills of design and innovation known to the world.",
			paperpresentation: "Participants are invited to present papers spanning various research topics pertaining to the different branches of engineering and science.",
			industrialprocessdesign: "Industrial Design Problem is an event created to test and enhance innovation, technical knowledge and creativity of future engineers. The participants have to come up with the most economical and feasible solution to practical Industrial problems faced by Engineers.",
			schoolbag: "School Bag is a mixed bag of events, interactive sessions and workshops/talks, designed for the participation of students of Secondary and Higher Secondary Schools. It has events ranging from education, to arts and fun. The aim of this event is to promote education and learning of our young minds and nurture the potential within them by providing an opportunities to explore innovative technical projects and exhibits, and to participate in exciting events. ",
			shutterup: "Photographs are works of art- stories you can't put into words. Come, be the artist, paint magnificent works and showcase them in the Quark 2017 Photography Contest \"Shutter Up\". Prep your lenses, filters, flashes, tripods, and put your skills to the test. With cash prizes upto 15k this isn't an opportunity you'd want to miss. As they say, Shutter Up!"
		},

		corporate: {
			quest: "Quest is a National B-Plan competition designed for young entrepreneurs, which forms an excellent platform to pitch in their ideas before the corporate world and get an opportunity to win an incubation or the starting push to their innovation. It is an opportunity for potential ideas and early stage start-ups to evaluate their business idea in the risk-free environment of a competition, bridging the gap between ideas and the realization of an enterprise.",
			opstrat: "Opstrat is a growth hackathon. It requires participants to study the working and supply chain of the business and identify the problems of the existing supply chain and come up with new ideas to eradicate the inefficiencies in the system.",
			bluechipbeatdown: "An event focusing on convincing and persuasive skills of participants. It tests their marketing skills and selling tactics by giving them hands-on experience of the market as a seller.",
			wolfofwallstreet: "A real stock market game played with virtual money. Apply any knowledge on stock markets and their working to trade in a simulated environment and gain maximum profits.  The players face real time share price fluctuations and trade accordingly.",
			wallstreetrevolution: "WallstreetRevolution is the game to test your marketing skills, you don’t just offer, you calculate your profit and your loss, and keep a track of your remaining goods. You are given gold, you are given money, buy and sell in the right way and make maximum profit in the end to mark your victory.",
			bitcoinideationchallenge: "Interested in Bitcoin, Ethereum and Blockchain technology? Quark in association with Unocoin present to you the first ever Bitcoin event. The aim is to encourage innovation using Blockchain and Digital Currency technology. The participants have to present a model/solution to replace the current currency model with that of Bitcoins and how can it be promoted amongst people keeping in mind various factors that limits their plan of execution."
		},



	}



	// WHEN ANYTHING ON BOTTOM NAVBAR IS CLICKED ---------------------------------------------

	// WHEN EVENTS IS CLICKED
	$('#events-heading').click(function () {
		wrapper.animate({'opacity' : '0'},{duration: 300, queue: false});
		front.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});
		
	});

	// WHEN DESIGN AND BUILD IS CLICKED
	event1.click(function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		designandbuild.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});
		
	});

	// WHEN ROBOFICIAL IS CLICKED
	event2.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		roboficial.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});

	});

	// WHEN INITIATIVES IS CLICKED
	event3.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		initiatives.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});

	});

	// WHEN PROGRAMMER'S INC. IS CLICKED
	event4.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		programmersinc.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});

	});

	// WHEN ELECTRIFY IS CLICKED
	event5.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		electrify.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});
		
	});

	// WHEN ELIXIR IS CLICKED
	event6.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		elixir.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});
		
	});

	// WHEN MATKA IS CLICKED
	event7.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		matka.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});

	});

	// WHEN CUBING IS CLICKED
	event8.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		cubing.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});
		
	});

	// WHEN BITSMUN IS CLICKED
	event9.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		bitsmun.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});
		
	});

	// WHEN SPECIALS IS CLICKED
	event10.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		specials.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});
		
	});

	// WHEN CORPORATE IS CLICKED
	event11.on('click', function () {
		wrapper.animate({'opacity': '0', 'z-index' : '0'},{duration: 300, queue: false});
		corporate.animate({'opacity': '1', 'z-index' : '1'},{duration: 300, queue: false});

	});

	// BY DEFAULT, FIRST ITEM ON SUBEVENT MENU IS ALREADY SELECTED
	subevent_wrapper.children('li:nth-child(1)').addClass('active');



	// WHEN ANYTHING ON SUBEVENTS MENU IS CLICKED ---------------------------------------------

	subevent.on('click', function () {

		// Get all siblings of this subevent and if something has class active, remove it and add it to the one that's clicked
		$(this).parent().children('li').removeClass('active');
		$(this).addClass('active');

		// GETTING THE ID OF THE EVENT THAT CONTAINS THE SUBEVENT THAT IS BEING CLICKED
		var superset_event_name = $(this).parent().parent().parent().parent().attr('id');
		console.log(superset_event_name);

		// Get the text on the subevent that's clicked, remove all non alphanumeric characters, make it lowercase and store the text in a variable.
		var subevent_name = $(this).text();
		var subevent_name_lowercase = subevent_name.toLowerCase().replace(/\W/g, '');
		
		// Text of corresponding middle subwrapper
		var text_of_corresponding_middle_subwrapper_paragraph = $(this).parent().parent().next().find('p').text();
		var text_of_corresponding_middle_subwrapper_heading4 = $(this).parent().parent().next().find('h4').text();

		text_of_corresponding_middle_subwrapper_paragraph = contentObject[superset_event_name][subevent_name_lowercase];
		text_of_corresponding_middle_subwrapper_heading4 = subevent_name;

		$(this).parent().parent().next().find('p').text(text_of_corresponding_middle_subwrapper_paragraph);
		$(this).parent().parent().next().find('h4').text(text_of_corresponding_middle_subwrapper_heading4);
		// Rulebook of subevent

	});

})(); 


