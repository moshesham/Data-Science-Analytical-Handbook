import os
from datetime import date, timedelta
from typing import Dict, Optional

import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf
from fredapi import Fred

# --- Constants and Configurations ---
EQUITY_MAPPING: Dict[str, str] = {
    "SPY": "S&P 500",
    "XLK": "Technology",
    "XLV": "Healthcare",
    "XLF": "Financials",
    "XLY": "Consumer Discretionary",
    "XLE": "Energy",
    "XLI": "Industrials",
    "XLB": "Materials",
    "XLU": "Utilities",
    "XLRE": "Real Estate",
    "XLP": "Consumer Staples",
    "XLC": "Communication Services",
}
COMMODITY_MAPPING: Dict[str, str] = {
    "CL=F": "Crude Oil",
    "GC=F": "Gold",
    "SI=F": "Silver",
    "HG=F": "Copper",
}
TREASURY_MAPPING: Dict[str, str] = {
    "^IRX": "13-Week Treasury",
    "^FVX": "5-Year Treasury",
    "^TNX": "10-Year Treasury",
    "^TYX": "30-Year Treasury",
}
FRED_SERIES: Dict[str, str] = {
    "FEDFUNDS": "Federal Funds Rate",
    "GDPC1": "Real GDP",
    "UNRATE": "Unemployment Rate",
    "CPIAUCSL": "CPI All Items",
    "CPILFESL": "Core CPI",
    "RSXFS": "Retail Sales",
    "HOUST": "Housing Starts",
    "UMCSENT": "Consumer Sentiment",
    "INDPRO": "Industrial Production",
    "PCE": "Personal Consumption",
    "M2": "M2 Money Supply",
}
MOVING_AVERAGE_OPTIONS: Dict[str, Optional[int]] = {
    "None": None,
    "50-Day": 50,
    "200-Day": 200,
}
FRED_API_KEY_NAME = "FRED_API_KEY"

# --- Data Fetching Functions ---  <---- fetch_market_data() and fetch_fred_data() DEFINITIONS RE-INSERTED


@st.cache_data(ttl="1h")
def fetch_market_data(
    tickers: Dict[str, str], start_date: str, end_date: str, use_adj_close: bool = False
) -> pd.DataFrame:  # <---- fetch_market_data() DEFINITION RE-INSERTED
    price_type = "Close"
    all_data = pd.DataFrame()
    for ticker, name in tickers.items():
        try:
            ticker_data = yf.download(
                ticker, start=start_date, end=end_date, progress=False
            )
            if not ticker_data.empty and price_type in ticker_data.columns:
                all_data[ticker] = ticker_data[price_type]
                st.session_state.api_error = None
                print(f"Fetched market data for {name} ({ticker}) - {price_type}")
            else:
                error_msg = (
                    f"No '{price_type}' data found for {name} ({ticker}) from yfinance."
                )
                st.warning(error_msg)
                print(
                    f"WARNING: {error_msg} Columns found: {ticker_data.columns if not ticker_data.empty else 'Empty DataFrame'}"
                )
        except Exception as e:
            error_msg = f"Error fetching {name} ({ticker}) from yfinance: {e}"
            st.error(error_msg)
            print(f"ERROR: {error_msg}")
            st.session_state.api_error = error_msg
            continue
    return all_data


@st.cache_data(ttl="24h")
def fetch_fred_data(
    series_dict: Dict[str, str], _fred: Optional[Fred], start_date: str, end_date: str
) -> pd.DataFrame:  # <---- fetch_fred_data() DEFINITION RE-INSERTED
    all_data = pd.DataFrame()
    if _fred is None:
        error_msg = "FRED API client not initialized. Check API key."
        st.error(error_msg)
        print(f"ERROR: {error_msg}")
        st.session_state.api_error = error_msg
        return pd.DataFrame()
    for series_id, name in series_dict.items():
        try:
            series_data = _fred.get_series(
                series_id, observation_start=start_date, observation_end=end_date
            )
            if not series_data.empty:
                all_data[series_id] = series_data
                print(f"Fetched FRED data for {name} ({series_id})")
                st.session_state.api_error = None
            else:
                error_msg = f"No data retrieved for FRED series {name} ({series_id})."
                st.warning(error_msg)
                print(f"WARNING: {error_msg}")
        except Exception as e:
            error_msg = f"Error fetching FRED series {name} ({series_id}): {e}"
            st.error(error_msg)
            print(f"ERROR: {error_msg}")
            st.session_state.api_error = error_msg
            continue
    return all_data


# --- Visualization Functions (Matplotlib) ---


def create_correlation_heatmap_mpl(
    data: pd.DataFrame, title: str = "Market Correlations"
) -> plt.Figure:
    """Creates correlation heatmap using Matplotlib."""
    fig, ax = plt.subplots(figsize=(8, 6))
    if data.empty or data.shape[1] < 2:
        return fig

    corr_matrix = data.corr()
    im = ax.imshow(corr_matrix, cmap="RdBu_r", interpolation="nearest")
    ax.set_xticks(np.arange(len(corr_matrix.columns)))
    ax.set_yticks(np.arange(len(corr_matrix.columns)))
    ax.set_xticklabels(corr_matrix.columns, rotation=45, ha="right")
    ax.set_yticklabels(corr_matrix.columns)

    ax.figure.colorbar(im, ax=ax)

    for i in range(len(corr_matrix.columns)):
        for j in range(len(corr_matrix.columns)):
            ax.text(
                j,
                i,
                f"{corr_matrix.iloc[i, j]:.2f}",
                ha="center",
                va="center",
                color="w",
                size="small",
            )

    ax.set_title(title)
    fig.tight_layout()
    return fig


def create_performance_chart_mpl(
    data: pd.DataFrame,
    title: str,
    display_mode: str = "normalized",
    is_fred_data: bool = False,
    moving_average_period: Optional[int] = None,
) -> plt.Figure:
    """Creates performance line chart using Matplotlib with corrected step chart style."""
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = list(matplotlib.colors.TABLEAU_COLORS.keys())

    if display_mode == "normalized":
        normalized_data = data.apply(
            lambda x: (x / x.iloc[0]) * 100 if not x.empty else x
        )
        y_label = "Normalized Value (100 = Start)"
        data_to_plot = normalized_data
    elif display_mode == "level":
        data_to_plot = data
        y_label = "Value (Level)"
    else:
        st.error(f"Invalid display_mode: {display_mode}. Using 'normalized'.")
        normalized_data = data.apply(
            lambda x: (x / x.iloc[0]) * 100 if not x.empty else x
        )
        y_label = "Normalized Value (100 = Start)"
        data_to_plot = normalized_data

    for i, column in enumerate(data_to_plot.columns):
        line_style = None  # Set line_style to None for default linear lines - UPDATED
        draw_style = (
            "steps-post" if is_fred_data and display_mode == "normalized" else "default"
        )  # Use drawstyle for step plots
        ax.plot(
            data_to_plot.index,
            data_to_plot[column],
            label=column,
            linestyle=line_style,
            color=colors[i % len(colors)],
            drawstyle=draw_style,
        )  # Use drawstyle here

    if moving_average_period and moving_average_period > 1:
        ma_data = data.rolling(window=moving_average_period).mean()
        ma_data_to_plot = ma_data.apply(
            lambda x: (x / x.iloc[moving_average_period - 1]) * 100
            if display_mode == "normalized"
            and moving_average_period - 1 < len(x)
            and not x.iloc[moving_average_period - 1] == 0
            else x
            if display_mode == "level"
            else x
        )
        for column in ma_data_to_plot.columns:
            ax.plot(
                ma_data_to_plot.index,
                ma_data_to_plot[column],
                label=f"{column} MA({moving_average_period})",
                linestyle="--",
                color=colors[i % len(colors)],
            )

    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel("Date")
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
    ax.grid(True)
    fig.tight_layout(rect=[0, 0, 0.85, 1.0])
    return fig


def create_sector_performance_bar_chart_mpl(
    data: pd.DataFrame, title: str, date_range_str: str
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 6))
    if data.empty or data.shape[1] < 2:
        return fig

    start_values = data.iloc[0]
    end_values = data.iloc[-1]
    performance_pct = ((end_values - start_values) / start_values) * 100
    performance_pct_sorted = performance_pct.sort_values(ascending=False)

    ax.bar(
        performance_pct_sorted.index,
        performance_pct_sorted.values,
        color=list(matplotlib.colors.TABLEAU_COLORS.keys()),
    )
    ax.set_ylabel("Period Performance (%)")
    ax.set_xlabel("Sector")
    ax.set_title(f"{title} - Performance over {date_range_str}")
    ax.tick_params(axis="x", rotation=45, ha="right")
    fig.tight_layout()
    return fig


def create_yoy_chart_mpl(data: pd.DataFrame, title: str) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 6))
    if data.empty:
        return fig
    yoy_data = data.pct_change(periods=12).dropna() * 100
    colors = list(matplotlib.colors.TABLEAU_COLORS.keys())

    for i, column in enumerate(yoy_data.columns):
        ax.plot(
            yoy_data.index,
            yoy_data[column],
            label=column,
            color=colors[i % len(colors)],
        )

    ax.set_title(title)
    ax.set_ylabel("YoY Change (%)")
    ax.set_xlabel("Date")
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
    ax.grid(True)
    fig.tight_layout(rect=[0, 0, 0.85, 1.0])
    return fig


def display_correlation_analysis(
    equity_data: pd.DataFrame,
    treasury_data: pd.DataFrame,
    commodity_data: pd.DataFrame,
    fred_data: pd.DataFrame,
) -> None:
    """Displays Cross-Asset Correlation Heatmap using Matplotlib."""
    st.header("Cross-Asset Correlations")
    if not all(
        df.empty for df in [equity_data, treasury_data, commodity_data, fred_data]
    ):
        all_data = pd.concat(
            [
                equity_data["SPY"]
                if not equity_data.empty and "SPY" in equity_data
                else pd.Series(),
                treasury_data["^TNX"]
                if not treasury_data.empty and "^TNX" in treasury_data
                else pd.Series(),
                commodity_data["CL=F"]
                if not commodity_data.empty and "CL=F" in commodity_data
                else pd.Series(),
                fred_data["CPIAUCSL"]
                if not fred_data.empty and "CPIAUCSL" in fred_data
                else pd.Series(),
            ],
            axis=1,
        ).dropna()
        if not all_data.empty and all_data.shape[1] > 1:
            fig = create_correlation_heatmap_mpl(
                all_data, title="Cross-Asset Correlation Heatmap"
            )
            st.pyplot(fig)
        else:
            st.warning("Insufficient data for correlation analysis.")
    else:
        st.warning("No data available for correlation analysis.")


def display_market_overview(
    equity_data: pd.DataFrame,
    treasury_data: pd.DataFrame,
    commodity_data: pd.DataFrame,
    fred_data: pd.DataFrame,
) -> None:
    st.header("Market Overview")
    col1, col2, col3, col4 = st.columns(4)

    def get_metric_value(
        df: pd.DataFrame, ticker: str, format_str: str = ".2f", percentage: bool = False
    ) -> str:
        if not df.empty and ticker in df.columns and not df[ticker].empty:
            value = df[ticker].iloc[-1]
            formatted_value = (
                f"{value:{format_str}}%" if percentage else f"{value:{format_str}}"
            )
            return formatted_value
        return "N/A"

    spx_last = get_metric_value(equity_data, "SPY")
    spx_return_pct = (
        get_metric_value(equity_data, "SPY", format_str=".1f", percentage=True)
        if not equity_data.empty
        and "SPY" in equity_data
        and len(equity_data["SPY"]) > 1
        else "N/A"
    )
    col1.metric(
        "S&P 500", spx_last, f"{spx_return_pct}" if spx_return_pct != "N/A" else "N/A"
    )

    treasury_10y_yield = get_metric_value(
        treasury_data, "^TNX", format_str=".2f", percentage=True
    )
    col2.metric(
        "10Y Treasury",
        f"{treasury_10y_yield}%" if treasury_10y_yield != "N/A" else "N/A",
    )

    oil_price = get_metric_value(commodity_data, "CL=F")
    oil_return_pct = (
        get_metric_value(commodity_data, "CL=F", format_str=".1f", percentage=True)
        if not commodity_data.empty
        and "CL=F" in commodity_data
        and len(commodity_data["CL=F"]) > 1
        else "N/A"
    )
    col3.metric(
        "Crude Oil",
        f"${oil_price}" if oil_price != "N/A" else "N/A",
        f"{oil_return_pct}" if oil_return_pct != "N/A" else "N/A",
    )

    unemployment_rate = get_metric_value(
        fred_data, "UNRATE", format_str=".1f", percentage=True
    )
    col4.metric(
        "Unemployment", f"{unemployment_rate}%" if unemployment_rate != "N/A" else "N/A"
    )


def display_market_performance_charts(
    equity_data: pd.DataFrame,
    treasury_data: pd.DataFrame,
    commodity_data: pd.DataFrame,
    fred_data: pd.DataFrame,
    display_mode_value: str,
    moving_average_period: Optional[int],
    date_range_str: str,
) -> None:
    st.header("Market Performance Charts")
    display_mode = st.radio(
        "Display Mode:",
        options=["Normalized (Rebased to 100)", "Level (Raw Values)"],
        index=0,
        horizontal=True,
        key="display_mode_radio",
    )
    display_mode_value = (
        "normalized" if display_mode == "Normalized (Rebased to 100)" else "level"
    )
    ma_option = st.selectbox(
        "Moving Average:",
        options=list(MOVING_AVERAGE_OPTIONS.keys()),
        index=0,
        key="ma_selectbox",
    )
    moving_average_period = MOVING_AVERAGE_OPTIONS[ma_option]

    tabs = st.tabs(
        [
            "Equities",
            "Fixed Income",
            "Commodities",
            "Economic Indicators",
            "Sector Ranking",
            "YoY Economic Indicators",
        ]
    )

    with tabs[0]:  # Equities - Matplotlib Line Chart
        if not equity_data.empty:
            fig = create_performance_chart_mpl(
                equity_data,
                "Equity Market Performance",
                display_mode=display_mode_value,
                moving_average_period=moving_average_period,
            )
            st.pyplot(fig)
        else:
            st.warning("No equity data available for the selected range.")

    with tabs[1]:  # Fixed Income - Matplotlib Line Chart
        if not treasury_data.empty:
            fig = create_performance_chart_mpl(
                treasury_data,
                "Treasury Yields",
                display_mode=display_mode_value,
                moving_average_period=moving_average_period,
            )
            st.pyplot(fig)
        else:
            st.warning("No treasury data available for the selected range.")

    with tabs[2]:  # Commodities - Matplotlib Line Chart
        if not commodity_data.empty:
            fig = create_performance_chart_mpl(
                commodity_data,
                "Commodity Performance",
                display_mode=display_mode_value,
                moving_average_period=moving_average_period,
            )
            st.pyplot(fig)
        else:
            st.warning("No commodity data available for the selected range.")

    with tabs[3]:  # Economic Indicators - Matplotlib Line Chart
        if not fred_data.empty:
            selected_indicators = st.multiselect(
                "Select Economic Indicators:",
                list(FRED_SERIES.keys()),
                default=["UNRATE", "CPIAUCSL", "GDPC1"],
            )
            valid_indicators = [
                indicator
                for indicator in selected_indicators
                if indicator in fred_data.columns
            ]
            if valid_indicators:
                indicator_data = fred_data[valid_indicators]
                fig = create_performance_chart_mpl(
                    indicator_data,
                    "Economic Indicators",
                    is_fred_data=True,
                    display_mode=display_mode_value,
                    moving_average_period=moving_average_period,
                )
                st.pyplot(fig)
            else:
                st.warning(
                    "None of the selected economic indicators were fetched from FRED."
                )
        else:
            st.warning("No economic indicator data available from FRED.")

    with tabs[4]:  # Sector Ranking - Matplotlib Bar Chart
        if not equity_data.empty:
            fig = create_sector_performance_bar_chart_mpl(
                equity_data, "Equity Sector Performance Ranking", date_range_str
            )
            st.pyplot(fig)
        else:
            st.warning("No equity data available to display sector ranking.")

    with tabs[5]:  # YoY Economic Indicators - Matplotlib Line Chart
        if not fred_data.empty:
            selected_indicators_yoy = st.multiselect(
                "Select Economic Indicators for YoY Chart:",
                list(FRED_SERIES.keys()),
                default=["CPIAUCSL", "GDPC1"],
                key="yoy_indicators_multiselect",
            )
            valid_indicators_yoy = [
                indicator
                for indicator in selected_indicators_yoy
                if indicator in fred_data.columns
            ]
            if valid_indicators_yoy:
                indicator_data_yoy = fred_data[valid_indicators_yoy]
                fig = create_yoy_chart_mpl(
                    indicator_data_yoy, "YoY Change in Economic Indicators"
                )
                st.pyplot(fig)
            else:
                st.warning(
                    "None of the selected economic indicators were fetched from FRED for YoY chart."
                )
        else:
            st.warning("No economic indicator data available from FRED for YoY chart.")


def main() -> (
    None
):  # <---- main() DEFINITION NOW *AFTER* display_correlation_analysis()
    st.set_page_config(
        page_title="Enhanced Economic Dashboard", page_icon="📊", layout="wide"
    )
    st.title("Enhanced Economic & Market Dashboard")
    st.markdown("---")

    if "api_error" not in st.session_state:
        st.session_state.api_error = None

    if st.session_state.api_error:
        st.error(st.session_state.api_error)

    fred = initialize_fred_api()

    # --- Sidebar for Settings ---
    with st.sidebar:
        st.header("Dashboard Settings")
        selected_range = st.selectbox(
            "Select Time Range:", options=list(preset_ranges.keys()), index=4
        )
        display_mode = st.radio(
            "Display Mode:",
            options=["Normalized (Rebased to 100)", "Level (Raw Values)"],
            index=0,
        )
        moving_average_option = st.selectbox(
            "Moving Average:", options=list(MOVING_AVERAGE_OPTIONS.keys()), index=0
        )

    display_mode_value = (
        "normalized" if display_mode == "Normalized (Rebased to 100)" else "level"
    )
    moving_average_period = MOVING_AVERAGE_OPTIONS[moving_average_option]
    end_date = date.today()
    start_date = end_date - timedelta(days=preset_ranges[selected_range])
    date_range_str = (
        f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    )

    st.write(f"Data from: {date_range_str}")

    with st.spinner("Fetching data..."):
        equity_data = fetch_market_data(
            EQUITY_MAPPING,
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
        )
        commodity_data = fetch_market_data(
            COMMODITY_MAPPING,
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
        )
        treasury_data = fetch_market_data(
            TREASURY_MAPPING,
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
        )
        fred_data = fetch_fred_data(
            FRED_SERIES,
            fred,
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
        )

    # --- Main Panel Display ---
    display_market_overview(equity_data, treasury_data, commodity_data, fred_data)
    display_market_performance_charts(
        equity_data,
        treasury_data,
        commodity_data,
        fred_data,
        display_mode_value,
        moving_average_period,
        date_range_str,
    )
    display_correlation_analysis(equity_data, treasury_data, commodity_data, fred_data)


def initialize_fred_api() -> Optional[Fred]:
    """Initializes the FRED API client using environment variable or Streamlit secrets.

    Returns None when an API key is not available or initialization fails.
    """
    api_key = os.environ.get(FRED_API_KEY_NAME)
    # fall back to Streamlit secrets if available
    try:
        if (
            not api_key
            and hasattr(st, "secrets")
            and isinstance(st.secrets, dict)
            and "FRED_API_KEY" in st.secrets
        ):
            api_key = st.secrets.get("FRED_API_KEY")
    except Exception:
        # st.secrets may not be available in some contexts
        pass

    if not api_key:
        st.warning(
            "FRED API key not found in environment or Streamlit secrets; FRED data will be skipped."
        )
        return None

    try:
        fred_client = Fred(api_key=api_key)
        return fred_client
    except Exception as e:
        st.error(f"Error initializing FRED API client: {e}")
        st.session_state.api_error = str(e)
        return None


preset_ranges = {
    "1M": 30,
    "3M": 90,
    "6M": 180,
    "YTD": (date.today() - date(date.today().year, 1, 1)).days,
    "1Y": 365,
    "2Y": 730,
    "2Y": 730,
}

if __name__ == "__main__":
    main()  # <---- main() CALL IS *AFTER* ITS DEFINITION
