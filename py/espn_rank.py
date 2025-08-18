import csv
import os

# Define the input CSV file path
input_dir = "/Users/austinmoore/Desktop/FFL"
csv_file = os.path.join(input_dir, "espn_rank.csv")

# Ensure the input directory exists
if not os.path.exists(input_dir):
    print(f"Error: Directory '{input_dir}' does not exist.")
    exit(1)

# Player ranking data
player_data = [
    {"espn_rank": "1", "player": "Ja'Marr Chase", "team": "CIN", "position": "WR", "position_rank": "WR1", "bye_week": "10"},
    {"espn_rank": "2", "player": "Bijan Robinson", "team": "ATL", "position": "RB", "position_rank": "RB1", "bye_week": "5"},
    {"espn_rank": "3", "player": "Justin Jefferson", "team": "MIN", "position": "WR", "position_rank": "WR2", "bye_week": "6"},
    {"espn_rank": "4", "player": "Saquon Barkley", "team": "PHI", "position": "RB", "position_rank": "RB2", "bye_week": "9"},
    {"espn_rank": "5", "player": "Jahmyr Gibbs", "team": "DET", "position": "RB", "position_rank": "RB3", "bye_week": "8"},
    {"espn_rank": "6", "player": "CeeDee Lamb", "team": "DAL", "position": "WR", "position_rank": "WR3", "bye_week": "10"},
    {"espn_rank": "7", "player": "Christian McCaffrey", "team": "SF", "position": "RB", "position_rank": "RB4", "bye_week": "14"},
    {"espn_rank": "8", "player": "Puka Nacua", "team": "LAR", "position": "WR", "position_rank": "WR4", "bye_week": "8"},
    {"espn_rank": "9", "player": "Malik Nabers", "team": "NYG", "position": "WR", "position_rank": "WR5", "bye_week": "14"},
    {"espn_rank": "10", "player": "Amon-Ra St. Brown", "team": "DET", "position": "WR", "position_rank": "WR6", "bye_week": "8"},
    {"espn_rank": "11", "player": "Ashton Jeanty", "team": "LV", "position": "RB", "position_rank": "RB5", "bye_week": "8"},
    {"espn_rank": "12", "player": "De'Von Achane", "team": "MIA", "position": "RB", "position_rank": "RB6", "bye_week": "12"},
    {"espn_rank": "13", "player": "Nico Collins", "team": "HOU", "position": "WR", "position_rank": "WR7", "bye_week": "6"},
    {"espn_rank": "14", "player": "Brian Thomas Jr.", "team": "JAC", "position": "WR", "position_rank": "WR8", "bye_week": "8"},
    {"espn_rank": "15", "player": "A.J. Brown", "team": "PHI", "position": "WR", "position_rank": "WR9", "bye_week": "9"},
    {"espn_rank": "16", "player": "Drake London", "team": "ATL", "position": "WR", "position_rank": "WR10", "bye_week": "5"},
    {"espn_rank": "17", "player": "Jonathan Taylor", "team": "IND", "position": "RB", "position_rank": "RB7", "bye_week": "11"},
    {"espn_rank": "18", "player": "Josh Jacobs", "team": "GB", "position": "RB", "position_rank": "RB8", "bye_week": "5"},
    {"espn_rank": "19", "player": "Derrick Henry", "team": "BAL", "position": "RB", "position_rank": "RB9", "bye_week": "7"},
    {"espn_rank": "20", "player": "Brock Bowers", "team": "LV", "position": "TE", "position_rank": "TE1", "bye_week": "8"},
    {"espn_rank": "21", "player": "Trey McBride", "team": "ARI", "position": "TE", "position_rank": "TE2", "bye_week": "8"},
    {"espn_rank": "22", "player": "Bucky Irving", "team": "TB", "position": "RB", "position_rank": "RB10", "bye_week": "9"},
    {"espn_rank": "23", "player": "Chase Brown", "team": "CIN", "position": "RB", "position_rank": "RB11", "bye_week": "10"},
    {"espn_rank": "24", "player": "Tee Higgins", "team": "CIN", "position": "WR", "position_rank": "WR11", "bye_week": "10"},
    {"espn_rank": "25", "player": "Tyreek Hill", "team": "MIA", "position": "WR", "position_rank": "WR12", "bye_week": "12"},
    {"espn_rank": "26", "player": "Ladd McConkey", "team": "LAC", "position": "WR", "position_rank": "WR13", "bye_week": "12"},
    {"espn_rank": "27", "player": "Davante Adams", "team": "LAR", "position": "WR", "position_rank": "WR14", "bye_week": "8"},
    {"espn_rank": "28", "player": "Josh Allen", "team": "BUF", "position": "QB", "position_rank": "QB1", "bye_week": "7"},
    {"espn_rank": "29", "player": "Lamar Jackson", "team": "BAL", "position": "QB", "position_rank": "QB2", "bye_week": "7"},
    {"espn_rank": "30", "player": "Jayden Daniels", "team": "WAS", "position": "QB", "position_rank": "QB3", "bye_week": "12"},
    {"espn_rank": "31", "player": "Jalen Hurts", "team": "PHI", "position": "QB", "position_rank": "QB4", "bye_week": "9"},
    {"espn_rank": "32", "player": "Kyren Williams", "team": "LAR", "position": "RB", "position_rank": "RB12", "bye_week": "8"},
    {"espn_rank": "33", "player": "James Cook", "team": "BUF", "position": "RB", "position_rank": "RB13", "bye_week": "7"},
    {"espn_rank": "34", "player": "Jaxon Smith-Njigba", "team": "SEA", "position": "WR", "position_rank": "WR15", "bye_week": "8"},
    {"espn_rank": "35", "player": "Terry McLaurin", "team": "WAS", "position": "WR", "position_rank": "WR16", "bye_week": "12"},
    {"espn_rank": "36", "player": "Garrett Wilson", "team": "NYJ", "position": "WR", "position_rank": "WR17", "bye_week": "9"},
    {"espn_rank": "37", "player": "Omarion Hampton", "team": "LAC", "position": "RB", "position_rank": "RB14", "bye_week": "12"},
    {"espn_rank": "38", "player": "Kenneth Walker III", "team": "SEA", "position": "RB", "position_rank": "RB15", "bye_week": "8"},
    {"espn_rank": "39", "player": "Joe Burrow", "team": "CIN", "position": "QB", "position_rank": "QB5", "bye_week": "10"},
    {"espn_rank": "40", "player": "George Kittle", "team": "SF", "position": "TE", "position_rank": "TE3", "bye_week": "14"},
    {"espn_rank": "41", "player": "Alvin Kamara", "team": "NO", "position": "RB", "position_rank": "RB16", "bye_week": "11"},
    {"espn_rank": "42", "player": "Chuba Hubbard", "team": "CAR", "position": "RB", "position_rank": "RB17", "bye_week": "14"},
    {"espn_rank": "43", "player": "James Conner", "team": "ARI", "position": "RB", "position_rank": "RB18", "bye_week": "8"},
    {"espn_rank": "44", "player": "TreVeyon Henderson", "team": "NE", "position": "RB", "position_rank": "RB19", "bye_week": "14"},
    {"espn_rank": "45", "player": "Mike Evans", "team": "TB", "position": "WR", "position_rank": "WR18", "bye_week": "9"},
    {"espn_rank": "46", "player": "Marvin Harrison Jr.", "team": "ARI", "position": "WR", "position_rank": "WR19", "bye_week": "8"},
    {"espn_rank": "47", "player": "Xavier Worthy", "team": "KC", "position": "WR", "position_rank": "WR20", "bye_week": "10"},
    {"espn_rank": "48", "player": "DK Metcalf", "team": "PIT", "position": "WR", "position_rank": "WR21", "bye_week": "5"},
    {"espn_rank": "49", "player": "DJ Moore", "team": "CHI", "position": "WR", "position_rank": "WR22", "bye_week": "5"},
    {"espn_rank": "50", "player": "Rashee Rice", "team": "KC", "position": "WR", "position_rank": "WR23", "bye_week": "10"},
    {"espn_rank": "51", "player": "Breece Hall", "team": "NYJ", "position": "RB", "position_rank": "RB20", "bye_week": "9"},
    {"espn_rank": "52", "player": "D'Andre Swift", "team": "CHI", "position": "RB", "position_rank": "RB21", "bye_week": "5"},
    {"espn_rank": "53", "player": "Zay Flowers", "team": "BAL", "position": "WR", "position_rank": "WR24", "bye_week": "7"},
    {"espn_rank": "54", "player": "Courtland Sutton", "team": "DEN", "position": "WR", "position_rank": "WR25", "bye_week": "12"},
    {"espn_rank": "55", "player": "Calvin Ridley", "team": "TEN", "position": "WR", "position_rank": "WR26", "bye_week": "10"},
    {"espn_rank": "56", "player": "DeVonta Smith", "team": "PHI", "position": "WR", "position_rank": "WR27", "bye_week": "9"},
    {"espn_rank": "57", "player": "Jaylen Waddle", "team": "MIA", "position": "WR", "position_rank": "WR28", "bye_week": "12"},
    {"espn_rank": "58", "player": "Jerry Jeudy", "team": "CLE", "position": "WR", "position_rank": "WR29", "bye_week": "9"},
    {"espn_rank": "59", "player": "Jameson Williams", "team": "DET", "position": "WR", "position_rank": "WR30", "bye_week": "8"},
    {"espn_rank": "60", "player": "George Pickens", "team": "DAL", "position": "WR", "position_rank": "WR31", "bye_week": "10"},
    {"espn_rank": "61", "player": "Sam LaPorta", "team": "DET", "position": "TE", "position_rank": "TE4", "bye_week": "8"},
    {"espn_rank": "62", "player": "Patrick Mahomes", "team": "KC", "position": "QB", "position_rank": "QB6", "bye_week": "10"},
    {"espn_rank": "63", "player": "Baker Mayfield", "team": "TB", "position": "QB", "position_rank": "QB7", "bye_week": "9"},
    {"espn_rank": "64", "player": "Rome Odunze", "team": "CHI", "position": "WR", "position_rank": "WR32", "bye_week": "5"},
    {"espn_rank": "65", "player": "Tetairoa McMillan", "team": "CAR", "position": "WR", "position_rank": "WR33", "bye_week": "14"},
    {"espn_rank": "66", "player": "Travis Hunter", "team": "JAC", "position": "WR", "position_rank": "WR34", "bye_week": "8"},
    {"espn_rank": "67", "player": "David Montgomery", "team": "DET", "position": "RB", "position_rank": "RB22", "bye_week": "8"},
    {"espn_rank": "68", "player": "Aaron Jones", "team": "MIN", "position": "RB", "position_rank": "RB23", "bye_week": "6"},
    {"espn_rank": "69", "player": "T.J. Hockenson", "team": "MIN", "position": "TE", "position_rank": "TE5", "bye_week": "6"},
    {"espn_rank": "70", "player": "Tony Pollard", "team": "TEN", "position": "RB", "position_rank": "RB24", "bye_week": "10"},
    {"espn_rank": "71", "player": "RJ Harvey", "team": "DEN", "position": "RB", "position_rank": "RB25", "bye_week": "12"},
    {"espn_rank": "72", "player": "Isiah Pacheco", "team": "KC", "position": "RB", "position_rank": "RB26", "bye_week": "10"},
    {"espn_rank": "73", "player": "Chris Godwin", "team": "TB", "position": "WR", "position_rank": "WR35", "bye_week": "9"},
    {"espn_rank": "74", "player": "Jakobi Meyers", "team": "LV", "position": "WR", "position_rank": "WR36", "bye_week": "8"},
    {"espn_rank": "75", "player": "Chris Olave", "team": "NO", "position": "WR", "position_rank": "WR37", "bye_week": "11"},
    {"espn_rank": "76", "player": "Cooper Kupp", "team": "SEA", "position": "WR", "position_rank": "WR38", "bye_week": "8"},
    {"espn_rank": "77", "player": "Stefon Diggs", "team": "NE", "position": "WR", "position_rank": "WR39", "bye_week": "14"},
    {"espn_rank": "78", "player": "Matthew Golden", "team": "GB", "position": "WR", "position_rank": "WR40", "bye_week": "5"},
    {"espn_rank": "79", "player": "Jordan Addison", "team": "MIN", "position": "WR", "position_rank": "WR41", "bye_week": "6"},
    {"espn_rank": "80", "player": "Tyrone Tracy Jr.", "team": "NYG", "position": "RB", "position_rank": "RB27", "bye_week": "14"},
    {"espn_rank": "81", "player": "Jaylen Warren", "team": "PIT", "position": "RB", "position_rank": "RB28", "bye_week": "5"},
    {"espn_rank": "82", "player": "Kaleb Johnson", "team": "PIT", "position": "RB", "position_rank": "RB29", "bye_week": "5"},
    {"espn_rank": "83", "player": "Travis Kelce", "team": "KC", "position": "TE", "position_rank": "TE6", "bye_week": "10"},
    {"espn_rank": "84", "player": "David Njoku", "team": "CLE", "position": "TE", "position_rank": "TE7", "bye_week": "9"},
    {"espn_rank": "85", "player": "Mark Andrews", "team": "BAL", "position": "TE", "position_rank": "TE8", "bye_week": "7"},
    {"espn_rank": "86", "player": "Evan Engram", "team": "DEN", "position": "TE", "position_rank": "TE9", "bye_week": "12"},
    {"espn_rank": "87", "player": "Bo Nix", "team": "DEN", "position": "QB", "position_rank": "QB8", "bye_week": "12"},
    {"espn_rank": "88", "player": "Kyler Murray", "team": "ARI", "position": "QB", "position_rank": "QB9", "bye_week": "8"},
    {"espn_rank": "89", "player": "Brock Purdy", "team": "SF", "position": "QB", "position_rank": "QB10", "bye_week": "14"},
    {"espn_rank": "90", "player": "Joe Mixon", "team": "HOU", "position": "RB", "position_rank": "RB30", "bye_week": "6"},
    {"espn_rank": "91", "player": "Quinshon Judkins", "team": "CLE", "position": "RB", "position_rank": "RB31", "bye_week": "9"},
    {"espn_rank": "92", "player": "Brian Robinson Jr.", "team": "WAS", "position": "RB", "position_rank": "RB32", "bye_week": "12"},
    {"espn_rank": "93", "player": "J.K. Dobbins", "team": "DEN", "position": "RB", "position_rank": "RB33", "bye_week": "12"},
    {"espn_rank": "94", "player": "Rhamondre Stevenson", "team": "NE", "position": "RB", "position_rank": "RB34", "bye_week": "14"},
    {"espn_rank": "95", "player": "Javonte Williams", "team": "DAL", "position": "RB", "position_rank": "RB35", "bye_week": "10"},
    {"espn_rank": "96", "player": "Khalil Shakir", "team": "BUF", "position": "WR", "position_rank": "WR42", "bye_week": "7"},
    {"espn_rank": "97", "player": "Jauan Jennings", "team": "SF", "position": "WR", "position_rank": "WR43", "bye_week": "14"},
    {"espn_rank": "98", "player": "Deebo Samuel Sr.", "team": "WAS", "position": "WR", "position_rank": "WR44", "bye_week": "12"},
    {"espn_rank": "99", "player": "Ricky Pearsall", "team": "SF", "position": "WR", "position_rank": "WR45", "bye_week": "14"},
    {"espn_rank": "100", "player": "Keon Coleman", "team": "BUF", "position": "WR", "position_rank": "WR46", "bye_week": "7"},
    {"espn_rank": "101", "player": "Michael Pittman Jr.", "team": "IND", "position": "WR", "position_rank": "WR47", "bye_week": "11"},
    {"espn_rank": "102", "player": "Jayden Reed", "team": "GB", "position": "WR", "position_rank": "WR48", "bye_week": "5"},
    {"espn_rank": "103", "player": "Justin Herbert", "team": "LAC", "position": "QB", "position_rank": "QB11", "bye_week": "12"},
    {"espn_rank": "104", "player": "Caleb Williams", "team": "CHI", "position": "QB", "position_rank": "QB12", "bye_week": "5"},
    {"espn_rank": "105", "player": "Dak Prescott", "team": "DAL", "position": "QB", "position_rank": "QB13", "bye_week": "10"},
    {"espn_rank": "106", "player": "Justin Fields", "team": "NYJ", "position": "QB", "position_rank": "QB14", "bye_week": "9"},
    {"espn_rank": "107", "player": "Keenan Allen", "team": "LAC", "position": "WR", "position_rank": "WR49", "bye_week": "12"},
    {"espn_rank": "108", "player": "Darnell Mooney", "team": "ATL", "position": "WR", "position_rank": "WR50", "bye_week": "5"},
    {"espn_rank": "109", "player": "Josh Downs", "team": "IND", "position": "WR", "position_rank": "WR51", "bye_week": "11"},
    {"espn_rank": "110", "player": "Rashid Shaheed", "team": "NO", "position": "WR", "position_rank": "WR52", "bye_week": "11"},
    {"espn_rank": "111", "player": "Jayden Higgins", "team": "HOU", "position": "WR", "position_rank": "WR53", "bye_week": "6"},
    {"espn_rank": "112", "player": "Emeka Egbuka", "team": "TB", "position": "WR", "position_rank": "WR54", "bye_week": "9"},
    {"espn_rank": "113", "player": "Tucker Kraft", "team": "GB", "position": "TE", "position_rank": "TE10", "bye_week": "5"},
    {"espn_rank": "114", "player": "Austin Ekeler", "team": "WAS", "position": "RB", "position_rank": "RB36", "bye_week": "12"},
    {"espn_rank": "115", "player": "Cam Skattebo", "team": "NYG", "position": "RB", "position_rank": "RB37", "bye_week": "14"},
    {"espn_rank": "116", "player": "Travis Etienne Jr.", "team": "JAC", "position": "RB", "position_rank": "RB38", "bye_week": "8"},
    {"espn_rank": "117", "player": "Tyjae Spears", "team": "TEN", "position": "RB", "position_rank": "RB39", "bye_week": "10"},
    {"espn_rank": "118", "player": "Tank Bigsby", "team": "JAC", "position": "RB", "position_rank": "RB40", "bye_week": "8"},
    {"espn_rank": "119", "player": "Jordan Mason", "team": "MIN", "position": "RB", "position_rank": "RB41", "bye_week": "6"},
    {"espn_rank": "120", "player": "Rachaad White", "team": "TB", "position": "RB", "position_rank": "RB42", "bye_week": "9"},
    {"espn_rank": "121", "player": "Drake Maye", "team": "NE", "position": "QB", "position_rank": "QB15", "bye_week": "14"},
    {"espn_rank": "122", "player": "Jordan Love", "team": "GB", "position": "QB", "position_rank": "QB16", "bye_week": "5"},
    {"espn_rank": "123", "player": "Jared Goff", "team": "DET", "position": "QB", "position_rank": "QB17", "bye_week": "8"},
    {"espn_rank": "124", "player": "J.J. McCarthy", "team": "MIN", "position": "QB", "position_rank": "QB18", "bye_week": "6"},
    {"espn_rank": "125", "player": "Colston Loveland", "team": "CHI", "position": "TE", "position_rank": "TE11", "bye_week": "5"}
]

# Write data to CSV file
try:
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ["espn_rank", "player", "team", "position", "position_rank", "bye_week"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(player_data)
    print(f"CSV file 'espn_rank.csv' has been created successfully at '{input_dir}'.")
except PermissionError:
    print(f"Error: Permission denied when trying to write to '{csv_file}'. Please ensure you have write permissions for the directory.")
except Exception as e:
    print(f"Error: An unexpected error occurred while writing the file: {str(e)}")
    exit(1)