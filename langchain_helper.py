import os
from langchain_community.tools.google_lens import GoogleLensQueryRun
from langchain_community.utilities.google_lens import GoogleLensAPIWrapper


os.environ["SERPAPI_API_KEY"] = os.getenv("SERP_API_KEY")


def get_image_data(img):
    tool = GoogleLensQueryRun(api_wrapper=GoogleLensAPIWrapper())
    answer = tool.run(img)
    return answer
