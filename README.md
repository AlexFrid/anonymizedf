# Anonymize df: a convenient way to anonymize your data

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## What is it?

**Anonymize df** is a package that helps you quickly and easily generate realistic
fake data from a Pandas DataFrame.

## What are the expected use cases / why was this made?
- You're hiring consultants to work on your data but need to anonymize it first (GDPR and all that)
- You're a consultant and created something great that you want to make into a template

## Example usage

```python
import pandas as pd
from anonymizedf import anonymize

# Import the data
df = pd.read_csv("customers.csv")

# Prepare the data to be anonymized
an = anonymize(df)

# Select what data you want to anonymize and your preferred style

# Option 1 - Method chaining
fake_df = (
    an
    .fake_names("Customer Name", chaining=True)
    .fake_ids("Customer ID", chaining=True)
    .fake_whole_numbers("Loyalty Reward Points", chaining=True)
    .fake_categories("Segment", chaining=True)
    .fake_dates("Date", chaining=True)
    .fake_decimal_numbers("Fraction", chaining=True)
    .show_data_frame()
)

# Option 2 - multiple assignments
fake_df = an.fake_names("Customer Name")
fake_df = an.fake_ids("Customer ID")
fake_df = an.fake_whole_numbers("Loyalty Reward Points")
fake_df = an.fake_categories("Segment")
fake_df = an.fake_dates("Date")
fake_df = an.fake_decimal_numbers("Fraction")

fake_df.to_csv("fake_customers.csv", index=False)

```

### Example output

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Customer ID</th>
      <th>Customer Name</th>
      <th>Loyalty Reward Points</th>
      <th>Segment</th>
      <th>Date</th>
      <th>Fraction</th>
      <th>Fake_Customer Name</th>
      <th>Fake_Customer ID</th>
      <th>Fake_Loyalty Reward Points</th>
      <th>Fake_Segment</th>
      <th>Fake_Date</th>
      <th>Fake_Fraction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AA-10315</td>
      <td>Alex Avila</td>
      <td>76</td>
      <td>Consumer</td>
      <td>01/01/2000</td>
      <td>7.6</td>
      <td>Christian Metcalfe-Reid</td>
      <td>YEJP71011502726136</td>
      <td>558</td>
      <td>Segment 1</td>
      <td>1978-11-09</td>
      <td>29.96</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AA-10375</td>
      <td>Allen Armold</td>
      <td>369</td>
      <td>Consumer</td>
      <td>02/01/2000</td>
      <td>36.9</td>
      <td>Helen Taylor</td>
      <td>XWOB83170110594048</td>
      <td>286</td>
      <td>Segment 1</td>
      <td>1989-12-29</td>
      <td>72.50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AA-10480</td>
      <td>Andrew Allen</td>
      <td>162</td>
      <td>Consumer</td>
      <td>03/01/2000</td>
      <td>16.2</td>
      <td>Joanne Price</td>
      <td>VVCJ28547588747677</td>
      <td>742</td>
      <td>Segment 1</td>
      <td>1982-09-23</td>
      <td>79.77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AA-10645</td>
      <td>Anna Andreadi</td>
      <td>803</td>
      <td>Consumer</td>
      <td>04/01/2000</td>
      <td>80.3</td>
      <td>Rhys Jones</td>
      <td>OXCI12190813836802</td>
      <td>206</td>
      <td>Segment 1</td>
      <td>2000-10-14</td>
      <td>7.15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AB-10015</td>
      <td>Aaron Bergman</td>
      <td>935</td>
      <td>Consumer</td>
      <td>05/01/2000</td>
      <td>93.5</td>
      <td>Nigel Baldwin-Cook</td>
      <td>JOXS05799252235987</td>
      <td>914</td>
      <td>Segment 1</td>
      <td>2018-01-30</td>
      <td>40.66</td>
    </tr>
  </tbody>
</table>

## Dependencies
- [Pandas](https://pandas.pydata.org)
- [Faker](https://github.com/joke2k/faker)