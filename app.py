import streamlit as st
import os
from google import genai
from google.genai import types

# Initialize Gemini client
@st.cache_resource
def get_gemini_client():
    """Initialize and cache the Gemini client"""
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        st.error("GEMINI_API_KEY environment variable is not set")
        st.stop()
    return genai.Client(api_key=api_key)

def generate_acrostic_poem(word: str, client) -> str:
    """Generate Korean acrostic poem using Gemini API"""
    try:
        # Create prompt for Korean acrostic poem generation
        prompt = f"""
한국어 N행시(삼행시, 사행시 등)를 만들어주세요.

주어진 단어: {word}

규칙:
1. 주어진 단어의 각 글자로 시작하는 행을 만들어주세요
2. 각 행은 의미가 있고 서로 연결되는 내용이어야 합니다
3. 자연스러운 한국어 표현을 사용해주세요
4. 시적이고 아름다운 표현을 사용해주세요

예시 형식:
ㄱ: (ㄱ으로 시작하는 행)
ㅏ: (ㅏ로 시작하는 행)
...

단어 "{word}"로 N행시를 만들어주세요:
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text if response.text else "시를 생성할 수 없습니다."

    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

def main():
    # App title and description
    st.title("🎭 한국어 N행시 생성기")
    st.markdown("**Gemini AI를 활용한 한국어 N행시(삼행시, 사행시 등) 자동 생성 도구**")
    
    # Initialize Gemini client
    client = get_gemini_client()
    
    # Input section
    st.header("단어 입력")
    
    # Text input for Korean word
    user_word = st.text_input(
        "N행시를 만들고 싶은 한국어 단어나 구문을 입력하세요:",
        placeholder="예: 사랑, 친구, 행복 등",
        help="한글 자모, 단어, 또는 짧은 구문을 입력할 수 있습니다."
    )
    
    # Generate button
    if st.button("N행시 생성하기", type="primary"):
        if not user_word.strip():
            st.warning("단어를 입력해주세요!")
            return
        
        # Validate Korean characters
        if not any('\uac00' <= char <= '\ud7af' or '\u3131' <= char <= '\u318e' for char in user_word):
            st.warning("한국어 단어를 입력해주세요!")
            return
            
        # Show loading spinner
        with st.spinner("N행시를 생성하고 있습니다... 잠시만 기다려주세요!"):
            # Generate acrostic poem
            poem = generate_acrostic_poem(user_word.strip(), client)
        
        # Display results
        st.header("생성된 N행시")
        
        # Create two columns for better layout
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.subheader("입력 단어")
            st.write(f"**{user_word.strip()}**")
            st.write(f"글자 수: {len(user_word.strip())}자")
        
        with col2:
            st.subheader("N행시 결과")
            # Display poem in a nice container
            st.markdown(f"""
            <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #ff6b6b;">
                <pre style="white-space: pre-wrap; font-family: 'Noto Sans KR', sans-serif; font-size: 16px; line-height: 1.6; margin: 0;">{poem}</pre>
            </div>
            """, unsafe_allow_html=True)
    
    # Instructions and examples
    st.header("사용 방법")
    with st.expander("N행시란?"):
        st.markdown("""
        **N행시**는 주어진 단어의 각 글자로 시작하는 문장이나 구절을 만들어 하나의 시를 완성하는 언어유희입니다.
        
        - **삼행시**: 3글자 단어로 만드는 시
        - **사행시**: 4글자 단어로 만드는 시
        - **오행시**: 5글자 단어로 만드는 시
        
        예시:
        ```
        사: 사랑하는 마음으로
        랑: 랑랑한 웃음소리가
        사: 사라지지 않길 바라며
        ```
        """)
    
    with st.expander("사용 팁"):
        st.markdown("""
        1. **한글 단어 입력**: 한국어 단어나 구문을 입력하세요
        2. **적당한 길이**: 2-6글자 정도가 가장 좋은 결과를 보여줍니다
        3. **의미있는 단어**: 구체적이고 의미가 있는 단어일수록 더 좋은 시가 생성됩니다
        4. **재생성**: 마음에 들지 않으면 같은 단어로 다시 생성해보세요
        """)

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666; font-size: 14px;'>"
        "💡 Powered by Google Gemini AI | Made with ❤️ using Streamlit"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
