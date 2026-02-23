import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def artist_bar(artist_df: pd.DataFrame) -> go.Figure:
    return px.bar(
        artist_df, x="count", y="artist", orientation="h",
        title="🎤 많이 들은 아티스트 Top 10",
        color="count", color_continuous_scale="Purples",
        labels={"count": "재생 횟수", "artist": "아티스트"},
    ).update_layout(yaxis={"categoryorder": "total ascending"}, showlegend=False)

def pop_tier_donut(df: pd.DataFrame) -> go.Figure:
    counts = df["pop_tier"].value_counts().reset_index()
    counts.columns = ["tier", "count"]
    return px.pie(
        counts, names="tier", values="count",
        title="💎 인기도 티어 분포", hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )

def hourly_bar(hourly_df: pd.DataFrame) -> go.Figure:
    fig = px.bar(
        hourly_df, x="hour", y="count",
        title="🕐 시간대별 청취 패턴",
        labels={"hour": "시간 (0~23시)", "count": "재생 횟수"},
        color="count", color_continuous_scale="Blues",
    )
    fig.update_xaxes(dtick=1)
    return fig

def popularity_histogram(df: pd.DataFrame) -> go.Figure:
    return px.histogram(
        df, x="track_popularity", nbins=20,
        title="📊 트랙 인기도 분포",
        labels={"track_popularity": "인기도 (0~100)"},
        color_discrete_sequence=["mediumpurple"],
    )

def time_slot_bar(df: pd.DataFrame) -> go.Figure:
    order = ["🌅 오전", "☀️ 오후", "🌆 저녁", "🌙 새벽"]
    counts = df["time_slot"].value_counts().reindex(order).reset_index()
    counts.columns = ["time_slot", "count"]
    return px.bar(
        counts, x="time_slot", y="count",
        title="⏰ 시간대별 청취 비중",
        color="time_slot",
        color_discrete_sequence=px.colors.qualitative.Pastel,
    ).update_layout(showlegend=False)