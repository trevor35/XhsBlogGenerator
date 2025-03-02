# Title:
# 2025/2/28 21:43

from utils import get_XhsBlog
import streamlit as st

st.header("🔥爆款小红书AI写作助手")
with st.sidebar:
    api_key = st.text_input("🔑请输入DashScope API密钥：", type="password")
    st.markdown("[🔍获取DashScope API密钥](https://www.aliyun.com/product/bailian)")

theme = st.text_input("💡请输入小红书的写作主题")
submit = st.button("👉开始写作")

if submit and not api_key:
    st.info("请输入你的DashScope API密钥")
    st.stop()

if submit and not theme:
    st.info("请输入需要的小红书写作主题")
    st.stop()

if submit:
    with st.spinner("🚀AI正在努力创作中，请稍等。。。"):
        result = get_XhsBlog(theme, api_key)
    st.divider()
    left, right = st.columns(2)
    with left:
        st.markdown("##### ✨小红书标题1")
        st.write(result.titles[0])
        st.markdown("##### ✨小红书标题2")
        st.write(result.titles[1])
        st.markdown("##### ✨小红书标题3")
        st.write(result.titles[2])
        st.markdown("##### ✨小红书标题4")
        st.write(result.titles[3])
        st.markdown("##### ✨小红书标题5")
        st.write(result.titles[4])
    with right:
        st.markdown("##### 📕小红书正文")
        st.write(result.content)
