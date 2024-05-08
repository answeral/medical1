import pandas as pd
df = pd.read_excel('scroe.xlsx',index_col='지원번호')


df.head() # 상단 5개 확인
df.tail() # 하단 5개 확인
df.info() # 컬럼별 타입, 크기 정보
df.values # rows 데이터 배열로 출력
df.index # index 정보
df.columns # 컬럼 정보
df.shape # 데이터 크기 정보 (8,9) (row, 컬럼)
df.describe() # 컬럼별 대략적인 정보, 최소값, 최대값, 평균, 분산, % 등 확인

df['키']
df['이름']
df[['이름','키']]

df['키'].nlargest(3) # 큰 순서대로
df['키'].nsmallest(4) #작은 순서대로 
df['키'].max()
df['키'].min()
df['키'].mean()
df['키'].count()
df['키'].describe()
df['키'].info()
df['SW특기'].count() # Nan데이터는 개수에 들어가지 않음.
df['국어'].sum()