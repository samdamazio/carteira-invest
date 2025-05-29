Always show details

Copy
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import seaborn as sns
import ace_tools as tools

# Dados baseados nos cartões manuscritos do Sam

# Composição geral da carteira
carteira = {
    "Ações BR": 20,
    "ETFs Exterior": 20,
    "Renda Fixa (BR)": 20,
    "FIIs/REITs": 15,
    "Ações Exterior": 5,
    "Reserva de valor (Ouro/Cripto)": 5,
    "Reserva de oportunidade (Selic)": 5,
    "Reserva de emergência (R$)": 0  # Fora do percentual
}

# Subdivisão dos ETFs
etfs = {
    "Ações globais (VT/ACWI)": 8,
    "Tech (QQQ/ARKK)": 4,
    "Emergentes (VWO/IEMG)": 3,
    "Setores Saúde/Educação (XLV/KLE)": 2,
    "Renda Fixa em dólar (BND/TLT)": 3
}

# Subdivisão dos FIIs/REITs
fiis = {
    "FIIs Papel (KNCR11, IRDM11, MXRF11)": 4.5,
    "FIIs Tijolo (HGLG11, XPLG11, VISC11)": 4.5,
    "FIIs Híbridos e FI Agro": 3,
    "REITs (VNQ, REET, SCHH)": 3
}

# Subdivisão da Renda Fixa
renda_fixa = {
    "Tesouro IPCA+": 8,
    "Prefixado": 4,
    "CDB/LCI/LCA": 4,
    "Tesouro Selic": 4
}

# Criar DataFrames para exibir
df_geral = pd.DataFrame(list(carteira.items()), columns=["Categoria", "Porcentagem"])
df_etfs = pd.DataFrame(list(etfs.items()), columns=["ETF", "Peso % na carteira"])
df_fiis = pd.DataFrame(list(fiis.items()), columns=["FIIs/REITs", "Peso % na carteira"])
df_rf = pd.DataFrame(list(renda_fixa.items()), columns=["Renda Fixa (BR)", "Peso % na carteira"])

# Exibir as tabelas organizadas
tools.display_dataframe_to_user(name="Distribuição Geral da Carteira", dataframe=df_geral)
tools.display_dataframe_to_user(name="Composição dos ETFs no Exterior", dataframe=df_etfs)
tools.display_dataframe_to_user(name="Composição de FIIs e REITs", dataframe=df_fiis)
tools.display_dataframe_to_user(name="Composição da Renda Fixa (BR)", dataframe=df_rf)
