In real-world data science, we may not find an ideal data set. The solution is to aggregate disparate data sources instead, or do a good amount of data cleaning.

FiveThirtyEight website became interested in answering some questions about Star Wars fans. In particular, they wondered: does the rest of America realize that “The Empire Strikes Back” is clearly the best of the Star Wars series?

The team needed to collect data addressing this question. To do this, they surveyed Star Wars fans using the online tool SurveyMonkey. They received 835 total responses.

The data has several columns, including:
	1. RespondentID - An anonymized ID for the respondent (person taking the survey)
	2. Gender - The respondent's gender
	3. Age - The respondent's age
	4. Household Income - The respondent's income
	5. Education - The respondent's education level
	6. Location (Census Region) - The respondent's location
	7. Have you seen any of the 6 films in the Star Wars franchise? - Has a Yesor No response
	8. Do you consider yourself to be a fan of the Star Wars film franchise? - Has a Yes or No response

There are several other columns containing answers to questions about the Star Wars movies. For some questions, the respondent had to check one or more boxes. This type of data is difficult to represent in columnar format. As a result, this data set needs a lot of cleaning.














