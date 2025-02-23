import json
from jsonschema import validate, exceptions

# Your JSON schema
your_schema = {
	"$schema": "http://json-schema.org/draft-04/schema#",
	"type": "object",
	"additionalProperties": False,
	"properties": {
		"ITR": {
			"$ref": "#/definitions/ITR"
		}
	},
	"definitions": {
		"ITR": {
			"type": "object",
			"description": "This is root node. Irrespective of Individual or bulk IT returns filed.",
			"additionalProperties": False,
			"properties": {
				"ITR1": {
					"$ref": "#/definitions/ITR1"
				}
			},
			"required": [
				"ITR1"
			]
		},
		"ITR1": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"CreationInfo": {
					"$ref": "#/definitions/CreationInfo"
				},
				"Form_ITR1": {
					"$ref": "#/definitions/Form_ITR1"
				},
				"PersonalInfo": {
					"$ref": "#/definitions/PersonalInfo"
				},
				"FilingStatus": {
					"$ref": "#/definitions/FilingStatus"
				},
				"ITR1_IncomeDeductions": {
					"$ref": "#/definitions/ITR1_IncomeDeductions"
				},
				"ITR1_TaxComputation": {
					"$ref": "#/definitions/ITR1_TaxComputation"
				},
				"TaxPaid": {
					"$ref": "#/definitions/TaxPaid"
				},
				"Refund": {
					"$ref": "#/definitions/Refund"
				},
				"Schedule80G": {
					"$ref": "#/definitions/Schedule80G"
				},
				"Schedule80GGA": {
					"$ref": "#/definitions/Schedule80GGA"
				},
				"Schedule80GGC": {
					"$ref": "#/definitions/Schedule80GGC"
				},
				"Schedule80D": {
					"$ref": "#/definitions/Schedule80D"
				},
				"Schedule80DD": {
					"$ref": "#/definitions/Schedule80DD"
				},
				"Schedule80U": {
					"$ref": "#/definitions/Schedule80U"
				},
				"TDSonSalaries": {
					"$ref": "#/definitions/TDSonSalaries"
				},
				"TDSonOthThanSals": {
					"$ref": "#/definitions/TDSonOthThanSals"
				},
				"ScheduleTDS3Dtls": {
					"$ref": "#/definitions/ScheduleTDS3Dtls"
				},
				"ScheduleTCS": {
					"$ref": "#/definitions/ScheduleTCS"
				},
				"TaxPayments": {
					"$ref": "#/definitions/TaxPayments"
				},
				"Verification": {
					"$ref": "#/definitions/Verification"
				},
				"TaxReturnPreparer": {
					"$ref": "#/definitions/TaxReturnPreparer"
				}
			},
			"required": [
				"CreationInfo",
				"Form_ITR1",
				"PersonalInfo",
				"FilingStatus",
				"ITR1_IncomeDeductions",
				"ITR1_TaxComputation",
				"TaxPaid",
				"Refund",
				"Verification"
			]
		},
		"CreationInfo": {
			"type": "object",
			"description": "This element will be used by third party vendors and intermediaries to give details of their software or JSON creation.",
			"additionalProperties": False,
			"properties": {
				"SWVersionNo": {
					"maxLength": 10,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					],
					"default": "1.0"
				},
				"SWCreatedBy": {
					"pattern": "[S][W][0-9]{8}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"JSONCreatedBy": {
					"pattern": "[S][W][0-9]{8}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"JSONCreationDate": {
					"description": "JSONCreationDate in YYYY-MM-DD format",
					"type": "string",
					"pattern": "([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))"
				},
				"IntermediaryCity": {
					"maxLength": 25,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					],
					"default": "Delhi"
				},
				"Digest": {
					"pattern": "-|.{44}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				}
			},
			"required": [
				"SWVersionNo",
				"SWCreatedBy",
				"JSONCreatedBy",
				"JSONCreationDate",
				"IntermediaryCity",
				"Digest"
			]
		},
		"Form_ITR1": {
			"type": "object",
			"description": "This is the element identified for ITR-1, holding AY, Form and Schema version values.",
			"additionalProperties": False,
			"properties": {
				"FormName": {
					"pattern": "ITR-1",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"Description": {
					"maxLength": 75,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"AssessmentYear": {
					"maxLength": 4,
					"minLength": 4,
					"pattern": "2024",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"SchemaVer": {
					"maxLength": 10,
					"minLength": 1,
					"pattern": "Ver1.0",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"FormVer": {
					"maxLength": 10,
					"minLength": 1,
					"pattern": "Ver1.0",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				}
			},
			"required": [
				"FormName",
				"Description",
				"AssessmentYear",
				"SchemaVer",
				"FormVer"
			]
		},
		"PersonalInfo": {
			"type": "object",
			"description": "Enter personal information",
			"additionalProperties": False,
			"properties": {
				"AssesseeName": {
					"$ref": "#/definitions/AssesseeName"
				},
				"PAN": {
					"pattern": "[A-Z]{3}[P][A-Z][0-9]{4}[A-Z]",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"Address": {
					"$ref": "#/definitions/Address"
				},
				"DOB": {
					"description": "Date of Birth of the Assessee format YYYY-MM-DD; maximimum date allowed 2024-03-31",
					"type": "string",
					"pattern": "([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))"
				},
				"EmployerCategory": {
					"type": "string",
					"description": "CGOV:Central Government, SGOV:State Government, PSU:Public Sector Unit, PE:Pensioners - Central Government, PESG:Pensioners - State Government, PEPS:Pensioners - Public sector undertaking, PEO:Pensioners - Others, OTH:Others, NA:Not Applicable",
					"enum": [
						"CGOV",
						"SGOV",
						"PSU",
						"PE",
						"PESG",
						"PEPS",
						"PEO",
						"OTH",
						"NA"
					]
				},
				"AadhaarCardNo": {
					"pattern": "[0-9]{12}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"AadhaarEnrolmentId": {
					"pattern": "[0-9]{28}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				}
			},
			"required": [
				"AssesseeName",
				"PAN",
				"Address",
				"DOB",
				"EmployerCategory"
			]
		},
		"FilingStatus": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"ReturnFileSec": {
					"type": "integer",
					"description": "11 : 139(1)-On or before due date, 12 : 139(4)-After due date, 13 : 142(1), 14 : 148,  16 : 153C, 17 : 139(5)-Revised , 18 : 139(9), 20 : 119(2)(b)- after condonation of delay",
					"enum": [
						11,
						12,
						13,
						14,
						16,
						17,
						18,
						20
					],
					"maximum": 20,
					"minimum": 11,
					"exclusiveMinimum": False,
					"default": 11
				},
				"OptOutNewTaxRegime": {
					"pattern": "Y|N",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"SeventhProvisio139": {
					"pattern": "Y|N",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"IncrExpAggAmt2LkTrvFrgnCntryFlg": {
					"pattern": "Y|N",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"AmtSeventhProvisio139ii": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 200000,
					"exclusiveMinimum": False
				},
				"IncrExpAggAmt1LkElctrctyPrYrFlg": {
					"pattern": "Y|N",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"AmtSeventhProvisio139iii": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 100000,
					"exclusiveMinimum": False
				},
				"clauseiv7provisio139i": {
					"pattern": "Y|N",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"clauseiv7provisio139iDtls": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/clauseiv7provisio139iType"
					}
				},
				"ReceiptNo": {
					"type": "string",
					"description": "Enter the Acknowledgement number of the original return.",
					"pattern": "[0-9]{15}"
				},
				"NoticeNo": {
					"maxLength": 100,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"OrigRetFiledDate": {
					"type": "string",
					"description": "Enter Date of filing of Original return in YYYY-MM-DD format",
					"pattern": "([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))"
				},
				"NoticeDateUnderSec": {
					"type": "string",
					"description": "Enter Date of Notice or Order in YYYY-MM-DD format",
					"pattern": "([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))"
				},
				"ItrFilingDueDate":{
					"maxLength": 10,
					"minLength": 9,
					"pattern": "2024-07-31",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]

				}
			},
			"required": [
				"ReturnFileSec",
				"OptOutNewTaxRegime",
				"ItrFilingDueDate"
			]
		},
		"clauseiv7provisio139iType": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"clauseiv7provisio139iNature": {
					"type": "string",
					"description": "1 - the aggregate of tax deducted at source and tax collected at source during the previous year, in the case of the person, is twenty-five thousand rupees or more(fifty thousand for resident senior citizen); 2 - the deposit in one or more savings bank account of the person, in aggregate, is fifty lakh rupees or more, in the previous year",
					"enum": [
						"1",
						"2"
					]
				},
				"clauseiv7provisio139iAmount": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"clauseiv7provisio139iNature",
				"clauseiv7provisio139iAmount"
			]
		},
		"ITR1_IncomeDeductions": {
			"type": "object",
			"description": "Income and deduction details",
			"additionalProperties": False,
			"properties": {
				"GrossSalary": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Salary": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"PerquisitesValue": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"ProfitsInSalary": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"IncomeNotified89A": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"IncomeNotified89AType": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/NOT89AType"
					}
				},
				"IncomeNotifiedOther89A": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"AllwncExemptUs10": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"AllwncExemptUs10Dtls": {
							"type": "array",
							"items": {
								"$ref": "#/definitions/AllwncExemptUs10DtlsType"
							}
						},
						"TotalAllwncExemptUs10": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						}
					},
					"required": [
						"TotalAllwncExemptUs10"
					]
				},
				"Increliefus89A": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"NetSalary": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"DeductionUs16": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"DeductionUs16ia": {
					"type": "integer",
					"maximum": 50000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"EntertainmentAlw16ii": {
					"type": "integer",
					"maximum": 5000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"ProfessionalTaxUs16iii": {
					"type": "integer",
					"maximum": 5000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"IncomeFromSal": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TypeOfHP": {
					"description": "House Property income Type - S:Self Occupied; L:Let Out; D:Deemed let out",
					"pattern": "S|L|D",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"GrossRentReceived": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"TaxPaidlocalAuth": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"AnnualValue": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
                    "exclusiveMinimum": False
				},
				"StandardDeduction": {
					"type": "integer",
					"description": "This field refers to Part-B B2 iv - 30% of Annual Value",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"InterestPayable": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"ArrearsUnrealizedRentRcvd": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"TotalIncomeOfHP": {
					"type": "integer",
					"description": "House Property income",
					"minimum": -200000,
					"exclusiveMinimum": False,
					"default": 0
				},
				"IncomeOthSrc": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"OthersInc": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"OthersIncDtlsOthSrc": {
							"type": "array",
							"items": {
								"$ref": "#/definitions/OtherSourceIncome"
							}
						}
					}
				},
				"DeductionUs57iia": {
					"type": "integer",
					"maximum": 15000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Increliefus89AOS": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"GrossTotIncome": {
					"type": "integer",
					"maximum": 99999999999999,
					"default": 0
				},
				"UsrDeductUndChapVIA": {
					"$ref": "#/definitions/UsrDeductUndChapVIAType"
				},
				"DeductUndChapVIA": {
					"$ref": "#/definitions/DeductUndChapVIAType"
				},
				"TotalIncome": {
					"type": "integer",
					"maximum": 5000000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False,
					"default": 0
				},
				"ExemptIncAgriOthUs10": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"ExemptIncAgriOthUs10Dtls": {
							"type": "array",
							"items": {
								"$ref": "#/definitions/ExemptIncAgriOthUs10Type"
							}
						},
						"ExemptIncAgriOthUs10Total": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						}
					},
					"required": [
						"ExemptIncAgriOthUs10Total"
					]
				}
			},
			"required": [
				"GrossSalary",
				"IncomeNotified89A",
				"NetSalary",
				"DeductionUs16",
				"AnnualValue",
				"StandardDeduction",
				"IncomeFromSal",
				"TotalIncomeOfHP",
				"IncomeOthSrc",
				"GrossTotIncome",
				"UsrDeductUndChapVIA",
				"DeductUndChapVIA",
				"TotalIncome"
			]
		},
		"ITR1_TaxComputation": {
			"type": "object",
			"description": "Tax computation details",
			"additionalProperties": False,
			"properties": {
				"TotalTaxPayable": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"Rebate87A": {
					"type": "integer",
					"maximum": 25000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False,
					"default": 0
				},
				"TaxPayableOnRebate": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"EducationCess": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"GrossTaxLiability": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"Section89": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"NetTaxLiability": {
					"description": "Balance Tax After Relief",
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalIntrstPay": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"IntrstPay": {
					"$ref": "#/definitions/IntrstPay"
				},
				"TotTaxPlusIntrstPay": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalTaxPayable",
				"Rebate87A",
				"TaxPayableOnRebate",
				"EducationCess",
				"GrossTaxLiability",
				"Section89",
				"NetTaxLiability",
				"TotalIntrstPay",
				"IntrstPay",
				"TotTaxPlusIntrstPay"
			]
		},
		"TaxPaid": {
			"type": "object",
			"description": "Tax paid details",
			"additionalProperties": False,
			"properties": {
				"TaxesPaid": {
					"$ref": "#/definitions/TaxesPaid"
				},
				"BalTaxPayable": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TaxesPaid",
				"BalTaxPayable"
			]
		},
		"Refund": {
			"type": "object",
			"description": "Refund details",
			"additionalProperties": False,
			"properties": {
				"RefundDue": {
					"type": "integer",
					"description": "Refund due if Total Taxes Paid is greater than AggregateTaxInterest",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"BankAccountDtls": {
					"$ref": "#/definitions/BankAccountDtls"
				}
			},
			"required": [
				"RefundDue",
				"BankAccountDtls"
			]
		},
		"Schedule80G": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"Don100Percent": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"DoneeWithPan": {
							"type": "array",
							"minItems": 1,
							"items": {
								"$ref": "#/definitions/DoneeWithPan"
							}
						},
						"TotDon100PercentCash": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotDon100PercentOtherMode": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotDon100Percent": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotEligibleDon100Percent": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						}
					},
					"required": [
						"TotDon100PercentCash",
						"TotDon100PercentOtherMode",
						"TotDon100Percent",
						"TotEligibleDon100Percent"
					]
				},
				"Don50PercentNoApprReqd": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"DoneeWithPan": {
							"type": "array",
							"minItems": 1,
							"items": {
								"$ref": "#/definitions/DoneeWithPan"
							}
						},
						"TotDon50PercentNoApprReqdCash": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotDon50PercentNoApprReqdOtherMode": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotDon50PercentNoApprReqd": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotEligibleDon50Percent": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						}
					},
					"required": [
						"TotDon50PercentNoApprReqdCash",
						"TotDon50PercentNoApprReqdOtherMode",
						"TotDon50PercentNoApprReqd",
						"TotEligibleDon50Percent"
					]
				},
				"Don100PercentApprReqd": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"DoneeWithPan": {
							"type": "array",
							"minItems": 1,
							"items": {
								"$ref": "#/definitions/DoneeWithPan"
							}
						},
						"TotDon100PercentApprReqdCash": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotDon100PercentApprReqdOtherMode": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotDon100PercentApprReqd": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotEligibleDon100PercentApprReqd": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						}
					},
					"required": [
						"TotDon100PercentApprReqdCash",
						"TotDon100PercentApprReqdOtherMode",
						"TotDon100PercentApprReqd",
						"TotEligibleDon100PercentApprReqd"
					]
				},
				"Don50PercentApprReqd": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"DoneeWithPan": {
							"type": "array",
							"minItems": 1,
							"items": {
								"$ref": "#/definitions/DoneeWithPan"
							}
						},
						"TotDon50PercentApprReqdCash": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotDon50PercentApprReqdOtherMode": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotDon50PercentApprReqd": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						},
						"TotEligibleDon50PercentApprReqd": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False,
							"default": 0
						}
					},
					"required": [
						"TotDon50PercentApprReqdCash",
						"TotDon50PercentApprReqdOtherMode",
						"TotDon50PercentApprReqd",
						"TotEligibleDon50PercentApprReqd"
					]
				},
				"TotalDonationsUs80GCash": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalDonationsUs80GOtherMode": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalDonationsUs80G": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalEligibleDonationsUs80G": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalDonationsUs80GCash",
				"TotalDonationsUs80GOtherMode",
				"TotalDonationsUs80G",
				"TotalEligibleDonationsUs80G"
			]
		},
		"Schedule80GGA": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"DonationDtlsSciRsrchRuralDev": {
					"type": "array",
					"items": {
						"type": "object",
						"additionalProperties": False,
						"properties": {
							"RelevantClauseUndrDedClaimed": {
								"type": "string",
								"description": "80GGA(2)(a) - Sum paid to Research Association or University, college or other institution for Scientific Research; 80GGA(2)(aa) - Sum paid to Research Association or University, college or other institution for Social science or Statistical Research; 80GGA(2)(b) - Sum paid to an association or institution for Rural Development; 80GGA(2)(bb) - Sum paid to PSU or Local Authority or an association or institution approved by the National Committee for carrying out any eligible project; 80GGA(2)(c) - Sum paid to an association or institution for Conservation of Natural Resources or for afforestation; 80GGA(2)(cc) - Sum paid for Afforestation, to the funds, which are notified by Central Govt.; 80GGA(2)(d) - Sum paid for Rural Development to the funds, which are notified by Central Govt.; 80GGA(2)(e) - Sum paid to National Urban Poverty Eradication Fund as setup and notified by Central Govt.",
								"enum": [
									"80GGA2a",
									"80GGA2aa",
									"80GGA2b",
									"80GGA2bb",
									"80GGA2c",
									"80GGA2cc",
									"80GGA2d",
									"80GGA2e"
								]
							},
							"NameOfDonee": {
								"maxLength": 125,
								"minLength": 1,
								"allOf": [
									{
										"$ref": "#/definitions/nonEmptyString"
									}
								]
							},
							"AddressDetail": {
								"$ref": "#/definitions/AddressDetail"
							},
							"DoneePAN": {
								"pattern": "[A-Z]{5}[0-9]{4}[A-Z]",
								"allOf": [
									{
										"$ref": "#/definitions/nonEmptyString"
									}
								]
							},
							"DonationAmtCash": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False
							},
							"DonationAmtOtherMode": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False
							},
							"DonationAmt": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False
							},
							"EligibleDonationAmt": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False
							}
						},
						"required": [
							"RelevantClauseUndrDedClaimed",
							"NameOfDonee",
							"AddressDetail",
							"DoneePAN",
							"DonationAmtCash",
							"DonationAmtOtherMode",
							"DonationAmt",
							"EligibleDonationAmt"
						]
					}
				},
				"TotalDonationAmtCash80GGA": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalDonationAmtOtherMode80GGA": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalDonationsUs80GGA": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalEligibleDonationAmt80GGA": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalDonationAmtCash80GGA",
				"TotalDonationAmtOtherMode80GGA",
				"TotalDonationsUs80GGA",
				"TotalEligibleDonationAmt80GGA"
			]
		},
		"Schedule80GGC": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"Schedule80GGCDetails": {
					"type": "array",
					"items": {
						"type": "object",
						"additionalProperties": False,
						"properties": {
							"DonationDate": {
								"description": "Date of Donation in YYYY-MM-DD format",
					            "type": "string",
					            "pattern": "([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))"
							},
							"DonationAmtCash": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False
							},
							"DonationAmtOtherMode": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False
							},
                            "TransactionRefNum":{
                                "type": "string",
								"maxLength": 50
                            },
                            "IFSCCode": {
                                "maxLength": 11,
                                "pattern": "[A-Z]{4}[0][A-Z0-9]{6}",
                                "allOf": [
                                    {
                                        "$ref": "#/definitions/nonEmptyString"
                                    }
                                ]
                            },
							"DonationAmt": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False
							},
							"EligibleDonationAmt": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False
							}
						},
						"required": [
							"DonationDate",
							"DonationAmtCash",
							"DonationAmtOtherMode",
							"DonationAmt",
							"EligibleDonationAmt"
						]
					}
				},
				"TotalDonationAmtCash80GGC": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalDonationAmtOtherMode80GGC": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalDonationsUs80GGC": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalEligibleDonationAmt80GGC": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalDonationAmtCash80GGC",
				"TotalDonationAmtOtherMode80GGC",
				"TotalDonationsUs80GGC",
				"TotalEligibleDonationAmt80GGC"
			]
		},
		"Schedule80D": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"Sec80DSelfFamSrCtznHealth": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"SeniorCitizenFlag": {
							"description": "Y - Yes; N - No; S - Not claiming for Self/ Family",
							"pattern": "Y|N|S",
							"allOf": [
								{
									"$ref": "#/definitions/nonEmptyString"
								}
							]
						},
						"SelfAndFamily": {
							"type": "integer",
							"maximum": 25000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						},
						"HealthInsPremSlfFam": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"PrevHlthChckUpSlfFam": {
							"type": "integer",
							"maximum": 5000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						},
						"SelfAndFamilySeniorCitizen": {
							"type": "integer",
							"maximum": 50000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						},
						"HlthInsPremSlfFamSrCtzn": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"PrevHlthChckUpSlfFamSrCtzn": {
							"type": "integer",
							"maximum": 5000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						},
						"MedicalExpSlfFamSrCtzn": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"ParentsSeniorCitizenFlag": {
							"description": "Y - Yes; N - No; P - Not claiming for Parents",
							"pattern": "Y|N|P",
							"allOf": [
								{
									"$ref": "#/definitions/nonEmptyString"
								}
							]
						},
						"Parents": {
							"type": "integer",
							"maximum": 25000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						},
						"HlthInsPremParents": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"PrevHlthChckUpParents": {
							"type": "integer",
							"maximum": 5000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						},
						"ParentsSeniorCitizen": {
							"type": "integer",
							"maximum": 50000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						},
						"HlthInsPremParentsSrCtzn": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"PrevHlthChckUpParentsSrCtzn": {
							"type": "integer",
							"maximum": 5000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						},
						"MedicalExpParentsSrCtzn": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"EligibleAmountOfDedn": {
							"type": "integer",
							"maximum": 100000,
							"minimum": 0,
							"exclusiveMinimum": False,
							"exclusiveMaximum": False
						}
					},
					"required": [
						"SeniorCitizenFlag",
						"ParentsSeniorCitizenFlag",
						"EligibleAmountOfDedn"
					]
				}
			},
			"required": [
				"Sec80DSelfFamSrCtznHealth"
			]
		},
		"Schedule80DD":{
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"NatureOfDisability":{
					"description": "1 : Dependent person with disability  ; 2 : Dependent person with severe disability",
					"enum": [
						"1",
						"2"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"DeductionAmount":{
					"type":"integer",
					"maximum": 99999999999999,
					"minimum": 0
				},
				"DependentType":{
					"description": "1. Spouse; 2. Son; 3. Daughter; 4. Father; 5. Mother; 6. Brother; 7. Sister;",
					"enum": [
						"1",
						"2",
						"3",
						"4",
						"5",
						"6",
						"7"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"DependentPan":{
					"pattern": "[A-Z]{5}[0-9]{4}[A-Z]",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"DependentAadhaar":{
					"pattern": "[0-9]{12}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"Form10IAFilingDate":{
					"type":"string",
					"pattern": "([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))"
				},
				"Form10IAAckNum":{
					"type":"string",
					"maxLength":15
				},
				"UDIDNum":{
					"type":"string",
					"maxLength":18
				}
			},
			"required":[
				"NatureOfDisability",
				"DeductionAmount",
				"DependentType"
			]
		},
		"Schedule80U":{
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"NatureOfDisability":{
					"description": "1 : Self with disability  ; 2 : Self with severe disability",
					"enum": [
						"1",
						"2"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"DeductionAmount":{
					"type":"integer",
					"maximum": 99999999999999,
					"minimum": 0
				},
				"Form10IAFilingDate":{
					"type":"string",
					"pattern": "([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))"
				},
				"Form10IAAckNum":{
					"type":"string",
					"maxLength":15
				},
				"UDIDNum":{
					"type":"string",
					"maxLength":18
				}
			},
			"required":[
				"NatureOfDisability",
				"DeductionAmount"
			]
		},
		"TDSonSalaries": {
			"type": "object",
			"description": "Salary TDS details",
			"additionalProperties": False,
			"properties": {
				"TDSonSalary": {
					"type": "array",
					"minItems": 1,
					"items": {
						"$ref": "#/definitions/TDSonSalary"
					}
				},
				"TotalTDSonSalaries": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalTDSonSalaries"
			]
		},
		"TDSonOthThanSals": {
			"type": "object",
			"description": "22. Details of Tax Deducted at Source on Interest [As per Form 16 A issued by Deductor(s)]",
			"additionalProperties": False,
			"properties": {
				"TDSonOthThanSal": {
					"type": "array",
					"minItems": 1,
					"items": {
						"$ref": "#/definitions/TDSonOthThanSal"
					}
				},
				"TotalTDSonOthThanSals": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalTDSonOthThanSals"
			]
		},
		"ScheduleTDS3Dtls": {
			"type": "object",
			"description": "Details of Tax Deducted at Source [16C furnished by the Deductor(s)]",
			"additionalProperties": False,
			"properties": {
				"TDS3Details": {
					"type": "array",
					"minItems": 1,
					"items": {
						"$ref": "#/definitions/TDS3Details"
					}
				},
				"TotalTDS3Details": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalTDS3Details"
			]
		},
		"ScheduleTCS": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"TCS": {
					"type": "array",
					"minItems": 1,
					"items": {
						"type": "object",
						"additionalProperties": False,
						"properties": {
							"EmployerOrDeductorOrCollectDetl": {
								"$ref": "#/definitions/EmployerOrDeductorOrCollectDetl"
							},

							"AmtTaxCollected": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False,
								"default": 0
							},
							"CollectedYr": {
								"type": "string",
								"description": "2023: 2023-24; 2022: 2022-23; 2021: 2021-22; 2020: 2020-21; 2019: 2019-20; 2018: 2018-19; 2017: 2017-18; 2016: 2016-17; 2015: 2015-16; 2014: 2014-15; 2013: 2013-14; 2012: 2012-13; 2011: 2011-12; 2010: 2010-11; 2009: 2009-10; 2008: 2008-09",
								"enum": [
									"2023",
									"2022",
									"2021",
									"2020",
									"2019",
									"2018",
									"2017",
									"2016",
									"2015",
									"2014",
									"2013",
									"2012",
									"2011",
									"2010",
									"2009",
									"2008"
								]
							},
							"TotalTCS": {
								"type": "integer",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False,
								"default": 0
							},
							"AmtTCSClaimedThisYear": {
								"type": "integer",
								"description": "Amount out of (5) claimed for this year",
								"maximum": 99999999999999,
								"minimum": 0,
								"exclusiveMinimum": False,
								"default": 0
							}
						},
						"required": [
							"EmployerOrDeductorOrCollectDetl",
							"AmtTaxCollected",
							"CollectedYr",
							"TotalTCS",
							"AmtTCSClaimedThisYear"
						]
					}
				},
				"TotalSchTCS": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalSchTCS"
			]
		},
		"TaxPayments": {
			"type": "object",
			"description": "Tax payment details",
			"additionalProperties": False,
			"properties": {
				"TaxPayment": {
					"type": "array",
					"minItems": 1,
					"items": {
						"$ref": "#/definitions/TaxPayment"
					}
				},
				"TotalTaxPayments": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"TotalTaxPayments"
			]
		},
		"Verification": {
			"type": "object",
			"description": "Verification declaration details",
			"additionalProperties": False,
			"properties": {
				"Declaration": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"AssesseeVerName": {
							"maxLength": 127,
							"minLength": 1,
							"allOf": [
								{
									"$ref": "#/definitions/nonEmptyString"
								}
							]
						},
						"FatherName": {
							"maxLength": 125,
							"minLength": 1,
							"allOf": [
								{
									"$ref": "#/definitions/nonEmptyString"
								}
							]
						},
						"AssesseeVerPAN": {
							"pattern": "[A-Z]{3}[P][A-Z][0-9]{4}[A-Z]",
							"allOf": [
								{
									"$ref": "#/definitions/nonEmptyString"
								}
							]
						}
					},
					"required": [
						"AssesseeVerName",
						"FatherName",
						"AssesseeVerPAN"
					]
				},
				"Capacity": {
					"type": "string",
					"description": "S : Self ; R : Representative",
					"enum": [
						"S",
						"R"
					]
				},
				"Place": {
					"maxLength": 50,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				}
			},
			"required": [
				"Declaration",
				"Capacity",
				"Place"
			]
		},
		"TaxReturnPreparer": {
			"type": "object",
			"description": "TRP details",
			"additionalProperties": False,
			"properties": {
				"IdentificationNoOfTRP": {
					"pattern": "[T][0-9]{9}|[0-9]{6}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"NameOfTRP": {
					"maxLength": 125,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"ReImbFrmGov": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"IdentificationNoOfTRP",
				"NameOfTRP"
			]
		},
		"BankAccountDtls": {
			"type": "object",
			"description": "Bank details",
			"additionalProperties": False,
			"properties": {
				"AddtnlBankDetails": {
					"type": "array",
					"minItems": 1,
					"items": {
						"$ref": "#/definitions/BankDetailType"
					}
				}
			}
		},
		"AssesseeName": {
			"type": "object",
			"description": "Assessee name with Surname mandatory.",
			"additionalProperties": False,
			"properties": {
				"FirstName": {
					"maxLength": 25,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"MiddleName": {
					"maxLength": 25,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"SurNameOrOrgName": {
					"description": "Enter Last or Sur name for Individual name here",
					"maxLength": 75,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				}
			},
			"required": [
				"SurNameOrOrgName"
			]
		},
		"Address": {
			"type": "object",
			"description": "Address of assessee",
			"additionalProperties": False,
			"properties": {
				"ResidenceNo": {
					"maxLength": 50,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"ResidenceName": {
					"maxLength": 50,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"RoadOrStreet": {
					"maxLength": 50,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"LocalityOrArea": {
					"maxLength": 50,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"CityOrTownOrDistrict": {
					"maxLength": 50,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"StateCode": {
					"description": "01-Andaman and Nicobar islands; 02-Andhra Pradesh; 03-Arunachal Pradesh; 04-Assam; 05-Bihar; 06-Chandigarh; 07-Dadra Nagar and Haveli; 08-Daman and Diu; 09- Delhi; 10- Goa; 11-Gujarat; 12- Haryana; 13- Himachal Pradesh; 14-Jammu and Kashmir; 15- Karnataka; 16- Kerala; 17- Lakshadweep; 18-Madhya Pradesh; 19-Maharashtra; 20-Manipur; 21-meghalaya; 22-Mizoram; 23-Nagaland; 24- Odisha; 25- Puducherry; 26- Punjab; 27-Rajasthan; 28- Sikkim; 29-Tamil Nadu; 30- Tripura; 31-Uttar Pradesh; 32- West Bengal; 33- Chhattisgarh; 34- Uttarakhand; 35- Jharkhand; 36- Telangana; 37- Ladakh; 99-Foreign",
					"enum": [
						"01",
						"02",
						"03",
						"04",
						"05",
						"06",
						"07",
						"08",
						"09",
						"10",
						"11",
						"12",
						"13",
						"14",
						"15",
						"16",
						"17",
						"18",
						"19",
						"20",
						"21",
						"22",
						"23",
						"24",
						"25",
						"26",
						"27",
						"28",
						"29",
						"30",
						"31",
						"32",
						"33",
						"34",
						"35",
						"36",
						"37",
						"99"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"CountryCode": {
					"$ref": "#/definitions/CountryCode"
				},
				"PinCode": {
					"type": "integer",
					"pattern": "[1-9]{1}[0-9]{5}"
				},
				"ZipCode": {
					"maxLength": 8,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"CountryCodeMobile": {
					"type": "integer",
					"pattern": "[0-9]{1,5}"
				},
				"MobileNo": {
					"type": "integer",
					"pattern": "[1-9]{1}[0-9]{9}|[1-9]{1}[0-9]{4,9}"
				},
				"EmailAddress": {
					"maxLength": 125,
					"pattern": "([\\.a-zA-Z0-9_\\-])+@([a-zA-Z0-9_\\-])+(([a-zA-Z0-9_\\-])*\\.([a-zA-Z0-9_\\-])+)+",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				}
			},
			"required": [
				"ResidenceNo",
				"LocalityOrArea",
				"CityOrTownOrDistrict",
				"StateCode",
				"CountryCode",
				"CountryCodeMobile",
				"MobileNo",
				"EmailAddress"
			]
		},
		"IntrstPay": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"IntrstPayUs234A": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"IntrstPayUs234B": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"IntrstPayUs234C": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"LateFilingFee234F": {
					"type": "integer",
					"maximum": 5000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False,
					"default": 0
				}
			},
			"required": [
				"IntrstPayUs234A",
				"IntrstPayUs234B",
				"IntrstPayUs234C",
				"LateFilingFee234F"
			]
		},
		"TaxesPaid": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"AdvanceTax": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"TDS": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"TCS": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"SelfAssessmentTax": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"TotalTaxesPaid": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"AdvanceTax",
				"TDS",
				"TCS",
				"SelfAssessmentTax",
				"TotalTaxesPaid"
			]
		},
		"DoneeWithPan": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"DoneeWithPanName": {
					"maxLength": 125,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"DoneePAN": {
					"pattern": "[A-Z]{5}[0-9]{4}[A-Z]",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"ArnNbr": {
					"description": "Please enter ARN (Donation reference Number)",
					"maxLength": 25,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"AddressDetail": {
					"$ref": "#/definitions/AddressDetail"
				},
				"DonationAmtCash": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"DonationAmtOtherMode": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"DonationAmt": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"EligibleDonationAmt": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"DoneeWithPanName",
				"DoneePAN",
				"AddressDetail",
				"DonationAmtCash",
				"DonationAmtOtherMode",
				"DonationAmt",
				"EligibleDonationAmt"
			]
		},
		"TDSonSalary": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"EmployerOrDeductorOrCollectDetl": {
					"$ref": "#/definitions/EmployerOrDeductorOrCollectDetl"
				},
				"IncChrgSal": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalTDSSal": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"EmployerOrDeductorOrCollectDetl",
				"IncChrgSal",
				"TotalTDSSal"
			]
		},
		"TDSonOthThanSal": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"EmployerOrDeductorOrCollectDetl": {
					"$ref": "#/definitions/EmployerOrDeductorOrCollectDetl"
				},
				"AmtForTaxDeduct": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"DeductedYr": {
					"description": "2023: 2023-24; 2022: 2022-23; 2021: 2021-22; 2020: 2020-21; 2019: 2019-20; 2018: 2018-19; 2017: 2017-18; 2016: 2016-17; 2015: 2015-16; 2014: 2014-15; 2013: 2013-14; 2012: 2012-13; 2011: 2011-12; 2010: 2010-11; 2009: 2009-10; 2008: 2008-09",
					"enum": [
						"2023",
						"2022",
						"2021",
						"2020",
						"2019",
						"2018",
						"2017",
						"2016",
						"2015",
						"2014",
						"2013",
						"2012",
						"2011",
						"2010",
						"2009",
						"2008"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"TotTDSOnAmtPaid": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"ClaimOutOfTotTDSOnAmtPaid": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"EmployerOrDeductorOrCollectDetl",
				"AmtForTaxDeduct",
				"DeductedYr",
				"TotTDSOnAmtPaid",
				"ClaimOutOfTotTDSOnAmtPaid"
			]
		},
		"TDS3Details": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"PANofTenant": {
					"pattern": "[A-Z]{5}[0-9]{4}[A-Z]",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"AadhaarofTenant": {
					"pattern": "[0-9]{12}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"NameOfTenant": {
					"maxLength": 125,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"GrsRcptToTaxDeduct": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"DeductedYr": {
					"description": "2023:2023-24; 2022:2022-23; 2021:2021-22; 2020:2020-21; 2019:2019-20; 2018:2018-19; 2017:2017-18;",
					"enum": [
						"2023",
						"2022",
						"2021",
						"2020",
						"2019",
						"2018",
						"2017"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"TDSDeducted": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"TDSClaimed": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"PANofTenant",
				"NameOfTenant",
				"GrsRcptToTaxDeduct",
				"DeductedYr",
				"TDSDeducted",
				"TDSClaimed"
			]
		},
		"TaxPayment": {
			"type": "object",
			"description": "Tax payment detail",
			"additionalProperties": False,
			"properties": {
				"BSRCode": {
					"pattern": "[0-9]{3}[0-9A-Z]{4}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"DateDep": {
					"type": "string",
					"description": "Date of deposit should be on or after 2023-04-01  in YYYY-MM-DD format",
					"pattern": "([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))"
				},
				"SrlNoOfChaln": {
					"type": "integer",
					"maximum": 99999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Amt": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				}
			},
			"required": [
				"BSRCode",
				"DateDep",
				"SrlNoOfChaln",
				"Amt"
			]
		},
		"AddressDetail": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"AddrDetail": {
					"maxLength": 200,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"CityOrTownOrDistrict": {
					"maxLength": 50,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"StateCode": {
					"description": "01-Andaman and Nicobar islands; 02-Andhra Pradesh; 03-Arunachal Pradesh; 04-Assam; 05-Bihar; 06-Chandigarh; 07-Dadra Nagar and Haveli; 08-Daman and Diu; 09- Delhi; 10- Goa; 11-Gujarat; 12- Haryana; 13- Himachal Pradesh; 14-Jammu and Kashmir; 15- Karnataka; 16- Kerala; 17- Lakshadweep; 18-Madhya Pradesh; 19-Maharashtra; 20-Manipur; 21-meghalaya; 22-Mizoram; 23-Nagaland; 24- Odisha; 25- Puducherry; 26- Punjab; 27-Rajasthan; 28- Sikkim; 29-Tamil Nadu; 30- Tripura; 31-Uttar Pradesh; 32- West Bengal; 33- Chhattisgarh; 34- Uttarakhand; 35- Jharkhand; 36- Telangana; 37- Ladakh",
					"enum": [
						"01",
						"02",
						"03",
						"04",
						"05",
						"06",
						"07",
						"08",
						"09",
						"10",
						"11",
						"12",
						"13",
						"14",
						"15",
						"16",
						"17",
						"18",
						"19",
						"20",
						"21",
						"22",
						"23",
						"24",
						"25",
						"26",
						"27",
						"28",
						"29",
						"30",
						"31",
						"32",
						"33",
						"34",
						"35",
						"36",
						"37"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"PinCode": {
					"type": "integer",
					"maximum": 999999,
					"minimum": 100000,
					"exclusiveMinimum": False,
					"pattern": "[1-9]{1}[0-9]{5}"
				}
			},
			"required": [
				"AddrDetail",
				"CityOrTownOrDistrict",
				"StateCode",
				"PinCode"
			]
		},
		"EmployerOrDeductorOrCollectDetl": {
			"type": "object",
			"description": "Dedcutor Details",
			"additionalProperties": False,
			"properties": {
				"TAN": {
					"pattern": "HYD[A-Z][0-9]{5}[A-Z]|VPN[A-Z][0-9]{5}[A-Z]|BBN[A-Z][0-9]{5}[A-Z]|BPL[A-Z][0-9]{5}[A-Z]|JBP[A-Z][0-9]{5}[A-Z]|CHE[A-Z][0-9]{5}[A-Z]|CMB[A-Z][0-9]{5}[A-Z]|MRI[A-Z][0-9]{5}[A-Z]|DEL[A-Z][0-9]{5}[A-Z]|CAL[A-Z][0-9]{5}[A-Z]|MRT[A-Z][0-9]{5}[A-Z]|AHM[A-Z][0-9]{5}[A-Z]|BRD[A-Z][0-9]{5}[A-Z]|RKT[A-Z][0-9]{5}[A-Z]|SRT[A-Z][0-9]{5}[A-Z]|BLR[A-Z][0-9]{5}[A-Z]|AGR[A-Z][0-9]{5}[A-Z]|KNP[A-Z][0-9]{5}[A-Z]|CHN[A-Z][0-9]{5}[A-Z]|TVD[A-Z][0-9]{5}[A-Z]|ALD[A-Z][0-9]{5}[A-Z]|LKN[A-Z][0-9]{5}[A-Z]|MUM[A-Z][0-9]{5}[A-Z]|NGP[A-Z][0-9]{5}[A-Z]|AMR[A-Z][0-9]{5}[A-Z]|JLD[A-Z][0-9]{5}[A-Z]|PTL[A-Z][0-9]{5}[A-Z]|RTK[A-Z][0-9]{5}[A-Z]|KLP[A-Z][0-9]{5}[A-Z]|NSK[A-Z][0-9]{5}[A-Z]|PNE[A-Z][0-9]{5}[A-Z]|PTN[A-Z][0-9]{5}[A-Z]|RCH[A-Z][0-9]{5}[A-Z]|JDH[A-Z][0-9]{5}[A-Z]|JPR[A-Z][0-9]{5}[A-Z]|SHL[A-Z][0-9]{5}[A-Z]",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"EmployerOrDeductorOrCollecterName": {
					"maxLength": 125,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				}
			},
			"required": [
				"TAN",
				"EmployerOrDeductorOrCollecterName"
			]
		},
		"CountryCode": {
			"description": "93:AFGHANISTAN; 1001:ÅLAND ISLANDS; 355:ALBANIA; 213:ALGERIA; 684:AMERICAN SAMOA; 376:ANDORRA; 244:ANGOLA; 1264:ANGUILLA; 1010:ANTARCTICA; 1268:ANTIGUA AND BARBUDA; 54:ARGENTINA; 374:ARMENIA; 297:ARUBA; 61:AUSTRALIA; 43:AUSTRIA; 994:AZERBAIJAN; 1242:BAHAMAS; 973:BAHRAIN; 880:BANGLADESH; 1246:BARBADOS; 375:BELARUS; 32:BELGIUM; 501:BELIZE; 229:BENIN; 1441:BERMUDA; 975:BHUTAN; 591:BOLIVIA (PLURINATIONAL STATE OF); 1002:BONAIRE, SINT EUSTATIUS AND SABA; 387:BOSNIA AND HERZEGOVINA; 267:BOTSWANA; 1003:BOUVET ISLAND; 55:BRAZIL; 1014:BRITISH INDIAN OCEAN TERRITORY; 673:BRUNEI DARUSSALAM; 359:BULGARIA; 226: BURKINA FASO; 257:BURUNDI; 238:CABO VERDE; 855:CAMBODIA; 237:CAMEROON; 1:CANADA; 1345:CAYMAN ISLANDS; 236:CENTRAL AFRICAN REPUBLIC; 235:CHAD; 56:CHILE; 86:CHINA; 9:CHRISTMAS ISLAND; 672:COCOS (KEELING) ISLANDS; 57:COLOMBIA; 270:COMOROS; 242:CONGO; 243:CONGO (DEMOCRATIC REPUBLIC OF THE); 682:COOK ISLANDS; 506:COSTA RICA; 225:CÔTE D'IVOIRE; 385:CROATIA; 53:CUBA; 1015:CURAÇAO; 357:CYPRUS; 420:CZECHIA; 45:DENMARK; 253:DJIBOUTI; 1767:DOMINICA; 1809:DOMINICAN REPUBLIC; 593:ECUADOR; 20:EGYPT; 503:EL SALVADOR; 240:EQUATORIAL GUINEA; 291:ERITREA; 372:ESTONIA; 251:ETHIOPIA; 500:FALKLAND ISLANDS (MALVINAS); 298:FAROE ISLANDS; 679:FIJI; 358:FINLAND; 33:FRANCE; 594:FRENCH GUIANA; 689:FRENCH POLYNESIA; 1004:FRENCH SOUTHERN TERRITORIES; 241:GABON; 220:GAMBIA; 995:GEORGIA; 49:GERMANY; 233:GHANA; 350:GIBRALTAR; 30:GREECE; 299:GREENLAND; 1473:GRENADA; 590:GUADELOUPE; 1671:GUAM; 502:GUATEMALA; 1481:GUERNSEY; 224:GUINEA; 245:GUINEA-BISSAU; 592:GUYANA; 509:HAITI; 1005:HEARD ISLAND AND MCDONALD ISLANDS; 6:HOLY SEE; 504:HONDURAS; 852:HONG KONG; 36:HUNGARY; 354:ICELAND; 91:INDIA; 62:INDONESIA; 98:IRAN (ISLAMIC REPUBLIC OF); 964:IRAQ; 353:IRELAND; 1624:ISLE OF MAN; 972:ISRAEL; 5:ITALY; 1876:JAMAICA; 81:JAPAN; 1534:JERSEY; 962:JORDAN; 7:KAZAKHSTAN; 254:KENYA; 686:KIRIBATI; 850:KOREA(DEMOCRATIC PEOPLE'S REPUBLIC OF); 82:KOREA (REPUBLIC OF); 965:KUWAIT; 996:KYRGYZSTAN; 856:LAO PEOPLE'S DEMOCRATIC REPUBLIC; 371:LATVIA; 961:LEBANON; 266:LESOTHO; 231:LIBERIA; 218:LIBYA; 423:LIECHTENSTEIN; 370:LITHUANIA; 352:LUXEMBOURG; 853:MACAO; 389:MACEDONIA(THE FORMER YUGOSLAV REPUBLIC OF); 261:MADAGASCAR; 256:MALAWI; 60:MALAYSIA; 960:MALDIVES; 223:MALI; 356:MALTA; 692:MARSHALL ISLANDS; 596:MARTINIQUE; 222:MAURITANIA; 230:MAURITIUS; 269:MAYOTTE; 52:MEXICO; 691:MICRONESIA (FEDERATED STATES OF); 373:MOLDOVA (REPUBLIC OF); 377:MONACO; 976:MONGOLIA; 382:MONTENEGRO; 1664:MONTSERRAT; 212:MOROCCO; 258:MOZAMBIQUE; 95:MYANMAR; 264:NAMIBIA; 674:NAURU; 977:NEPAL; 31:NETHERLANDS; 687:NEW CALEDONIA; 64:NEW ZEALAND; 505:NICARAGUA; 227:NIGER; 234:NIGERIA; 683:NIUE; 15:NORFOLK ISLAND; 1670:NORTHERN MARIANA ISLANDS; 47:NORWAY; 968:OMAN; 92:PAKISTAN; 680:PALAU; 970:PALESTINE, STATE OF; 507:PANAMA; 675:PAPUA NEW GUINEA; 595:PARAGUAY; 51:PERU; 63:PHILIPPINES; 1011:PITCAIRN; 48:POLAND; 14:PORTUGAL; 1787:PUERTO RICO; 974:QATAR; 262:RÉUNION; 40:ROMANIA; 8:RUSSIAN FEDERATION; 250:RWANDA; 1006:SAINT BARTHÉLEMY; 290: SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA; 1869:SAINT KITTS AND NEVIS; 1758:SAINT LUCIA; 1007:SAINT MARTIN (FRENCH PART); 508:SAINT PIERRE AND MIQUELON; 1784:SAINT VINCENT AND THE GRENADINES; 685:SAMOA; 378:SAN MARINO; 239:SAO TOME AND PRINCIPE; 966:SAUDI ARABIA; 221:SENEGAL; 381:SERBIA; 248:SEYCHELLES; 232:SIERRA LEONE; 65:SINGAPORE; 1721:SINT MAARTEN (DUTCH PART); 421:SLOVAKIA; 386:SLOVENIA; 677:SOLOMON ISLANDS; 252:SOMALIA; 28:SOUTH AFRICA; 1008:SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS; 211:SOUTH SUDAN; 35:SPAIN; 94:SRI LANKA; 249:SUDAN; 597:SURINAME; 1012:SVALBARD AND JAN MAYEN; 268:SWAZILAND; 46:SWEDEN; 41:SWITZERLAND; 963:SYRIAN ARAB REPUBLIC; 886:TAIWAN; 992:TAJIKISTAN; 255:TANZANIA, UNITED REPUBLIC OF; 66:THAILAND; 670:TIMOR-LESTE (EAST TIMOR); 228:TOGO; 690:TOKELAU; 676:TONGA; 1868:TRINIDAD AND TOBAGO; 216:TUNISIA; 90:TURKEY; 993:TURKMENISTAN; 1649:TURKS AND CAICOS ISLANDS; 688:TUVALU; 256:UGANDA; 380:UKRAINE; 971:UNITED ARAB EMIRATES; 44:UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND; 2:UNITED STATES OF AMERICA; 1009:UNITED STATES MINOR OUTLYING ISLANDS; 598:URUGUAY; 998:UZBEKISTAN; 678:VANUATU; 58:VENEZUELA (BOLIVARIAN REPUBLIC OF); 84:VIET NAM; 1284:VIRGIN ISLANDS (BRITISH); 1340:VIRGIN ISLANDS (U.S.); 681:WALLIS AND FUTUNA; 1013:WESTERN SAHARA; 967:YEMEN; 260:ZAMBIA; 263:ZIMBABWE; 9999:OTHERS",
			"enum": [
				"93",
				"1001",
				"355",
				"213",
				"684",
				"376",
				"244",
				"1264",
				"1010",
				"1268",
				"54",
				"374",
				"297",
				"61",
				"43",
				"994",
				"1242",
				"973",
				"880",
				"1246",
				"375",
				"32",
				"501",
				"229",
				"1441",
				"975",
				"591",
				"1002",
				"387",
				"267",
				"1003",
				"55",
				"1014",
				"673",
				"359",
				"226",
				"257",
				"238",
				"855",
				"237",
				"1",
				"1345",
				"236",
				"235",
				"56",
				"86",
				"9",
				"672",
				"57",
				"270",
				"242",
				"243",
				"682",
				"506",
				"225",
				"385",
				"53",
				"1015",
				"357",
				"420",
				"45",
				"253",
				"1767",
				"1809",
				"593",
				"20",
				"503",
				"240",
				"291",
				"372",
				"251",
				"500",
				"298",
				"679",
				"358",
				"33",
				"594",
				"689",
				"1004",
				"241",
				"220",
				"995",
				"49",
				"233",
				"350",
				"30",
				"299",
				"1473",
				"590",
				"1671",
				"502",
				"1481",
				"224",
				"245",
				"592",
				"509",
				"1005",
				"6",
				"504",
				"852",
				"36",
				"354",
				"91",
				"62",
				"98",
				"964",
				"353",
				"1624",
				"972",
				"5",
				"1876",
				"81",
				"1534",
				"962",
				"7",
				"254",
				"686",
				"850",
				"82",
				"965",
				"996",
				"856",
				"371",
				"961",
				"266",
				"231",
				"218",
				"423",
				"370",
				"352",
				"853",
				"389",
				"261",
				"265",
				"60",
				"960",
				"223",
				"356",
				"692",
				"596",
				"222",
				"230",
				"269",
				"52",
				"691",
				"373",
				"377",
				"976",
				"382",
				"1664",
				"212",
				"258",
				"95",
				"264",
				"674",
				"977",
				"31",
				"687",
				"64",
				"505",
				"227",
				"234",
				"683",
				"15",
				"1670",
				"47",
				"968",
				"92",
				"680",
				"970",
				"507",
				"675",
				"595",
				"51",
				"63",
				"1011",
				"48",
				"14",
				"1787",
				"974",
				"262",
				"40",
				"8",
				"250",
				"1006",
				"290",
				"1869",
				"1758",
				"1007",
				"508",
				"1784",
				"685",
				"378",
				"239",
				"966",
				"221",
				"381",
				"248",
				"232",
				"65",
				"1721",
				"421",
				"386",
				"677",
				"252",
				"28",
				"1008",
				"211",
				"35",
				"94",
				"249",
				"597",
				"1012",
				"268",
				"46",
				"41",
				"963",
				"886",
				"992",
				"255",
				"66",
				"670",
				"228",
				"690",
				"676",
				"1868",
				"216",
				"90",
				"993",
				"1649",
				"688",
				"256",
				"380",
				"971",
				"44",
				"2",
				"1009",
				"598",
				"998",
				"678",
				"58",
				"84",
				"1284",
				"1340",
				"681",
				"1013",
				"967",
				"260",
				"263",
				"9999"
			],
			"allOf": [
				{
					"$ref": "#/definitions/nonEmptyString"
				}
			]
		},
		"BankDetailType": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"IFSCCode": {
					"pattern": "[A-Z]{4}[0][A-Z0-9]{6}",
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"BankName": {
					"maxLength": 125,
					"minLength": 1,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"BankAccountNo": {
					"maxLength": 20,
					"minLength": 1,
					"pattern": "[a-zA-Z0-9]([/-]?(((\\d*[1-9]\\d*)*[a-zA-Z/-])|(\\d*[1-9]\\d*[a-zA-Z]*))+)*[0-9]*",
					"allOf": [
						{
							"$ref": "#/definitions/nonZeroString"
						}
					]
				},
				"AccountType":{
					"type": "string",
					"description": "SB: Savings Account, CA: Current Account,CC: Cash Credit Account, OD: Over draft account, NRO: Non Resident Account, OTH: Other",
					"enum": [
						"SB",
						"CA",
						"CC",
						"OD",
						"NRO",
						"OTH"
					]

				}
			},
			"required": [
				"IFSCCode",
				"BankName",
				"BankAccountNo",
				"AccountType"
			]
		},
		"UsrDeductUndChapVIAType": {
			"type": "object",
			"description": "Deductions from income",
			"additionalProperties": False,
			"properties": {
				"Section80C": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80CCC": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80CCDEmployeeOrSE": {
					"type": "integer",
					"description": "For Employee/SelfEmployed",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80CCD1B": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80CCDEmployer": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80D": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80DD": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
},
				"Section80DDBUsrType": {
					"description": "1 : Self or dependent ; 2 : Self or Dependent - Senior Citizen",
					"enum": [
						"1",
						"2"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"Section80DDB": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80E": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80EE": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80EEA": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80EEB": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80G": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80GG": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80GGA": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80GGC": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80U": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80TTA": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80TTB": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"AnyOthSec80CCH": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalChapVIADeductions": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"Section80C",
				"Section80CCC",
				"Section80CCDEmployeeOrSE",
				"Section80CCD1B",
				"Section80CCDEmployer",
				"Section80D",
				"Section80DD",
				"Section80DDB",
				"Section80E",
				"Section80EE",
				"Section80G",
				"Section80GG",
				"Section80GGA",
				"Section80GGC",
				"Section80U",
				"Section80TTA",
				"Section80TTB",
				"AnyOthSec80CCH",
				"TotalChapVIADeductions"
			]
		},
		"DeductUndChapVIAType": {
			"type": "object",
			"description": "Deductions from income",
			"additionalProperties": False,
			"properties": {
				"Section80C": {
					"type": "integer",
					"maximum": 150000,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80CCC": {
					"type": "integer",
					"maximum": 150000,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80CCDEmployeeOrSE": {
					"type": "integer",
					"description": "For Employee/SelfEmployed",
					"maximum": 150000,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80CCD1B": {
					"type": "integer",
					"maximum": 50000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80CCDEmployer": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80D": {
					"type": "integer",
					"maximum": 100000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80DD": {
					"type": "integer",
					"maximum": 125000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80DDB": {
					"type": "integer",
					"maximum": 100000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80E": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80EE": {
					"type": "integer",
					"maximum": 50000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80EEA": {
					"type": "integer",
					"maximum": 150000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80EEB": {
					"type": "integer",
					"maximum": 150000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80G": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80GG": {
					"type": "integer",
					"maximum": 60000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80GGA": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80GGC": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"Section80U": {
					"type": "integer",
					"maximum": 125000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80TTA": {
					"type": "integer",
					"maximum": 10000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"Section80TTB": {
					"type": "integer",
					"maximum": 50000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"exclusiveMaximum": False
				},
				"AnyOthSec80CCH": {
					"type": "integer",
					"maximum": 288000,
					"minimum": 0,
					"exclusiveMinimum": False,
					"default": 0
				},
				"TotalChapVIADeductions": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"Section80C",
				"Section80CCC",
				"Section80CCDEmployeeOrSE",
				"Section80CCD1B",
				"Section80CCDEmployer",
				"Section80D",
				"Section80DD",
				"Section80DDB",
				"Section80E",
				"Section80EE",
				"Section80EEA",
				"Section80EEB",
				"Section80G",
				"Section80GG",
				"Section80GGA",
				"Section80GGC",
				"Section80U",
				"Section80TTA",
				"Section80TTB",
				"AnyOthSec80CCH",
				"TotalChapVIADeductions"
			]
		},
		"AllwncExemptUs10DtlsType": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"SalNatureDesc": {
					"description": "10(5) - Sec 10(5)-Leave Travel concession/assistance; 10(6) - Sec 10(6)-Remuneration received as an official, by whatever name called, of an embassy, high commission etc.; 10(7) - Sec 10(7)-Allowances or perquisites paid or allowed as such outside India by the Government to a citizen of India for rendering service outside India; 10(10) - Sec 10(10)-Death-cum-retirement gratuity received ; 10(10A) - Sec 10(10A)-Commuted value of pension received; 10(10AA) - Sec 10(10AA)-Earned leave encashment on Retirement; 10(10B)(i) - Sec 10(10B)-First proviso - Compensation limit notified by CG in the Official Gazette; 10(10B)(ii) - Sec 10(10B)-Second proviso - Compensation under scheme approved by the Central Government; 10(10C) - Sec 10(10C)- Amount received/receivable on voluntary retirement or termination of service; 10(10CC) - Sec 10(10CC)-Tax paid by employer on non-monetary perquisite; 10(13A) - Sec 10(13A)-Allowance to meet expenditure incurred on house rent; 10(14)(i) - Sec 10(14)(i)- Prescribed Allowances or benefits (not in a nature of perquisite) specifically granted to meet expenses wholly, necessarily and exclusively and to the extent actually incurred, in performance of duties of office or employment; 10(14)(ii) - Sec 10(14)(ii) -Prescribed Allowances or benefits granted to meet personal expenses in performance of duties of office or employment or to compensate him for increased cost of living. ; 10(14)(i)(115BAC) - Sec 10(14)(i) -Allowances referred in sub-clauses (a) to (c) of sub-rule (1) in Rule 2BB ; 10(14)(ii)(115BAC) - Sec 10(14)(ii) -Transport allowance granted to certain physically handicapped assessee ; EIC - Exempt income received by a judge covered under the payment of salaries to Supreme Court/High Court judges Act /Rules ; OTH - Any Other",
					"enum": [
						"10(5)",
						"10(6)",
						"10(7)",
						"10(10)",
						"10(10A)",
						"10(10AA)",
						"10(10B)(i)",
						"10(10B)(ii)",
						"10(10C)",
						"10(10CC)",
						"10(13A)",
						"10(14)(i)",
						"10(14)(ii)",
						"10(14)(i)(115BAC)",
						"10(14)(ii)(115BAC)",
						"EIC",
						"OTH"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"SalOthNatOfInc": {
					"maxLength": 125,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"SalOthAmount": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"SalNatureDesc",
				"SalOthAmount"
			]
		},
		"OtherSourceIncome": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"OthSrcNatureDesc": {
					"description": "SAV : Interest from Saving Account; IFD : Interest from Deposit(Bank/Post Office/Cooperative Society); TAX : Interest from Income Tax Refund; FAP : Family pension; DIV : Dividend; 10(11)(iP) : Interest accrued on contributions to provident fund to the extent taxable as per first proviso to section 10(11); 10(11)(iiP) : Interest accrued on contributions to provident fund to the extent taxable as per second proviso to section 10(11); 10(12)(iP) : Interest accrued on contributions to provident fund to the extent taxable as per first proviso to section 10(12); 10(12)(iiP) : Interest accrued on contributions to provident fund to the extent taxable as per second proviso to section 10(12); NOT89A : Income from retirement benefit account maintained in a notified country u/s 89A ; OTHNOT89A : Income from retirement benefit account maintained in a country other than a country notified u/s 89A ; OTH : Any Other",
					"enum": [
						"SAV",
						"IFD",
						"TAX",
						"FAP",
						"DIV",
						"10(11)(iP)",
						"10(11)(iiP)",
						"10(12)(iP)",
						"10(12)(iiP)",
						"NOT89A",
						"OTHNOT89A",
						"OTH"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"NOT89A": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/NOT89AType"
					}
				},
				"OthSrcOthNatOfInc": {
					"maxLength": 125,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"OthSrcOthAmount": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				},
				"DividendInc": {
					"$ref": "#/definitions/DateRangeType"
				},
				"NOT89AInc": {
					"$ref": "#/definitions/DateRangeType"
				}
			},
			"required": [
				"OthSrcNatureDesc",
				"OthSrcOthAmount"
			]
		},
		"NOT89AType": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"NOT89ACountrycode": {
					"type": "string",
					"description": "US - United States; UK - United Kingdom; CA - Canada",
					"enum": [
						"US",
						"UK",
						"CA"
					]
				},
				"NOT89AAmount": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"NOT89ACountrycode",
				"NOT89AAmount"
			]
		},
		"DateRangeType": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"DateRange": {
					"type": "object",
					"additionalProperties": False,
					"properties": {
						"Upto15Of6": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"Upto15Of9": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"Up16Of9To15Of12": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"Up16Of12To15Of3": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						},
						"Up16Of3To31Of3": {
							"type": "integer",
							"maximum": 99999999999999,
							"minimum": 0,
							"exclusiveMinimum": False
						}
					},
					"required": [
						"Upto15Of6",
						"Upto15Of9",
						"Up16Of9To15Of12",
						"Up16Of12To15Of3",
						"Up16Of3To31Of3"
					]
				}
			},
			"required": [
				"DateRange"
			]
		},
		"ExemptIncAgriOthUs10Type": {
			"type": "object",
			"additionalProperties": False,
			"properties": {
				"NatureDesc": {
					"description": "AGRI : Agriculture Income (= Rs.5000); 10(10BC): Sec 10(10BC)-Any amount from the Central/State Govt./local authority by way of compensation on account of any disaster; 10(10D) : Sec 10(10D)- Any sum received under a life insurance policy, including the sum allocated by way of bonus on such policy except sum as mentioned in sub-clause (a) to (d) of Sec.10(10D); 10(11) : Sec 10(11)-Statuory Provident Fund received; 10(12) : Sec 10(12)-Recognised Provident Fund received;10(12C) : Sec 10(12C)-Any payment from the Agniveer Corpus Fund to a person enrolled under the Agnipath Scheme, or to his nominee.; 10(13) : Sec 10(13)-Approved superannuation fund received; 10(16) : Sec 10(16)-Scholarships granted to meet the cost of education; 10(17) : Sec 10(17)-Allowance MP/MLA/MLC; 10(17A) : Sec 10(17A)-Award instituted by Government; 10(18) : Sec 10(18)-Pension received by winner of \"Param Vir Chakra\" or \"Maha Vir Chakra\" or \"Vir Chakra\" or such other gallantry award; DMDP : Defense medical disability pension; 10(19) : Sec 10(19)-Armed Forces Family pension in case of death during operational duty; 10(26) : Sec 10(26)-Any income as referred to in section 10(26); 10(26AAA): Sec 10(26AAA)-Any income as referred to in section 10(26AAA) ; OTH : Any Other",
					"enum": [
						"AGRI",
						"10(10BC)",
						"10(10D)",
						"10(11)",
						"10(12)",
						"10(12C)",
						"10(13)",
						"10(16)",
						"10(17)",
						"10(17A)",
						"10(18)",
						"DMDP",
						"10(19)",
						"10(26)",
						"10(26AAA)",
						"OTH"
					],
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"OthNatOfInc": {
					"maxLength": 125,
					"allOf": [
						{
							"$ref": "#/definitions/nonEmptyString"
						}
					]
				},
				"OthAmount": {
					"type": "integer",
					"maximum": 99999999999999,
					"minimum": 0,
					"exclusiveMinimum": False
				}
			},
			"required": [
				"NatureDesc",
				"OthAmount"
			]
		},
		"nonEmptyString": {
			"type": "string",
			"pattern": "|(\\s*([\\w\\d_=!@#$%\\^*\\(\\){}\\[\\]\\|\\\\:;',\\.\\?/~`\\-\\+<>&\"][\\s\\w\\d_=!@#$%\\^*\\(\\){}\\[\\]\\|\\\\:;',\\.\\?/~`\\-\\+<>&\"]*)\\s*)"
		},
		"nonZeroString": {
			"pattern": ".*[1-9].*",
			"allOf": [
				{
					"$ref": "#/definitions/endWithDigit"
				}
			]
		},
		"endWithDigit": {
			"type": "string",
			"pattern": ".*[0-9]"
		}
	}
}



# Your JSON data
your_json_data = {
  "ITR": {
    "ITR1": {
      "CreationInfo": {
        "SWVersionNo": "P1.43.1.0",
        "SWCreatedBy": "SW20000297",
        "JSONCreatedBy": "SW20000297",
        "JSONCreationDate": "2024-02-08",
        "IntermediaryCity": "Pune",
        "Digest": "VON77i4Ox1jbay2hSHsxXCZKBecS+ejmqGFFX46lE+Y="
      },
      "Form_ITR1": {
        "FormName": "ITR-1",
        "Description": "For Indls having Income from Salary, Pension, family pension and Interest",
        "AssessmentYear": "2024",
        "SchemaVer": "Ver1.0",
        "FormVer": "Ver1.0"
      },
      "PersonalInfo": {
        "AssesseeName": {
          "FirstName": "ITR",
          "MiddleName": "one",
          "SurNameOrOrgName": "EG Four"
        },
        "Address": {
          "ResidenceNo": "Varun C 106",
          "ResidenceName": "DSK Vishwa",
          "RoadOrStreet": "Dhayari",
          "LocalityOrArea": "Sinhagad Road",
          "CityOrTownOrDistrict": "Pune",
          "StateCode": "19",
          "CountryCode": "91",
          "PinCode": 411041,
          "CountryCodeMobile": 91,
          "MobileNo": 7769055500,
          "EmailAddress": "caanuptabe@gmail.com"
        },
        "PAN": "ATQPP2374P",
        "DOB": "1990-05-26",
        "EmployerCategory": "PE",
        "AadhaarCardNo": "959959999999"
      },
      "FilingStatus": {
        "ReturnFileSec": 12,
        "NewTaxRegime": "N",
        "SeventhProvisio139": "N",
        "clauseiv7provisio139i": "N"
      },
      "ITR1_IncomeDeductions": {
        "GrossSalary": 25000,
        "Salary": 25000,
        "PerquisitesValue": 0,
        "ProfitsInSalary": 0,
        "IncomeNotified89A": 0,
        "IncomeNotified89AType": [],
        "IncomeNotifiedOther89A": 0,
        "Increliefus89A": 0,
        "NetSalary": 25000,
        "DeductionUs16": 25000,
        "DeductionUs16ia": 25000,
        "EntertainmentAlw16ii": 0,
        "ProfessionalTaxUs16iii": 0,
        "IncomeFromSal": 0,
        "GrossRentReceived": 0,
        "TaxPaidlocalAuth": 0,
        "AnnualValue": 0,
        "StandardDeduction": 0,
        "InterestPayable": 0,
        "ArrearsUnrealizedRentRcvd": 0,
        "TotalIncomeOfHP": 349600,
        "IncomeOthSrc": 5000000,
        "OthersInc": {
          "OthersIncDtlsOthSrc": [
            {
              "OthSrcNatureDesc": "OTH",
              "OthSrcOthNatOfInc": "Any Other",
              "OthSrcOthAmount": 5000000,
              "DividendInc": {
                "DateRange": {
                  "Upto15Of6": 0,
                  "Upto15Of9": 0,
                  "Up16Of9To15Of12": 0,
                  "Up16Of12To15Of3": 0,
                  "Up16Of3To31Of3": 0
                }
              }
            },
            {
              "OthSrcNatureDesc": "DIV",
              "OthSrcOthNatOfInc": "Dividend",
              "OthSrcOthAmount": 0,
              "DividendInc": {
                "DateRange": {
                  "Upto15Of6": 0,
                  "Upto15Of9": 0,
                  "Up16Of9To15Of12": 0,
                  "Up16Of12To15Of3": 0,
                  "Up16Of3To31Of3": 0
                }
              }
            }
          ]
        },
        "DeductionUs57iia": 0,
        "Increliefus89AOS": 0,
        "GrossTotIncome": 5349600,
        "UsrDeductUndChapVIA": {
          "Section80C": 150000,
          "Section80CCC": 0,
          "Section80CCDEmployeeOrSE": 0,
          "Section80CCD1B": 0,
          "Section80CCDEmployer": 0,
          "Section80D": 0,
          "Section80DD": 0,
          "Section80DDB": 0,
          "Section80E": 0,
          "Section80EE": 0,
          "Section80EEA": 0,
          "Section80EEB": 0,
          "Section80G": 0,
          "Section80GG": 0,
          "Section80GGA": 0,
          "Section80GGC": 0,
          "Section80U": 0,
          "Section80TTA": 0,
          "Section80TTB": 0,
          "AnyOthSec80CCH": 10000,
          "TotalChapVIADeductions": 160000
        },
        "DeductUndChapVIA": {
          "Section80C": 150000,
          "Section80CCC": 0,
          "Section80CCDEmployeeOrSE": 0,
          "Section80CCD1B": 0,
          "Section80CCDEmployer": 0,
          "Section80D": 0,
          "Section80DD": 0,
          "Section80DDB": 0,
          "Section80E": 0,
          "Section80EE": 0,
          "Section80EEA": 0,
          "Section80EEB": 0,
          "Section80G": 0,
          "Section80GG": 0,
          "Section80GGA": 0,
          "Section80GGC": 0,
          "Section80U": 0,
          "Section80TTA": 0,
          "Section80TTB": 0,
          "AnyOthSec80CCH": 10000,
          "TotalChapVIADeductions": 160000
        },
        "TotalIncome": 5189600,
        "ExemptIncAgriOthUs10": {
          "ExemptIncAgriOthUs10Dtls": [],
          "ExemptIncAgriOthUs10Total": 0
        }
      },
      "ITR1_TaxComputation": {
        "TotalTaxPayable": 1369380,
        "Rebate87A": 0,
        "TaxPayableOnRebate": 1369380,
        "EducationCess": 60084,
        "GrossTaxLiability": 1562184,
        "Section89": 0,
        "NetTaxLiability": 1562184,
        "TotalIntrstPay": 98911,
        "IntrstPay": {
          "IntrstPayUs234A": 0,
          "IntrstPayUs234B": 15523,
          "IntrstPayUs234C": 78388,
          "LateFilingFee234F": 5000
        },
        "TotTaxPlusIntrstPay": 1661095
      },
      "TaxPaid": {
        "TaxesPaid": {
          "AdvanceTax": 0,
          "TDS": 9850,
          "TCS": 0,
          "SelfAssessmentTax": 0,
          "TotalTaxesPaid": 9850
        },
        "BalTaxPayable": 1651250
      },
      "Refund": {
        "RefundDue": 0,
        "BankAccountDtls": {}
      },
      "Schedule80G": {
        "TotalDonationsUs80GCash": 0,
        "TotalDonationsUs80GOtherMode": 0,
        "TotalDonationsUs80G": 0,
        "TotalEligibleDonationsUs80G": 0
      },
      "Schedule80GGA": {
        "DonationDtlsSciRsrchRuralDev": [],
        "TotalDonationAmtCash80GGA": 0,
        "TotalDonationAmtOtherMode80GGA": 0,
        "TotalDonationsUs80GGA": 0,
        "TotalEligibleDonationAmt80GGA": 0
      },
      "Schedule80D": {
        "Sec80DSelfFamSrCtznHealth": {
          "SeniorCitizenFlag": "S",
          "SelfAndFamily": 0,
          "HealthInsPremSlfFam": 0,
          "PrevHlthChckUpSlfFam": 0,
          "SelfAndFamilySeniorCitizen": 0,
          "HlthInsPremSlfFamSrCtzn": 0,
          "PrevHlthChckUpSlfFamSrCtzn": 0,
          "MedicalExpSlfFamSrCtzn": 0,
          "ParentsSeniorCitizenFlag": "P",
          "Parents": 0,
          "HlthInsPremParents": 0,
          "PrevHlthChckUpParents": 0,
          "ParentsSeniorCitizen": 0,
          "HlthInsPremParentsSrCtzn": 0,
          "PrevHlthChckUpParentsSrCtzn": 0,
          "MedicalExpParentsSrCtzn": 0,
          "EligibleAmountOfDedn": 0
        }
      },
      "TDSonSalaries": {
        "TDSonSalary": [
          {
            "EmployerOrDeductorOrCollectDetl": {
              "TAN": "PNER06453G",
              "EmployerOrDeductorOrCollecterName": "REDR INDIA"
            },
            "IncChrgSal": 25000,
            "TotalTDSSal": 9800
          }
        ],
        "TotalTDSonSalaries": 9800
      },
      "TDSonOthThanSals": {
        "TDSonOthThanSal": [
          {
            "EmployerOrDeductorOrCollectDetl": {
              "TAN": "PNET04092E",
              "EmployerOrDeductorOrCollecterName": "TEST 001"
            },
            "AmtForTaxDeduct": 50000,
            "DeductedYr": "2019",
            "TotTDSOnAmtPaid": 1000,
            "ClaimOutOfTotTDSOnAmtPaid": 50
          }
        ],
        "TotalTDSonOthThanSals": 50
      },
      "TaxPayments": {
        "TotalTaxPayments": 0
      },
      "Verification": {
        "Declaration": {
          "AssesseeVerName": "ITR 1 EG 4",
          "FatherName": "TEST TEST TEST",
          "AssesseeVerPAN": "AHNPT4848S"
        },
        "Capacity": "R",
        "Place": "Pune"
      }
    }
  }
}

# Validate your JSON data against the schema
try:
    validate(instance=your_json_data, schema=your_schema)
    print("Schema correct.")
except exceptions.ValidationError as e:
    print(f"Schema wrong: {e}")