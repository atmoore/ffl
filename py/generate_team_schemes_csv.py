import csv
import os

# Define the output directory and file
output_dir = "/Users/austinmoore/Desktop/FFL"
csv_file = os.path.join(output_dir, "team_schemes.csv")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Data organized by team with updated Position_Focus
team_data = [
    {"Division": "AFC East", "Team": "Buffalo Bills", "Head Coach": "Sean McDermott", "Offensive Scheme": "Erhardt-Perkins", "Scheme_Balance": "balanced", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "AFC East", "Team": "Miami Dolphins", "Head Coach": "Mike McDaniel", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "AFC East", "Team": "New England Patriots", "Head Coach": "Mike Vrabel", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "AFC East", "Team": "New York Jets", "Head Coach": "Aaron Glenn", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "AFC North", "Team": "Baltimore Ravens", "Head Coach": "John Harbaugh", "Offensive Scheme": "Air Coryell", "Scheme_Balance": "run-heavy", "Position_Focus": "RB", "Defensive Scheme": "3-4"},
    {"Division": "AFC North", "Team": "Cincinnati Bengals", "Head Coach": "Zac Taylor", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "AFC North", "Team": "Cleveland Browns", "Head Coach": "Kevin Stefanski", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "AFC North", "Team": "Pittsburgh Steelers", "Head Coach": "Mike Tomlin", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "RB", "Defensive Scheme": "3-4"},
    {"Division": "AFC South", "Team": "Houston Texans", "Head Coach": "DeMeco Ryans", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "AFC South", "Team": "Indianapolis Colts", "Head Coach": "Shane Steichen", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "AFC South", "Team": "Jacksonville Jaguars", "Head Coach": "Liam Coen", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "AFC South", "Team": "Tennessee Titans", "Head Coach": "Brian Callahan", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "RB", "Defensive Scheme": "3-4"},
    {"Division": "AFC West", "Team": "Denver Broncos", "Head Coach": "Sean Payton", "Offensive Scheme": "Air Coryell", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "AFC West", "Team": "Kansas City Chiefs", "Head Coach": "Andy Reid", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "AFC West", "Team": "Las Vegas Raiders", "Head Coach": "Pete Carroll", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "RB", "Defensive Scheme": "4-3"},
    {"Division": "AFC West", "Team": "Los Angeles Chargers", "Head Coach": "Jim Harbaugh", "Offensive Scheme": "West Coast", "Scheme_Balance": "run-heavy", "Position_Focus": "RB", "Defensive Scheme": "4-3"},
    {"Division": "NFC East", "Team": "Dallas Cowboys", "Head Coach": "Brian Schottenheimer", "Offensive Scheme": "Air Coryell", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "NFC East", "Team": "New York Giants", "Head Coach": "Brian Daboll", "Offensive Scheme": "Erhardt-Perkins", "Scheme_Balance": "balanced", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "NFC East", "Team": "Philadelphia Eagles", "Head Coach": "Nick Sirianni", "Offensive Scheme": "Air Coryell", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "NFC East", "Team": "Washington Commanders", "Head Coach": "Dan Quinn", "Offensive Scheme": "Spread", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "NFC North", "Team": "Chicago Bears", "Head Coach": "Ben Johnson", "Offensive Scheme": "Erhardt-Perkins", "Scheme_Balance": "balanced", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "NFC North", "Team": "Detroit Lions", "Head Coach": "Dan Campbell", "Offensive Scheme": "Erhardt-Perkins", "Scheme_Balance": "balanced", "Position_Focus": "RB", "Defensive Scheme": "4-3"},
    {"Division": "NFC North", "Team": "Green Bay Packers", "Head Coach": "Matt LaFleur", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "NFC North", "Team": "Minnesota Vikings", "Head Coach": "Kevin O’Connell", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "NFC South", "Team": "Atlanta Falcons", "Head Coach": "Raheem Morris", "Offensive Scheme": "West Coast", "Scheme_Balance": "run-heavy", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "NFC South", "Team": "Carolina Panthers", "Head Coach": "Dave Canales", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "NFC South", "Team": "New Orleans Saints", "Head Coach": "Kellen Moore", "Offensive Scheme": "Air Coryell", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "4-3"},
    {"Division": "NFC South", "Team": "Tampa Bay Buccaneers", "Head Coach": "Todd Bowles", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "NFC West", "Team": "Arizona Cardinals", "Head Coach": "Jonathan Gannon", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "TE", "Defensive Scheme": "3-4"},
    {"Division": "NFC West", "Team": "Los Angeles Rams", "Head Coach": "Sean McVay", "Offensive Scheme": "West Coast", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "3-4"},
    {"Division": "NFC West", "Team": "San Francisco 49ers", "Head Coach": "Kyle Shanahan", "Offensive Scheme": "West Coast", "Scheme_Balance": "balanced", "Position_Focus": "TE", "Defensive Scheme": "4-3"},
    {"Division": "NFC West", "Team": "Seattle Seahawks", "Head Coach": "Mike Macdonald", "Offensive Scheme": "Spread", "Scheme_Balance": "pass-heavy", "Position_Focus": "WR", "Defensive Scheme": "3-4"}
]

# Write to CSV file with explicit text formatting
try:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Division", "Team", "Head Coach", "Offensive Scheme", "Scheme_Balance", "Position_Focus", "Defensive Scheme"], quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(team_data)
    print(f"CSV file '{csv_file}' has been created successfully at {output_dir}.")
except PermissionError:
    print(f"Error: Permission denied when trying to write to '{csv_file}'. Please ensure you have write permissions for the directory.")
except Exception as e:
    print(f"Error: An unexpected error occurred: {str(e)}")