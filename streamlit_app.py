#기본적인 Streamlit 페이지 예제

# streamlit_app.py
import streamlit as st
import pandas as pd

# 1. 제목
st.title("손예소의 스트림릿 서비스")

# 2. 부제목
st.subheader("암세포의 진행단계에 따른 분류 서비스")

# 3. 판다스 데이터프레임 기반 표 출력
df = pd.DataFrame({
    "세포 종류": ["정상세포", "초기 암세포" , "말기 암세포"],
   
st.write("데이터프레임 예제")
st.dataframe(df)

# 4. HTML 활용 예제
st.write("HTML 예제")
st.markdown(
    """
    <div style="color: blue; font-size: 20px;">
        HTML을 활용한 예시 텍스트입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 5. HTML과 CSS 활용 예제
st.write("HTML과 CSS 예제")
st.markdown(
    """
    <style>
    .styled-box {
        padding: 10px;
        margin: 5px;
        background-color: lightgreen;
        border-radius: 5px;
        color: darkgreen;
    }
    </style>
    <div class="styled-box">
        HTML과 CSS를 함께 사용하여 스타일링한 박스입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 6. 이미지 표시
st.write("이미지 표시 예제")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBarulKtcWODPEx71P1EesgV6_AHm5WMDVMg&s", caption="Streamlit 로고")
st.image("https://cdn.mkhealth.co.kr/news/photo/202004/img_MKH200402006_0.jpg", caption="Streamlit 로고")
st.image("https://cdn.newsworks.co.kr/news/thumbnail/201712/158103_49597_3642_v150.jpg", caption="Streamlit 로고")

# 7. 유튜브 링크 (썸네일 표시)
st.write("유튜브 동영상 예제")
st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")
