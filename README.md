# **Election Analysis**

##	Overview of Project
In this election analysis we will be working with Tom to perform an election audit for the Colorado Board of Elections. The audit will generate the total number of votes casted, the candidates that received votes, the total number of votes per candidate, the percentage of votes each candidate received and the winner of the election. Using the raw data found in the *election_results.csv*, we will be creating a Python script to determine the election results and writing data to a text file *election_results.txt* to facilitate reading the results. Through coding, our evaluation will help determine the winner and thus help deliver a comprehensive report of the election turnout. 

Creating an election audit, is a fundamental process to understand voters’ behavior. In our case, the turnout of a congressional election, will help the state of Colorado grasp the amount of their population who go out and vote in the county of Arapahoe, Denver and Jefferson. Given the total number of votes, we will be able to determine the amount and percentage of votes that came from each county and display the county with the largest voter turnout. In addition, we will determine the distribution of votes throughout the candidates. This information will not only show us the winner of the election, but the amount and percentage of overall votes that they received. Conducting an audit, gives an inside to voter response and provides an appreciation to the success of exercising the right to vote.
### Election-Audit Results
The outcome of the election-audit serves as a platform to understand the behavior of the population, when it comes to elections. In our case, we will be focused on one congressional election in the state of Colorado. For this we will turn our attention to the counties of Arapahoe, Denver and Jefferson. For which, the candidates on the ballot are Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. We will go through the following steps to evaluate our results: 
- How many votes were cast in this congressional election?
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
#### Congressional Election Votes
A congressional election is done by each state to determine the individual that will be representing them in Congress. It is a vital position in American politics and that is why we need to insure we understand who many American citizens went out and voted in the Colorado election. Tom has provided us with a raw data in the *election_results.csv*, however this is large dataset. Therefore, though VS code, we will be using the programing language Python to create a script and interpret our dataset. 
We will start by adding our dependencies and adding a variable load file and save file. This will allow for us to abstract the data from our dataset and create an area into which our findings will be saved as text form. 

Next, we will initialize a total vote count and set it to zero. Once this is done, we can go ahead and open the election results file with our dataset and ask it to read the total amount of rows that contain the number of votes. We need to specify it to skip the header row, as it’s a title “Ballot ID” and does not contain a vote. Lastly, we will print out the total votes and thus have the total number of votes for the election. The result is a total of 369,711 casted votes for the congressional election. Let’s not forget that we want our results to print out our text file, so above the command for printing the results, we must open and write a code to save our results to our text file. Once this is done, we will find the total vote count and print it to our text file. 

![Congressional_Election_Votes_Code](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Congressional_Election_Votes_Code.png)  
![Congressional_Election_Vote_text_file.](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Congressional_Election_Vote_text_file.png)

#### County Votes
The county votes determine the amount of the county population that went out and voted. The counties for our analysis are Arapahoe, Denver and Jefferson. We want to analyze what percentage of the population voted in each county and the total amount of votes that were casted in each county. We need to set county list, that contains the names of each county, and a county dictionary that sets the county as a key and holds the number of votes for each. In order to get an accurate list, we need to create an ‘If’ statement, the code goes as follow. 

![County_Vote_code1](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/County_Vote_code1.png)

Now that we have set up a way of isolating each county, we can go ahead and write a loop that will give us the number of votes each county received and the percentage of votes each county obtained in relation to the total votes. To do this, we will start by retrieving the county vote count and then, percentage by using the float function. Once this is done, we can go ahead and print our results. Our findings show that Jefferson obtained 10.5% and a total of 38,855 votes. Denver received 82.8% of the votes and a total of 306,055. Meanwhile Arapahoe obtained 6.7% of the votes and had a turnout of 24,801 voters. By glancing at our data, we can determine that Arapahoe has the smallest turnout of voters at 6.7%, then we see that Jefferson had a bigger turnout of 10.5% but it does not compare to the massive turnout from Denver at 82.8%. We will go ahead and save our findings to the text file, so that it’s displays it in our text file and makes it easier to read. 

![Couny_Vote_code2](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Couny_Vote_code2.png)

![County_Vote_text_file](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/County_Vote_text_file.png)

#### Largest County Turnout
The election commission has asked we provide the county with the largest turnout in our audit. In order to obtain this data, we want to set “largest_county_turnout” as a sting and set “largest_vote_turnout”and “winning_count_county” to zero. This will help us track the largest county and county voter turnout. Next, we want to create the following “If” statement and print our results. 

![Largest_County_Turout_code](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Largest_County_Turout_code.png)

The results of our analysis, show that Denver was the county with the largest turnout. We can make a few assumptions as to why, such as Denver may be the county with the largest population in Colorado, and therefore out of the three counties, had the biggest turnout. Given its high population, more people go out and vote. Knowing what the county with the largest population, can help the election commission predict that in the future they will continue to swing the elections. Therefore, the candidate that is the most popular in Denver will get a high percentage of the votes in a congressional and other elections.

![Largest_County_Turnout_text_file](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Largest_County_Turnout_text_file.png)

#### Candidate Votes
So far, we have gathered information that has helped us determine the total population that votes in the congressional election, the votes and percentages per county and which was the county with the largest voter turnout. Now, let’s find out how many votes each candidate received and the percentage of the votes in relation to the total votes casted. We will go ahead and determine the candidate in the ballot first. Next, we will count the number of votes they received, as we go through each row on the dataset, print the result and save them to our text file.

![Candidate_Vote_code](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Candidate_Vote_code.png)

Our results show that there were three candidates on the ballot for the congressional seat: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. The candidate with the least votes was Raymon Anthony Doane, with a total of 11,606 votes and 3.1% of total votes. Next, Charles Casper Stockham received 85,213 votes for a total of 23% of the votes. Finally, Diana DeGette was the candidate with the most votes at 272,892 and a total of 73.8% of the votes. The distribution of votes shows the favoritism of candidates and their popularity in the election.

![Candidate_Vote_text_file](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Candidate_Vote_text_file.png)

#### Winner of Election
In order to track the winner of the election we need set the “winner_candidate” as a string and set the “winning_count” and “winning_percentage” to zero. Next, we want to set an “If” statement to determine the winning candidate, the count of votes and percentage. Once this is done, we need to set an “F” sting to help us create a summary of the results. Then, print out our finding and save it to the text file. 

![Winner_of_Election_code](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Winner_of_Election_code.png)

The results show us that Diana DeGette was the winner of the congressional seat for Denver. The winning vote count was 272,892 and the winning percentage was 73.8% This was a land slide! The winning candidate received over three times the number of votes than the second runner up.   

![Winner_of_Election_text_file](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Winner_of_Election_text_file.png)

## Election-Audit Summary
The election audit has determined that the total votes of for the congressional election were 369,711. It has shown us that there were three counties in the election and given us their percentage of votes and the number count. Also, it helped us determine that Denver was the county with the largest voter turnout. Likewise, it provided the candidates, their voter count and percentage of votes in relation to the total votes in the election. Lastly, it showed that Diana DeGette was the winning candidate of the congressional election. Through coding we have been able to deliver a detailed summary of the election audit.

![Election_Results_text_file](https://github.com/cynmmarin/Election_Analysis/blob/ed1f834447b55f14bb3cdcb3995d1735bea90512/Images/Election_Results_text_file.png)

Given the details and data manipulation of our code, this framework can be used to audit future elections. For example, if the election commission wishes to determine the results of a county election, they can evaluate the towns turnout. They can make a list of the towns in the county, add it to the county dictionary and create a loop that goes through each row and given them the voter turnout of each town, the percentage of total vote that came from each town and the voter count. This can help determine the candidate that won the positions for County Executive, Freeholders and County Sheriff. 

However, if they do not wish to alter the code and would rather use the code as it stands. They can do the same method to analyze a state election. They can evaluate the turnout per county and determine senators. Also, they can use our code to determine the governor. All that would be needed is to obtain the data for the respected election and our code should be able to provide an election audit of the candidate position they want to analyze. Overall, our code can be modified to obtain a wide range of election data and it can be applied to other elections. 


