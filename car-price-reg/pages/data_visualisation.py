# importing required modules
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def app(data_df):
    df = data_df
    st.header("Data Visualisation")
    side, main = st.beta_columns(2)
    st.set_option("deprecation.showPyplotGlobalUse", False)
    with side:
        input_data = {}
        plots = st.multiselect(
            "Selct th plot through which you want to visualise",
            ("Scatter Plot", "Histogram", "Box plot", "Correlation Heatmap"))
        if "Scatter Plot" in plots:
            st.subheader("Scatter Plot")
            input_data["Scatter X"] = st.multiselect(
                "Select features for Scatter Plot for X-axis",
                tuple(df.columns),
                key="X Scatter")

            input_data["Scatter Y"] = st.multiselect(
                "Select features for Scatter Plot for Y-axis",
                tuple(df.columns),
                default="price",
                key="Y Scatter")

        if "Histogram" in plots:
            st.subheader("Histogram")
            input_data["Hist"] = st.multiselect(
                "Select features for Histogram for X-axis",
                tuple(df.columns),
                key="X hist")

        if "Box plot" in plots:
            st.subheader("Box Plot")
            input_data["Box"] = st.multiselect(
                "Select features for Box plot for X-axis",
                tuple(df.columns),
                key="X zbox")

        if "Correlation Heatmap" in plots:
            st.subheader("Correlation Heatmap")
            input_data["Heat"] = st.multiselect(
                "Select features for Correlation Heatmap for X-axis",
                tuple(df.columns),
                key="X corr heat")

    if "Scatter Plot" in plots:

        for X in input_data["Scatter X"]:
            for Y in input_data["Scatter Y"]:
                st.subheader(f"Scatter plot between {X} and {Y}".title())
                plt.figure(figsize=(20, 5))
                sns.scatterplot(x=X, y=Y, data=df)
                st.pyplot()

    if "Histogram" in plots:

        for X in input_data["Hist"]:
            st.subheader(f"Histogram for {X}".title())
            plt.figure(figsize=(20, 5))
            sns.distplot(df[X],
                         bins="sturges",
                         kde=st.checkbox("KDE"),
                         hist=st.checkbox("Histogram", value=True))
            st.pyplot()

    if "Box plot" in plots:
        for X in input_data["Box"]:
            st.subheader(f"Box plot for {X}".title())
            plt.figure(figsize=(20, 5))
            sns.boxplot(x=X, data=df)
            st.pyplot()

    if "Correlation Heatmap" in plots:
        st.subheader(f"Heat map".title())
        plt.figure(figsize=(20, 5))
        sns.heatmap(df[input_data["Heat"]].corr(), annot=True)
        st.pyplot()
