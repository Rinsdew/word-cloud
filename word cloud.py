import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Sample text
text = """
ı love new york city
"""

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud Example", fontsize=20)
plt.show()
#To run this code, you'll need to have the matplotlib and wordcloud libraries installed. You can install them using pip: pip install matplotlib wordcloud
