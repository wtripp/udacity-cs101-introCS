# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network [Option 1] #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <username> is connected to <name1>, <name2>,...,<nameN>. 
# <username> likes to play <game1>,...,<gameN>.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a gamer profile. For example:
# 
# John is connected to Bryant, Debra, Walter. 
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two - (e.g. lists of dictionaries). Pick one which
# will allow you to manage the data above and implement the procedures below. 
# 
# You can assume that <username> is a unique identifier for a user. In other
# words, there is only one John in the network. Furthermore, connections are not
# symmetric - if John is connected with Alice, it does not mean that Alice is
# connected with John. 
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
# Some details:  Each sentence will be separated from one another with only
# a period (there will not be whitespace or new lines between sentences)
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information. 
# 
# Arguments: 
#   string_input: block of text containing the network information
# 
# Return: 
#   The new network data structure

# verify_text(string_input,text,invalid_text):
#   Helper procedure. Verifies that the text of a given string input is valid.
# 
# Arguments: 
#   string_input: block of text containing the network information (string)
#   text: text of string input, such as 'is connected to' or 'likes to play' (string)
#   invalid_text: error message stating that text is invalid (string)
#
# Return:
#   If the string text is invalid, the invalid_text error message.

def verify_text(string_input,text,invalid_text):
    if string_input[0:len(text)] != text:
        return invalid_text

#   def add_network_data(string_input,text,network,user_data,user_data_list):
#   Helper procedure. Parses the text of a string and adds data from that string to the network as a list.
# 
# Arguments: 
#   string_input: block of text containing the network information (string)
#   text: text of string input, such as 'is connected to' or 'likes to play' (string)
#   network: The network data structure being created from the string input (dict)
#   user_data: Subset of the network data for a user, such as ['Connections'] or ['Games'] (dict)
#   user_data_list: List from the given network data for a user. (list)
#
# Return:
#   Nothing. Procedure adds the user data to the network and updates the user data list.
    
def add_network_data(string_input,text,network,user_data,user_data_list):
    text_list = string_input[0:string_input.find('.')].strip()
    text_list = text_list.split(',')
    for item in text_list:
        item = item.strip()
        network[user_data][user_data_list].append(item)
        if network[user_data][user_data_list] == ['']:
            network[user_data][user_data_list] = []
            
def create_data_structure(string_input):
    
    # Initialize network dictionary and define the global variables.
    network = {}
    connect_text = 'is connected to'
    connect_len = len(connect_text)
    game_text = 'likes to play'
    game_len = len(game_text)
    invalid_input = 'Invalid input string. Use this format: <username> is connected to <friend>, <friend>. <username> likes to play <game>, <game>.'
    
    # Go through users and add them to the network.
    while string_input:
        
        # Create a username variable and store the user in the network.
        username = string_input[0:string_input.find(connect_text)].strip()
        network[username] = {'Connections': [] , 'Games': []}

        # Verify that the connection text is correct.
        string_input = string_input[string_input.find(connect_text):]
        verify_text(string_input,connect_text,invalid_input)

        # Add user's connections to the network.
        string_input = string_input[connect_len:].strip()
        add_network_data(string_input,connect_text,network,username,'Connections')

        # Verify that the username in the first and second sentences match.
        string_input = string_input[string_input.find('.')+1:]
        if string_input[0:string_input.find(game_text)].strip() != username:
            return invalid_input
        
        # Verify that the game text is correct.
        string_input = string_input[string_input.find(game_text):]
        verify_text(string_input,game_text,invalid_input)

        # Add user's games to the network.
        string_input = string_input[game_len:].strip()
        add_network_data(string_input,game_text,network,username,'Games')

        # Start at the next user.            
        string_input = string_input[string_input.find('.')+1:]
        
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections a user has.
#
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of the user.
# 
# Return: 
#   A list of all connections the user has. If the user has no connections, 
#   return an empty list. If the user is not in network, return None.

def get_connections(network, user):
    if user in network:
        return network[user]['Connections']
    return None

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:  String with the name of the user ("Gary")
#   user_B:  String with the name of the user that will be the new connection.
#
# Return: 
#   The updated network with the new connection added (if necessary), or False 
#   if user_A or user_B do not exist in network.
    
def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network or user_A == user_B: # Users cannot add themselves as connections.
        return False
    if user_B not in newtork[user_A]['Connections']:
        network[user_A]['Connections'].append(user_B)
    return network


# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user:    String containing the users name to be added (e.g. "Dave")
#   games:   List containing the user's favorite games, e.g.:
#            ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. If the 
#   user is already in the network, update their game preferences as necessary.

def add_new_user(network, user, games):
    if user in network:
        for game in games:
            if game not in network[user]['Games']:
                network[user]['Games'].append(game)
    else:
        network[user] = {'Connections': [] , 'Games': games}
    return network

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections, i.e. connections of connections, of a 
#   given user.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of a user.
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   If the user is not in the network, return None. If a user has no primary 
#   connections to begin with, you should return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

def get_secondary_connections(network, user):
    if user not in network:
        return None
    secondary_connections = []
    for connection in network[user]['Connections']:                     # Loop through user's connections.
        for secondary_connection in network[connection]['Connections']: # Loop through the connections of connections
            if secondary_connection not in secondary_connections:       # Add the secondary connections to the list
                secondary_connections.append(secondary_connection)            
    return secondary_connections

# -----------------------------------------------------------------------------     
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:    String containing the name of user_A.
#   user_B:    String containing the name of user_B.
#
# Return: 
#   The number of connections in common (integer). Should return False if 
#   user_A or user_B are not in network.

def connections_in_common(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    common_connections = 0
    for connection in network[user_A]['Connections']:
        if connection in network[user_B]['Connections']:
            common_connections += 1
    return common_connections

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A List showing the path from user_A to user_B. If such a path does not 
#   exist, return None
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

def path_to_friend(network, user_A, user_B, path=None, checked=None):
    
    # Check that both users are in the network and that the users are different.
    if user_A not in network or user_B not in network:
        return None
    if user_A == user_B:
        return [user_A]
    
    # Initialize the default parameter to track the current path to user.
    if path == None:
        path = []

        # Initialize the default parameter to track the users that have been checked.
    if checked == None:
        checked = []

    # Track which users' lists have been checked and add current user to the path.
    checked.append(user_A)
    path.append(user_A)
    
    # Base case
    if user_B in network[user_A]['Connections']:
        path.append(user_B)
        return path
    
    # Loop through the users in the network, recursively adding them to the path.
    for connection in network[user_A]['Connections']:
        if connection not in checked:
            path_to_friend(network, connection, user_B, path, checked)
            
            # Once the user is found, return the path.
            if user_B in path:
                return path

    # If the user is not found, remove that user from the path and return to the previous connection depth.
    path.pop()
    return None

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun! 

# game_index(network,user):
#   Crawls the user's connections and creates a game index to track
#   how many people in the user's network like each game.

# Arguments:
#   network: The network created with create_data_structure. 
#   user:  String containing the name of a user.
# 
# Return:
#   An index of the games in the user's network and the number of likes for each game.
#
# Sample output:
#   >>> print game_index(net,'Debra')
#   >>> [('Call of Arms', 3), ('City Comptroller: The Fiscal Dilemma', 2),
#        ('Dinosaur Diner', 2), ('Dwarves and Swords', 2), ('Ninja Hamsters', 2),
#        ('Pirates in Java Island', 1), ('Seahorse Adventures', 3), ('Seven Schemers', 1),
#        ('Starfleet Commander', 2), ('Super Mushroom Man', 3), ('The Legend of Corgi', 4),
#        ('The Movie: The Game', 2)]

def game_index(network,user):
    if user not in network:
        return None
    tocrawl = network[user]['Connections'][:]  # List of user's connections to crawl.
    crawled = [user]                           # List of crawled users. User is not crawled.
    game_index = {}                            # Initialized game index.
    while tocrawl:                             # Crawls through the network and updates the game index.
        for connection in tocrawl:
            if connection not in crawled:
                for game in network[connection]['Games']:
                    if game in game_index:
                        game_index[game] += 1
                    else:
                        game_index[game] = 1
            crawled.append(connection)
            tocrawl.remove(connection)
            for secondary_connection in network[connection]['Connections']:
                if secondary_connection not in crawled:
                    tocrawl.append(secondary_connection)                    
    return game_index

# game_recs(network,user,n):
#   Crawls the user's connections and creates a game index to tracks
#   how many people in the user's network like each game.

# Arguments:
#   network: The network created with create_data_structure. 
#   user:  String containing the name of a user.
#   n: Number of game recommendations.
# Return:
#   An list of n game recommendations based on how many people in the user's network like each game.
#
# Sample output:
#   >>> print game_recs(net,'Debra',5)
#   >>> Game Recommendations:
#       The Legend of Corgi - 4 people in your network like this game.
#       Call of Arms - 3 people in your network like this game.
#       Seahorse Adventures - 3 people in your network like this game.
#       Super Mushroom Man - 3 people in your network like this game.
#       City Comptroller: The Fiscal Dilemma - 2 people in your network like this game.

def game_recs(network,user,n):
    if n < 1:
        return "Sorry, we have no games to recommend to you."
    
    # Copy the game index to a list and sort by the number of likes for each game.
    index = game_index(network,user)
    game_list = index.items()
    sorted_games = sorted(game_list, key=lambda game_list: game_list[1], reverse=True)
    
    # Creates the text for each game recommendation.
    game_text = []
    for game in sorted_games:
        if game[1] > 1:
            game_text.append(game[0] + " - " + str(game[1]) + " people in your network like this game.")
        else:
            game_text.append(game[0] + " - " + str(game[1]) + " person in your network likes this game.")

    # Returns n number of game recommendations.
    return "Game Recommendations:\n" + "\n".join(game_text[0:n])

# ----------------------------------------------------------------------------- 
# TEST CASES

example_input_alternate = """John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""
net = create_data_structure(example_input_alternate)
#print net
#print connections_in_common(net, "Mercedes", "John")
#print get_secondary_connections(net, "Mercedes")
#print path_to_friend(net, 'John', 'Bryant')
#print path_to_friend(net, 'John', 'Ollie')
#print path_to_friend(net, 'Mercedes', 'Debra')
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print game_index(net,'Debra')
print game_recs(net,'Debra',5)