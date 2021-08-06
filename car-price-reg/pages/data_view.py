# importing required modules
import pandas as pd
import streamlit as st


def app(data_df):
    st.header("View Data")
    with st.beta_expander("View raw Data"):
        st.table(data_df)

    st.subheader("Description")
    if st.checkbox("Show Summary"):
        st.table(data_df.describe())

    beta_col1, beta_col2, beta_col3 = st.beta_columns(3)

    with beta_col1:
        if st.checkbox("Show all column names"):
            st.table(list(data_df.columns))

    with beta_col2:
        if st.checkbox("View column datatype"):
            st.table(pd.Series(data_df.dtypes.astype(str)))

    with beta_col3:
        if st.checkbox("View column data"):
            col = st.selectbox("Select column", tuple(data_df.columns))
            st.table(data_df[col])
