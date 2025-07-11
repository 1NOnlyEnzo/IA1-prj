
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title(" Analyse des Prix des Logements en Californie")


df = pd.read_csv("housing.csv")


st.subheader(" Aperçu des donnees")
st.write(df.head())


st.subheader(" Statistiques descriptives")
st.write(df.describe())


numeric_df = df.select_dtypes(include='number')


st.write("**Medianes :**")
st.write(numeric_df.median())


st.write("**Variances :**")
st.write(numeric_df.var())


st.write("**Ecarts-types :**")
st.write(numeric_df.std())


st.subheader(" Distribution des prix des logements")
fig_price, ax_price = plt.subplots()
sns.histplot(df['median_house_value'], bins=50, kde=True, ax=ax_price, color='skyblue')
st.pyplot(fig_price)




st.subheader(" Distribution de l age des maisons")
fig_age, ax_age = plt.subplots()
sns.histplot(df['housing_median_age'], bins=50, kde=True, ax=ax_age, color='orange')
st.pyplot(fig_age)


st.subheader(" Distribution du nombre total de pieces")
fig_rooms, ax_rooms = plt.subplots()
sns.histplot(df['total_rooms'], bins=50, kde=True, ax=ax_rooms, color='purple')
st.pyplot(fig_rooms)



st.subheader(" Correlations entre caracteristiques et prix")
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)


st.subheader(" Prix par tranches de nombre de pieces (total_rooms)")

df["rooms_cat"] = pd.cut(df["total_rooms"], bins=5)

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.boxplot(x="rooms_cat", y="median_house_value", data=df, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)


st.header("Prix selon la proximité à l’océan")
fig3, ax3 = plt.subplots()
sns.boxplot(x='ocean_proximity', y='median_house_value', data=df, ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)


st.subheader("📊 Boxplot des prix selon l age des maisons")

df['age_cat'] = pd.cut(df['housing_median_age'], bins=5)
fig4, ax4 = plt.subplots(figsize=(12,6))
sns.boxplot(x='age_cat', y='median_house_value', data=df, ax=ax4)
st.pyplot(fig4)


st.header("Carte  des maisons")
st.map(df[['latitude', 'longitude']])



st.subheader("📑 Rapport Final")

st.write("""
**Objectif :**  
Analyser les facteurs qui influencent le prix des logements en Californie à partir d’un jeu de données, en utilisant une application Streamlit.

**Résultats :**  
Les facteurs qui influencent le plus les prix sont :
- Le revenu médian des habitants : plus il est élevé, plus les prix sont hauts.
- La localisation géographique : les maisons proches de l’océan et au sud-ouest coûtent plus cher.
- Le nombre total de pièces : influence légère, les grandes maisons sont un peu plus chères.
- L’âge des maisons : influence faible sur le prix.

**Recommandations :**
- Cibler les régions à revenu médian élevé.
- Mettre en avant les maisons situées près de l’océan.
- Valoriser les maisons avec un grand nombre de pièces.
- Ne pas trop se baser sur l’âge des maisons pour estimer le prix.

**Conclusion :**  
Le revenu médian et la localisation sont les deux facteurs principaux à considérer pour bien estimer et vendre un logement en Californie.
""")



