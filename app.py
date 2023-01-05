import streamlit as st
import pandas as pd
from problem import CarGroupProblem
# タイトル
st.title('学生の乗車グループ分け問題')
# ファイルのアップロード
st.text('学生データ')
students_data = st.file_uploader("choose students data")
st.text('車データ')
cars_data = st.file_uploader("choose cars data")

# ボタンが押された際に最適化を実行
if st.button('最適化を実行'):
    st.header('最適化結果')
    # 前処理（データ読み込み）
    students_df, cars_df = pd.read_csv(students_data), pd.read_csv(cars_data)
    # 最適化実行
    solution_df = CarGroupProblem(students_df, cars_df).solve()
    st.dataframe(solution_df)
    # ダウンロードボタン
    st.download_button('ダウンロード', data=solution_df.to_csv(),
                       file_name='solution.csv')
