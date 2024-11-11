
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

# Initialize WebDriver
driver = webdriver.Chrome()

def test_all_scores():
    # Navigate to the score table page
    url = "http://127.0.0.1:5000/score_table"
    print(f"Testing URL: {url}")
    driver.get(url)
    time.sleep(2)  # Wait for page to load

    # Find all rows in the score table
    rows = driver.find_elements(By.TAG_NAME, "tr")
    print(f"Found {len(rows)} rows in the score table.")

    for row in rows:
        # Extract player name and score from each row
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) == 2:
            player_name = columns[0].text.strip()
            score_text = columns[1].text.strip()

            pattern = r"^(0|[1-9][0-9]{0,2}|1000)$"  # regex to determine numbers are within range
            # Validate the score is a number in the range 0-1000
            if re.match(pattern, score_text):
                score = int(score_text)
                print(f"{player_name}'s score is valid: {score}")
            else:
                print(f"Invalid score format for {player_name}: {score_text}")
                return False
        else:
            print("Unexpected row format, skipping:", row.text)

    return True

# Run the test
assert test_all_scores(), "Some scores are not valid numbers."

# Close the browser
driver.quit()