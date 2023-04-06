# Tyfabian Williams
# 2142655

class Team:
    def init(self):
        self.teamname = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        percent = self.team_wins / (self.team_wins + self.team_losses)
        return percent

if __name__ == '__main__':


    student_team = Team()
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    student_team.teamname = team_name
    student_team.team_wins = team_wins
    student_team.team_losses = team_losses

    if student_team.get_win_percentage() >= 0.5:
        print(f'Congratulations, Team {student_team.teamname} has a winning average!')
    else:
        print(f'Team {student_team.teamname} has a losing average.')
