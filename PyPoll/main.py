#dependencies
import os
import csv

#defining my file"s path
file=os.path.join("/Users/francoiseelismbazoaokala/Documents/python_challenge/PyPoll/Resources/election_data.csv")

#reading file using csv module
with open(file,"r") as csvfile:

         #specifying delimiter and variables to hold contents
        csv_reader = csv.reader(csvfile, delimiter=",")
        #print(csv_reader)

         #reading the header rows first
        csv_header = next(csv_reader)
        #print(f"csv header:{csv_header}")

        #defining variables to store  in values
        winner = ""
        votes_count = 0
        candidate_votes= 0
        winner_vote_count = 0

        #defining lists to store in entries
        count_list = []
        percentage_list = []
        candidate_list = []
        unique_candidate_list = []

        #reading the rest of the rows
        for row in csv_reader:

            #appending rows to their corresponding list
            candidate_list.append(row[2])

            #calculatting votes_count by incrementing each row by 1
            votes_count +=1
        
            #storing values into the unique candidate list
            candidate = row[2]
            if candidate not in unique_candidate_list:
                unique_candidate_list.append(candidate)

         #determining each candidate votes count and their corresponding percentages
        for candidate_name in unique_candidate_list:
                for value in candidate_list:    
                     if value==candidate_name:
                        candidate_votes +=1         
                candidate_vote_percentage=round(((candidate_votes/votes_count)*100),3)

                #storing values in count_list and percentage list 
                count_list.append(candidate_votes)      
                percentage_list.append(candidate_vote_percentage)

                #determining the winner of the election
                if candidate_votes > winner_vote_count:
                    winner_vote_count = candidate_votes
                    winner = candidate_name

                #looping through the next candidate by resetting candidate's votes 
                candidate_votes=0




print(f"Election Results")            
print("---------------------------------------------")
print(f"Total Votes : {votes_count}")
print(f"--------------------------------------------")

 #print statistics  for each  unique candidate by iterating through the 3 lists storing data
for (name,percentage,count) in zip(unique_candidate_list, percentage_list ,count_list):
  print(f"{name}: {percentage}%  ({count})")
print(f"--------------------------------------------")
print(f"Winner : {winner}")
print(f"----------------------------------------------")

with open("PyPoll/analysis/analysis.txt","w")  as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write("---------------------------------------------\n")
    txt_file.write(f"Total Votes : {votes_count}\n")
    txt_file.write(f"--------------------------------------------\n")

    #txt_file.write statistics  for each  unique candidate by iterating through the 3 lists storing data
    for (name,percentage,count) in zip(unique_candidate_list,percentage_list,count_list):
     txt_file.write(f"{name}:{percentage}% {count}\n")
    txt_file.write(f"--------------------------------------------\n")
    txt_file.write(f"Winner : {winner}\n")
    txt_file.write(f"----------------------------------------------\n")      
                            
                
                

