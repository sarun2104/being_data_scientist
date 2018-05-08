Project: Winning Jeopardy

Jeopardy is a popular TV show in the US where participants answer questions to win money. It's been running for a few decades, and is a major force in popular culture.

In this project, I worked with a dataset of Jeopardy questions to figure out some patterns in the questions. The dataset is named jeopardy.csv, and contains 20000 rows from the beginning of a full dataset of Jeopardy questions.

Before doing analysis on the Jeopardy questions, there is a need to normalize all of the text columns (the Question and Answer columns). The idea is to ensure that lowercase words and uppercase words are treated equally when compared. The Value column should also be numeric, to allow us to manipulate it more easily. There is also a need to remove the dollar sign from the beginning of each value and convert the column from text to numeric. The Air Date column should also be a datetime, not a string.

In order to figure out whether to study past questions, study general knowledge, or not study it all, it would be helpful to figure out two things:
	1. How often the answer is deducible from the question.
	2. How often new questions are repeats of older questions.

Later I investigated how often new questions are repeats of older ones. The iterrows Dataframe method was used to loop through each row of jeopardy.

Next aim was to study questions that pertain to high value questions instead of low value questions. This will help to earn more money when on Jeopardy. A chi-squared test was actually used to figure out which terms correspond to high-value questions.
