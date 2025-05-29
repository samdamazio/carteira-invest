with pd.ExcelWriter("/mnt/data/Carteira_Arvore_do_Cerrado.xlsx") as writer:
    df_geral.to_excel(writer, sheet_name="Carteira Geral", index=False)
    df_etfs.to_excel(writer, sheet_name="ETFs Exterior", index=False)
    df_fiis.to_excel(writer, sheet_name="FIIs e REITs", index=False)
    df_rf.to_excel(writer, sheet_name="Renda Fixa BR", index=False)

"/mnt/data/Carteira_Arvore_do_Cerrado.xlsx"
