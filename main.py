import os
from dotenv import load_dotenv
from langchain_community.tools.google_lens import GoogleLensQueryRun
from langchain_community.utilities.google_lens import GoogleLensAPIWrapper

load_dotenv()

os.environ["SERPAPI_API_KEY"] = os.getenv("SERP_API_KEY")
tool = GoogleLensQueryRun(api_wrapper=GoogleLensAPIWrapper())

try:
    # Copy Image Address
    answer = tool.run("https://i.imgur.com/HBrB8p0.png")
    print(answer)

except Exception as e:
    print(e)
