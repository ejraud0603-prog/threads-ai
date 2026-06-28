import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# 앱 디자인 설정
st.set_page_config(page_title="스레드 홍보글 생성기", page_icon="📸", layout="wide")
st.title("📸 스레드 홍보글 자동 생성기")
st.markdown("상품 사진을 올리면 AI가 매력적인 스레드 글을 써줍니다.")

# API 키 설정
api_key = st.sidebar.text_input("Google AI API Key 입력", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        uploaded_files = st.file_uploader("상품 사진 업로드", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])

        if uploaded_files and st.button("글 생성 시작하기"):
            with st.spinner("AI가 게시물을 작성 중입니다..."):
                images = []
                for f in uploaded_files:
                    # 파일 데이터를 안전하게 바이트로 변환 후 PIL 이미지로 로드
                    bytes_data = f.getvalue()
                    images.append(Image.open(io.BytesIO(bytes_data)))
                
                prompt = """
                당신은 스레드 마케팅 전문가입니다. 제공된 사진을 분석하여 다음 내용을 포함한 매력적인 스레드 글을 작성하세요:
                1. 시선을 확 끄는 후킹 문구 (첫 줄 필수)
                2. 제품의 특징과 장점을 살린 공감 가는 정보성 리뷰
                3. 자연스러운 구매 유도 ("구매 링크는 댓글에 남겨둘게요!")
                4. 적절한 해시태그 3개
                """
                response = model.generate_content([prompt] + images)
                st.subheader("📝 완성된 게시물")
                st.text_area("결과 복사하기", response.text, height=400)
                
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")
        st.write("API 키가 올바른지 다시 한번 확인해주세요.")
else:
    st.info("왼쪽 사이드바에 API Key를 입력하면 시작할 수 있습니다.")
