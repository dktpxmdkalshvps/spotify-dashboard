import streamlit as st
from src.auth import get_spotify_client
from src.fetcher import fetch_recently_played
from src.processor import (
    to_dataframe, enrich_dataframe,
    get_top_artists, get_listening_by_hour, get_summary_stats
)
from src.visualizer import (
    artist_bar, pop_tier_donut, hourly_bar,
    popularity_histogram, time_slot_bar
)

st.set_page_config(page_title="🎵 Spotify 자아 성찰", page_icon="🎵", layout="wide")
st.title("🎵 나의 음악 취향 분석 대시보드")

@st.cache_resource
def load_client():
    return get_spotify_client()

@st.cache_data(ttl=60)
def load_data():
    sp = load_client()
    raw = fetch_recently_played(sp, limit=50)
    df  = to_dataframe(raw)
    df  = enrich_dataframe(df)
    return df

with st.spinner("Spotify 데이터 불러오는 중..."):
    df = load_data()

# KPI 카드
stats = get_summary_stats(df)
cols = st.columns(len(stats))
for col, (label, value) in zip(cols, stats.items()):
    col.metric(label, value)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(artist_bar(get_top_artists(df)), use_container_width=True)
with col2:
    st.plotly_chart(pop_tier_donut(df), use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(hourly_bar(get_listening_by_hour(df)), use_container_width=True)
with col4:
    st.plotly_chart(popularity_histogram(df), use_container_width=True)

st.plotly_chart(time_slot_bar(df), use_container_width=True)

with st.expander("📋 최근 재생 목록 전체 보기"):
    st.dataframe(
        df[["played_at", "track_name", "artist", "track_popularity", "time_slot", "pop_tier"]]
        .sort_values("played_at", ascending=False),
        use_container_width=True, hide_index=True,
    )

if st.button("🔄 새로고침"):
    st.cache_data.clear()
    st.rerun()