import langchain_helper as lch
import streamlit as st

# 設置頁面配置
st.set_page_config(
    page_title="Pet Name Generator",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 主標題
st.title("🐾 Pet Name Generator")
st.markdown("---")

# 側邊欄
with st.sidebar:
    st.header("🔑 API Configuration")
    openai_api_key = st.text_input(
        label="OpenAI API Key",
        type="password",
        placeholder="sk-...",
        help="Enter your OpenAI API key to generate pet names"
    )
    
    # API Key 獲取連結
    st.markdown("""
    <div style='font-size: 0.8em; color: #666; margin-top: -10px; margin-bottom: 20px;'>
    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">Get an OpenAI API Key</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.header("📝 Pet Information")
    animal_type = st.selectbox(
        "What is your pet?", 
        ["Dog", "Cat", "Bird", "Rabbit", "Hamster"],
        help="Please select your pet type"
    )
    
    pet_color = st.text_input(
        label=f"What color is your {animal_type}?", 
        max_chars=15,
        placeholder="e.g., brown, white, black, etc.",
        help="Please describe your pet's main color"
    )
    
    # 生成按鈕
    generate_button = st.button(
        "🎯 Generate Names", 
        type="primary",
        use_container_width=True,
        disabled=not pet_color.strip() or not openai_api_key.strip()
    )

# 主內容區域
col1, col2 = st.columns([2, 1])

with col1:
    if generate_button and pet_color.strip() and openai_api_key.strip():
        with st.spinner("Generating names for your pet..."):
            pet_names = lch.generate_pet_name(animal_type, pet_color)
            
            pet_names = pet_names.strip()  # 清理前後的空白字符和斷行符號
            
        # 顯示結果
        st.success("✨ Here are some name suggestions for your pet:")
        st.markdown("---")
        
        # 美化顯示結果
        st.markdown(f"**Name suggestions for your {pet_color} {animal_type}:**")
        st.text_area(
            "Generated Names",
            value=pet_names,
            height=150,
            label_visibility="collapsed",
            key="generated_names_display"
        )
        
        # 重新生成按鈕
        if st.button("🔄 Regenerate", type="secondary"):
            st.rerun()
            
    elif generate_button and not pet_color.strip() and not openai_api_key.strip():
        st.warning("⚠️ Please enter your pet's color and OpenAI API key first!")
    elif generate_button and not pet_color.strip():
        st.warning("⚠️ Please enter your pet's color first!")
    
    else:
        # 初始狀態顯示
        st.info("👆 Please fill in your API key and pet information on the left, then click 'Generate Names' button")
        
        # 顯示示例
        with st.expander("💡 Usage Tips", expanded=False):
            st.markdown("""
            **How to use:**
            1. Enter your OpenAI API key on the left
            2. Select your pet type on the left
            2. Enter your pet's main color
            3. Click the 'Generate Names' button
            4. View AI-recommended pet names
            
            **Tips:**
            - Your API key is stored locally and not shared with anyone
            - The more specific the color description, the more fitting the names will be
            - Try different color descriptions to get more creative suggestions
            - If you're not satisfied with the results, click 'Regenerate'
            """)

with col2:
    # 顯示寵物圖標
    pet_emojis = {
        "Dog": "🐕",
        "Cat": "🐱", 
        "Bird": "🐦",
        "Rabbit": "🐰",
        "Hamster": "🐹"
    }
    
    st.markdown("### Your Pet")
    st.markdown(f"# {pet_emojis.get(animal_type, '🐾')}")
    st.markdown(f"**Type:** {animal_type}")
    if pet_color.strip():
        st.markdown(f"**Color:** {pet_color}")
    else:
        st.markdown("**Color:** Not specified")

# 頁腳
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "🐾 Powered by LangChain and OpenAI - Smart Pet Name Generator 🐾"
    "</div>", 
    unsafe_allow_html=True
)