import csv
import os

# Define the input CSV file path
input_dir = "/Users/austinmoore/Desktop/FFL"
csv_file = os.path.join(input_dir, "player_stats.csv")

# Ensure the input directory exists
if not os.path.exists(input_dir):
    print(f"Error: Directory '{input_dir}' does not exist.")
    exit(1)

# Fantasy football scoring rules
SCORING = {
    "pass_yards_per_point": 20,  # 1 point per 20 passing yards
    "pass_td_points": 6,         # 6 points per passing TD
    "rec_yards_per_point": 10,   # 1 point per 10 receiving yards
    "rec_td_points": 6,          # 6 points per receiving TD
    "rush_yards_per_point": 10,  # 1 point per 10 rushing yards
    "rush_td_points": 6,         # 6 points per rushing TD
    "ppr_points": 1             # 1 point per reception (PPR)
}

# Read CSV and calculate xFP and xFP per game
player_data = []
try:
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert string values to float, handle empty strings as 0
            over_pass_yards = float(row["Over_Pass_Yards"]) if row["Over_Pass_Yards"] else 0
            throw_tds = float(row["Throw_TDs"]) if row["Throw_TDs"] else 0
            rec_yards = float(row["Rec_Yards"]) if row["Rec_Yards"] else 0
            rec_tds = float(row["Rec_TDs"]) if row["Rec_TDs"] else 0
            rush_yards = float(row["Rush_Yards"]) if row["Rush_Yards"] else 0
            rush_tds = float(row["Rush_TDs"]) if row["Rush_TDs"] else 0

            # Assume 1 reception if Rec_Yards > 0 for PPR (simplified approximation)
            receptions = 1 if rec_yards > 0 else 0

            # Calculate xFP
            xfp = (over_pass_yards / SCORING["pass_yards_per_point"]) + \
                  (throw_tds * SCORING["pass_td_points"]) + \
                  (rec_yards / SCORING["rec_yards_per_point"]) + \
                  (rec_tds * SCORING["rec_td_points"]) + \
                  (rush_yards / SCORING["rush_yards_per_point"]) + \
                  (rush_tds * SCORING["rush_td_points"]) + \
                  (receptions * SCORING["ppr_points"])

            # Calculate xFP per game with special handling for Jordan Addison
            if row["Player"] == "Jordan Addison":
                xfp_per_game = xfp / 14  # 17 - 3 game suspension
            else:
                xfp_per_game = xfp / 17  # Standard 17 games

            # Add xFP and xFP per game to the row
            row["xFP"] = round(xfp, 2)
            row["xFP_per_game"] = round(xfp_per_game, 2)
            player_data.append(row)
except FileNotFoundError:
    print(f"Error: File '{csv_file}' not found. Please ensure the CSV file exists in '{input_dir}'.")
    exit(1)
except Exception as e:
    print(f"Error: An unexpected error occurred while reading the file: {str(e)}")
    exit(1)

# Write updated data back to a new CSV file
output_file = os.path.join(input_dir, "player_stats_with_xfp.csv")
try:
    with open(output_file, mode='w', newline='') as file:
        fieldnames = ["Player", "Team", "Position", "Over_Pass_Yards", "Throw_TDs", "Rec_Yards", "Rec_TDs", "Rush_Yards", "Rush_TDs", "xFP", "xFP_per_game"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(player_data)
    print(f"CSV file with xFP and xFP per game calculated has been created successfully at '{output_file}'.")
except PermissionError:
    print(f"Error: Permission denied when trying to write to '{output_file}'. Please ensure you have write permissions for the directory.")
except Exception as e:
    print(f"Error: An unexpected error occurred while writing the file: {str(e)}")