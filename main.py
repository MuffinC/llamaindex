from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt,instruction_str

load_dotenv()


songs_path = os.path.join("data", "Popular_Spotify_Songs.csv")
songs_df = pd.read_csv(songs_path,encoding='latin-1')

song_query_engine = PandasQueryEngine(df=songs_df, verbose=True, instruction_str=instruction_str)
song_query_engine.update_prompts({"pandas_prompt":new_prompt})
song_query_engine.query("What is the most played song on spotify")