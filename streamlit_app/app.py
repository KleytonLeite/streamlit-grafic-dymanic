import streamlit as st
import pandas as pd

def main():
    st.title('Gerador de Gráficos Dinâmico')

    # Upload do arquivo
    uploaded_file = st.file_uploader("Escolha um arquivo CSV ou Excel", type=["csv", "xls", "xlsx"])
    
    if uploaded_file is not None:
        # Carregar o arquivo dependendo do tipo
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)
            
            st.write("Arquivo carregado com sucesso!")
            st.write(data)
            
            # Selecionar colunas para os eixos X e Y
            x_axis = st.selectbox('Selecione a coluna para o eixo X', data.columns)
            y_axis = st.selectbox('Selecione a coluna para o eixo Y', data.columns)
            
            # Selecionar tipo de gráfico
            chart_type = st.selectbox('Selecione o tipo de gráfico', ['Line Chart', 'Bar Chart', 'Area Chart', 'Scatter Plot', 'Histogram'])
            
            # Gerar o gráfico conforme o tipo selecionado
            if st.button('Gerar Gráfico'):
                if chart_type == 'Line Chart':
                    st.line_chart(data.set_index(x_axis)[y_axis])
                elif chart_type == 'Bar Chart':
                    st.bar_chart(data.set_index(x_axis)[y_axis])
                elif chart_type == 'Area Chart':
                    st.area_chart(data.set_index(x_axis)[y_axis])
                elif chart_type == 'Scatter Plot':
                    st.write("Scatter Plot")
                    st.altair_chart(alt.Chart(data).mark_circle().encode(
                        x=x_axis,
                        y=y_axis
                    ).interactive())
                elif chart_type == 'Histogram':
                    st.write("Histogram")
                    st.bar_chart(data[y_axis].value_counts())
                else:
                    st.error("Tipo de gráfico inválido")

        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {e}")

if __name__ == "__main__":
    main()
