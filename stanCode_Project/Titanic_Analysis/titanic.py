import pandas as pd
import matplotlib.pyplot as plt


def main():
	filepath = 'titanic_data/train.csv'
	data = pd.read_csv(filepath)
	print(data)
	print(data.count())

	plt.figure(figsize=(18, 7))
# ######
# 	normalize => 除總數
	plt.subplot2grid((3, 4), (0, 0))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar', color='#fb8500')
	plt.title('Survived')

	plt.subplot2grid((3, 4), (0, 1))
	data.Survived.value_counts().plot(kind='bar', color='#f4a261')
	plt.title('Pclass')

	plt.subplot2grid((3, 4), (0, 2))
	data.Sex.value_counts().plot(kind='bar', color='#e9c46a')
	plt.title('Sex')

	# plt.subplot2grid((3, 1), (1, 0))
	# data.Age.value_counts(normalize=True).sort_index().plot(kind='bar', color='#2a9d8f')
	# plt.title('Age')

	plt.subplot2grid((3, 4), (2, 0))
	data.Survived[data.Sex == 'female'].value_counts(normalize=True).sort_index().plot(kind='bar', color='#264653')
	plt.title('Female Survived')

	plt.subplot2grid((3, 4), (2, 1))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='#a3b18a')
	plt.title('Male Survived')

	plt.subplot2grid((3, 4), (2, 2))
	data.Survived[data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar', color='#3a5a40')
	plt.title('Pclass3 Survived')

	plt.subplot2grid((3, 4), (2, 3))
	data.Survived[data.Sex == 'male'][data.Pclass == 1].value_counts(normalize=True).sort_index()\
		.plot(kind='bar', color='#dad7cd')
	plt.title('Rich Male Survived')
	######
	plt.show()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
