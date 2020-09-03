# In this final chapter, you will learn how to add informative plot titles and axis labels, which are one of the most important parts of any data visualization! You will also learn how to customize the style of your visualizations in order to more quickly orient your audience to the key takeaways. Then, you will put everything you have learned together for the final exercises of the course!

# Changing style and palette
# Let's return to our dataset containing the results of a survey given to young people about their habits and preferences. We've provided the code to create a count plot of their responses to the question "How often do you listen to your parents' advice?". Now let's change the style and palette to make this plot easier to interpret.

# We've already imported Seaborn as sns and matplotlib.pyplot as plt.

# Set the style to "whitegrid"
sns.set_style('whitegrid')

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes",
                  "Often", "Always"]

sns.catplot(x="Parents Advice",
            data=survey_data,
            kind="count",
            order=category_order)

# Show plot
plt.show()

# Changing the scale
# In this exercise, we'll continue to look at the dataset containing responses from a survey of young people. Does the percentage of people reporting that they feel lonely vary depending on how many siblings they have? Let's find out using a bar plot, while also exploring Seaborn's four different plot scales("contexts").

# We've already imported Seaborn as sns and matplotlib.pyplot as plt.

# Set the context to "paper"
sns.set_context('paper')

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()
