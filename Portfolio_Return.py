
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
import time

# # Your JSON data
# json_data = [
#   {
#     "S/N": "1",
#     "Name of Script": "ASHOKLEY.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "11-11-2022 00:00:00",
#     "QTY": "1000",
#     "Rate": "148.14",
#     "Net Purchase Value": "148140",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "169.5",
#     "Current Market Rate": "169.5",
#     "Net Sale / Market Value": "169500",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "21360",
#     "Total (Profit/ Loss)": "21360",
#     "Return": "14.42",
#     "Days": "557",
#     "Ann Ret%": "9.45",
#     "Weightage": "0.0224",
#     "Wtg*Ret": "0.21168",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "148140",
#     "Status": null
#   },
#   {
#     "S/N": "2",
#     "Name of Script": "BAJFINANCE.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "02-12-2022 00:00:00",
#     "QTY": "30",
#     "Rate": "6707.8",
#     "Net Purchase Value": "201234",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "7694.45",
#     "Current Market Rate": "7694.45",
#     "Net Sale / Market Value": "230833.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "29599.5",
#     "Total (Profit/ Loss)": "29599.5",
#     "Return": "14.71",
#     "Days": "536",
#     "Ann Ret%": "10.02",
#     "Weightage": "0.0304",
#     "Wtg*Ret": "0.304608",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "201234",
#     "Status": null
#   },
#   {
#     "S/N": "3",
#     "Name of Script": "BAJFINANCE.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "12-12-2022 00:00:00",
#     "QTY": "30",
#     "Rate": "6477.17",
#     "Net Purchase Value": "194315.1",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "7694.45",
#     "Current Market Rate": "7694.45",
#     "Net Sale / Market Value": "230833.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "36518.4",
#     "Total (Profit/ Loss)": "36518.4",
#     "Return": "18.79",
#     "Days": "526",
#     "Ann Ret%": "13.04",
#     "Weightage": "0.0294",
#     "Wtg*Ret": "0.383376",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "194315.1",
#     "Status": null
#   },
#   {
#     "S/N": "4",
#     "Name of Script": "BAJFINANCE.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "13-12-2022 00:00:00",
#     "QTY": "30",
#     "Rate": "6588.53",
#     "Net Purchase Value": "197655.9",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "7694.45",
#     "Current Market Rate": "7694.45",
#     "Net Sale / Market Value": "230833.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "33177.6",
#     "Total (Profit/ Loss)": "33177.6",
#     "Return": "16.79",
#     "Days": "525",
#     "Ann Ret%": "11.67",
#     "Weightage": "0.0299",
#     "Wtg*Ret": "0.348933",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "197655.9",
#     "Status": null
#   },
#   {
#     "S/N": "5",
#     "Name of Script": "BAJFINANCE.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "23-11-2022 00:00:00",
#     "QTY": "50",
#     "Rate": "6728.84",
#     "Net Purchase Value": "336442",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "7694.45",
#     "Current Market Rate": "7694.45",
#     "Net Sale / Market Value": "384722.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "48280.5",
#     "Total (Profit/ Loss)": "48280.5",
#     "Return": "14.35",
#     "Days": "545",
#     "Ann Ret%": "9.61",
#     "Weightage": "0.0509",
#     "Wtg*Ret": "0.489149",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "336442",
#     "Status": null
#   },
#   {
#     "S/N": "6",
#     "Name of Script": "BAJFINANCE.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "16-12-2022 00:00:00",
#     "QTY": "50",
#     "Rate": "6703.78",
#     "Net Purchase Value": "335189",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "7694.45",
#     "Current Market Rate": "7694.45",
#     "Net Sale / Market Value": "384722.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "49533.5",
#     "Total (Profit/ Loss)": "49533.5",
#     "Return": "14.78",
#     "Days": "522",
#     "Ann Ret%": "10.33",
#     "Weightage": "0.0507",
#     "Wtg*Ret": "0.523731",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "335189",
#     "Status": null
#   },
#   {
#     "S/N": "7",
#     "Name of Script": "BAJFINANCE.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "21-12-2022 00:00:00",
#     "QTY": "30",
#     "Rate": "6669.7",
#     "Net Purchase Value": "200091",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "7694.45",
#     "Current Market Rate": "7694.45",
#     "Net Sale / Market Value": "230833.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "30742.5",
#     "Total (Profit/ Loss)": "30742.5",
#     "Return": "15.36",
#     "Days": "517",
#     "Ann Ret%": "10.84",
#     "Weightage": "0.0303",
#     "Wtg*Ret": "0.328452",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "200091",
#     "Status": null
#   },
#   {
#     "S/N": "8",
#     "Name of Script": "BPCL.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "21-01-2022 00:00:00",
#     "QTY": "500",
#     "Rate": "393.56",
#     "Net Purchase Value": "196780",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "339.95",
#     "Current Market Rate": "339.95",
#     "Net Sale / Market Value": "169975",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "-26805",
#     "Total (Profit/ Loss)": "-26805",
#     "Return": "-13.62",
#     "Days": "851",
#     "Ann Ret%": "-5.84",
#     "Weightage": "0.0298",
#     "Wtg*Ret": "-0.174032",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "196780",
#     "Status": null
#   },
#   {
#     "S/N": "9",
#     "Name of Script": "IBULHSGFIN.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "10-11-2021 00:00:00",
#     "QTY": "1000",
#     "Rate": "251.52",
#     "Net Purchase Value": "251520",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "156.1",
#     "Current Market Rate": "156.1",
#     "Net Sale / Market Value": "156100",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "-95420",
#     "Total (Profit/ Loss)": "-95420",
#     "Return": "-37.94",
#     "Days": "923",
#     "Ann Ret%": "-15",
#     "Weightage": "0.038",
#     "Wtg*Ret": "-0.57",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "251520",
#     "Status": null
#   },
#   {
#     "S/N": "10",
#     "Name of Script": "IBULHSGFIN.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "07-01-2022 00:00:00",
#     "QTY": "1000",
#     "Rate": "223.56",
#     "Net Purchase Value": "223560",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "156.1",
#     "Current Market Rate": "156.1",
#     "Net Sale / Market Value": "156100",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "-67460",
#     "Total (Profit/ Loss)": "-67460",
#     "Return": "-30.18",
#     "Days": "865",
#     "Ann Ret%": "-12.73",
#     "Weightage": "0.0338",
#     "Wtg*Ret": "-0.430274",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "223560",
#     "Status": null
#   },
#   {
#     "S/N": "11",
#     "Name of Script": "IBULHSGFIN.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "08-12-2022 00:00:00",
#     "QTY": "1000",
#     "Rate": "142.57",
#     "Net Purchase Value": "142570",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "156.1",
#     "Current Market Rate": "156.1",
#     "Net Sale / Market Value": "156100",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "13530",
#     "Total (Profit/ Loss)": "13530",
#     "Return": "9.49",
#     "Days": "530",
#     "Ann Ret%": "6.54",
#     "Weightage": "0.0216",
#     "Wtg*Ret": "0.141264",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "142570",
#     "Status": null
#   },
#   {
#     "S/N": "12",
#     "Name of Script": "IBULHSGFIN.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "14-12-2022 00:00:00",
#     "QTY": "1000",
#     "Rate": "148.74",
#     "Net Purchase Value": "148740",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "156.1",
#     "Current Market Rate": "156.1",
#     "Net Sale / Market Value": "156100",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "7360",
#     "Total (Profit/ Loss)": "7360",
#     "Return": "4.95",
#     "Days": "524",
#     "Ann Ret%": "3.45",
#     "Weightage": "0.0225",
#     "Wtg*Ret": "0.077625",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "148740",
#     "Status": null
#   },
#   {
#     "S/N": "13",
#     "Name of Script": "IBULHSGFIN.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "15-12-2022 00:00:00",
#     "QTY": "1000",
#     "Rate": "147.99",
#     "Net Purchase Value": "147990",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "156.1",
#     "Current Market Rate": "156.1",
#     "Net Sale / Market Value": "156100",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "8110",
#     "Total (Profit/ Loss)": "8110",
#     "Return": "5.48",
#     "Days": "523",
#     "Ann Ret%": "3.82",
#     "Weightage": "0.0224",
#     "Wtg*Ret": "0.085568",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "147990",
#     "Status": null
#   },
#   {
#     "S/N": "14",
#     "Name of Script": "MARUTI.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "04-01-2023 00:00:00",
#     "QTY": "30",
#     "Rate": "8451.97",
#     "Net Purchase Value": "253559.1",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "10588.85",
#     "Current Market Rate": "10588.85",
#     "Net Sale / Market Value": "317665.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "64106.4",
#     "Total (Profit/ Loss)": "64106.4",
#     "Return": "25.28",
#     "Days": "503",
#     "Ann Ret%": "18.34",
#     "Weightage": "0.0383",
#     "Wtg*Ret": "0.702422",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "253559.1",
#     "Status": null
#   },
#   {
#     "S/N": "15",
#     "Name of Script": "MARUTI.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "14-12-2022 00:00:00",
#     "QTY": "50",
#     "Rate": "8653.08",
#     "Net Purchase Value": "432654",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "10588.85",
#     "Current Market Rate": "10588.85",
#     "Net Sale / Market Value": "529442.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "96788.5",
#     "Total (Profit/ Loss)": "96788.5",
#     "Return": "22.37",
#     "Days": "524",
#     "Ann Ret%": "15.58",
#     "Weightage": "0.0654",
#     "Wtg*Ret": "1.018932",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "432654",
#     "Status": null
#   },
#   {
#     "S/N": "16",
#     "Name of Script": "MARUTI.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "16-12-2022 00:00:00",
#     "QTY": "30",
#     "Rate": "8567.17",
#     "Net Purchase Value": "257015.1",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "10588.85",
#     "Current Market Rate": "10588.85",
#     "Net Sale / Market Value": "317665.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "60650.4",
#     "Total (Profit/ Loss)": "60650.4",
#     "Return": "23.6",
#     "Days": "522",
#     "Ann Ret%": "16.5",
#     "Weightage": "0.0389",
#     "Wtg*Ret": "0.64185",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "257015.1",
#     "Status": null
#   },
#   {
#     "S/N": "17",
#     "Name of Script": "MARUTI.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "19-12-2022 00:00:00",
#     "QTY": "25",
#     "Rate": "8568.16",
#     "Net Purchase Value": "214204",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "10588.85",
#     "Current Market Rate": "10588.85",
#     "Net Sale / Market Value": "264721.25",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "50517.25",
#     "Total (Profit/ Loss)": "50517.25",
#     "Return": "23.58",
#     "Days": "519",
#     "Ann Ret%": "16.58",
#     "Weightage": "0.0324",
#     "Wtg*Ret": "0.537192",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "214204",
#     "Status": null
#   },
#   {
#     "S/N": "18",
#     "Name of Script": "MARUTI.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "22-12-2022 00:00:00",
#     "QTY": "30",
#     "Rate": "8330.3",
#     "Net Purchase Value": "249909",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "10588.85",
#     "Current Market Rate": "10588.85",
#     "Net Sale / Market Value": "317665.5",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "67756.5",
#     "Total (Profit/ Loss)": "67756.5",
#     "Return": "27.11",
#     "Days": "516",
#     "Ann Ret%": "19.18",
#     "Weightage": "0.0378",
#     "Wtg*Ret": "0.725004",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "249909",
#     "Status": null
#   },
#   {
#     "S/N": "19",
#     "Name of Script": "MARUTI.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "30-12-2022 00:00:00",
#     "QTY": "35",
#     "Rate": "8435.89",
#     "Net Purchase Value": "295256.15",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "10588.85",
#     "Current Market Rate": "10588.85",
#     "Net Sale / Market Value": "370609.75",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "75353.6",
#     "Total (Profit/ Loss)": "75353.6",
#     "Return": "25.52",
#     "Days": "508",
#     "Ann Ret%": "18.34",
#     "Weightage": "0.0447",
#     "Wtg*Ret": "0.819798",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "295256.15",
#     "Status": null
#   },
#   {
#     "S/N": "20",
#     "Name of Script": "NATIONALUM.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "22-04-2022 00:00:00",
#     "QTY": "2000",
#     "Rate": "117.65",
#     "Net Purchase Value": "235300",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "91.65",
#     "Current Market Rate": "91.65",
#     "Net Sale / Market Value": "183300",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "-52000",
#     "Total (Profit/ Loss)": "-52000",
#     "Return": "-22.1",
#     "Days": "760",
#     "Ann Ret%": "-10.61",
#     "Weightage": "0.0356",
#     "Wtg*Ret": "-0.377716",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "235300",
#     "Status": null
#   },
#   {
#     "S/N": "21",
#     "Name of Script": "NATIONALUM.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "08-04-2022 00:00:00",
#     "QTY": "2000",
#     "Rate": "126.82",
#     "Net Purchase Value": "253640",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "91.65",
#     "Current Market Rate": "91.65",
#     "Net Sale / Market Value": "183300",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "-70340",
#     "Total (Profit/ Loss)": "-70340",
#     "Return": "-27.73",
#     "Days": "774",
#     "Ann Ret%": "-13.08",
#     "Weightage": "0.0384",
#     "Wtg*Ret": "-0.502272",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "253640",
#     "Status": null
#   },
#   {
#     "S/N": "22",
#     "Name of Script": "NATIONALUM.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "09-05-2022 00:00:00",
#     "QTY": "2000",
#     "Rate": "95.43",
#     "Net Purchase Value": "190860",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "91.65",
#     "Current Market Rate": "91.65",
#     "Net Sale / Market Value": "183300",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "-7560",
#     "Total (Profit/ Loss)": "-7560",
#     "Return": "-3.96",
#     "Days": "743",
#     "Ann Ret%": "-1.95",
#     "Weightage": "0.0289",
#     "Wtg*Ret": "-0.056355",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "190860",
#     "Status": null
#   },
#   {
#     "S/N": "23",
#     "Name of Script": "NATIONALUM.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "15-06-2022 00:00:00",
#     "QTY": "2000",
#     "Rate": "85.25",
#     "Net Purchase Value": "170500",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "91.65",
#     "Current Market Rate": "91.65",
#     "Net Sale / Market Value": "183300",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "12800",
#     "Total (Profit/ Loss)": "12800",
#     "Return": "7.51",
#     "Days": "706",
#     "Ann Ret%": "3.88",
#     "Weightage": "0.0258",
#     "Wtg*Ret": "0.100104",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "170500",
#     "Status": null
#   },
#   {
#     "S/N": "24",
#     "Name of Script": "TATAMOTORS.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "22-09-2021 00:00:00",
#     "QTY": "1000",
#     "Rate": "508.19",
#     "Net Purchase Value": "508190",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "637.85",
#     "Current Market Rate": "637.85",
#     "Net Sale / Market Value": "637850",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "129660",
#     "Total (Profit/ Loss)": "129660",
#     "Return": "25.51",
#     "Days": "972",
#     "Ann Ret%": "9.58",
#     "Weightage": "0.0769",
#     "Wtg*Ret": "0.736702",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "508190",
#     "Status": null
#   },
#   {
#     "S/N": "25",
#     "Name of Script": "TECHM.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "16-09-2022 00:00:00",
#     "QTY": "200",
#     "Rate": "1052.46",
#     "Net Purchase Value": "210492",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "1142.15",
#     "Current Market Rate": "1142.15",
#     "Net Sale / Market Value": "228430",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "17938",
#     "Total (Profit/ Loss)": "17938",
#     "Return": "8.52",
#     "Days": "613",
#     "Ann Ret%": "5.07",
#     "Weightage": "0.0318",
#     "Wtg*Ret": "0.161226",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "210492",
#     "Status": null
#   },
#   {
#     "S/N": "26",
#     "Name of Script": "WIPRO.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "15-09-2022 00:00:00",
#     "QTY": "1000",
#     "Rate": "414.94",
#     "Net Purchase Value": "414940",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "381.85",
#     "Current Market Rate": "381.85",
#     "Net Sale / Market Value": "381850",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "-33090",
#     "Total (Profit/ Loss)": "-33090",
#     "Return": "-7.97",
#     "Days": "614",
#     "Ann Ret%": "-4.74",
#     "Weightage": "0.0628",
#     "Wtg*Ret": "-0.297672",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "414940",
#     "Status": null
#   },
#   {
#     "S/N": "27",
#     "Name of Script": "WIPRO.NS",
#     "Ass Name": "a a a",
#     "Purchase Date": "06-09-2022 00:00:00",
#     "QTY": "500",
#     "Rate": "403.14",
#     "Net Purchase Value": "201570",
#     "Sale / Valuation Date": "21-05-2024 00:00:00",
#     "Sale / Market Rate": "381.85",
#     "Current Market Rate": "381.85",
#     "Net Sale / Market Value": "190925",
#     "Realized (Profit/ Loss)": null,
#     "Unrealized (Profit/ Loss)": "-10645",
#     "Total (Profit/ Loss)": "-10645",
#     "Return": "-5.28",
#     "Days": "623",
#     "Ann Ret%": "-3.09",
#     "Weightage": "0.0305",
#     "Wtg*Ret": "-0.094245",
#     "Transaction": null,
#     "Sale Value": null,
#     "STT Charges": null,
#     "Other Charges": null,
#     "Purchase Value": "201570",
#     "Status": null
#   }
# ]
#
# # Convert null values to None in Python
# json_data = json.dumps(json_data)
# json_data = json.loads(json_data.replace("null", "None"))
#
# # Convert the JSON data to a Pandas DataFrame
# data = pd.DataFrame(json_data)
#
# # # Display the DataFrame
# # print(df)
#
# # file_name = r"C:\Users\Sinewave#2022\Downloads\stock_portfolio_transformed.xlsx"
# #
# # # Process the uploaded file
# # dt = pd.read_excel(file_name)
# # Sort the DataFrame by 'Purchase Date'
# # Convert 'Purchase Date' and 'Sale / Valuation Date' to datetime format
# data['Purchase Date'] = pd.to_datetime(data['Purchase Date'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d')
# data['Sale / Valuation Date'] = pd.to_datetime(data['Sale / Valuation Date'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d')
#
# # Ensure 'QTY' is numeric
# data['QTY'] = pd.to_numeric(data['QTY'])
#
# # Sort values by 'Purchase Date'
# data.sort_values(by='Purchase Date', inplace=True)
#
# close_prices_with_qty = pd.DataFrame()
#
# for index, row in data.iterrows():
#     script = row['Name of Script']
#     purchase_date = row['Purchase Date']
#     sell_date = row['Sale / Valuation Date']
#     qty = row['QTY']
#
#     stock_data = yf.download(script, start=purchase_date, end=sell_date)
#     close_price = stock_data['Close']
#
#     close_price_with_qty = pd.DataFrame({
#         script: close_price.values,
#         script + '_QTY': qty,
#         script + '_Value': qty * close_price,
#     }, index=close_price.index)
#
#     close_prices_with_qty = pd.concat([close_prices_with_qty, close_price_with_qty], axis=1)
#
# merged_df = close_prices_with_qty.groupby(level=0, axis=1).sum()
# merged_df.reset_index(inplace=True)
# close_prices_with_qty = merged_df
#
# ns_columns = [col for col in merged_df.columns if col.endswith('.NS')]
#
# ns_columns_df = merged_df[ns_columns]
#
# close_prices_with_qty.set_index('Date', inplace=True)
#
# date_column = close_prices_with_qty.index
#
# ns_columns_df.insert(0, 'Date', date_column)
#
# stocks = ns_columns_df.columns[1:]  # Pehla column 'Date' hai isliye 1 se start karo
#
# stock_data = {}
#
# for stock in stocks:
#     non_zero_rows = ns_columns_df[ns_columns_df[stock] != 0]
#     # Start date
#     start_date = non_zero_rows['Date'].iloc[0]
#     # End date
#     end_date = non_zero_rows['Date'].iloc[-1]
#     stock_prices = yf.download(stock, start=start_date, end=end_date)['Close']  # Stock ka close price
#     stock_data[stock] = stock_prices
#
# stock_prices_df = pd.DataFrame(stock_data)
#
# stock_prices_df = stock_prices_df.reindex(close_prices_with_qty.index)
#
# for column in stock_prices_df.columns:
#
#     if column in close_prices_with_qty.columns:
#         close_prices_with_qty[column] = stock_prices_df[column].values
#
# close_prices_with_qty.reset_index(inplace=True)
#
# close_prices_with_qty['Portfolio_Value'] = close_prices_with_qty.filter(like='_Value').sum(axis=1)
# close_prices_with_qty['Portfolio_Return'] = close_prices_with_qty['Portfolio_Value'].pct_change()
#
# first_purchase_date_processed = False
# for index, row in data.iterrows():
#     purchase_date = row['Purchase Date']
#     purchase_price = row['Rate']
#     purchase_QTY = row['QTY']
#
#     # Convert purchase_price from string to float
#     purchase_price = float(purchase_price)
#
#     if purchase_date in data['Purchase Date'].values:
#         # Convert purchase_date to a datetime object
#         purchase_date = pd.to_datetime(purchase_date)
#
#         # Initialize a flag to check if a matching row was found
#         match_found = False
#         day_increment = 1
#
#         # Loop until a match is found or a reasonable limit is reached
#         while not match_found and day_increment <= 30:  # Limit to 30 days
#             potential_date = purchase_date + pd.Timedelta(days=day_increment)
#             matched_rows = close_prices_with_qty[close_prices_with_qty['Date'] == potential_date]
#
#             if not matched_rows.empty:
#                 row_index = matched_rows.index[0]
#                 portfolio_value = close_prices_with_qty.loc[row_index, 'Portfolio_Value']
#                 net_purchase_value = purchase_price * purchase_QTY
#
#                 try:
#                     previous_day_portfolio_value = close_prices_with_qty.iloc[row_index - 1]['Portfolio_Value']
#                 except KeyError:
#                     previous_day_portfolio_value = 0
#
#                 denominator = net_purchase_value + previous_day_portfolio_value
#                 result = portfolio_value / denominator / 100
#
#                 close_prices_with_qty.at[row_index, 'Portfolio_Return'] = result
#
#                 match_found = True
#             else:
#                 day_increment += 1
#
#         if not match_found:
#             print(f"No matching row found within 30 days for purchase date: {purchase_date}")
#
#         # Example usage of first_purchase_date_processed
#         if not first_purchase_date_processed:
#             first_purchase_date_processed = True
#
#
# sell_transactions_grouped = data[data['Sale / Valuation Date'] >= '11/07/2023'].groupby(
#     'Sale / Valuation Date')
#
# for sell_date, group_data in sell_transactions_grouped:
#     sell_date_np = np.datetime64(sell_date)
#
#     if sell_date_np in close_prices_with_qty['Date'].values:
#         row_index = close_prices_with_qty[close_prices_with_qty['Date'] == sell_date].index[0]
#         portfolio_value = close_prices_with_qty.loc[row_index, 'Portfolio_Value']
#
#         if sell_date in data['Purchase Date'].values:
#             purchase_data = data[data['Purchase Date'] == sell_date]
#             net_transaction_value = group_data['Net Sale / Market Value'].sum() - purchase_data[
#                 'Net Purchase Value'].sum()
#         else:
#             net_transaction_value = group_data['Net Sale / Market Value'].sum()
#
#         try:
#             previous_day_portfolio_value = close_prices_with_qty.iloc[row_index - 1]['Portfolio_Value']
#         except KeyError:
#             previous_day_portfolio_value = 0
#
#         denominator = previous_day_portfolio_value - net_transaction_value
#         result = portfolio_value / denominator / 100
#
#         close_prices_with_qty.at[row_index, 'Portfolio_Return'] = result
#
# rolling_std_dev = close_prices_with_qty['Portfolio_Return'].rolling(window=30).std()
# close_prices_with_qty['Portfolio_std_dev'] = rolling_std_dev
#
# rolling_sharpe_ratio = close_prices_with_qty['Portfolio_Return'].rolling(window=30).mean() / \
#                        close_prices_with_qty['Portfolio_Return'].rolling(window=30).std()
# close_prices_with_qty['Sharpe_Ratio'] = rolling_sharpe_ratio
#
# rolling_max = close_prices_with_qty['Portfolio_Value'].cummax()
# daily_drawdown = close_prices_with_qty['Portfolio_Value'] / rolling_max - 1
# max_daily_drawdown = daily_drawdown.expanding(min_periods=1).min()
# close_prices_with_qty['Max_Drawdown'] = max_daily_drawdown
#
# close_prices_with_qty.fillna(0, inplace=True)
#
# close_prices_with_qty.reset_index(inplace=True)
#
# output_file = f'C:\\Users\\Sinewave#2022\\Downloads\\close_prices_with_qty.csv'
# close_prices_with_qty.to_csv(output_file)
# # Filter the DataFrame
# filtered_df = merged_df[(merged_df['Date'] >= '2023-04-01') & (merged_df['Date'] <= '2024-03-31')]
#
# # Convert 'Date' column to datetime
# filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
#
# # Calculate cumulative return
# filtered_df['Cumulative_Return'] = (1 + filtered_df['Portfolio_Return']).cumprod() - 1
#
# # Calculate amplified standard deviation
# amplification_factor = 50  # Adjust as needed
# filtered_df['Amplified_Std_Dev'] = filtered_df['Portfolio_std_dev'] * amplification_factor
#
# # Plotting
# sns.set_style("whitegrid")
# fig, ax1 = plt.subplots(figsize=(19, 10))
#
# # Plot Cumulative Return
# ax1.plot(filtered_df['Date'], filtered_df['Cumulative_Return'], color='blue', label='Cumulative Return')
#
# # Plot Amplified Standard Deviation
# ax1.plot(filtered_df['Date'], filtered_df['Amplified_Std_Dev'], color='red', linestyle='--', label='Amplified Standard Deviation')
#
# # Set labels and tick parameters for ax1
# ax1.set_xlabel('Date')
# ax1.set_ylabel('Cumulative Return and Amplified Standard Deviation', color='blue')
# ax1.tick_params(axis='y', labelcolor='blue')
#
# # Create a twin axis for Sharpe Ratio
# ax2 = ax1.twinx()
#
# # Plot Sharpe Ratio
# ax2.plot(filtered_df['Date'], filtered_df['Sharpe_Ratio'], color='green', linestyle='-.', label='Sharpe Ratio')
#
# # Set labels and tick parameters for ax2
# ax2.set_ylabel('Sharpe Ratio', color='green')
# ax2.tick_params(axis='y', labelcolor='green')
#
# # Combine legends from both axes
# lines1, labels1 = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', bbox_to_anchor=(0.05, 0.95))
#
# # Title of the plot
# plt.title('Cumulative Return, Amplified Standard Deviation, and Sharpe Ratio')
#
# # Add a short delay to allow the plot to fully render
# time.sleep(1)  # Adjust the delay time as needed
#
# # Define the path to save the plot
# download_path = os.path.expanduser('~/Downloads/plot.png')
#
# # Save the plot
# plt.savefig(download_path)
#
# # Close plot after displaying
# plt.close()
#
#
#







import json


# Your JSON data
json_data = [
  {
    "S/N": "1",
    "Name of Script": "ASHOKLEY.NS",
    "Ass Name": "a a a",
    "Purchase Date": "30-03-2022 00:00:00",
    "QTY": "2000",
    "Rate": "116.34",
    "Net Purchase Value": "232680",
    "Sale / Valuation Date": "07-04-2022 00:00:00",
    "Sale / Market Rate": "126.05",
    "Current Market Rate": "134.85",
    "Net Sale / Market Value": "252100",
    "Realized (Profit/ Loss)": "19420",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19420",
    "Return": "8.35",
    "Days": "8",
    "Ann Ret%": "380.97",
    "Weightage": "0.0142",
    "Wtg*Ret": "5.409774",
    "Transaction": "0",
    "Sale Value": "252100",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "232680",
    "Status": "0"
  },
  {
    "S/N": "2",
    "Name of Script": "ASHOKLEY.NS",
    "Ass Name": "a a a",
    "Purchase Date": "11-11-2022 00:00:00",
    "QTY": "1000",
    "Rate": "148.14",
    "Net Purchase Value": "148140",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "134.85",
    "Current Market Rate": "134.85",
    "Net Sale / Market Value": "134850",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-13290",
    "Total (Profit/ Loss)": "-13290",
    "Return": "-8.97",
    "Days": "561",
    "Ann Ret%": "-5.84",
    "Weightage": "0.009",
    "Wtg*Ret": "-0.05256",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "148140",
    "Status": "0"
  },
  {
    "S/N": "3",
    "Name of Script": "BAJFINANCE.NS",
    "Ass Name": "a a a",
    "Purchase Date": "10-05-2022 00:00:00",
    "QTY": "30",
    "Rate": "6012.73",
    "Net Purchase Value": "180381.9",
    "Sale / Valuation Date": "28-07-2022 00:00:00",
    "Sale / Market Rate": "6945.77",
    "Current Market Rate": "5568.84",
    "Net Sale / Market Value": "208373.1",
    "Realized (Profit/ Loss)": "27991",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "27991.2",
    "Return": "15.52",
    "Days": "79",
    "Ann Ret%": "71.71",
    "Weightage": "0.011",
    "Wtg*Ret": "0.78881",
    "Transaction": "0",
    "Sale Value": "208373.1",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "180381.9",
    "Status": "0"
  },
  {
    "S/N": "4",
    "Name of Script": "BAJFINANCE.NS",
    "Ass Name": "a a a",
    "Purchase Date": "02-12-2022 00:00:00",
    "QTY": "30",
    "Rate": "6707.8",
    "Net Purchase Value": "201234",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "5568.84",
    "Current Market Rate": "5568.84",
    "Net Sale / Market Value": "167065.2",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-34168.8",
    "Total (Profit/ Loss)": "-34168.8",
    "Return": "-16.98",
    "Days": "540",
    "Ann Ret%": "-11.48",
    "Weightage": "0.0123",
    "Wtg*Ret": "-0.141204",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "201234",
    "Status": "0"
  },
  {
    "S/N": "5",
    "Name of Script": "BAJFINANCE.NS",
    "Ass Name": "a a a",
    "Purchase Date": "12-12-2022 00:00:00",
    "QTY": "30",
    "Rate": "6477.17",
    "Net Purchase Value": "194315.1",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "5568.84",
    "Current Market Rate": "5568.84",
    "Net Sale / Market Value": "167065.2",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-27249.9",
    "Total (Profit/ Loss)": "-27249.9",
    "Return": "-14.02",
    "Days": "530",
    "Ann Ret%": "-9.66",
    "Weightage": "0.0119",
    "Wtg*Ret": "-0.114954",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "194315.1",
    "Status": "0"
  },
  {
    "S/N": "6",
    "Name of Script": "BAJFINANCE.NS",
    "Ass Name": "a a a",
    "Purchase Date": "13-12-2022 00:00:00",
    "QTY": "30",
    "Rate": "6588.53",
    "Net Purchase Value": "197655.9",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "5568.84",
    "Current Market Rate": "5568.84",
    "Net Sale / Market Value": "167065.2",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-30590.7",
    "Total (Profit/ Loss)": "-30590.7",
    "Return": "-15.48",
    "Days": "529",
    "Ann Ret%": "-10.68",
    "Weightage": "0.0121",
    "Wtg*Ret": "-0.129228",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "197655.9",
    "Status": "0"
  },
  {
    "S/N": "7",
    "Name of Script": "BAJFINANCE.NS",
    "Ass Name": "a a a",
    "Purchase Date": "23-11-2022 00:00:00",
    "QTY": "50",
    "Rate": "6728.84",
    "Net Purchase Value": "336442",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "5568.84",
    "Current Market Rate": "5568.84",
    "Net Sale / Market Value": "278442",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-58000",
    "Total (Profit/ Loss)": "-58000",
    "Return": "-17.24",
    "Days": "549",
    "Ann Ret%": "-11.46",
    "Weightage": "0.0205",
    "Wtg*Ret": "-0.23493",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "336442",
    "Status": "0"
  },
  {
    "S/N": "8",
    "Name of Script": "BAJFINANCE.NS",
    "Ass Name": "a a a",
    "Purchase Date": "16-12-2022 00:00:00",
    "QTY": "50",
    "Rate": "6703.78",
    "Net Purchase Value": "335189",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "5568.84",
    "Current Market Rate": "5568.84",
    "Net Sale / Market Value": "278442",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-56747",
    "Total (Profit/ Loss)": "-56747",
    "Return": "-16.93",
    "Days": "526",
    "Ann Ret%": "-11.75",
    "Weightage": "0.0204",
    "Wtg*Ret": "-0.2397",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "335189",
    "Status": "0"
  },
  {
    "S/N": "9",
    "Name of Script": "BAJFINANCE.NS",
    "Ass Name": "a a a",
    "Purchase Date": "21-12-2022 00:00:00",
    "QTY": "30",
    "Rate": "6669.7",
    "Net Purchase Value": "200091",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "5568.84",
    "Current Market Rate": "5568.84",
    "Net Sale / Market Value": "167065.2",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-33025.8",
    "Total (Profit/ Loss)": "-33025.8",
    "Return": "-16.51",
    "Days": "521",
    "Ann Ret%": "-11.57",
    "Weightage": "0.0122",
    "Wtg*Ret": "-0.141154",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "200091",
    "Status": "0"
  },
  {
    "S/N": "10",
    "Name of Script": "BHEL.NS",
    "Ass Name": "a a a",
    "Purchase Date": "11-01-2022 00:00:00",
    "QTY": "3500",
    "Rate": "62.78",
    "Net Purchase Value": "219730",
    "Sale / Valuation Date": "18-10-2022 00:00:00",
    "Sale / Market Rate": "68.21",
    "Current Market Rate": "69.77",
    "Net Sale / Market Value": "238735",
    "Realized (Profit/ Loss)": "19005",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19005",
    "Return": "8.65",
    "Days": "280",
    "Ann Ret%": "11.28",
    "Weightage": "0.0134",
    "Wtg*Ret": "0.151152",
    "Transaction": "0",
    "Sale Value": "238735",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "219730",
    "Status": "0"
  },
  {
    "S/N": "11",
    "Name of Script": "BHEL.NS",
    "Ass Name": "a a a",
    "Purchase Date": "14-11-2022 00:00:00",
    "QTY": "5000",
    "Rate": "70.16",
    "Net Purchase Value": "350800",
    "Sale / Valuation Date": "22-11-2022 00:00:00",
    "Sale / Market Rate": "73.89",
    "Current Market Rate": "69.77",
    "Net Sale / Market Value": "369450",
    "Realized (Profit/ Loss)": "18650",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "18650",
    "Return": "5.32",
    "Days": "8",
    "Ann Ret%": "242.73",
    "Weightage": "0.0214",
    "Wtg*Ret": "5.194422",
    "Transaction": "0",
    "Sale Value": "369450",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "350800",
    "Status": "0"
  },
  {
    "S/N": "12",
    "Name of Script": "BPCL.NS",
    "Ass Name": "a a a",
    "Purchase Date": "21-01-2022 00:00:00",
    "QTY": "500",
    "Rate": "393.56",
    "Net Purchase Value": "196780",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "340.5",
    "Current Market Rate": "340.5",
    "Net Sale / Market Value": "170250",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-26530",
    "Total (Profit/ Loss)": "-26530",
    "Return": "-13.48",
    "Days": "855",
    "Ann Ret%": "-5.75",
    "Weightage": "0.012",
    "Wtg*Ret": "-0.069",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "196780",
    "Status": "0"
  },
  {
    "S/N": "13",
    "Name of Script": "BPCL.NS",
    "Ass Name": "a a a",
    "Purchase Date": "16-03-2022 00:00:00",
    "QTY": "500",
    "Rate": "352.04",
    "Net Purchase Value": "176020",
    "Sale / Valuation Date": "21-04-2022 00:00:00",
    "Sale / Market Rate": "393.89",
    "Current Market Rate": "340.5",
    "Net Sale / Market Value": "196945",
    "Realized (Profit/ Loss)": "20925",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "20925",
    "Return": "11.89",
    "Days": "36",
    "Ann Ret%": "120.55",
    "Weightage": "0.0107",
    "Wtg*Ret": "1.289885",
    "Transaction": "0",
    "Sale Value": "196945",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "176020",
    "Status": "0"
  },
  {
    "S/N": "14",
    "Name of Script": "BPCL.NS",
    "Ass Name": "a a a",
    "Purchase Date": "31-10-2022 00:00:00",
    "QTY": "700",
    "Rate": "303.9",
    "Net Purchase Value": "212730",
    "Sale / Valuation Date": "28-11-2022 00:00:00",
    "Sale / Market Rate": "340.04",
    "Current Market Rate": "340.5",
    "Net Sale / Market Value": "238028",
    "Realized (Profit/ Loss)": "25298",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "25298",
    "Return": "11.89",
    "Days": "28",
    "Ann Ret%": "154.99",
    "Weightage": "0.013",
    "Wtg*Ret": "2.01487",
    "Transaction": "0",
    "Sale Value": "238028",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "212730",
    "Status": "0"
  },
  {
    "S/N": "15",
    "Name of Script": "DLF.NS",
    "Ass Name": "a a a",
    "Purchase Date": "21-01-2022 00:00:00",
    "QTY": "1000",
    "Rate": "401.66",
    "Net Purchase Value": "401660",
    "Sale / Valuation Date": "07-12-2022 00:00:00",
    "Sale / Market Rate": "405.49",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "405490",
    "Realized (Profit/ Loss)": "3830",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "3830",
    "Return": "0.95",
    "Days": "320",
    "Ann Ret%": "1.08",
    "Weightage": "0.0245",
    "Wtg*Ret": "0.02646",
    "Transaction": "0",
    "Sale Value": "405490",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "401660",
    "Status": "0"
  },
  {
    "S/N": "16",
    "Name of Script": "DLF.NS",
    "Ass Name": "a a a",
    "Purchase Date": "21-02-2022 00:00:00",
    "QTY": "500",
    "Rate": "354.76",
    "Net Purchase Value": "177380",
    "Sale / Valuation Date": "04-04-2022 00:00:00",
    "Sale / Market Rate": "386.46",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "193230",
    "Realized (Profit/ Loss)": "15850",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "15850",
    "Return": "8.94",
    "Days": "42",
    "Ann Ret%": "77.69",
    "Weightage": "0.0108",
    "Wtg*Ret": "0.839052",
    "Transaction": "0",
    "Sale Value": "193230",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "177380",
    "Status": "0"
  },
  {
    "S/N": "17",
    "Name of Script": "DLF.NS",
    "Ass Name": "a a a",
    "Purchase Date": "05-04-2022 00:00:00",
    "QTY": "500",
    "Rate": "388.55",
    "Net Purchase Value": "194275",
    "Sale / Valuation Date": "07-12-2022 00:00:00",
    "Sale / Market Rate": "405.58",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "202790",
    "Realized (Profit/ Loss)": "8515",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "8515",
    "Return": "4.38",
    "Days": "246",
    "Ann Ret%": "6.5",
    "Weightage": "0.0119",
    "Wtg*Ret": "0.07735",
    "Transaction": "0",
    "Sale Value": "202790",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "194275",
    "Status": "0"
  },
  {
    "S/N": "18",
    "Name of Script": "HCLTECH.NS",
    "Ass Name": "a a a",
    "Purchase Date": "23-08-2022 00:00:00",
    "QTY": "200",
    "Rate": "947.24",
    "Net Purchase Value": "189448",
    "Sale / Valuation Date": "19-10-2022 00:00:00",
    "Sale / Market Rate": "992.28",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "198456",
    "Realized (Profit/ Loss)": "9008",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "9008",
    "Return": "4.75",
    "Days": "57",
    "Ann Ret%": "30.42",
    "Weightage": "0.0116",
    "Wtg*Ret": "0.352872",
    "Transaction": "0",
    "Sale Value": "198456",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "189448",
    "Status": "0"
  },
  {
    "S/N": "19",
    "Name of Script": "HCLTECH.NS",
    "Ass Name": "a a a",
    "Purchase Date": "08-09-2022 00:00:00",
    "QTY": "200",
    "Rate": "936.96",
    "Net Purchase Value": "187392",
    "Sale / Valuation Date": "19-10-2022 00:00:00",
    "Sale / Market Rate": "992.6",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "198520",
    "Realized (Profit/ Loss)": "11128",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "11128",
    "Return": "5.94",
    "Days": "41",
    "Ann Ret%": "52.88",
    "Weightage": "0.0114",
    "Wtg*Ret": "0.602832",
    "Transaction": "0",
    "Sale Value": "198520",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "187392",
    "Status": "0"
  },
  {
    "S/N": "20",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "14-07-2021 00:00:00",
    "QTY": "1000",
    "Rate": "282.03",
    "Net Purchase Value": "282030",
    "Sale / Valuation Date": "12-07-2022 00:00:00",
    "Sale / Market Rate": "94.87",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "94870",
    "Realized (Profit/ Loss)": "-187160",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "-187160",
    "Return": "-66.36",
    "Days": "363",
    "Ann Ret%": "-66.73",
    "Weightage": "0.0172",
    "Wtg*Ret": "-1.147756",
    "Transaction": "0",
    "Sale Value": "94870",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "282030",
    "Status": "0"
  },
  {
    "S/N": "21",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "10-11-2021 00:00:00",
    "QTY": "1000",
    "Rate": "251.52",
    "Net Purchase Value": "251520",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "96.72",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "96720",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-154800",
    "Total (Profit/ Loss)": "-154800",
    "Return": "-61.55",
    "Days": "927",
    "Ann Ret%": "-24.23",
    "Weightage": "0.0153",
    "Wtg*Ret": "-0.370719",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "251520",
    "Status": "0"
  },
  {
    "S/N": "22",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "27-07-2022 00:00:00",
    "QTY": "1000",
    "Rate": "102.9",
    "Net Purchase Value": "102900",
    "Sale / Valuation Date": "19-08-2022 00:00:00",
    "Sale / Market Rate": "130.33",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "130330",
    "Realized (Profit/ Loss)": "27430",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "27430",
    "Return": "26.66",
    "Days": "23",
    "Ann Ret%": "423.08",
    "Weightage": "0.0063",
    "Wtg*Ret": "2.665404",
    "Transaction": "0",
    "Sale Value": "130330",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "102900",
    "Status": "0"
  },
  {
    "S/N": "23",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "28-07-2022 00:00:00",
    "QTY": "1000",
    "Rate": "103.76",
    "Net Purchase Value": "103760",
    "Sale / Valuation Date": "19-08-2022 00:00:00",
    "Sale / Market Rate": "130.33",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "130330",
    "Realized (Profit/ Loss)": "26570",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "26570",
    "Return": "25.61",
    "Days": "22",
    "Ann Ret%": "424.89",
    "Weightage": "0.0063",
    "Wtg*Ret": "2.676807",
    "Transaction": "0",
    "Sale Value": "130330",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "103760",
    "Status": "0"
  },
  {
    "S/N": "24",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "11-08-2022 00:00:00",
    "QTY": "1000",
    "Rate": "124.72",
    "Net Purchase Value": "124720",
    "Sale / Valuation Date": "29-11-2022 00:00:00",
    "Sale / Market Rate": "142.3",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "142300",
    "Realized (Profit/ Loss)": "17580",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "17580",
    "Return": "14.1",
    "Days": "110",
    "Ann Ret%": "46.79",
    "Weightage": "0.0076",
    "Wtg*Ret": "0.355604",
    "Transaction": "0",
    "Sale Value": "142300",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "124720",
    "Status": "0"
  },
  {
    "S/N": "25",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "07-01-2022 00:00:00",
    "QTY": "1000",
    "Rate": "223.56",
    "Net Purchase Value": "223560",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "96.72",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "96720",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-126840",
    "Total (Profit/ Loss)": "-126840",
    "Return": "-56.74",
    "Days": "869",
    "Ann Ret%": "-23.83",
    "Weightage": "0.0136",
    "Wtg*Ret": "-0.324088",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "223560",
    "Status": "0"
  },
  {
    "S/N": "26",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "12-07-2022 00:00:00",
    "QTY": "1000",
    "Rate": "94.97",
    "Net Purchase Value": "94970",
    "Sale / Valuation Date": "19-08-2022 00:00:00",
    "Sale / Market Rate": "130.63",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "130630",
    "Realized (Profit/ Loss)": "35660",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "35660",
    "Return": "37.55",
    "Days": "38",
    "Ann Ret%": "360.68",
    "Weightage": "0.0058",
    "Wtg*Ret": "2.091944",
    "Transaction": "0",
    "Sale Value": "130630",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "94970",
    "Status": "0"
  },
  {
    "S/N": "27",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "22-08-2022 00:00:00",
    "QTY": "1000",
    "Rate": "128.43",
    "Net Purchase Value": "128430",
    "Sale / Valuation Date": "06-12-2022 00:00:00",
    "Sale / Market Rate": "146.14",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "146140",
    "Realized (Profit/ Loss)": "17710",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "17710",
    "Return": "13.79",
    "Days": "106",
    "Ann Ret%": "47.48",
    "Weightage": "0.0078",
    "Wtg*Ret": "0.370344",
    "Transaction": "0",
    "Sale Value": "146140",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "128430",
    "Status": "0"
  },
  {
    "S/N": "28",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "23-08-2022 00:00:00",
    "QTY": "1000",
    "Rate": "127.07",
    "Net Purchase Value": "127070",
    "Sale / Valuation Date": "02-12-2022 00:00:00",
    "Sale / Market Rate": "142.5",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "142500",
    "Realized (Profit/ Loss)": "15430",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "15430",
    "Return": "12.14",
    "Days": "101",
    "Ann Ret%": "43.87",
    "Weightage": "0.0078",
    "Wtg*Ret": "0.342186",
    "Transaction": "0",
    "Sale Value": "142500",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "127070",
    "Status": "0"
  },
  {
    "S/N": "29",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "08-12-2022 00:00:00",
    "QTY": "1000",
    "Rate": "142.57",
    "Net Purchase Value": "142570",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "96.72",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "96720",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-45850",
    "Total (Profit/ Loss)": "-45850",
    "Return": "-32.16",
    "Days": "534",
    "Ann Ret%": "-21.98",
    "Weightage": "0.0087",
    "Wtg*Ret": "-0.191226",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "142570",
    "Status": "0"
  },
  {
    "S/N": "30",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "14-12-2022 00:00:00",
    "QTY": "1000",
    "Rate": "148.74",
    "Net Purchase Value": "148740",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "96.72",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "96720",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-52020",
    "Total (Profit/ Loss)": "-52020",
    "Return": "-34.97",
    "Days": "528",
    "Ann Ret%": "-24.17",
    "Weightage": "0.0091",
    "Wtg*Ret": "-0.219947",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "148740",
    "Status": "0"
  },
  {
    "S/N": "31",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "15-12-2022 00:00:00",
    "QTY": "1000",
    "Rate": "147.99",
    "Net Purchase Value": "147990",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "96.72",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "96720",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-51270",
    "Total (Profit/ Loss)": "-51270",
    "Return": "-34.64",
    "Days": "527",
    "Ann Ret%": "-23.99",
    "Weightage": "0.009",
    "Wtg*Ret": "-0.21591",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "147990",
    "Status": "0"
  },
  {
    "S/N": "32",
    "Name of Script": "IBULHSGFIN.NS",
    "Ass Name": "a a a",
    "Purchase Date": "26-12-2022 00:00:00",
    "QTY": "1000",
    "Rate": "134.04",
    "Net Purchase Value": "134040",
    "Sale / Valuation Date": "29-12-2022 00:00:00",
    "Sale / Market Rate": "153.52",
    "Current Market Rate": "96.72",
    "Net Sale / Market Value": "153520",
    "Realized (Profit/ Loss)": "19480",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19480",
    "Return": "14.53",
    "Days": "3",
    "Ann Ret%": "1767.82",
    "Weightage": "0.0082",
    "Wtg*Ret": "14.496124",
    "Transaction": "0",
    "Sale Value": "153520",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "134040",
    "Status": "0"
  },
  {
    "S/N": "33",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "06-05-2022 00:00:00",
    "QTY": "200",
    "Rate": "917",
    "Net Purchase Value": "183400",
    "Sale / Valuation Date": "28-07-2022 00:00:00",
    "Sale / Market Rate": "1016.09",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "203218",
    "Realized (Profit/ Loss)": "19818",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19818",
    "Return": "10.81",
    "Days": "83",
    "Ann Ret%": "47.54",
    "Weightage": "0.0112",
    "Wtg*Ret": "0.532448",
    "Transaction": "0",
    "Sale Value": "203218",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "183400",
    "Status": "0"
  },
  {
    "S/N": "34",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "04-04-2022 00:00:00",
    "QTY": "200",
    "Rate": "969.86",
    "Net Purchase Value": "193972",
    "Sale / Valuation Date": "02-08-2022 00:00:00",
    "Sale / Market Rate": "1067.39",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "213478",
    "Realized (Profit/ Loss)": "19506",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19506",
    "Return": "10.06",
    "Days": "120",
    "Ann Ret%": "30.6",
    "Weightage": "0.0118",
    "Wtg*Ret": "0.36108",
    "Transaction": "0",
    "Sale Value": "213478",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "193972",
    "Status": "0"
  },
  {
    "S/N": "35",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "07-04-2022 00:00:00",
    "QTY": "200",
    "Rate": "974.87",
    "Net Purchase Value": "194974",
    "Sale / Valuation Date": "10-08-2022 00:00:00",
    "Sale / Market Rate": "1060.56",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "212112",
    "Realized (Profit/ Loss)": "17138",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "17138",
    "Return": "8.79",
    "Days": "125",
    "Ann Ret%": "25.67",
    "Weightage": "0.0119",
    "Wtg*Ret": "0.305473",
    "Transaction": "0",
    "Sale Value": "212112",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "194974",
    "Status": "0"
  },
  {
    "S/N": "36",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "19-10-2021 00:00:00",
    "QTY": "300",
    "Rate": "1217.57",
    "Net Purchase Value": "365271",
    "Sale / Valuation Date": "18-10-2022 00:00:00",
    "Sale / Market Rate": "1217.57",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "365271",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "0",
    "Return": "0",
    "Days": "364",
    "Ann Ret%": "0",
    "Weightage": "0.0223",
    "Wtg*Ret": "0",
    "Transaction": "0",
    "Sale Value": "365271",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "365271",
    "Status": "0"
  },
  {
    "S/N": "37",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "08-11-2021 00:00:00",
    "QTY": "200",
    "Rate": "1060.01",
    "Net Purchase Value": "212002",
    "Sale / Valuation Date": "13-09-2022 00:00:00",
    "Sale / Market Rate": "1158.74",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "231748",
    "Realized (Profit/ Loss)": "19746",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19746",
    "Return": "9.31",
    "Days": "309",
    "Ann Ret%": "11",
    "Weightage": "0.0129",
    "Wtg*Ret": "0.1419",
    "Transaction": "0",
    "Sale Value": "231748",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "212002",
    "Status": "0"
  },
  {
    "S/N": "38",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "12-11-2021 00:00:00",
    "QTY": "400",
    "Rate": "1039.55",
    "Net Purchase Value": "415820",
    "Sale / Valuation Date": "19-08-2022 00:00:00",
    "Sale / Market Rate": "1065.35",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "426140",
    "Realized (Profit/ Loss)": "10320",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "10320",
    "Return": "2.48",
    "Days": "280",
    "Ann Ret%": "3.23",
    "Weightage": "0.0254",
    "Wtg*Ret": "0.082042",
    "Transaction": "0",
    "Sale Value": "426140",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "415820",
    "Status": "0"
  },
  {
    "S/N": "39",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "16-02-2022 00:00:00",
    "QTY": "200",
    "Rate": "976.28",
    "Net Purchase Value": "195256",
    "Sale / Valuation Date": "11-08-2022 00:00:00",
    "Sale / Market Rate": "1075.87",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "215174",
    "Realized (Profit/ Loss)": "19918",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19918",
    "Return": "10.2",
    "Days": "176",
    "Ann Ret%": "21.15",
    "Weightage": "0.0119",
    "Wtg*Ret": "0.251685",
    "Transaction": "0",
    "Sale Value": "215174",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "195256",
    "Status": "0"
  },
  {
    "S/N": "40",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "23-03-2022 00:00:00",
    "QTY": "250",
    "Rate": "940.27",
    "Net Purchase Value": "235067.5",
    "Sale / Valuation Date": "02-05-2022 00:00:00",
    "Sale / Market Rate": "1016.14",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "254035",
    "Realized (Profit/ Loss)": "18968",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "18967.5",
    "Return": "8.07",
    "Days": "40",
    "Ann Ret%": "73.64",
    "Weightage": "0.0143",
    "Wtg*Ret": "1.053052",
    "Transaction": "0",
    "Sale Value": "254035",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "235067.5",
    "Status": "0"
  },
  {
    "S/N": "41",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "24-03-2022 00:00:00",
    "QTY": "200",
    "Rate": "934.75",
    "Net Purchase Value": "186950",
    "Sale / Valuation Date": "29-07-2022 00:00:00",
    "Sale / Market Rate": "1032.6",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "206520",
    "Realized (Profit/ Loss)": "19570",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19570",
    "Return": "10.47",
    "Days": "127",
    "Ann Ret%": "30.09",
    "Weightage": "0.0114",
    "Wtg*Ret": "0.343026",
    "Transaction": "0",
    "Sale Value": "206520",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "186950",
    "Status": "0"
  },
  {
    "S/N": "42",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "25-03-2022 00:00:00",
    "QTY": "200",
    "Rate": "925.73",
    "Net Purchase Value": "185146",
    "Sale / Valuation Date": "04-05-2022 00:00:00",
    "Sale / Market Rate": "1021.52",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "204304",
    "Realized (Profit/ Loss)": "19158",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19158",
    "Return": "10.35",
    "Days": "40",
    "Ann Ret%": "94.44",
    "Weightage": "0.0113",
    "Wtg*Ret": "1.067172",
    "Transaction": "0",
    "Sale Value": "204304",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "185146",
    "Status": "0"
  },
  {
    "S/N": "43",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "28-09-2022 00:00:00",
    "QTY": "200",
    "Rate": "1155.82",
    "Net Purchase Value": "231164",
    "Sale / Valuation Date": "14-12-2022 00:00:00",
    "Sale / Market Rate": "1249.98",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "249996",
    "Realized (Profit/ Loss)": "18832",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "18832",
    "Return": "8.15",
    "Days": "77",
    "Ann Ret%": "38.63",
    "Weightage": "0.0141",
    "Wtg*Ret": "0.544683",
    "Transaction": "0",
    "Sale Value": "249996",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "231164",
    "Status": "0"
  },
  {
    "S/N": "44",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "17-10-2022 00:00:00",
    "QTY": "300",
    "Rate": "1193.17",
    "Net Purchase Value": "357951",
    "Sale / Valuation Date": "15-12-2022 00:00:00",
    "Sale / Market Rate": "1241.5",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "372450",
    "Realized (Profit/ Loss)": "14499",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "14499",
    "Return": "4.05",
    "Days": "59",
    "Ann Ret%": "25.06",
    "Weightage": "0.0218",
    "Wtg*Ret": "0.546308",
    "Transaction": "0",
    "Sale Value": "372450",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "357951",
    "Status": "0"
  },
  {
    "S/N": "45",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "27-10-2022 00:00:00",
    "QTY": "200",
    "Rate": "1143.42",
    "Net Purchase Value": "228684",
    "Sale / Valuation Date": "13-12-2022 00:00:00",
    "Sale / Market Rate": "1232.93",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "246586",
    "Realized (Profit/ Loss)": "17902",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "17902",
    "Return": "7.83",
    "Days": "47",
    "Ann Ret%": "60.81",
    "Weightage": "0.014",
    "Wtg*Ret": "0.85134",
    "Transaction": "0",
    "Sale Value": "246586",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "228684",
    "Status": "0"
  },
  {
    "S/N": "46",
    "Name of Script": "INDUSINDBK.NS",
    "Ass Name": "a a a",
    "Purchase Date": "08-12-2022 00:00:00",
    "QTY": "200",
    "Rate": "1179.92",
    "Net Purchase Value": "235984",
    "Sale / Valuation Date": "15-12-2022 00:00:00",
    "Sale / Market Rate": "1241.04",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "248208",
    "Realized (Profit/ Loss)": "12224",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "12224",
    "Return": "5.18",
    "Days": "7",
    "Ann Ret%": "270.1",
    "Weightage": "0.0144",
    "Wtg*Ret": "3.88944",
    "Transaction": "0",
    "Sale Value": "248208",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "235984",
    "Status": "0"
  },
  {
    "S/N": "47",
    "Name of Script": "INFY.NS",
    "Ass Name": "a a a",
    "Purchase Date": "30-08-2022 00:00:00",
    "QTY": "100",
    "Rate": "1478.31",
    "Net Purchase Value": "147831",
    "Sale / Valuation Date": "30-11-2022 00:00:00",
    "Sale / Market Rate": "1637.54",
    "Current Market Rate": "1372.54",
    "Net Sale / Market Value": "163754",
    "Realized (Profit/ Loss)": "15923",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "15923",
    "Return": "10.77",
    "Days": "92",
    "Ann Ret%": "42.73",
    "Weightage": "0.009",
    "Wtg*Ret": "0.38457",
    "Transaction": "0",
    "Sale Value": "163754",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "147831",
    "Status": "0"
  },
  {
    "S/N": "48",
    "Name of Script": "INFY.NS",
    "Ass Name": "a a a",
    "Purchase Date": "19-09-2022 00:00:00",
    "QTY": "100",
    "Rate": "1403.14",
    "Net Purchase Value": "140314",
    "Sale / Valuation Date": "11-11-2022 00:00:00",
    "Sale / Market Rate": "1565.53",
    "Current Market Rate": "1372.54",
    "Net Sale / Market Value": "156553",
    "Realized (Profit/ Loss)": "16239",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "16239",
    "Return": "11.57",
    "Days": "53",
    "Ann Ret%": "79.68",
    "Weightage": "0.0086",
    "Wtg*Ret": "0.685248",
    "Transaction": "0",
    "Sale Value": "156553",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "140314",
    "Status": "0"
  },
  {
    "S/N": "49",
    "Name of Script": "LT.NS",
    "Ass Name": "a a a",
    "Purchase Date": "02-05-2022 00:00:00",
    "QTY": "100",
    "Rate": "1681.95",
    "Net Purchase Value": "168195",
    "Sale / Valuation Date": "12-08-2022 00:00:00",
    "Sale / Market Rate": "1839.81",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "183981",
    "Realized (Profit/ Loss)": "15786",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "15786",
    "Return": "9.39",
    "Days": "102",
    "Ann Ret%": "33.6",
    "Weightage": "0.0103",
    "Wtg*Ret": "0.34608",
    "Transaction": "0",
    "Sale Value": "183981",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "168195",
    "Status": "0"
  },
  {
    "S/N": "50",
    "Name of Script": "LT.NS",
    "Ass Name": "a a a",
    "Purchase Date": "21-01-2022 00:00:00",
    "QTY": "200",
    "Rate": "1992.87",
    "Net Purchase Value": "398574",
    "Sale / Valuation Date": "07-12-2022 00:00:00",
    "Sale / Market Rate": "2125.87",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "425174",
    "Realized (Profit/ Loss)": "26600",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "26600",
    "Return": "6.67",
    "Days": "320",
    "Ann Ret%": "7.61",
    "Weightage": "0.0243",
    "Wtg*Ret": "0.184923",
    "Transaction": "0",
    "Sale Value": "425174",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "398574",
    "Status": "0"
  },
  {
    "S/N": "51",
    "Name of Script": "LT.NS",
    "Ass Name": "a a a",
    "Purchase Date": "24-01-2022 00:00:00",
    "QTY": "100",
    "Rate": "1899.59",
    "Net Purchase Value": "189959",
    "Sale / Valuation Date": "16-11-2022 00:00:00",
    "Sale / Market Rate": "1995.4",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "199540",
    "Realized (Profit/ Loss)": "9581",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "9581",
    "Return": "5.04",
    "Days": "296",
    "Ann Ret%": "6.21",
    "Weightage": "0.0116",
    "Wtg*Ret": "0.072036",
    "Transaction": "0",
    "Sale Value": "199540",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "189959",
    "Status": "0"
  },
  {
    "S/N": "52",
    "Name of Script": "LT.NS",
    "Ass Name": "a a a",
    "Purchase Date": "14-11-2022 00:00:00",
    "QTY": "100",
    "Rate": "2004.27",
    "Net Purchase Value": "200427",
    "Sale / Valuation Date": "07-12-2022 00:00:00",
    "Sale / Market Rate": "2129.21",
    "Current Market Rate": "0",
    "Net Sale / Market Value": "212921",
    "Realized (Profit/ Loss)": "12494",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "12494",
    "Return": "6.23",
    "Days": "23",
    "Ann Ret%": "98.87",
    "Weightage": "0.0122",
    "Wtg*Ret": "1.206214",
    "Transaction": "0",
    "Sale Value": "212921",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "200427",
    "Status": "0"
  },
  {
    "S/N": "53",
    "Name of Script": "MARUTI.NS",
    "Ass Name": "a a a",
    "Purchase Date": "04-01-2023 00:00:00",
    "QTY": "30",
    "Rate": "8451.97",
    "Net Purchase Value": "253559.1",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "8214.84",
    "Current Market Rate": "8214.84",
    "Net Sale / Market Value": "246445.2",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-7113.89999999999",
    "Total (Profit/ Loss)": "-7113.9",
    "Return": "-2.81",
    "Days": "507",
    "Ann Ret%": "-2.02",
    "Weightage": "0.0155",
    "Wtg*Ret": "-0.03131",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "253559.1",
    "Status": "0"
  },
  {
    "S/N": "54",
    "Name of Script": "MARUTI.NS",
    "Ass Name": "a a a",
    "Purchase Date": "03-10-2022 00:00:00",
    "QTY": "25",
    "Rate": "8585.36",
    "Net Purchase Value": "214634",
    "Sale / Valuation Date": "28-10-2022 00:00:00",
    "Sale / Market Rate": "9353.64",
    "Current Market Rate": "8214.84",
    "Net Sale / Market Value": "233841",
    "Realized (Profit/ Loss)": "19207",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "19207",
    "Return": "8.95",
    "Days": "25",
    "Ann Ret%": "130.67",
    "Weightage": "0.0131",
    "Wtg*Ret": "1.711777",
    "Transaction": "0",
    "Sale Value": "233841",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "214634",
    "Status": "0"
  },
  {
    "S/N": "55",
    "Name of Script": "MARUTI.NS",
    "Ass Name": "a a a",
    "Purchase Date": "14-12-2022 00:00:00",
    "QTY": "50",
    "Rate": "8653.08",
    "Net Purchase Value": "432654",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "8214.84",
    "Current Market Rate": "8214.84",
    "Net Sale / Market Value": "410742",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-21912",
    "Total (Profit/ Loss)": "-21912",
    "Return": "-5.06",
    "Days": "528",
    "Ann Ret%": "-3.5",
    "Weightage": "0.0264",
    "Wtg*Ret": "-0.0924",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "432654",
    "Status": "0"
  },
  {
    "S/N": "56",
    "Name of Script": "MARUTI.NS",
    "Ass Name": "a a a",
    "Purchase Date": "16-12-2022 00:00:00",
    "QTY": "30",
    "Rate": "8567.17",
    "Net Purchase Value": "257015.1",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "8214.84",
    "Current Market Rate": "8214.84",
    "Net Sale / Market Value": "246445.2",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-10569.9",
    "Total (Profit/ Loss)": "-10569.9",
    "Return": "-4.11",
    "Days": "526",
    "Ann Ret%": "-2.85",
    "Weightage": "0.0157",
    "Wtg*Ret": "-0.044745",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "257015.1",
    "Status": "0"
  },
  {
    "S/N": "57",
    "Name of Script": "MARUTI.NS",
    "Ass Name": "a a a",
    "Purchase Date": "19-12-2022 00:00:00",
    "QTY": "25",
    "Rate": "8568.16",
    "Net Purchase Value": "214204",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "8214.84",
    "Current Market Rate": "8214.84",
    "Net Sale / Market Value": "205371",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-8833",
    "Total (Profit/ Loss)": "-8833",
    "Return": "-4.12",
    "Days": "523",
    "Ann Ret%": "-2.88",
    "Weightage": "0.0131",
    "Wtg*Ret": "-0.037728",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "214204",
    "Status": "0"
  },
  {
    "S/N": "58",
    "Name of Script": "MARUTI.NS",
    "Ass Name": "a a a",
    "Purchase Date": "22-12-2022 00:00:00",
    "QTY": "30",
    "Rate": "8330.3",
    "Net Purchase Value": "249909",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "8214.84",
    "Current Market Rate": "8214.84",
    "Net Sale / Market Value": "246445.2",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-3463.79999999999",
    "Total (Profit/ Loss)": "-3463.8",
    "Return": "-1.39",
    "Days": "520",
    "Ann Ret%": "-0.98",
    "Weightage": "0.0152",
    "Wtg*Ret": "-0.014896",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "249909",
    "Status": "0"
  },
  {
    "S/N": "59",
    "Name of Script": "MARUTI.NS",
    "Ass Name": "a a a",
    "Purchase Date": "30-12-2022 00:00:00",
    "QTY": "35",
    "Rate": "8435.89",
    "Net Purchase Value": "295256.15",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "8214.84",
    "Current Market Rate": "8214.84",
    "Net Sale / Market Value": "287519.4",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-7736.75",
    "Total (Profit/ Loss)": "-7736.75",
    "Return": "-2.62",
    "Days": "512",
    "Ann Ret%": "-1.87",
    "Weightage": "0.018",
    "Wtg*Ret": "-0.03366",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "295256.15",
    "Status": "0"
  },
  {
    "S/N": "60",
    "Name of Script": "NATIONALUM.NS",
    "Ass Name": "a a a",
    "Purchase Date": "22-04-2022 00:00:00",
    "QTY": "2000",
    "Rate": "117.65",
    "Net Purchase Value": "235300",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "77.61",
    "Current Market Rate": "77.61",
    "Net Sale / Market Value": "155220",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-80080",
    "Total (Profit/ Loss)": "-80080",
    "Return": "-34.03",
    "Days": "764",
    "Ann Ret%": "-16.26",
    "Weightage": "0.0144",
    "Wtg*Ret": "-0.234144",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "235300",
    "Status": "0"
  },
  {
    "S/N": "61",
    "Name of Script": "NATIONALUM.NS",
    "Ass Name": "a a a",
    "Purchase Date": "08-04-2022 00:00:00",
    "QTY": "2000",
    "Rate": "126.82",
    "Net Purchase Value": "253640",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "77.61",
    "Current Market Rate": "77.61",
    "Net Sale / Market Value": "155220",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-98420",
    "Total (Profit/ Loss)": "-98420",
    "Return": "-38.8",
    "Days": "778",
    "Ann Ret%": "-18.2",
    "Weightage": "0.0155",
    "Wtg*Ret": "-0.2821",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "253640",
    "Status": "0"
  },
  {
    "S/N": "62",
    "Name of Script": "NATIONALUM.NS",
    "Ass Name": "a a a",
    "Purchase Date": "17-03-2022 00:00:00",
    "QTY": "2000",
    "Rate": "118.46",
    "Net Purchase Value": "236920",
    "Sale / Valuation Date": "06-04-2022 00:00:00",
    "Sale / Market Rate": "131.23",
    "Current Market Rate": "77.61",
    "Net Sale / Market Value": "262460",
    "Realized (Profit/ Loss)": "25540",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "25540",
    "Return": "10.78",
    "Days": "20",
    "Ann Ret%": "196.74",
    "Weightage": "0.0145",
    "Wtg*Ret": "2.85273",
    "Transaction": "0",
    "Sale Value": "262460",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "236920",
    "Status": "0"
  },
  {
    "S/N": "63",
    "Name of Script": "NATIONALUM.NS",
    "Ass Name": "a a a",
    "Purchase Date": "09-05-2022 00:00:00",
    "QTY": "2000",
    "Rate": "95.43",
    "Net Purchase Value": "190860",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "77.61",
    "Current Market Rate": "77.61",
    "Net Sale / Market Value": "155220",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-35640",
    "Total (Profit/ Loss)": "-35640",
    "Return": "-18.67",
    "Days": "747",
    "Ann Ret%": "-9.12",
    "Weightage": "0.0116",
    "Wtg*Ret": "-0.105792",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "190860",
    "Status": "0"
  },
  {
    "S/N": "64",
    "Name of Script": "NATIONALUM.NS",
    "Ass Name": "a a a",
    "Purchase Date": "15-06-2022 00:00:00",
    "QTY": "2000",
    "Rate": "85.25",
    "Net Purchase Value": "170500",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "77.61",
    "Current Market Rate": "77.61",
    "Net Sale / Market Value": "155220",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-15280",
    "Total (Profit/ Loss)": "-15280",
    "Return": "-8.96",
    "Days": "710",
    "Ann Ret%": "-4.61",
    "Weightage": "0.0104",
    "Wtg*Ret": "-0.047944",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "170500",
    "Status": "0"
  },
  {
    "S/N": "65",
    "Name of Script": "NATIONALUM.NS",
    "Ass Name": "a a a",
    "Purchase Date": "28-11-2022 00:00:00",
    "QTY": "3000",
    "Rate": "74.72",
    "Net Purchase Value": "224160",
    "Sale / Valuation Date": "30-12-2022 00:00:00",
    "Sale / Market Rate": "82.07",
    "Current Market Rate": "77.61",
    "Net Sale / Market Value": "246210",
    "Realized (Profit/ Loss)": "22050",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "22050",
    "Return": "9.84",
    "Days": "32",
    "Ann Ret%": "112.24",
    "Weightage": "0.0137",
    "Wtg*Ret": "1.537688",
    "Transaction": "0",
    "Sale Value": "246210",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "224160",
    "Status": "0"
  },
  {
    "S/N": "66",
    "Name of Script": "TATAMOTORS.NS",
    "Ass Name": "a a a",
    "Purchase Date": "22-09-2021 00:00:00",
    "QTY": "1000",
    "Rate": "508.19",
    "Net Purchase Value": "508190",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "419.49",
    "Current Market Rate": "419.49",
    "Net Sale / Market Value": "419490",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-88700",
    "Total (Profit/ Loss)": "-88700",
    "Return": "-17.45",
    "Days": "976",
    "Ann Ret%": "-6.53",
    "Weightage": "0.031",
    "Wtg*Ret": "-0.20243",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "508190",
    "Status": "0"
  },
  {
    "S/N": "67",
    "Name of Script": "TATAMOTORS.NS",
    "Ass Name": "a a a",
    "Purchase Date": "15-03-2022 00:00:00",
    "QTY": "500",
    "Rate": "422.24",
    "Net Purchase Value": "211120",
    "Sale / Valuation Date": "01-08-2022 00:00:00",
    "Sale / Market Rate": "464.89",
    "Current Market Rate": "419.49",
    "Net Sale / Market Value": "232445",
    "Realized (Profit/ Loss)": "21325",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "21325",
    "Return": "10.1",
    "Days": "139",
    "Ann Ret%": "26.52",
    "Weightage": "0.0129",
    "Wtg*Ret": "0.342108",
    "Transaction": "0",
    "Sale Value": "232445",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "211120",
    "Status": "0"
  },
  {
    "S/N": "68",
    "Name of Script": "TATAMOTORS.NS",
    "Ass Name": "a a a",
    "Purchase Date": "26-09-2022 00:00:00",
    "QTY": "500",
    "Rate": "397.77",
    "Net Purchase Value": "198885",
    "Sale / Valuation Date": "07-11-2022 00:00:00",
    "Sale / Market Rate": "433.78",
    "Current Market Rate": "419.49",
    "Net Sale / Market Value": "216890",
    "Realized (Profit/ Loss)": "18005",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "18005",
    "Return": "9.05",
    "Days": "42",
    "Ann Ret%": "78.65",
    "Weightage": "0.0121",
    "Wtg*Ret": "0.951665",
    "Transaction": "0",
    "Sale Value": "216890",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "198885",
    "Status": "0"
  },
  {
    "S/N": "69",
    "Name of Script": "TATAMOTORS.NS",
    "Ass Name": "a a a",
    "Purchase Date": "18-10-2022 00:00:00",
    "QTY": "1000",
    "Rate": "407.05",
    "Net Purchase Value": "407050",
    "Sale / Valuation Date": "09-11-2022 00:00:00",
    "Sale / Market Rate": "432.93",
    "Current Market Rate": "419.49",
    "Net Sale / Market Value": "432930",
    "Realized (Profit/ Loss)": "25880",
    "Unrealized (Profit/ Loss)": "0",
    "Total (Profit/ Loss)": "25880",
    "Return": "6.36",
    "Days": "22",
    "Ann Ret%": "105.52",
    "Weightage": "0.0248",
    "Wtg*Ret": "2.616896",
    "Transaction": "0",
    "Sale Value": "432930",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "407050",
    "Status": "0"
  },
  {
    "S/N": "70",
    "Name of Script": "TECHM.NS",
    "Ass Name": "a a a",
    "Purchase Date": "16-09-2022 00:00:00",
    "QTY": "200",
    "Rate": "1052.46",
    "Net Purchase Value": "210492",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "1046.1",
    "Current Market Rate": "1046.1",
    "Net Sale / Market Value": "209220",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-1272",
    "Total (Profit/ Loss)": "-1272",
    "Return": "-0.6",
    "Days": "617",
    "Ann Ret%": "-0.35",
    "Weightage": "0.0128",
    "Wtg*Ret": "-0.00448",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "210492",
    "Status": "0"
  },
  {
    "S/N": "71",
    "Name of Script": "WIPRO.NS",
    "Ass Name": "a a a",
    "Purchase Date": "15-09-2022 00:00:00",
    "QTY": "1000",
    "Rate": "414.94",
    "Net Purchase Value": "414940",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "365.25",
    "Current Market Rate": "365.25",
    "Net Sale / Market Value": "365250",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-49690",
    "Total (Profit/ Loss)": "-49690",
    "Return": "-11.98",
    "Days": "618",
    "Ann Ret%": "-7.08",
    "Weightage": "0.0253",
    "Wtg*Ret": "-0.179124",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "414940",
    "Status": "0"
  },
  {
    "S/N": "72",
    "Name of Script": "WIPRO.NS",
    "Ass Name": "a a a",
    "Purchase Date": "06-09-2022 00:00:00",
    "QTY": "500",
    "Rate": "403.14",
    "Net Purchase Value": "201570",
    "Sale / Valuation Date": "25-05-2024 00:00:00",
    "Sale / Market Rate": "365.25",
    "Current Market Rate": "365.25",
    "Net Sale / Market Value": "182625",
    "Realized (Profit/ Loss)": "0",
    "Unrealized (Profit/ Loss)": "-18945",
    "Total (Profit/ Loss)": "-18945",
    "Return": "-9.4",
    "Days": "627",
    "Ann Ret%": "-5.47",
    "Weightage": "0.0123",
    "Wtg*Ret": "-0.067281",
    "Transaction": "0",
    "Sale Value": "0",
    "STT Charges": "0",
    "Other Charges": "0",
    "Purchase Value": "201570",
    "Status": "0"
  }
]

import pandas as pd
# Convert null values to None in Python and replace "null" with "0"
json_data = json.dumps(json_data)
json_data = json.loads(json_data, parse_constant=lambda x: 0)  # Replace "null" with "0"
data = pd.DataFrame(json_data)
print(data)



# # Display the DataFrame
# print(df)

# file_name = r"C:\Users\Sinewave#2022\Downloads\stock_portfolio_transformed.xlsx"
#
# # Process the uploaded file
# dt = pd.read_excel(file_name)
# Sort the DataFrame by 'Purchase Date'
# Convert 'Purchase Date' and 'Sale / Valuation Date' to datetime format
data['Purchase Date'] = pd.to_datetime(data['Purchase Date'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d')
data['Sale / Valuation Date'] = pd.to_datetime(data['Sale / Valuation Date'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d')

# Ensure 'QTY' is numeric
data['QTY'] = pd.to_numeric(data['QTY'])

# Sort values by 'Purchase Date'
data.sort_values(by='Purchase Date', inplace=True)

close_prices_with_qty = pd.DataFrame()

for index, row in data.iterrows():
    script = row['Name of Script']
    purchase_date = row['Purchase Date']
    sell_date = row['Sale / Valuation Date']
    qty = row['QTY']

    stock_data = yf.download(script, start=purchase_date, end=sell_date)
    close_price = stock_data['Close']

    close_price_with_qty = pd.DataFrame({
        script: close_price.values,
        script + '_QTY': qty,
        script + '_Value': qty * close_price,
    }, index=close_price.index)

    close_prices_with_qty = pd.concat([close_prices_with_qty, close_price_with_qty], axis=1)

merged_df = close_prices_with_qty.groupby(level=0, axis=1).sum()
merged_df.reset_index(inplace=True)
close_prices_with_qty = merged_df

ns_columns = [col for col in merged_df.columns if col.endswith('.NS')]

ns_columns_df = merged_df[ns_columns]

close_prices_with_qty.set_index('Date', inplace=True)

date_column = close_prices_with_qty.index

ns_columns_df.insert(0, 'Date', date_column)

stocks = ns_columns_df.columns[1:]  # Pehla column 'Date' hai isliye 1 se start karo

stock_data = {}

for stock in stocks:
    non_zero_rows = ns_columns_df[ns_columns_df[stock] != 0]
    # Start date
    start_date = non_zero_rows['Date'].iloc[0]
    # End date
    end_date = non_zero_rows['Date'].iloc[-1]
    stock_prices = yf.download(stock, start=start_date, end=end_date)['Close']  # Stock ka close price
    stock_data[stock] = stock_prices

stock_prices_df = pd.DataFrame(stock_data)

stock_prices_df = stock_prices_df.reindex(close_prices_with_qty.index)

for column in stock_prices_df.columns:

    if column in close_prices_with_qty.columns:
        close_prices_with_qty[column] = stock_prices_df[column].values

close_prices_with_qty.reset_index(inplace=True)

close_prices_with_qty['Portfolio_Value'] = close_prices_with_qty.filter(like='_Value').sum(axis=1)
close_prices_with_qty['Portfolio_Return'] = close_prices_with_qty['Portfolio_Value'].pct_change()

first_purchase_date_processed = False
for index, row in data.iterrows():
    purchase_date = row['Purchase Date']
    purchase_price = row['Rate']
    purchase_QTY = row['QTY']

    # Convert purchase_price from string to float
    purchase_price = float(purchase_price)

    if purchase_date in data['Purchase Date'].values:
        # Convert purchase_date to a datetime object
        purchase_date = pd.to_datetime(purchase_date)

        # Initialize a flag to check if a matching row was found
        match_found = False
        day_increment = 1

        # Loop until a match is found or a reasonable limit is reached
        while not match_found and day_increment <= 30:  # Limit to 30 days
            potential_date = purchase_date + pd.Timedelta(days=day_increment)
            matched_rows = close_prices_with_qty[close_prices_with_qty['Date'] == potential_date]

            if not matched_rows.empty:
                row_index = matched_rows.index[0]
                portfolio_value = close_prices_with_qty.loc[row_index, 'Portfolio_Value']
                net_purchase_value = purchase_price * purchase_QTY

                try:
                    previous_day_portfolio_value = close_prices_with_qty.iloc[row_index - 1]['Portfolio_Value']
                except KeyError:
                    previous_day_portfolio_value = 0

                denominator = net_purchase_value + previous_day_portfolio_value
                result = portfolio_value / denominator / 100

                close_prices_with_qty.at[row_index, 'Portfolio_Return'] = result

                match_found = True
            else:
                day_increment += 1

        if not match_found:
            print(f"No matching row found within 30 days for purchase date: {purchase_date}")

        # Example usage of first_purchase_date_processed
        if not first_purchase_date_processed:
            first_purchase_date_processed = True


sell_transactions_grouped = data[data['Sale / Valuation Date'] >= '11/07/2023'].groupby(
    'Sale / Valuation Date')

for sell_date, group_data in sell_transactions_grouped:
    sell_date_np = np.datetime64(sell_date)

    if sell_date_np in close_prices_with_qty['Date'].values:
        row_index = close_prices_with_qty[close_prices_with_qty['Date'] == sell_date].index[0]
        portfolio_value = close_prices_with_qty.loc[row_index, 'Portfolio_Value']

        if sell_date in data['Purchase Date'].values:
            purchase_data = data[data['Purchase Date'] == sell_date]
            group_data['Net Sale / Market Value'] = group_data['Net Sale / Market Value'].astype(float)
            purchase_data['Net Purchase Value'] = purchase_data['Net Purchase Value'].astype(float)
            net_transaction_value = group_data['Net Sale / Market Value'].sum() - purchase_data[
                'Net Purchase Value'].sum()
        else:
            net_transaction_value = group_data['Net Sale / Market Value'].sum()

        try:
            previous_day_portfolio_value = close_prices_with_qty.iloc[row_index - 1]['Portfolio_Value']
        except KeyError:
            previous_day_portfolio_value = 0

        previous_day_portfolio_value = np.array(previous_day_portfolio_value, dtype=float)

        # Ensure net_transaction_value is a float
        net_transaction_value = float(net_transaction_value)

        denominator = previous_day_portfolio_value - net_transaction_value
        result = portfolio_value / denominator / 100

        close_prices_with_qty.at[row_index, 'Portfolio_Return'] = result

rolling_std_dev = close_prices_with_qty['Portfolio_Return'].rolling(window=30).std()
close_prices_with_qty['Portfolio_std_dev'] = rolling_std_dev

rolling_sharpe_ratio = close_prices_with_qty['Portfolio_Return'].rolling(window=30).mean() / \
                       close_prices_with_qty['Portfolio_Return'].rolling(window=30).std()
close_prices_with_qty['Sharpe_Ratio'] = rolling_sharpe_ratio

rolling_max = close_prices_with_qty['Portfolio_Value'].cummax()
daily_drawdown = close_prices_with_qty['Portfolio_Value'] / rolling_max - 1
max_daily_drawdown = daily_drawdown.expanding(min_periods=1).min()
close_prices_with_qty['Max_Drawdown'] = max_daily_drawdown

close_prices_with_qty.fillna(0, inplace=True)

close_prices_with_qty.reset_index(inplace=True)

output_file = f'C:\\Users\\Sinewave#2022\\Downloads\\close_prices_with_qty.csv'
close_prices_with_qty.to_csv(output_file)
# Filter the DataFrame
filtered_df = merged_df[(merged_df['Date'] >= '2023-04-01') & (merged_df['Date'] <= '2024-03-31')]

# Convert 'Date' column to datetime
filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])

# Calculate cumulative return
filtered_df['Cumulative_Return'] = (1 + filtered_df['Portfolio_Return']).cumprod() - 1

# Calculate amplified standard deviation
amplification_factor = 50  # Adjust as needed
filtered_df['Amplified_Std_Dev'] = filtered_df['Portfolio_std_dev'] * amplification_factor

# Plotting
sns.set_style("whitegrid")
fig, ax1 = plt.subplots(figsize=(19, 10))

# Plot Cumulative Return
ax1.plot(filtered_df['Date'], filtered_df['Cumulative_Return'], color='blue', label='Cumulative Return')

# Plot Amplified Standard Deviation
ax1.plot(filtered_df['Date'], filtered_df['Amplified_Std_Dev'], color='red', linestyle='--', label='Amplified Standard Deviation')

# Set labels and tick parameters for ax1
ax1.set_xlabel('Date')
ax1.set_ylabel('Cumulative Return and Amplified Standard Deviation', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a twin axis for Sharpe Ratio
ax2 = ax1.twinx()

# Plot Sharpe Ratio
ax2.plot(filtered_df['Date'], filtered_df['Sharpe_Ratio'], color='green', linestyle='-.', label='Sharpe Ratio')

# Set labels and tick parameters for ax2
ax2.set_ylabel('Sharpe Ratio', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', bbox_to_anchor=(0.05, 0.95))

# Title of the plot
plt.title('Cumulative Return, Amplified Standard Deviation, and Sharpe Ratio')

# Add a short delay to allow the plot to fully render
time.sleep(1)  # Adjust the delay time as needed

# Define the path to save the plot
download_path = os.path.expanduser('~/Downloads/plot.png')

# Save the plot
plt.savefig(download_path)

# Close plot after displaying
plt.close()



