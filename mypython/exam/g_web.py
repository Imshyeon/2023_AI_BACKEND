from wordcloud import WordCloud
import matplotlib.pyplot as plt


def create_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')   # 대상을 차트로 표시
    plt.axis('off')
    plt.show() #차트를 실행시킨다.

if __name__ == '__main__':
    #문장 또는 파일의 대상을 읽어서 가장 빈번한 단어를 구름으로 표시하고 구름  텍스트 크기는 그 빈도수에 해당한다.
    example_text = """
    Word clouds are a popular way to visualize the most frequent words in a text. 
    They are often used for text analysis and data visualization purposes. 
    The size of each word in the cloud corresponds to its frequency in the text.
    """


    create_word_cloud(example_text)