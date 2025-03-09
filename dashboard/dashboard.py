import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

sns.set(style='dark')

# Load dataset
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "day_df.csv"))

# Konversi kolom tanggal
df['dteday'] = pd.to_datetime(df['dteday'])

# Streamlit app
st.title("Dashboard Analisis Penyewaan Sepeda")

# Analisis 1: Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda
st.header("Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda")
weather_rental_avg = df.groupby("weathersit")["cnt"].mean().reset_index()
st.write(weather_rental_avg)

fig, ax = plt.subplots()
sns.barplot(x="weathersit", y="cnt", data=weather_rental_avg, color='#70a6b3', ax=ax)
ax.set_title("Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda")
ax.set_xlabel("Kategori Cuaca (weathersit)")
ax.set_ylabel("Rata-rata Jumlah Penyewaan Sepeda (cnt)")
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(["Cerah", "Berawan", "Hujan Ringan", "Hujan Deras"], rotation=45)
ax.grid(axis="y", linestyle="--")
st.pyplot(fig)

# Analisis 2: Perbandingan Penyewaan antara Registered dan Casual Users
st.header("Perbandingan Penyewaan Sepeda antara Registered dan Casual Users")
workingday_rental_avg = df.groupby("workingday")[["registered", "casual"]].mean()
workingday_rental_avg.index = ["Weekend/Holiday", "Working Day"]
st.write(workingday_rental_avg)

fig, ax = plt.subplots()
workingday_rental_avg.plot(kind="bar", stacked=False, colormap="tab10", width=0.7, ax=ax)
ax.set_title("Perbandingan Penyewaan Sepeda antara Registered dan Casual Users")
ax.set_xlabel("Hari")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
ax.set_xticklabels(["Weekend/Holiday", "Working Day"], rotation=0)
ax.legend(title="Tipe Pengguna")
ax.grid(axis="y", linestyle="--")
st.pyplot(fig)

# Analisis 3: Distribusi Penyewaan Berdasarkan Musim
st.header("Distribusi Penyewaan Sepeda Berdasarkan Musim")
season_labels = ["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"]
df["season_category"] = df["season"].map(dict(zip(range(1, 5), season_labels)))
season_distribution = df["season_category"].value_counts().sort_index()
st.write(season_distribution)

fig, ax = plt.subplots()
season_distribution.plot(kind="bar", colormap="tab10", ax=ax)
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Hari")
ax.set_xticklabels(season_labels, rotation=0)
ax.grid(axis='y', linestyle='--')
st.pyplot(fig)
