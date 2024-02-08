# This Python script can be used to facilitate the use of RABBIT.
# It retrieves the login names of all contributors
# obtained through the GitHub API for a given repository
# and returns it as a file that can be used as input for RABBIT.

import requests
import json
import sys

def get_contributors(repo_owner, repo_name):
    # GitHub API endpoint for retrieving contributors
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contributors"
    
    # Make a GET request to the GitHub API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        contributors_data = response.json()
        
        # Extract contributor names
        contributors = [contributor['login'] for contributor in contributors_data]
        
        return contributors
    else:
        print(f"API Error. Status code: {response.status_code}")
        return None

def main(repo_owner, repo_name, output_filename):

    # Get contributors list
    contributors = get_contributors(repo_owner, repo_name)
    
    if contributors:
        # Write contributors to a text file
        with open(output_filename, 'w') as file:
          file.writelines("%s\n" % login for login in contributors)
            
        print("List of repo contributor logins saved to " + output_filename)
    else:
        print("Failed to retrieve contributor list.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <repo_owner> <repo_name> <output_filename>")
        sys.exit(1)
        
    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]
    output_filename = sys.argv[3]

    main(repo_owner, repo_name, output_filename)