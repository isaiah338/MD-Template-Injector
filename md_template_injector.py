# imports 
from genericpath import isfile
from os import listdir
import os

# index markdown template constants 
INDEX_MD_FILE_PATH = "./index/"
INDEX_MD_FILENAME = "index.md"
INDEX_MD_ABSOLUTE_PATH = INDEX_MD_FILE_PATH + INDEX_MD_FILENAME

logFile = open("./log/recent.txt", "w")
# directory & markdown extension constants 
CURRENT_DIRECTPRY = "./"
MD_FILE_EXTENSION = ".md"

# identify index heading text constants 
INDEX_HEADING = "# Index"
INDEX_WRAPPING_TEXT = "---"

logFile.write("index heading="+INDEX_HEADING+"\n")

print("index heading=")
print(INDEX_HEADING)
# open markdown index template and save contents
indexMd = open(INDEX_MD_ABSOLUTE_PATH)
indexContents = indexMd.read()

# constant boolean to run without writing to files
OVERWRITE_FILES=1

# get all files in directory running the script 
files = listdir(CURRENT_DIRECTPRY)

# loop through each file 
for file in files:
    logFile.write("\nfile="+file+"\n")
    # verify file exists, is not directory, and is a markdown file 
    if isfile(file) and os.path.splitext(file)[1]==MD_FILE_EXTENSION:
        # open file for reading and save text contents
        fileRead = open(file, "r")
        fileContents = fileRead.read()
        logFile.write("\nmarkdown file="+file+"\n")
        print("contents=")
        print(fileContents)

        # check if specified index heading exist in file contents
        if fileContents.find(INDEX_HEADING)>0:
            logFile.write("\tcontains index heading=1\n")
            logFile.write("\tcontents=\n"+fileContents+"\n=====")
            print(file+" contains index heading")
            splitFileContents = fileContents.split('\n')

            # boolean to check if index heading is found in contents
            indexFound  = 0

            # index counter to see which line index the heading ends
            spliceIndex = 0

            # loop through each line in file contents 
            for line in splitFileContents:
                # check for index heading and flip boolean if found 
                if(line==INDEX_HEADING):
                    indexFound = 1

                ####
                # if the index has been found and the current line is blank 
                ## * index markdown template needs to have no blank
                ### lines in-between text for index, as this checks for 
                ### a blank line to know what line to cut off at
                #
                ## * may change this in the future to another value
                ### to look for, this is for inital running of the
                ### script
                #
                ####
                if(indexFound == 1 and len(line.strip())<=0):
                    break

                # incriment splice index counter
                spliceIndex=spliceIndex+1

            # save new array from old file lines, splicing at given splice 
            ## index to the end of the array, cutting off old index heading
            newArr = splitFileContents[spliceIndex:len(splitFileContents)]

            # reset the file contents string and append each index
            ## of updated line array to file contents string
            fileContents = ""
            for line in newArr:
                fileContents = fileContents + line + "\n"
        else:
            logFile.write("\tcontains index heading=0\n")
        if OVERWRITE_FILES==1:
            # prepend text from markdown index template to file contents string
            ## and write to given file
            newFileContents = indexContents+fileContents
            open(file, "w").write(newFileContents)