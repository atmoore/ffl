import csv
import os

# Define the input CSV file path
input_dir = "/Users/austinmoore/Desktop/FFL"
csv_file = os.path.join(input_dir, "team_proj_pts.csv")

# Ensure the input directory exists
if not os.path.exists(input_dir):
    print(f"Error: Directory '{input_dir}' does not exist.")
    exit(1)

# Team projection data
team_data = [
    {"Rank": "1", "Team": "Buffalo Bills", "Proj_Season_Pts": "457.5"},
    {"Rank": "2", "Team": "Baltimore Ravens", "Proj_Season_Pts": "452.5"},
    {"Rank": "3", "Team": "Cincinnati Bengals", "Proj_Season_Pts": "445.5"},
    {"Rank": "4", "Team": "Kansas City Chiefs", "Proj_Season_Pts": "435.5"},
    {"Rank": "5", "Team": "Philadelphia Eagles", "Proj_Season_Pts": "432.5"},
    {"Rank": "6", "Team": "Washington Commanders", "Proj_Season_Pts": "432.5"},
    {"Rank": "7", "Team": "Detroit Lions", "Proj_Season_Pts": "431.5"},
    {"Rank": "8", "Team": "Tampa Bay Buccaneers", "Proj_Season_Pts": "425.5"},
    {"Rank": "9", "Team": "Los Angeles Rams", "Proj_Season_Pts": "415.5"},
    {"Rank": "10", "Team": "San Francisco 49ers", "Proj_Season_Pts": "415.5"},
    {"Rank": "11", "Team": "Green Bay Packers", "Proj_Season_Pts": "410.5"},
    {"Rank": "12", "Team": "Denver Broncos", "Proj_Season_Pts": "403.5"},
    {"Rank": "13", "Team": "Los Angeles Chargers", "Proj_Season_Pts": "403.5"},
    {"Rank": "14", "Team": "Arizona Cardinals", "Proj_Season_Pts": "400.5"},
    {"Rank": "15", "Team": "Chicago Bears", "Proj_Season_Pts": "399.5"},
    {"Rank": "16", "Team": "Dallas Cowboys", "Proj_Season_Pts": "399.5"},
    {"Rank": "17", "Team": "Houston Texans", "Proj_Season_Pts": "399.5"},
    {"Rank": "18", "Team": "Miami Dolphins", "Proj_Season_Pts": "395.5"},
    {"Rank": "19", "Team": "Minnesota Vikings", "Proj_Season_Pts": "390.5"},
    {"Rank": "20", "Team": "Atlanta Falcons", "Proj_Season_Pts": "389.5"},
    {"Rank": "21", "Team": "Jacksonville Jaguars", "Proj_Season_Pts": "389.5"},
    {"Rank": "22", "Team": "New England Patriots", "Proj_Season_Pts": "389.5"},
    {"Rank": "23", "Team": "Seattle Seahawks", "Proj_Season_Pts": "389.5"},
    {"Rank": "24", "Team": "Pittsburgh Steelers", "Proj_Season_Pts": "379.5"},
    {"Rank": "25", "Team": "Carolina Panthers", "Proj_Season_Pts": "368.5"},
    {"Rank": "26", "Team": "Indianapolis Colts", "Proj_Season_Pts": "365.5"},
    {"Rank": "27", "Team": "Las Vegas Raiders", "Proj_Season_Pts": "359.5"},
    {"Rank": "28", "Team": "Tennessee Titans", "Proj_Season_Pts": "359.5"},
    {"Rank": "29", "Team": "New York Jets", "Proj_Season_Pts": "335.5"},
    {"Rank": "30", "Team": "New Orleans Saints", "Proj_Season_Pts": "331.5"},
    {"Rank": "31", "Team": "New York Giants", "Proj_Season_Pts": "331.5"},
    {"Rank": "32", "Team": "Cleveland Browns", "Proj_Season_Pts": "325.5"}
]

# Write data to CSV file
try:
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ["Rank", "Team", "Proj_Season_Pts"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(team_data)
    print(f"CSV file 'team_proj_pts.csv' has been created successfully at '{input_dir}'.")
except PermissionError:
    print(f"Error: Permission denied when trying to write to '{csv_file}'. Please ensure you have write permissions for the directory.")
except Exception as e:
    print(f"Error: An unexpected error occurred while writing the file: {str(e)}")
    exit(1)