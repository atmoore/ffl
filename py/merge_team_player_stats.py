import csv
import os
import pandas as pd

# Define file paths
team_schemes_file = "/Users/austinmoore/Desktop/FFL/output/team_schemes.csv"
player_stats_file = "/Users/austinmoore/Desktop/FFL/output/player_stats_with_xfp.csv"
team_proj_pts_file = "/Users/austinmoore/Desktop/FFL/output/team_proj_pts.csv"
rookie_file = "/Users/austinmoore/Desktop/FFL/output/rookie.csv"
espn_rank_file = "/Users/austinmoore/Desktop/FFL/output/espn_rank.csv"
output_dir = "/Users/austinmoore/Desktop/FFL/output"
master_file = os.path.join(output_dir, "master_team_player_stats.xlsx")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load team schemes data into a dictionary with Team as key
team_schemes = {}
with open(team_schemes_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        team_schemes[row["Team"]] = row

# Load team projection data into a dictionary with Team as key
team_proj_pts = {}
with open(team_proj_pts_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        team_proj_pts[row["Team"]] = {"Proj_Season_Pts": row["Proj_Season_Pts"]}

# Load rookie data into a dictionary with Player as key
rookie_data = {}
with open(rookie_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rookie_data[row["Player"]] = {
            "Percentile": row["Percentile"],
            "Hit_Rate": row["Hit_Rate"]
        }

# Load ESPN rank data into a dictionary with Player as key
espn_data = {}
with open(espn_rank_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        espn_data[row["player"]] = {
            "espn_rank": row["espn_rank"],
            "position_rank": row["position_rank"],
            "bye_week": row["bye_week"]
        }

# Load player stats data and merge with team schemes, projections, rookie data, and ESPN data
merged_data = []
with open(player_stats_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for player_row in reader:
        team = player_row.get("Team", "")
        player = player_row["Player"]
        if team in team_schemes and team in team_proj_pts:
            merged_row = player_row.copy()
            merged_row.update({
                "Scheme_Balance": team_schemes[team]["Scheme_Balance"],
                "Position_Focus": team_schemes[team]["Position_Focus"],
                "Proj_Season_Pts": team_proj_pts[team]["Proj_Season_Pts"]
            })
            # Add Percentile, Hit_Rate, and Rookie column if player is a rookie, otherwise leave blank
            rookie_info = rookie_data.get(player, {})
            merged_row["Percentile"] = rookie_info.get("Percentile", "")
            merged_row["Hit_Rate"] = rookie_info.get("Hit_Rate", "")
            merged_row["Rookie"] = "1" if player in rookie_data else "0"
            # Add ESPN data based on player name
            espn_info = espn_data.get(player, {})
            merged_row["espn_rank"] = espn_info.get("espn_rank", "")
            merged_row["position_rank"] = espn_info.get("position_rank", "")
            merged_row["bye_week"] = espn_info.get("bye_week", "")
            merged_data.append(merged_row)

# Load rookie data directly for the rookies tab
rookie_tab_data = []
with open(rookie_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rookie_tab_data.append(row)

# Convert to DataFrames
df_main = pd.DataFrame(merged_data)
df_rookies = pd.DataFrame(rookie_tab_data)

# Write to Excel with two sheets
if not df_main.empty or not df_rookies.empty:
    try:
        with pd.ExcelWriter(master_file, engine='xlsxwriter') as writer:
            df_main.to_excel(writer, sheet_name="master_team_player_stats", index=False)
            df_rookies.to_excel(writer, sheet_name="rookie", index=False)
        print(f"Excel file '{master_file}' with 'master_team_player_stats' and 'rookie' tabs has been created successfully at {output_dir}.")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{master_file}'. Please ensure you have write permissions for the directory.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
else:
    print("No matching data found to merge.")