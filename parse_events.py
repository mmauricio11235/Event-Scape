'''
The purpose of this project is to parse the large set of events
in a txt file and turn it into workable object
'''
__author__ = 'Mauricio'
import re


global numEvents
eventDict = {}
numEvents =0

class User:
    tags = []



class Event:
    date = ""
    location = ""
    startTime = ""
    endTime = ""
    description = ""
    link = ""
    title=""
    def __init__(self):
        global numEvents
        eventNumber = numEvents
        numEvents+=1
        print(numEvents)

    '''Getter and setters for elements of event'''
    def getDate(self):
        return self.date
    def getLocation(self):
        return self.location
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
    def getLink(self):
        return self.link
    def getTitle(self):
        return self.title
    def getDescription(self):
        return self.description
    def setDate(self, newDate):
        self.date = newDate
    def setLocation(self, newLocation):
        self.location = newLocation
    def setStartTime(self, newStartTime):
        self.startTime = newStartTime
    def setEndTime(self, newEndTime):
        self.endTime = newEndTime
    def setLink(self, newLink):
        self.link = newLink
    def setTitle(self, newTitle):
        self.title = newTitle
    def setDescription(self, newDescription):
        self.description = newDescription

    '''Return match score for this object'''



def getevents():
    currLine = "none"
    currEvent = Event()
    print ("hello world!")
    f = open("EventData", "r")
    lines = []
    eventList = []
    # This line removes all tabs from the document
    for line in f:
        cleanLine = line.replace('\n', ' ').replace('\t', ' ').split(' ')
        x = cleanLine[0]
        lines.append(cleanLine)

        if (currLine == "none" and "-----" == x[0:5]):
            print ("\n \nStart of a new object!")
            currLine = "Title"
            eventList.append(currEvent)
            currEvent = Event()

        elif(currLine == "Title"):
            newLine = cleanLine
            print("Title: " + newLine.__str__())
            currEvent.setTitle(cleanLine)
            currLine = "none"
        elif(x == "Start"):
            newLine = cleanLine[1:]
            print("Start: " + newLine.__str__())
            currEvent.setStartTime(cleanLine)
            currLine = "none"
        elif(x == "Description"):
            newLine = cleanLine[1:]
            print("Description: " + newLine.__str__())
            currEvent.setDescription(cleanLine)
            currLine = "none"
        elif(x == "Location"):
            newLine = cleanLine[1:]
            print("Location: " + newLine.__str__())
            currEvent.setLocation(cleanLine)
            currLine = "none"

    for event in eventList:
        print (event.getTitle())

    return eventList








