# Visualizing a Categorical and a Quantitative Variable
# Categorical variables are present in nearly every dataset, but they are especially prominent in survey data. In this chapter, you will learn how to create and customize categorical plots such as box plots, bar plots, count plots, and point plots. Along the way, you will explore survey data from young people about their interests, students about their study habits, and adult men about their feelings about masculinity.

# Count plots
# In this exercise, we'll return to exploring our dataset that contains the responses to a survey sent out to young people. We might suspect that young people spend a lot of time on the internet, but how much do they report using the internet each day? Let's use a count plot to break down the number of survey responses in each category and then explore whether it changes based on age.

# As a reminder, to create a count plot, we'll use the catplot() function and specify the name of the categorical variable to count(x=____), the Pandas DataFrame to use(data=____), and the type of plot(kind="count").

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
# Create count plot of internet usage
sns.catplot(x='Internet usage', data=survey_data, kind='count')


# Show plot
plt.show()

# Bar plots with percentages
# Let's continue exploring the responses to a survey sent out to young people. The variable "Interested in Math" is True if the person reported being interested or very interested in mathematics, and False otherwise. What percentage of young people report being interested in math, and does this vary based on gender? Let's use a bar plot to find out.

# As a reminder, we'll create a bar plot using the catplot() function, providing the name of categorical variable to put on the x-axis(x=____), the name of the quantitative variable to summarize on the y-axis(y=____), the Pandas DataFrame to use(data=____), and the type of categorical plot(kind="bar").

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y='Interested in Math', data=survey_data, kind='bar')


# Show plot
plt.show()

# Customizing bar plots
# In this exercise, we'll explore data from students in secondary school. The "study_time" variable records each student's reported weekly study time as one of the following categories: "<2 hours", "2 to 5 hours", "5 to 10 hours", or ">10 hours". Do students who report higher amounts of studying tend to get better final grades? Let's compare the average final grade among students in each category using a bar plot.

# Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
