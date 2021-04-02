# Dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Start the total vote counter
total_votes = 0

# Declare new list for the name of the candidate from each row
candidate_options = []

# Declare empty dictionary for candidates votes.
candidate_votes = {}

# Declare a variable that holds an empty string value for the winning candidate.
winning_candidate = ""

# Declare a variable for the "winning count" equal to zero.
winning_count = 0

# Declare a variable for the "winning_percentage" equal to zero.
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row in the CSV file.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        
        # Increment the total_votes variable by 1
        total_votes += 1
        
        # Print the candidate name for each row
        candidate_name = row[2]
        
        # Get unique names in the candidate_options list
        if candidate_name not in candidate_options:
           
            # Add candidate_name to the candidate_options list using the append() method
            candidate_options.append(candidate_name)
           
           # Create each candidate a key
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1
    
# Save the results to our text file.
with open(file_to_save, "w") as text_file:
       
    # Print the final vote count.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
        
    # Save the final vote count to the text file.
    text_file.write(election_results)     

    # Print the candidate vote dictionary.
    #print(candidate_votes)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
                    
        # Retrieve vote count of a candidate
        votes = candidate_votes.get(candidate_name)
                    
        # Calculate the percentage of votes for each candidate.
        vote_percentage = (float(votes) / float(total_votes))* 100
                
        # Print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
        # Print out the candidate, percentage of votes and total votes.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")        
        print(candidate_results)

        # Save the final vote count to the text file.
        text_file.write(candidate_results)    
        
        # Determine the winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                    
            # If true, the set winning_count = votes, and winning_percentage = vote_percentage 
            winning_count = votes
            winning_percentage = vote_percentage
                    
            # Set the winning_count equal to the variable, candidate_name, in the for loop.
            winning_candidate = candidate_name

    #Print winning candidate summary
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")

    print(winning_candidate_summary)
    text_file.write(winning_candidate_summary)
        