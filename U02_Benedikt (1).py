# open the file best shooters NHL in read mode
shooters = open("best shooters NHL.txt", "r")

# make an empty list to store the data of the players
players = []

# iterate through each line in  the file
for line in shooters.readlines():

    data=line.split(" - ") # split the line into name and goals based on - in between the 2 parameters
    name = data[0]  #extract the players name
    goals = int(data[1]) #extract the number of goals


    players.append({'name':name,'goals':goals}) # add a dictionary with player names and goals to the list
shooters.close() # close the file after reading

print(players) # print list of players and goals

print(f"number of players: {len(players)}") # print number of players in the list
print(f"type of players: {type(players)}") # print the type of the players variable (it is a list)


#creating a function that shows us the biggest amount of goals from the list
def max_goals(player_list):
    """
    function calculates maximal ammount of goals in player_list

    Parameters
    ----------
    player_list : list
        list of players

    Returns
    -------
    max_goals : int
        maximal amount of goals in player_list
    """
    goal_max = players[0]['goals']
    for player in player_list:
        if player['goals'] > goal_max:
            goal_max = player['goals']
    return goal_max

#creating a function that shows us the smallest amount of goals from the list
def min_goals(player_list):
    """
        function calculates minimal amount of goals in player_list

        Parameters
        ----------
        player_list : list
            list of players

        Returns
        -------
        min_goals : int
            minimal amount of goals in player_list
        """
    goal_min = players[0]['goals']
    for player in player_list:
        if player['goals'] < goal_min:
            goal_min = player['goals']
    return goal_min

# creating a function that makes the average amount of goals from the list
def average_goals(player_list):
    """
        function makes average amount of goals from the player_list

        Parameters
        ----------
        player_list : list
            list of players

        Returns
        -------
        average_goals : float
            average amount of goals from player_list
        """
    goal_sum = 0
    for player in player_list:
        goal_sum += player['goals']
    return goal_sum / len(player_list)

# defining variables
biggest_goal_amount = max_goals(players)
smallest_goal_amount = min_goals(players)
average_goal_amount = average_goals(players)


# printing the output of the functions
print(f"biggest number of goals in top 5: {biggest_goal_amount}")
print(f"smallest number of goals in top 5: {smallest_goal_amount}")
print(f"average number of goals in top 5: {average_goal_amount}")