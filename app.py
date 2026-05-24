import validators
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.summarize import load_summarize_chain  # ✅ fixed import

st.set_page_config(page_title="LangChain: Summarize Text From YouTube or Website", page_icon="🌐")
st.title("LangChain: Summarize Text From YouTube or Website")
st.subheader('Summarize URL')

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

if not groq_api_key:
    st.warning("Please enter your Groq API Key to access the application.")
    st.stop()

llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

prompt_template = """You are a helpful assistant that summarizes the content. 
Summarize the content in a concise manner, highlighting the key points and main ideas.
Content: {text}"""

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

combine_prompt_template = """
You are a helpful assistant that combines multiple summaries into one concise summary.
Combine the following summaries into a clear and concise final summary.

{text}"""  # ✅ fixed: must be {text}, not {doc_summaries}

combine_prompt = PromptTemplate(template=combine_prompt_template, input_variables=["text"])

generic_url = st.text_input("URL", label_visibility="collapsed")

if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")

    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YouTube video URL or a website URL")

    else:
        try:
            with st.spinner("Waiting..."):
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                        generic_url,
                        add_video_info=False  # ✅ avoids metadata fetch errors
                    )
                else:
                    loader = WebBaseLoader(
                        generic_url,
                        requests_kwargs={
                            "verify": False,
                            "headers": {
                                "User-Agent": "Mozilla/5.0"
                            }
                        }
                    )

                data = loader.load()

                if not data:
                    st.error("No content could be loaded from the URL. Try a different one.")
                    st.stop()

                # Smarter chunking
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
                docs = text_splitter.split_documents(data)

                chain = load_summarize_chain(
                        llm,                # used for map step
                        chain_type="map_reduce",
                        map_prompt=prompt,
                        combine_prompt=combine_prompt,
                        verbose=True
                    )
                    
                response = chain.invoke(docs)
                st.success(response["output_text"])   # ✅ extract the text field

        except Exception as e:
            st.exception(e)  # ✅ shows full traceback for easier debugging