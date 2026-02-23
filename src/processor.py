import pandas as pd
from collections import Counter

def to_dataframe(raw: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(raw)
    df["played_at"]   = pd.to_datetime(df["played_at"])
    df["hour"]        = df["played_at"].dt.hour
    df["duration_min"]= (df["duration_ms"] / 60000).round(2)
    return df

def classify_time_slot(hour: int) -> str:
    if 5 <= hour < 12:   return "🌅 오전"
    elif 12 <= hour < 18: return "☀️ 오후"
    elif 18 <= hour < 23: return "🌆 저녁"
    else:                 return "🌙 새벽"

def classify_popularity(score: int) -> str:
    if score >= 70:   return "🔥 메가히트"
    elif score >= 40: return "🎵 일반곡"
    else:             return "💎 언더레이티드"

def enrich_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df["time_slot"]  = df["hour"].apply(classify_time_slot)
    df["pop_tier"]   = df["track_popularity"].apply(classify_popularity)
    return df

def get_top_artists(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    counts = df["artist"].value_counts().head(top_n).reset_index()
    counts.columns = ["artist", "count"]
    return counts

def get_listening_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("hour").size().reset_index(name="count")

def get_summary_stats(df: pd.DataFrame) -> dict:
    return {
        "🎵 총 재생 수":       len(df),
        "🎤 고유 아티스트":    df["artist"].nunique(),
        "💿 고유 트랙":        df["track_id"].nunique(),
        "⭐ 평균 인기도":      round(df["track_popularity"].mean(), 1),
        "⏱ 평균 재생시간(분)": round(df["duration_min"].mean(), 2),
    }