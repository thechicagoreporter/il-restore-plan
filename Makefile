DOWNLOAD_URL = https://docs.google.com/spreadsheets/d/e/2PACX-1vTQAqt1jRmAxZ4yf6BltBFc9UWdueHDpmszjfQFVrQbT2SVPMX13mIjD-f_sAg1CSa5JNFF9TIAUpwe/pub\?gid\=535175200\&single\=true\&output\=csv


data/external/data.csv:
	curl -o $@ $(DOWNLOAD_URL)