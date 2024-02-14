import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

    'Done!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ内容を書く')


#text = st.text_input('貴方の趣味を教えてください。')
#condition = st.slider('貴方の今の調子は？',0, 100)

#'あなたの趣味は、', text, 'です。'
#'コンディション：', condition


#if st.checkbox('Show Image'):
    #img = Image.open('sample.jpeg')
    #st.image(img, caption='Keigo Oka', use_column_width=True)



#st.table(df.style.highlight_max(axis=1))





