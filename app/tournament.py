# Source: https://exercism.org/tracks/python/exercises/tournament
from pathlib import Path

class Team:
	def __init__(self, team_name):
		self.name = team_name
		self.mp = 0
		self.wins = 0
		self.draws = 0
		self.losses = 0
		self.points = 0
	def __str__(self):
		team_whitespace = 31 - len(self.name)
		team = self.name
		for i in range(team_whitespace):
			team += " "
		team += "|"
		mp = self.table_format(str(self.mp))
		win = self.table_format(str(self.wins))
		draw = self.table_format(str(self.draws))
		loss = self.table_format(str(self.losses))
		points = self.table_format(str(self.points))

		return team + mp + win + draw + loss + points
	def get_name(self):
		return self.name

	def win(self):
		self.wins += 1
		self.mp += 1
		self.points += 3
	def draw(self):
		self.draws += 1
		self.mp += 1
		self.points += 1
	def lose(self):
		self.losses += 1
		self.mp += 1

	def table_format(self, input):
		return "  " + input + " |"

def print_table(teams_list):
	print("Team                           | MP |  W |  D |  L |  P |")
	for team in teams_list:
		print(team)

def parse_input():
	values_list = []
	src = Path(__file__).parent
	relative_path = "input_files/tournament.txt"
	path = (src / relative_path).resolve()
	with path.open() as f:
		lines = f.readlines()
		for line in lines:
			values = []
			line = line.strip()
			values = line.split(";")
			values_list.append(values)
	return values_list

def check_team_list(team_name):
	result = None
	for team in teams_list:
		if team.get_name() == team_name:
			result = team
	return result;

def get_team(team_name, teams_list):
    team = check_team_list(team_name)
    if team == None:
        team = Team(team_name)
        teams_list.append(team)
    return team;

teams_list = []
fixtures = parse_input()
for fixture in fixtures:
	home_team_name = fixture[0]
	home_team = get_team(home_team_name, teams_list)	
	away_team_name = fixture[1]
	away_team = get_team(away_team_name, teams_list)
	result = fixture[2]
	match result:
		case "win":
			home_team.win()
			away_team.lose()
		case "draw":
			home_team.draw()
			away_team.draw()
		case "loss":
			home_team.lose()
			away_team.win()

teams_list.sort(key=lambda x: (x.points, x.name), reverse=True)
print_table(teams_list)
	
