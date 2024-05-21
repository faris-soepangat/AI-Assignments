import sys

# Creates a file called result.txt
f = open("result.txt", "w")             

# This function writes the probabilities (same output as print statements) to results.txt file
def write_results(hValues, cherryNext, limeNext):
    f.write(f"P(h1 | Q) = {hValues[0]:0.5f}\n")
    f.write(f"P(h2 | Q) = {hValues[1]:0.5f}\n")
    f.write(f"P(h3 | Q) = {hValues[2]:0.5f}\n")
    f.write(f"P(h4 | Q) = {hValues[3]:0.5f}\n")
    f.write(f"P(h5 | Q) = {hValues[4]:0.5f}\n")
    f.write(f"Probability that the next candy we pick will be C, given Q: {cherryNext:0.5f}\n")
    f.write(f"Probability that the next candy we pick will be L, given Q: {limeNext:0.5f}\n")

# number of arguments passed in
n = len(sys.argv)                       

observation_count = 0                   # Observation count is initilized to 0  
h = [0.1, 0.2, 0.4, 0.2, 0.1]           # 5 types of bags of candy - 10% are h1, 20% are h2, 40% are h3, 20% are h4, 10% are h5
lime = [0, 0.25, 0.5, 0.75, 1]          # Percentage of lime candies in the bag
cherry = [1, 0.75, 0.5, 0.25, 0]        # Percentage of cherry candies in the bag

current_prob = h          # probability values are same as hypothesis
prev_prob = h             # the probabilities are the same as the hypothesis
limeProb = lime           # lime probability is equal to lime
cherryProb = cherry       # cherry probability is equal to cherry
cherryNext = 0.5          # cherryNext is equal to 0.5
limeNext = 0.5            # limeNext is equal to 0.5

# If no commands are entered
if(n == 1):
    f.write("No Observations Made\n") # Write no obersations made in text file
    write_results(current_prob, cherryNext, limeNext) # Writes the results
    quit()    # Ends the program

# Q                          # Take in command line argument
Q = sys.argv[1]              # Q is a string representing a series of observations ex. CLLCCCLLL                               
length = len(Q)              # Length of Q

# Arguments passed
f.write(f"\nObservation sequence Q: {Q}\n")

f.write(f"Length of Q: {length}\n") # Writes the length of Q

while(observation_count < length):
    Qj = Q[observation_count]                         # Current letter being observed
    observation_count = observation_count + 1         # Increment observation count (starts at 1)

    f.write(f"\nAfter observation {observation_count}\n")

    # Check whether observation is a lime or cherry
    if (Qj == 'C'):

        # Calculate Pt(hi)
        for i in range (5):
            current_prob[i] = cherry[i] * current_prob[i] / cherryNext

        # Resetting probability of cherry next to calculate new value, based on updated probability
        cherryNext = 0                                          
        for i in range (5):
            cherryNext = cherryNext + cherry[i] * current_prob[i]

        # Compute the probability of lime next
        limeNext = 1 - cherryNext 

        write_results(current_prob, cherryNext, limeNext)

    elif(Qj == 'L'):

        # Calculate Pt(hi)
        for i in range (5):
            current_prob[i] = lime[i] * current_prob[i] / limeNext

        # Resetting probability of cherry next to calculate new value
        limeNext = 0                                          
        for i in range (5):
            limeNext = limeNext + lime[i] * current_prob[i]

        # Compute the probability of lime next
        cherryNext = 1 - limeNext 

        write_results(current_prob, cherryNext, limeNext)   