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

First, we'll need to remove the invalid rows. For example, RespondentID is supposed to be a unique ID for each respondent, but it's blank in some rows. So we will have to remove any rows where RespondentID is NaN. I used the pandas.notnull()function to accomplish this.

Take a look at the next two columns, which are: 1. Have you seen any of the 6 films in the Star Wars franchise? 2. Do you consider yourself to be a fan of the Star Wars film franchise

Both columns are currently string types, because the main values they contain are Yes and No. We can make the data a bit easier to analyze down the road by converting each column to a Boolean having only the values True, False, and NaN. Booleans are easier to work with because we can select the rows that are True or False without having to do a string comparison. I used the pandas.Series.map() method on series objects to perform the conversion.

The next six columns represent a single checkbox question. The respondent checked off a series of boxes in response to the question, Which of the following Star Wars films have you seen? Please select all that apply.

For each of these columns, if the value in a cell is the name of the movie, that means the respondent saw the movie. If the value is NaN, the respondent either didn't answer or didn't see the movie. We'll assume that they didn't see the movie.

We'll need to convert each of these columns to a Boolean, then rename the column something more intuitive. We can convert the values the same way we did earlier, except that we'll need to include the movie title and NaN in the mapping dictionary.

After calling the map() method on a series, the column should only contain the values True and False.

Next, we'll need to rename the columns to better reflect what they represent. We can use the pandas.DataFrame.rename() method on dataframes to accomplish this.

The next six columns ask the respondent to rank the Star Wars movies in order of least favorite to most favorite. 1 means the film was the most favorite, and 6 means it was the least favorite. Each of the following columns can contain the value 1, 2, 3, 4, 5, 6, or NaN. Fortunately, these columns don't require a lot of cleanup. We'll need to convert each column to a numeric type, though, then rename the columns so that we can tell what they represent more easily.We can do the numeric conversion with the pandas.DataFrame.astype() method on dataframes.














