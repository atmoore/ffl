import csv
import os

# Define the output directory and file path
output_dir = "/Users/austinmoore/Desktop/FFL/output"
output_csv_file = os.path.join(output_dir, "rookie.csv") # Changed filename to indicate filtering

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)
print(f"Ensured directory exists: '{output_dir}'")

# Rookie data with NFL teams and Hit_Rate
rookie_data = [
    {"Position": "RB", "Player": "Ashton Jeanty", "Percentile": "97.8%", "Hit_Rate": "91.3%", "Team": "Las Vegas Raiders"},
    {"Position": "RB", "Player": "Omarion Hampton", "Percentile": "94.7%", "Hit_Rate": "91.3%", "Team": "Los Angeles Chargers"},
    {"Position": "RB", "Player": "Quinshon Judkins", "Percentile": "93.3%", "Hit_Rate": "91.3%", "Team": "Cleveland Browns"},
    {"Position": "RB", "Player": "TreVeyon Henderson", "Percentile": "92.6%", "Hit_Rate": "91.3%", "Team": "New England Patriots"},
    {"Position": "RB", "Player": "Kaleb Johnson", "Percentile": "84.4%", "Hit_Rate": "60%", "Team": "Pittsburgh Steelers"},
    {"Position": "RB", "Player": "R.J. Harvey Jr.", "Percentile": "75.1%", "Hit_Rate": "35%", "Team": "Denver Broncos"},
    {"Position": "RB", "Player": "Bhayhaul Tsuten", "Percentile": "74.7%", "Hit_Rate": "35%", "Team": "Jacksonville Jaguars"},
    {"Position": "RB", "Player": "Cameron Skattebo", "Percentile": "66.5%", "Hit_Rate": "16.1%", "Team": "New York Giants"},
    {"Position": "RB", "Player": "DJ Giddens", "Percentile": "64.3%", "Hit_Rate": "16.1%", "Team": "Indianapolis Colts"},
    {"Position": "RB", "Player": "Dylan Sampson", "Percentile": "58.7%", "Hit_Rate": "16.1%", "Team": "Cleveland Browns"},
    {"Position": "RB", "Player": "Trevor Etienne", "Percentile": "55.4%", "Hit_Rate": "16.1%", "Team": "Carolina Panthers"},
    {"Position": "RB", "Player": "Jarquez Hunter", "Percentile": "53.1%", "Hit_Rate": "16.1%", "Team": "Los Angeles Rams"},
    {"Position": "RB", "Player": "Devin Neal", "Percentile": "50.5%", "Hit_Rate": "16.1%", "Team": "New Orleans Saints"},
    {"Position": "RB", "Player": "Jordan James", "Percentile": "42.4%", "Hit_Rate": "16.1%", "Team": "San Francisco 49ers"},
    {"Position": "RB", "Player": "Jo'Quavious Marks", "Percentile": "39.8%", "Hit_Rate": "16.1%", "Team": "Houston Texans"},
    {"Position": "RB", "Player": "Jaydon Blue", "Percentile": "38.7%", "Hit_Rate": "16.1%", "Team": "Dallas Cowboys"},
    {"Position": "RB", "Player": "Ollie Gordon II", "Percentile": "35.3%", "Hit_Rate": "16.1%", "Team": "Denver Broncos"},
    {"Position": "RB", "Player": "Damien Martinez", "Percentile": "33.1%", "Hit_Rate": "16.1%", "Team": "Seattle Seahawks"},
    {"Position": "RB", "Player": "Tahj Brooks", "Percentile": "24.9%", "Hit_Rate": "16.1%", "Team": "Cincinnati Bengals"},
    {"Position": "RB", "Player": "Lequint Allen", "Percentile": "23.8%", "Hit_Rate": "16.1%", "Team": "Jacksonville Jaguars"},
    {"Position": "RB", "Player": "Brashard Smith", "Percentile": "17.5%", "Hit_Rate": "16.1%", "Team": "Kansas City Chiefs"},
    {"Position": "RB", "Player": "Kalel Mullings", "Percentile": "11.9%", "Hit_Rate": "16.1%", "Team": "Tennessee Titans"},
    {"Position": "RB", "Player": "Kyle Monangai", "Percentile": "9.7%", "Hit_Rate": "16.1%", "Team": "Chicago Bears"},
    {"Position": "RB", "Player": "Phil Mafah", "Percentile": "6.7%", "Hit_Rate": "16.1%", "Team": "Dallas Cowboys"},
    {"Position": "RB", "Player": "Jacorry Croskey-Merritt", "Percentile": "4.8%", "Hit_Rate": "16.1%", "Team": "Washington Commanders"},
    {"Position": "WR", "Player": "Tetairoa McMillan", "Percentile": "93.7%", "Hit_Rate": "70%", "Team": "Carolina Panthers"},
    {"Position": "WR", "Player": "Emeka Egbuka", "Percentile": "90.6%", "Hit_Rate": "70%", "Team": "Tampa Bay Buccaneers"},
    {"Position": "WR", "Player": "Travis Hunter", "Percentile": "88.6%", "Hit_Rate": "41%", "Team": "Jacksonville Jaguars"},
    {"Position": "WR", "Player": "Luther Burden III", "Percentile": "86.5%", "Hit_Rate": "41%", "Team": "Chicago Bears"},
    {"Position": "WR", "Player": "Jayden Higgins", "Percentile": "78.9%", "Hit_Rate": "29%", "Team": "Houston Texans"},
    {"Position": "WR", "Player": "Matthew Golden", "Percentile": "78.3%", "Hit_Rate": "29%", "Team": "Green Bay Packers"},
    {"Position": "WR", "Player": "Kyle Williams", "Percentile": "72.8%", "Hit_Rate": "29%", "Team": "New England Patriots"},
    {"Position": "WR", "Player": "Tre Harris", "Percentile": "71.9%", "Hit_Rate": "29%", "Team": "Los Angeles Chargers"},
    {"Position": "WR", "Player": "Isaac TeSlaa", "Percentile": "67.3%", "Hit_Rate": "17%", "Team": "Detroit Lions"},
    {"Position": "WR", "Player": "Jaylin Noel", "Percentile": "61%", "Hit_Rate": "17%", "Team": "Houston Texans"},
    {"Position": "WR", "Player": "Patrick Bryant", "Percentile": "58%", "Hit_Rate": "3%", "Team": "Denver Broncos"},
    {"Position": "WR", "Player": "Jack Becht", "Percentile": "55.7%", "Hit_Rate": "3%", "Team": "Las Vegas Raiders"},
    {"Position": "WR", "Player": "Eli Ayomanor", "Percentile": "51.5%", "Hit_Rate": "3%", "Team": "Tennessee Titans"},
    {"Position": "WR", "Player": "Chimere Dike", "Percentile": "48.1%", "Hit_Rate": "3%", "Team": "Tennessee Titans"},
    {"Position": "WR", "Player": "Tal Faltion", "Percentile": "47.5%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Dont'e Thornton Jr.", "Percentile": "46.2%", "Hit_Rate": "3%", "Team": "Las Vegas Raiders"},
    {"Position": "WR", "Player": "Arian Smith", "Percentile": "42.6%", "Hit_Rate": "3%", "Team": "Green Bay Packers"},
    {"Position": "WR", "Player": "Savion Williams", "Percentile": "41.6%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Jalen Royals", "Percentile": "38.8%", "Hit_Rate": "3%", "Team": "Kansas City Chiefs"},
    {"Position": "WR", "Player": "Jaylin Lane", "Percentile": "38.1%", "Hit_Rate": "3%", "Team": "Washington Commanders"},
    {"Position": "WR", "Player": "Tory Horton", "Percentile": "35.4%", "Hit_Rate": "3%", "Team": "Seattle Seahawks"},
    {"Position": "WR", "Player": "Jordan Watkins", "Percentile": "32.7%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "KeAndre Lambert-Smith", "Percentile": "29.9%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Ricky White", "Percentile": "20.5%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Tez Johnson", "Percentile": "19.6%", "Hit_Rate": "3%", "Team": "Tampa Bay Buccaneers"},
    {"Position": "WR", "Player": "LaJohntay Wester", "Percentile": "18.3%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Konata Mumpfield", "Percentile": "13.1%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Dominic Lovett", "Percentile": "11.8%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Jimmy Horn Jr.", "Percentile": "7.6%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Kaden Prather", "Percentile": "3.6%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "WR", "Player": "Junior Bergen", "Percentile": "2.1%", "Hit_Rate": "3%", "Team": ""},
    {"Position": "TE", "Player": "Colston Loveland", "Percentile": "97.69%", "Hit_Rate": "100%", "Team": "Chicago Bears"},
    {"Position": "TE", "Player": "Tyler Warren", "Percentile": "97.12%", "Hit_Rate": "100%", "Team": "Indianapolis Colts"},
    {"Position": "TE", "Player": "Harold Fannin Jr.", "Percentile": "88.5%", "Hit_Rate": "36%", "Team": "Cleveland Browns"},
    {"Position": "TE", "Player": "Terrance Ferguson", "Percentile": "84.47%", "Hit_Rate": "36%", "Team": "Los Angeles Rams"},
    {"Position": "TE", "Player": "Elijah Arroyo", "Percentile": "80.45%", "Hit_Rate": "36%", "Team": "Seattle Seahawks"},
    {"Position": "TE", "Player": "Mason Taylor", "Percentile": "79.88%", "Hit_Rate": "15%", "Team": "Las Vegas Raiders"},
    {"Position": "TE", "Player": "Mitchell Evans", "Percentile": "55.74%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Oronde Gadsden II", "Percentile": "53.44%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Gunnar Helm", "Percentile": "52.86%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Gavin Bartholomew", "Percentile": "25.28%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Jackson Hawes", "Percentile": "20.1%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Robbie Ouzts", "Percentile": "19.53%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Moliki Matavao", "Percentile": "18.96%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Thomas Fidone II", "Percentile": "17.23%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Luke Lachey", "Percentile": "11.48%", "Hit_Rate": "5%", "Team": ""},
    {"Position": "TE", "Player": "Caleb Lohner", "Percentile": "1.71%", "Hit_Rate": "5%", "Team": ""}
]

# Filter data: only include players with Hit_Rate >= 5%
filtered_rookie_data = []
for player_info in rookie_data:
    try:
        # Convert Hit_Rate to a float for comparison
        hit_rate_str = player_info["Hit_Rate"].replace("%", "")
        hit_rate_float = float(hit_rate_str)
        if hit_rate_float >= 5.5:
            filtered_rookie_data.append(player_info)
    except ValueError:
        print(f"Warning: Could not parse Hit_Rate for {player_info.get('Player', 'Unknown Player')}: {player_info.get('Hit_Rate', 'N/A')}. Skipping entry.")
        continue # Skip to the next player if Hit_Rate is not a valid number

# Write filtered data to CSV file
try:
    with open(output_csv_file, mode='w', newline='') as file:
        fieldnames = ["Position", "Player", "Percentile", "Hit_Rate", "Team"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rookie_data)
    print(f"CSV file 'rookie.csv' has been created successfully at '{output_dir}'.")
except PermissionError:
    print(f"Error: Permission denied when trying to write to '{output_csv_file}'. Please ensure you have write permissions for the directory.")
except Exception as e:
    print(f"Error: An unexpected error occurred while writing the file: {str(e)}")
