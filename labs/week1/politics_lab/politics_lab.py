voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    senator_dict = {}
    for line in voting_data:
        elements = line.split()
        vote_list = []
        for vote in elements[3:]:
            vote_list.append(int(vote))
        senator_dict[elements[0]] = vote_list
    return senator_dict
 
#print(create_voting_dict())   
#print(len(create_voting_dict()))

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    voting_a = voting_dict[sen_a]
    voting_b = voting_dict[sen_b]
    result = 0
    for i in range(len(voting_a)):
        result += voting_a[i] * voting_b[i]
    return result


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    similarity = None
    person = ''
    for key in voting_dict:
        if key !=  sen:
            current_similarity = policy_compare(sen, key, voting_dict)
            if similarity == None or current_similarity > similarity:
                similarity = current_similarity
                person = key              
    return person
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    similarity = None
    person = ''
    for key in voting_dict:
        if key !=  sen:
            current_similarity = policy_compare(sen, key, voting_dict)
            if similarity == None or current_similarity < similarity:
                similarity = current_similarity
                person = key              
    return person
    
    

## Task 5
#voting_dict = create_voting_dict()
#print(most_similar("Chafee", voting_dict))
#print(least_similar("Santorum", voting_dict))

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    similarity = 0
    for person in sen_set:
        similarity += policy_compare(sen, person, voting_dict)           
    return similarity / len(sen_set)


# test 
#Democrats = set()
#for line in voting_data:
#    elements = line.split()
#    vote_list = []
#    if elements[1] == 'D':
#        Democrats.add(elements[0])
#print(Democrats)
#
#D_similarity = None       
#D_person = ''
#voting_dict = create_voting_dict()
#for key in voting_dict:
#    current_similarity = find_average_similarity(key, Democrats, voting_dict)
#    if D_similarity == None or current_similarity > D_similarity:
#        D_similarity = current_similarity
#        D_person = key                 
#print(D_person)

most_average_Democrat = "Biden" # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    length = 0
    for key in voting_dict:
        length =len(voting_dict[key])
        break
    result = [0 for x  in range(length)]
    for sen in sen_set:
        for i in range(length):
            result[i] += voting_dict[sen][i] 
    for i in range(length):
        result[i] /= len(sen_set)
    return result




average_Democrat_record = [-0.16279069767441862, -0.23255813953488372, 1.0, 0.8372093023255814, 0.9767441860465116, -0.13953488372093023, -0.9534883720930233, 0.813953488372093, 0.9767441860465116, 0.9767441860465116, 0.9069767441860465, 0.7674418604651163, 0.6744186046511628, 0.9767441860465116, -0.5116279069767442, 0.9302325581395349, 0.9534883720930233, 0.9767441860465116, -0.3953488372093023, 0.9767441860465116, 1.0, 1.0, 1.0, 0.9534883720930233, -0.4883720930232558, 1.0, -0.32558139534883723, -0.06976744186046512, 0.9767441860465116, 0.8604651162790697, 0.9767441860465116, 0.9767441860465116, 1.0, 1.0, 0.9767441860465116, -0.3488372093023256, 0.9767441860465116, -0.4883720930232558, 0.23255813953488372, 0.8837209302325582, 0.4418604651162791, 0.9069767441860465, -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488] # (give the vector)
#voting_dict["average"] = average_Democrat_record
#print(most_similar("average", voting_dict))

# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    similarity = None
    pair = (None,None)
    person = voting_dict.keys()
    for person1 in person:
        for person2 in person:
            if person1 !=  person2:
                current_similarity = policy_compare(person1, person2, voting_dict)
                if similarity == None or current_similarity < similarity:
                    similarity = current_similarity
                    pair = (person1,person2)              
    return pair