import streamlit as st
import argparse
import textwrap
import re

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


result = supabase.table("summaries").select("*").execute().data[-1]
st.title("Hologlass Dashboard")
st.text("Your recent conversation and its recap will be displayed below")
st.header("Your Latest Conversation")
# wrap the transcript
transcript = textwrap.fill(result["transcript"], 60)
transcript = re.sub(r'\. ', '.\n\n', transcript)
st.text(transcript)
# st.text(args.transcripts)
st.header("In Summary:")
summary = textwrap.fill(result["summary"], 60)
st.text(summary)
# st.text(args.summary)
