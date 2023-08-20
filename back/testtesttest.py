"""""

/onResponseReceivedActions/1/reloadContinuationItemsCommand/continuationItems/0/richItemRenderer/content/videoRenderer/navigationEndpoint/commandMetadata/webCommandMetadata/url
/onResponseReceivedActions/1/reloadContinuationItemsCommand/continuationItems/0/richItemRenderer/content/videoRenderer/thumbnail/thumbnails


/contents/twoColumnBrowseResultsRenderer/tabs/1/tabRenderer/content/richGridRenderer/contents/0/richItemRenderer/content/videoRenderer/navigationEndpoint/commandMetadata/webCommandMetadata/url
/contents/twoColumnBrowseResultsRenderer/tabs/1/tabRenderer/content/richGridRenderer/contents/0/richItemRenderer/content/videoRenderer/thumbnail/thumbnails/0/url




async def find_popular_video_titles(channel_name, token):
    # ... [остальной код не меняется]

    videos = []

    for _ in range(MAX_RETRIES):
        try:
            # ... [остальной код не меняется]

            items = data['onResponseReceivedActions'][1]['reloadContinuationItemsCommand']['continuationItems']
            for item in items:
                if 'richItemRenderer' in item:  # Проверка на наличие ключа 'richItemRenderer'
                    title = item['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
                    url_path = ["richItemRenderer", "content", "videoRenderer", "navigationEndpoint", "commandMetadata", "webCommandMetadata", "url"]
                    thumbnail_path = ["richItemRenderer", "content", "videoRenderer", "thumbnail", "thumbnails", 0, "url"]

                    url = get_value_by_path(item, url_path)
                    thumbnail = get_value_by_path(item, thumbnail_path)

                    video_info = {
                        "title": title,
                        "url": url,
                        "thumbnail": thumbnail
                    }
                    videos.append(video_info)

            return videos  # Возвращаем список словарей с информацией о видео

        # ... [остальной код не меняется]








в общем.... теперь я сделал получается пару функций. Что бы показать на основе чего мы генерируем идеи.... Они возращают на фронт список словарей.
Я так же беру ссылки на канылы конкуретов.
Как парсить конкуретов. Я могу как то адаптировать свои старые функции для этого?
"""


test = [
    {
        "ForbesBreakingNews": [
            "\u2018Convince The American People That You're Fighting The Cartels\u2019: Jackson Lee Pushes DEA For Action",
            "'It's Not Constitutional': Massie Grills FBI Director Wray About Access To Gun Purchase Records",
            "Debbie Wasserman Schultz Accuses GOP Of 'Generating A Controversy Where There Is None'",
            "Matt Gaetz Proposes Amendment To Defund 'A Ministry Of Truth In DOD'",
            "\u2018Protestors Came To My House!\u2019: Lindsey Graham Recounts Backlash From Kavanaugh Nomination Hearings",
            "JUST IN: Eric Adams Confronted By Constituent Who Says His First Amendment Rights Have Been Violated",
            "State Department: U.S. Seeks To \u2018Maintain Niger\u2019s Hard-Earned Democracy\u2019 Amidst Coup",
            "'This Case Is Far From A Foregone Conclusion Of Conviction': Dershowitz Discusses Trump Georgia Case",
            "\u2018Do You Think Systemic Racism Exists In America?\u2019: Vivek Ramaswamy Asked At Iowa State Fair",
            "'They're Trying To Cut SNAP And WIC': AOC Derides GOP's Leadership In Farm Bill Reauthorization",
            "'What Percent Of CDC Employees Are Vaccinated?': Cassidy Grills Walensky At Senate Hearing",
            "'You Think The Entire State Of Texas Is Racist?': Ted Cruz Grills Dem Witnesses On Voter ID Laws",
            "Jim Jordan Leads Hearing Targeting Govt Suppression Of Free Speech On Twitter Feat. Matt Taibbi",
            "'Just Read It, Read It Yourself!': Ted Cruz Uses Nominee's Document To Discredit Her",
            "JUST IN: Jim Jordan Chairs First Weaponization Of The Federal Government Committee Hearing - Part 2",
            "'If We Don't Stop It, This Country Will Not Survive': Chip Roy Issues Dire Warning On House Floor",
            "'This Is The Most Extraordinary Thing I Have Ever Seen': Hawley, Biden Nom Have Unbelievable Clash",
            "JUST IN: Jim Jordan Leads Fiery Hearing In Which ATF Director Testifies Before Judiciary Committee",
            "'Do You Need An ID To Rent An Apartment?': Nancy Mace Asks Witness Rapid-Fire Questions About ID",
            "BREAKING NEWS: Trump Mercilessly Unleashes On Biden In Speech Following Arraignment In Federal Court",
            "'Are You Going To Answer The Questions?': Cruz's Best Witness Grillings Of Past Year | 2021 Rewind",
            "JUST IN: Sparks Fly When John Kennedy Mercilessly Grills DEA Administrator: 'Why Don't You Do That?'",
            "BREAKING NEWS: Robert F. Kennedy Jr. Fires Back At Stacey Plaskett, Accusations He Is Racist",
            "'Is There A Difference Between Women And Men?': Ted Cruz Grills Human Rights Campaign President",
            "SHOCKING MOMENT: Local Reporter Brutally Confronts Lori Lightfoot, Tells Her, 'You Are A Pandemic!'",
            "Chip Roy Warns Biden: 'At Some Point The State Of Texas Is Going To Force A Constitutional Showdown'",
            "'Which Uses More Electricity...A Refrigerator When It's Running Or Electric Car When It's Charging?'",
            "WATCH: Trump Takes Rally Audience Questions About Hunter Biden, Illegal Immigration, And More",
            "'In This Letter, I'll Read It': Lankford Points To Letter Signed By Harris Supporting Filibuster",
            "Former New York Post Editor Laughs When Detailing Censorship Of Bombshell Hunter Biden Laptop Story",
            "'Let Me Just Finish': John Kennedy's Most Viral Witness Grillings | 2021 Rewind",
            "'Who The Hell Do You Think You Are!': Boebert Explodes At Ex-Twitter Exec For Shadow-Banning Her",
            "SHOCK MOMENT: FBI Official Admits Doc Alleging Biden Took $5 Million In Bribes Exists To Hawley",
            "BREAKING NEWS: Ted Cruz Explodes On Top FBI Official Over Biden 'Bribery  Scheme' Allegations",
            "Trump\u2019s lawyer plays a video of Democrats and celebrities advocating violence at impeachment trial",
            "'How Many Genders Are There?': John Kennedy Questions Human Rights Campaign Chief About Gender",
            "WATCH: Andy Biggs Fires Back At Swalwell By Playing Video Of Top Dems Discussing 'Defund The Police'",
            "'One Of My Constituents Got This In The Mail': John Kennedy Presents Surprising Letter At Hearing",
            "'I'm Just Asking...': John Kennedy Doesn't Let Up On Inspector General Of Federal Reserve",
            "BREAKING: All Hell Breaks Loose In House After Lauren Boebert Refuses To Cede Floor"
        ]
    },
    {
        "CBSNews": [
            "Hawaii wildfire recovery complicated by state of remains",
            "Hawaii animal shelter working to reunite pets with owners after Maui fires",
            "President Biden to travel to wildfire-ravaged Maui on Monday",
            "Iowa voters react to GOP candidates at state fair",
            "Rescue that never came: Hawaii survivors describe lack of help during and after wildfire",
            "Russian drones hit Ukrainian port near Romania border, Ukraine says",
            "Trump, co-defendants expected to be processed at Fulton County Jail",
            "North Korea confirms American Travis King is there, says he's escaping racism in U.S. Army",
            "What Trump's Georgia surrender could look like, case timeline, more | America Decides",
            "Sacred Indigenous sites lost in Maui fires, Montana climate case, more | CBS News Prime Time",
            "Defendant collapses in court after guilty verdict",
            "Photo of police officer breastfeeding malnourished baby goes viral",
            "Police pull over Florida state attorney",
            "Watch: Starbucks customer confronts employee for stealing credit card info",
            "Passenger captures the moment flight was told to \"brace for impact\"",
            "Football players' kind gesture to cheerleader goes viral",
            "Toddler rushes to hug pizza man \u2013 without knowing how meaningful it was to him",
            "100-year-old and 102-year-old runners break world records",
            "Chinese executions exposed by rare photos",
            "Trump and Clinton are asked to say something nice about each other",
            "Brothers convince little sister of zombie apocalypse",
            "Hamilton cast performs \"Alexander Hamilton\" at White House",
            "9/11/01: The towers are hit",
            "Obama stops for ice cream in Cedar Rapids",
            "Thankful teenage boy gives sweet speech during adoption",
            "Father of victims lunges at Larry Nassar in court",
            "Fatal Chicago shooting captured on Facebook Live",
            "Missing Titanic sub occupants dead, pieces of vessel found, Coast Guard announces",
            "Cop-killing suspect has chilling courtroom outburst",
            "Video shows moments after parents disarm alleged school gunman",
            "Hamilton cast performs \"My Shot\" at White House",
            "Trump roasts Clinton at Al Smith charity dinner",
            "Good Samaritan thwarts robbery with kick to the face",
            "\"Breaking Bad\" stars team with Julia Louis-Dreyfus in Emmy parody",
            "Woman fired after blocking black man from entering his apartment building",
            "NYPD releases video from police shooting of Brooklyn man",
            "R. Kelly was \"unhinged\" in interview with Gayle King, columnist says",
            "Full video: Trump-Clinton first presidential debate",
            "Sea lion pup jumps on boat, cuddles with driver",
            "3-year-old boy's prayer for Pre-K class goes viral"
        ]
    },
    {
        "LawAndCrime": [
            "Austin Ford Avoids Third Murder Trial for His Best Friend\u2019s Killing",
            "Bodycam Shows Lindsay Shiver, Husband Fighting Over Private Jet Before Bahamas Murder Plot Arrest",
            "\u2018Unspeakable Crime\u2019: Two Florida Women Ambushed, Shot to Death While Stopped at Train Tracks",
            "Colorado Dentist Allegedly Poisoned Wife\u2019s Protein Shake to Leave Her for Orthodontist",
            "\u2018Crazy Plane Lady\u2019 Issues Apology as Bodycam Showing Her Irate Reaction is Released",
            "Crime Scene Photos: Thomas Randolph\u2019s Home Wasn\u2019t Burglarized Day of Wife\u2019s Murder, Expert Says",
            "\u2018He Tried to Kill Me!\u2019: NJ Cops Shoot Armed Man Accused of Threatening Woman with Large Knife",
            "Parolee Fleeing Police Caught Hiding in Woman's Backyard (COPS)",
            "Family of Slain 10-Year-Old Girl Testifies Against Iowa Sex Offender Accused of Murdering Her",
            "8 Unruly Inmates Who Created Chaos After Being Arrested (JAIL)",
            "Bodycam Shows Police Tasing Armed Woman in Florida Walmart",
            "\"I did not punch you, I was hitting you\" - Audio Recording Between Johnny Depp & Amber Heard",
            "Bodycam Shows San Diego Police Tasing Alleged Sex Assault Suspect",
            "Video Shows Amber Heard Leaving Court After Devastating Loss",
            "Jury Hands Down Verdict in Johnny Depp's Favor at End of Defamation Trial with Amber Heard",
            "'That's Not My Dad': Cop Rescues Two Kids From Alleged Kidnapper",
            "Caught On Bodycam: Police Dealing with 'Entitled' Citizens In Public",
            "Witness Vapes & Starts Driving During Testimony",
            "Johnny Depp's Lawyer Grills Amber Heard on Late-Night Visit from James Franco",
            "BODYCAM: High-Speed Police Chase Ends in Collision, Gunfire on Oklahoma Highway",
            "Camille Vasquez Makes Johnny Depp Laugh Hysterically in Court",
            "Amber Heard Cross-Examined by Johnny Depp's Lawyer | Part One - Day 17 (Depp v Heard)",
            "Bodycam Shows Police Rescuing Kidnapped Child in Atlanta",
            "Johnny Depp Struggles to Stop Laughing During Witness Testimony",
            "Johnny Depp Testifies On Why He's Suing Amber Heard For Defamation",
            "Bodycam Shows YouTuber \u2018IShowSpeed\u2019 Handcuffed by Ohio Cops After Swatting Call",
            "Top Johnny Depp Comebacks & Reactions to Questioning While Testifying",
            "Johnny Depp\u2019s Legal Team Takes Victory Lap, Makes Statement on Verdict",
            "Ring Doorbell Shows Ohio Dad Shooting Daughter\u2019s Ex-Boyfriend in Chaotic Scene",
            "Johnny Depp Tells Story of Meeting Amber Heard",
            "Johnny Depp Talks Finding Human Fecal Matter On His Bed",
            "\u2018Dude, I Blew Zero!\u2019: College Athlete Sues Iowa Cops for DUI Arrest",
            "Video Shows Johnny Depp Angrily Slamming Cabinets During Argument with Amber Heard",
            "Amber Heard's Attorney Objects To His Own Question",
            "Murder Suspect Calls Cops Over Cold McDonald's Fries, Gets Arrested",
            "Video Shows Father Punch Son's Killer During Court Hearing",
            "Bodycam Shows SWAT Team Taking Down Masked Suspects Who Pistol-Whipped Hostage",
            "\u2018I\u2019m from Chicago, Bro\u2019: Would-Be Armed Robbery Suspect Backs Off When Florida Clerk Shows Gun",
            "Johnny Depp's Bodyguard Starts Laughing Uncontrollably & Leaves the Courtroom",
            "Bodycam Shows Police Snipers Shooting Allegedly Armed Minnesota Man"
        ]
    }
]


def views_to_int(view_string):
    """
    Преобразует строку просмотров в число.

    :param view_string: Строка вида "4,599 views".
    :return: Целое число просмотров.
    """
    # Удаление всех нецифровых символов
    view_number = int(''.join(filter(str.isdigit, view_string)))
    return view_number



"""
/onResponseReceivedActions/1/reloadContinuationItemsCommand/continuationItems/0/richItemRenderer/content/videoRenderer/shortViewCountText/accessibility/accessibilityData/label
"""