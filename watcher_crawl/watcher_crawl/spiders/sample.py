company_names = ['reliance-industries-ltd', 'hdfc-bank-ltd', 'bajaj-finance-ltd', 'bharti-airtel-ltd',
                 'adani-enterprises-ltd']
company_codes = [13215, 9195, 11260, 2718, 9074]
links = []
for i in range(len(company_names)):
    links.append(f"https://economictimes.indiatimes.com/{company_names[i]}/stocks/companyid-{company_codes[i]}")
print(links)