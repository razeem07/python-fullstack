sample_text_with_dates = """
The team will be leaving for the retreat on 12/04/2022.
Our last team-building event took place on 28/08/2019.
We are planning a company-wide celebration on 30/11/2024.
My niece was born on 07/06/2015.
The next board meeting is scheduled for 15/03/2023.
We expect the project to be completed by 22/09/2021.
His wedding anniversary is on 19/12/2018.
I moved to my new apartment on 05/10/2020.
"""

# Writing the sample text and dates to 'sample_text_with_dates.txt'
text_date_file_path = 'C:\\Users\\Luminar\\Desktop\\Pythonworks\\regexfileworks\\data.txt'
with open(text_date_file_path, 'w',encoding="utf-8") as file:
    file.write(sample_text_with_dates)