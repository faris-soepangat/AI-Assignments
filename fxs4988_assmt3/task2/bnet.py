import sys

def calculate_probability(input_tokens):
    # Total probability calculated
    total_probability = 1 
    # Checks if the keyword 'Given' is present in the code 
    given_is_present = False  

    # Use dictionary to store alarm,johnCalls and maryCalls values
    alarm_dictionary = {"B_value": None, "E_value": None}
    johnCalls_dictionary = {"A_value": None}
    maryCalls_dictionary = {"A_value": None}

    # Store the Bayesian Network - # P(Burglary) and P(Earthquake) 
    probability_burglary_t = 0.001  
    probability_earthquake_t = 0.002   

    # Probability of Alarm, given Burglary and Earthquake
    probability_alarm = [[True, True, 0.95], [True, False, 0.94], [False, True, 0.29], [False, False, 0.001]]
    
    # Probability of JohnCalls, given Alarm
    probability_johnCalls = [[True, 0.9], [False, 0.05]]

    # Probability of MaryCalls, given Alarm
    probability_maryCalls = [[True, 0.7], [False, 0.01]]

    for token in input_tokens:
        if token == "given":
            given_is_present = True
        elif token in ["Bt", "Bf", "Et", "Ef"]:
            if token[0] == "B":
                alarm_dictionary["B_value"] = token[1] == "t"
            else:
                alarm_dictionary["E_value"] = token[1] == "t"
        elif token in ["At", "Af"]:
            johnCalls_dictionary["A_value"] = token[1] == "t"
            maryCalls_dictionary["A_value"] = token[1] == "t"

    for token in input_tokens:
        if token in ["Bt", "Bf", "Et", "Ef"]:
            if token[0] == "B":
                probability = probability_burglary_t if token[1] == "t" else (1 - probability_burglary_t)
            else:
                probability = probability_earthquake_t if token[1] == "t" else (1 - probability_earthquake_t)
            total_probability *= probability
        elif token in ["At", "Af"]:
            index = 0 if johnCalls_dictionary["A_value"] else 1
            for prob in probability_alarm:
                if prob[0] == alarm_dictionary["B_value"] and prob[1] == alarm_dictionary["E_value"]:
                    total_probability *= prob[2] if token[1] == "t" else (1 - prob[2])
                    break
        elif token in ["Jt", "Jf"]:
            index = 0 if token[1] == "t" else 1
            total_probability *= probability_johnCalls[index][1] if johnCalls_dictionary["A_value"] else (1 - probability_johnCalls[index][1])
        elif token in ["Mt", "Mf"]:
            index = 0 if token[1] == "t" else 1
            total_probability *= probability_maryCalls[index][1] if maryCalls_dictionary["A_value"] else (1 - probability_maryCalls[index][1])

    # returns total probability
    return total_probability

# number of arguments passed in
n = len(sys.argv)

# if there arent enough arguments
if n < 2:
    print("Insufficient arguments.")
elif n == 2:
    if sys.argv[1] in ["Bt", "Bf", "Et", "Ef"]:
        total_probability = calculate_probability(sys.argv[1:])
        print(f"Probability = {total_probability}")
    else:
        print("Invalid argument.")

if n > 2 and n <= 6:
    total_probability = calculate_probability(sys.argv[1:])
    print(f"Probability = {total_probability:0.10f}")