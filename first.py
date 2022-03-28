import re

import requests
import matplotlib.pyplot as plt


api_url = 'https://api.v2.emissions-api.org/api/v2/carbonmonoxide/average.json?country=MK' \
          '&begin=2022-03-01&end=2022-03-28'

response = requests.get(api_url)

# print(response.status_code)

# print(response.headers)

response = response.json()

avg = []
days = []
for i in response:
    avg.append(i['average'])
    a = re.sub(r'T([\s\S]*)$', '',str(i['start']))
    days.append(re.sub(r'^\d+-\d+-','',a))

# print(days)

plt.plot(days, avg)
plt.title('Average C0$_2$ values, North Macedonia, March 2022 ')
plt.tick_params(axis='both', which='major', labelsize=11)
plt.subplots_adjust(left=0.17, bottom=0.17)
plt.ylabel('CO$_2$ [mol/m$^2$]')
plt.xlabel('day')
plt.grid(which='major', axis='both')
plt.show()
