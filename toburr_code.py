from math import ceil

def TextboxCount(lines): #this function takes as input a list of lines, and returns the numbers of characters and lines of the textbox
    n = [] #character count for each line
    l = len(lines) #number of lines
    for x in lines:
        n.append(len(x)-1) #is off by 1 for every line due to counting the line break
    return n, l;

def TextboxLengthNonJP(lines): #function takes lines as input and times how long the textbox will last
    n, l = TextboxCount(lines)
    if l == 0:
        return 0
    elif l == 1: #the length is max between time it takes for the blue line to appear and time it takes for all the characters to appear
        chara_time = 1 + 2*4 + 3 + (n[0]-5)*2 #1 QF for 1st and 2nd, 4QFs for 3rd and 4th, 3 QFs for 5th, 2 for the remaining characters in the line
        band_time_togo = 28 #ceil(1.109/.04)
        time = max(chara_time, band_time_togo)
    elif l == 2:
        chara_time_body = 1 + 2*4 + 3 + (n[0]-5)*2 #time for charas on the 1st line
        chara_time_tail = 1 + (n[1]-2)*2 #time for the charas on the 2nd line to appear
        band_timer = 2-((chara_time_body-1) * 0.04) #band timer that does not account for the >= 1 requirement
        remaining_band_timer = max(1.0, band_timer) #what the band timer is at on the QF it is allowed to go below 1
        band_time_togo = ceil((remaining_band_timer+0.109)/0.04) #time for the blue band to finish appearing
        time = chara_time_body + max(chara_time_tail, band_time_togo)
    else:
        chara_time_body = 1 + 2*4 + 3 + 1 + (n[0]+n[1]-7)*2
        chara_time_tail = 1 + (n[2]-2)*2
        band_timer = 3-((chara_time_body-1) * 0.04)
        remaining_band_timer = max(1.0, band_timer)
        band_time_togo = ceil((remaining_band_timer+0.109)/0.04)
        time = chara_time_body + max(chara_time_tail, band_time_togo)
    #time += 1.5 #avg timeloss from potentially starting on any QF
    return time

def TextboxLengthJP(lines): #function takes lines as input and times how long the textbox will last
    n, l = TextboxCount(lines)
    if l == 0:
        return 0
    elif l == 1: #the length is max between time it takes for the blue line to appear and time it takes for all the characters to appear
        chara_time = 1 + 10 + 8 + 4 + (n[0]-4)*3 #1 QF for 1st, 10QFs for 2nd, 8QF for 3rd, 4 QFs for 4th, 3 for the remaining characters in the line
        band_time_togo = 28 #ceil(1.109/.04)
        time = max(chara_time, band_time_togo)
    elif l == 2:
        chara_time_body = 1 + 10 + 8 + 4 + (n[0]-4)*3 #time for charas on the 1st line
        chara_time_tail = 1 + (n[1]-2)*3 #time for the charas on the 2nd line to appear
        band_timer = 2-((chara_time_body-1) * 0.04) #band timer that does not account for the >= 1 requirement
        remaining_band_timer = max(1.0, band_timer) #what the band timer is at on the QF it is allowed to go below 1
        band_time_togo = ceil((remaining_band_timer+0.109)/0.04) #time for the blue band to finish appearing
        time = chara_time_body + max(chara_time_tail, band_time_togo)
    else:
        chara_time_body = 1 + 10 + 8 + 4 + 1 + (n[0]+n[1]-6)*3
        chara_time_tail = 1 + (n[2]-2)*3
        band_timer = 3-((chara_time_body-1) * 0.04)
        remaining_band_timer = max(1.0, band_timer)
        band_time_togo = ceil((remaining_band_timer+0.109)/0.04)
        time = chara_time_body + max(chara_time_tail, band_time_togo)
    #time += 1.5 #avg timeloss from potentially starting on any QF
    return time


def LanguageTime(contents, isJP):
    total_time = 0
    tag_times = {}
    box_times = {}
    curr_lines = [] #represents the textbox currently being read
    for line in contents: #iterate through all the lines
        if line.startswith("/"):    #test if we are in a textbox or at the end of one
            #we are on a / so at the end of 1 textbox and at the start of the next.
            #we add the time spent on the box and move empty the current working lines
            tag_end = line.find(":")
            if tag_end == -1:
                tag_end = len(line) # if line doesn't have a tag delimiter just assume the whole annotation is the tag
            tag = line[2:tag_end]

            # time the textbox using the appropriate language mechanics
            if isJP:
                box_time = TextboxLengthJP(curr_lines)
            else:
                box_time = TextboxLengthNonJP(curr_lines)

            # update our various timing data
            if tag in tag_times:
                tag_times[tag] += box_time
            else:
                tag_times[tag] = box_time
            box_times[line[2:]] = box_time
            total_time += box_time
            curr_lines = []
        else:
            curr_lines.append(line)  #we are in the middle of a textbox so we add the line to the working set of lines
    return total_time, tag_times, box_times



# f = open("FormattedJapanese.txt","r")
# contentsJ = f.readlines()
# totalJ, tagJ, boxJ = LanguageTime(contentsJ, True)
# print(totalJ)
# f = open("AnnotatedJapanese.txt","r")
# contentsJ = f.readlines()
# totalJ, tagJ, boxJ = LanguageTime(contentsJ, True)
# print(totalJ)
# f = open("AnnotatedEnglish.txt","r")
# contentsE = f.readlines()
# totalE, tagE, boxE = LanguageTime(contentsE, False)
# print(totalE)
# jsum = 0
# esum = 0
# for tag in boxJ:
#     if tag.startswith('noki3'):
#         print(tag, boxJ[tag])
#     pass
