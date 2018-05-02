Project: Visualizing Earnings Based On College Majors

The dataset is on the job outcomes of students who graduated from college between 2010 and 2012.

Each row in the dataset represents a different major in college and contains information on gender diversity, employment rates, median salaries, and more. Here are some of the columns in the dataset:
	1. Rank - Rank by median earnings (the dataset is ordered by this column).
	2. Major_code - Major code.
	3. Major - Major description.
	4. Major_category - Category of major.
	5. Total - Total number of people with major.
	6. Sample_size - Sample size (unweighted) of full-time.
	7. Men - Male graduates.
	8. Women - Female graduates.
	9. ShareWomen - Women as share of total.
	10. Employed - Number employed.
	11. Median - Median salary of full-time, year-round workers.
	12. Low_wage_jobs - Number in low-wage service jobs.
	13. Full_time - Number employed 35 hours or more.
	14. Part_time - Number employed less than 35 hours.


Using visualizations, we can start to explore questions from the dataset like:
	1. Do students in more popular majors make more money? - Using scatter plots
	2. How many majors are predominantly male? Predominantly female? - Using histograms
	3. Which category of majors have the most students? - Using bar plots

Most of the plotting functionality in pandas is contained within the DataFrame.plot()method. When we call this method, we specify the data we want plotted as well as the type of plot. We use the kind parameter to specify the type of plot we want. We use x and y to specify the data we want on each axis.

