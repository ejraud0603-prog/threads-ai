import streamlit as st
import google.generativeai as genai
from PIL import Image

# 앱 디자인 설정
st.set_page_config(page_title="스레드 홍보글 생성기", page_icon="📸", layout="wide")
st.title("📸 스레드 홍보글 자동 생성기")
st.markdown("상품 사진을 업로드하고 버튼을 누르면 스레드 게시물이 뚝딱 만들어집니다.")

# API 키 설정 (왼쪽 사이드바)
api_key = st.sidebar.text_input("Google AI API Key 입력", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # 가장 안정적인 모델 사용
    model = genai.GenerativeModel('gemini-1.5-flash')

    uploaded_files = st.file_uploader("상품 사진 업로드", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])

    if uploaded_files and st.button("글 생성 시작하기"):
        with st.spinner("AI가 게시물을 작성 중입니다..."):
            try:
                images = [Image.open(f) for f in uploaded_files]
                prompt = """
                당신은 스레드 마케팅 전문가입니다. 사진을 보고 
                1. 시선을 끄는 후킹 문구
                2. 공감 가는 정보성 리뷰
                3. 자연스러운 구매 유도(구매 링크는 댓글)
                4. 적절한 해시태그 3개
                를 포함한 스레드 게시물을 작성해주세요.
                """
                response = model.generate_content([prompt] + images)
                st.subheader("📝 완성된 게시물")
                st.text_area("결과 복사하기", response.text, height=400)
            except Exception as e:
                st.error(f"오류: {e}")
else:
    st.info("왼쪽 사이드바에 API Key를 입력하면 시작할 수 있습니다.")
```

### 3단계: 저장하기 (가장 중요!)
1. 코드를 다 붙여넣었으면, 맨 아래로 쭉 내려가서 녹색 버튼 **`Commit changes...`**를 누르세요.
2. 조그만 창이 하나 뜨면, 그냥 고민하지 말고 아래에 있는 초록색 **`Commit changes`** 버튼을 한 번 더 누르세요.

**자, 이제 다 됐습니다!** 
이제 아까 말씀드린 대로 [Streamlit Cloud](https://share.streamlit.io/)에 접속해서 방금 만든 창고(`threads-ai`)를 선택하기만 하면 됩니다. 

거의 다 왔어요! 이 과정만 끝내면 정말로 앱이 만들어집니다. 여기까지 하고 저한테 알려주세요!
