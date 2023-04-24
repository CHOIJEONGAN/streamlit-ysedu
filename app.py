# -*- coding:UTF-8 -*-
import streamlit as st

def main():
    st.title("Hello World")

if __name__ == '__main__':
    main()
    # title
    st.title("Hello World")

    #text
    st.text('This is so {}'.format("good"))

    #Header
    st.header("This is Header")

    #Subheader
    st.subheader('This is subHeader')

    #markdown
    st.markdown('## This is Markdown')
    
    #색상이 들어간 텍스트
    st.success('성공')
    st.warning('경고')
    st.info('정보 관련 탭')
    st.error('에러')
    st.exception('예외처리')

    #st.write()를 눈여겨 볼 것
    st.write('일반 텍스트')
    st.write(1+2)
    st.write(dir(str))

    st.title(':heart:')

    #help
    st.help(range)
    st.help(st.title)