import React, { useEffect, useState, useRef, useCallback } from 'react';
import axios from 'axios';
import './App.css'; // Import a CSS file for styling
import Select from 'react-select';

// import App from PopUp.js

const Page1 = ({ handleCalculate, handleNameSelect, output }) => {
    const [name, setName] = useState();
    const [region, setRegion] = useState("Old");
    const [financialYear, setFinancialYear] = useState("2024-2025");
    const [status, setstatus] = useState();
    const [filingDate, setFilingDate] = useState("");
    const [taxPayableRefundable, setTaxPayableRefundable] = useState(0); // Assuming TaxPayableRefundable is defined here
  
    const [filingDateNew, setFilingDateNew] = useState('');
    const [age, setAge] = useState(0);
    const [ageCategory, setAgeCategory] = useState("");
    //const [age, setAge] = useState('');
    const [dueDate, setDueDate] = useState("");
    const [gender, setGender] = useState("male");
    const [ageGroup, setAgeGroup] = useState("Age 60");
    const [residentStatus, setResidentStatus] = useState("resident");
    const [ageDistribution, setAgeDistribution] = useState("ageDistribution");
    const [basicsalary, setbasicsalary] = useState('0');
    const [houseproperty, sethouseproperty] = useState('0');
    const [manuallyEnteredName, setManuallyEnteredName] = useState("");
    const [nameSelected, setNameSelected] = useState(false);
    const [firstSelection, setFirstSelection] = useState(true);
    const [isFirstSelection, setIsFirstSelection] = useState(true); // To track the first selection
    const [clickCount, setClickCount] = useState(0);
    const [oldFieldValue, setoldFieldValue] = useState('');
    const [ShortTerm11, setShortTerm11] = useState('0');
    const [ShortTerm12, setShortTerm12] = useState('0');
    const [ShortTerm13, setShortTerm13] = useState('0');
    const [ShortTerm14, setShortTerm14] = useState('0');
    const [ShortTerm15, setShortTerm15] = useState('0');
    const [ShortTerm16, setShortTerm16] = useState('0');
    const [ShortTerm21, setShortTerm21] = useState('0');
    const [ShortTerm22, setShortTerm22] = useState('0');
    const [ShortTerm23, setShortTerm23] = useState('0');
    const [ShortTerm24, setShortTerm24] = useState('0');
    const [ShortTerm25, setShortTerm25] = useState('0');
    const [ShortTerm26, setShortTerm26] = useState('0');
    const [ShortTerm31, setShortTerm31] = useState('0');
    const [ShortTerm32, setShortTerm32] = useState('0');
    const [ShortTerm33, setShortTerm33] = useState('0');
    const [ShortTerm34, setShortTerm34] = useState('0');
    const [ShortTerm35, setShortTerm35] = useState('0');
    const [ShortTerm36, setShortTerm36] = useState('0');
    const [ShortTerm41, setShortTerm41] = useState('0');
    const [ShortTerm42, setShortTerm42] = useState('0');
    const [ShortTerm43, setShortTerm43] = useState('0');
    const [ShortTerm44, setShortTerm44] = useState('0');
    const [ShortTerm45, setShortTerm45] = useState('0');
    const [ShortTerm46, setShortTerm46] = useState('0');
    const [ShortTerm51, setShortTerm51] = useState('0');
    const [ShortTerm52, setShortTerm52] = useState('0');
    const [ShortTerm53, setShortTerm53] = useState('0');
    const [ShortTerm54, setShortTerm54] = useState('0');
    const [ShortTerm55, setShortTerm55] = useState('0');
    const [ShortTerm56, setShortTerm56] = useState('0');
    const [Total1, setTotal1] = useState('');
    const [Total2, setTotal2] = useState('');
    const [Total3, setTotal3] = useState('');
    const [Total4, setTotal4] = useState('');
    const [Total5, setTotal5] = useState('');
    const [Total6, setTotal6] = useState('');
    const [initialLoad, setInitialLoad] = useState(true);
    const [selectedName, setSelectedName] = useState('');
    const [inputChanged, setInputChanged] = useState(false);
    const [options, setOptions] = useState([]);
    const [oldRegimeValue, setOldRegimeValue] = useState(0);




    





   
   ///
   const calculateAge = (birthdate) => {
    const today = new Date();
    const birthDate = new Date(birthdate);
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
};

const handleDateChange = (e) => {
    const currentDate = new Date();
    const birthDate = new Date(e.target.value);
    const diffInMilliseconds = Math.abs(currentDate - birthDate);
    const ageInYears = Math.floor(diffInMilliseconds / (1000 * 60 * 60 * 24 * 365));
    setAge(ageInYears);
    setFilingDateNew(e.target.value);

    // Update age group based on age
    if (ageInYears >= 1 && ageInYears <= 60) {
        setAgeGroup("age 1 to 60");
    } else if (ageInYears > 60 && ageInYears <= 80) {
        setAgeGroup("age 60 to 80");
    } else if (ageInYears > 80) {
        setAgeGroup("age l 80");
    }

    // Automatically check the checkbox based on age
    if (ageInYears > 60) {
        setAgeDistribution("resident");
    } else {
        setAgeDistribution("non-resident");
    }
};

const handleInputChangeNew = (e) => {
    // Your logic for handling other input changes
};
    ///




   
    




    const handleNameChange = (selectedOption) => {
        const selectedName = selectedOption.value;
        handleNameSelect(selectedOption.value);
        setSelectedName(selectedName);
        setManuallyEnteredName('');
        // Set the "name" state to the selected name
        setName(selectedName);

        // Retrieve the saved user data from local storage and parse it as JSON
        const userDataJSON = localStorage.getItem(selectedName);
        if (userDataJSON) {
            const userData = JSON.parse(userDataJSON);
            setShortTerm45(userData.input.LTCG_10Per_1503);
            setShortTerm15(userData.input.LTCG_10Per_1506);
            setShortTerm25(userData.input.LTCG_10Per_1509);
            setShortTerm35(userData.input.LTCG_10Per_1512);
            setShortTerm55(userData.input.LTCG_10Per_3103);
            setShortTerm44(userData.input.LTCG_112A_10Per_1503);
            setShortTerm14(userData.input.LTCG_112A_10Per_1506);
            setShortTerm24(userData.input.LTCG_112A_10Per_1509);
            setShortTerm34(userData.input.LTCG_112A_10Per_1512);
            setShortTerm54(userData.input.LTCG_112A_10Per_3103);
            setShortTerm46(userData.input.LTCG_20Per_1503);
            setShortTerm16(userData.input.LTCG_20Per_1506);
            setShortTerm26(userData.input.LTCG_20Per_1509);
            setShortTerm36(userData.input.LTCG_20Per_1512);
            setShortTerm56(userData.input.LTCG_20Per_3103);
            setShortTerm41(userData.input.STCG_15Per_1503);
            setShortTerm11(userData.input.STCG_15Per_1506);
            setShortTerm21(userData.input.STCG_15Per_1509);
            setShortTerm31(userData.input.STCG_15Per_1512);
            setShortTerm51(userData.input.STCG_15Per_3103);
            setShortTerm43(userData.input.STCG_Normal_1503);
            setShortTerm13(userData.input.STCG_Normal_1506);
            setShortTerm23(userData.input.STCG_Normal_1509);
            setShortTerm33(userData.input.STCG_Normal_1512);
            setShortTerm53(userData.input.STCG_Normal_3103);
            // Trigger the "Calculate" button programmatically
            handleCalculateClick(selectedName);
            console.log(selectedName);

        }

    };

    // useEffect(() => {
    //     // Programmatically click the "Calculate" button whenever selectedName changes
    //     if (selectedName) {
    //         handleCalculateClick(selectedName);
    //     }
    // }, [selectedName]);




    const handleCalculateClick = (selectedName) => {
        // Create an object containing the values/components you want to send
        const dataToSend = {
            name,
            region,
            financialYear,
            status,
            filingDate,
            filingDateNew,
            dueDate,
            gender,
            ageGroup,
            ageCategory, 
            residentStatus,
            ageDistribution,
            ShortTerm11,
            ShortTerm12,
            ShortTerm13,
            ShortTerm14,
            ShortTerm15,
            ShortTerm16,
            ShortTerm21,
            ShortTerm22,
            ShortTerm23,
            ShortTerm24,
            ShortTerm25,
            ShortTerm26,
            ShortTerm31,
            ShortTerm32,
            ShortTerm33,
            ShortTerm34,
            ShortTerm35,
            ShortTerm36,
            ShortTerm41,
            ShortTerm42,
            ShortTerm43,
            ShortTerm44,
            ShortTerm45,
            ShortTerm46,
            ShortTerm51,
            ShortTerm52,
            ShortTerm53,
            ShortTerm54,
            ShortTerm55,
            ShortTerm56,
            Total1,
            Total2,
            Total3,
            Total4,
            Total5,
            Total6,


        };
        handleCalculate(dataToSend);
    };

    const handleInputChange = (e) => {
        // Update the state based on input changes

        const { id, value } = e.target;
        switch (id) {
            case 'name':
                setName(value);
                break;
            case 'filingDate':
                setFilingDate(value);
                break;
            case 'filingDateNew':
                setFilingDateNew(value);
                break;  
    
            case 'dueDate':
                setDueDate(value);
                break;
            case 'residentStatus':
                setResidentStatus(value);
                break;
            case 'region':
                setRegion(value);
                break;
            case 'financialYear':
                setFinancialYear(value);
                break;
            case 'ShortTerm11':
                setShortTerm11(value);
                break;
            case 'ShortTerm12':
                setShortTerm12(value);
                break;
            case 'ShortTerm13':
                setShortTerm13(value);
                break;
            case 'ShortTerm14':
                setShortTerm14(value);
                break;
            case 'ShortTerm15':
                setShortTerm15(value);
                break;
            case 'ShortTerm16':
                setShortTerm16(value);
                break;
            case 'ShortTerm21':
                setShortTerm21(value);
                break;
            case 'ShortTerm22':
                setShortTerm22(value);
                break;
            case 'ShortTerm23':
                setShortTerm23(value);
                break;
            case 'ShortTerm24':
                setShortTerm24(value);
                break;
            case 'ShortTerm25':
                setShortTerm25(value);
                break;
            case 'ShortTerm26':
                setShortTerm26(value);
                break;
            case 'ShortTerm31':
                setShortTerm31(value);
                break;
            case 'ShortTerm32':
                setShortTerm32(value);
                break;
            case 'ShortTerm33':
                setShortTerm33(value);
                break;
            case 'ShortTerm34':
                setShortTerm34(value);
                break;
            case 'ShortTerm35':
                setShortTerm35(value);
                break;
            case 'ShortTerm36':
                setShortTerm36(value);
                break;
            case 'ShortTerm41':
                setShortTerm41(value);
                break;
            case 'ShortTerm42':
                setShortTerm42(value);
                break;
            case 'ShortTerm43':
                setShortTerm43(value);
                break;
            case 'ShortTerm44':
                setShortTerm44(value);
                break;
            case 'ShortTerm45':
                setShortTerm45(value);
                break;
            case 'ShortTerm46':
                setShortTerm46(value);
                break;
            case 'ShortTerm51':
                setShortTerm51(value);
                break;
            case 'ShortTerm52':
                setShortTerm52(value);
                break;
            case 'ShortTerm53':
                setShortTerm53(value);
                break;
            case 'ShortTerm54':
                setShortTerm54(value);
                break;
            case 'ShortTerm55':
                setShortTerm55(value);
                break;
            case 'ShortTerm56':
                setShortTerm56(value);
                break;
            case 'Total1':
                setTotal1(value);
                break;
            case 'Total2':
                setTotal2(value);
                break;
            case 'Total3':
                setTotal3(value);
                break;
            case 'Total4':
                setTotal4(value);
                break;
            case 'Total5':
                setTotal5(value);
                break;
            case 'Total6':
                setTotal6(value);
                break;
            case 'basicsalary':
                setbasicsalary(value);
                break;
            case 'houseproperty':
                sethouseproperty(value);
                break;

            default:
                break;

        }

        setInputChanged(true);
        // Programmatically click the "Calculate" button
        triggerCalculateButtonClick();
    };


    const triggerCalculateButtonClick = () => {
        // Use a ref to access the "Calculate" button element
        if (calculateButtonRef.current) {
            calculateButtonRef.current.click();
        }
    };

    const handleSubmit = () => {
        // Handle the calculation when the "Calculate" button is clicked
        const dataToSend = {
            name,
            region,
            financialYear,
            status,
            filingDate,
            dueDate,
            gender,
            residentStatus,
            ShortTerm11,
            ShortTerm12,
            ShortTerm13,
            ShortTerm14,
            ShortTerm15,
            ShortTerm16,
            ShortTerm21,
            ShortTerm22,
            ShortTerm23,
            ShortTerm24,
            ShortTerm25,
            ShortTerm26,
            ShortTerm31,
            ShortTerm32,
            ShortTerm33,
            ShortTerm34,
            ShortTerm35,
            ShortTerm36,
            ShortTerm41,
            ShortTerm42,
            ShortTerm43,
            ShortTerm44,
            ShortTerm45,
            ShortTerm46,
            ShortTerm51,
            ShortTerm52,
            ShortTerm53,
            ShortTerm54,
            ShortTerm55,
            ShortTerm56,
            Total1,
            Total2,
            Total3,
            Total4,
            Total5,
            Total6,
            selectedName,
            oldRegimeValue

        };

        handleCalculate(dataToSend);
    };

    // console.log(selectedName);

    // Create a ref for the "Calculate" button
    const calculateButtonRef = useRef();
    useEffect(() => {
        // Programmatically click the "Calculate" button whenever selectedName changes
        if (selectedName) {
            handleCalculateClick(selectedName);
        }
    }, [selectedName]);


    ///edit
    


    //new edit


    useEffect(() => {
        // Load options from local storage
        const localStorageKeys = Object.keys(localStorage);
        const nameOptions = localStorageKeys.map((key) => ({
            value: key,
            label: key,
        }));
        setOptions(nameOptions);
    }, []);



    useEffect(() => {
        // Set the default date when the component mounts
        setDueDate('2024-07-31');
    }, []);


    


    useEffect(() => {
        // Check if it's not the initial page load and any input field has changed
        if (!initialLoad && inputChanged) {
            // Programmatically click the Calculate button
            calculateButtonRef.current.click();

            // Reset inputChanged to false after triggering the click
            setInputChanged(false);
        } else {
            // If it's the initial load, set the initialLoad flag to false
            setInitialLoad(false);

            // If it's the initial load, also trigger the calculation
            handleCalculateClick();
        }
    }, [inputChanged, initialLoad]);

    useEffect(() => {
        // Set the default date to the current system date when the component mounts
        const currentDate = new Date().toISOString().split('T')[0];
        setFilingDate(currentDate);
    }, []);

    useEffect(() => {
        setTotal1(parseInt(ShortTerm11) + parseInt(ShortTerm21) + parseInt(ShortTerm31) + parseInt(ShortTerm41) + parseInt(ShortTerm51));
    }, [ShortTerm11, ShortTerm21, ShortTerm31, ShortTerm41, ShortTerm51]);

    useEffect(() => {
        setTotal3(parseInt(ShortTerm13) + parseInt(ShortTerm23) + parseInt(ShortTerm33) + parseInt(ShortTerm43) + parseInt(ShortTerm53));
    }, [ShortTerm13, ShortTerm23, ShortTerm33, ShortTerm43, ShortTerm53]);

    useEffect(() => {
        setTotal4(parseInt(ShortTerm14) + parseInt(ShortTerm24) + parseInt(ShortTerm34) + parseInt(ShortTerm44) + parseInt(ShortTerm54));
    }, [ShortTerm14, ShortTerm24, ShortTerm34, ShortTerm44, ShortTerm54]);

    useEffect(() => {
        setTotal5(parseInt(ShortTerm15) + parseInt(ShortTerm25) + parseInt(ShortTerm35) + parseInt(ShortTerm45) + parseInt(ShortTerm55));
    }, [ShortTerm15, ShortTerm25, ShortTerm35, ShortTerm45, ShortTerm55]);

    useEffect(() => {
        setTotal6(parseInt(ShortTerm16) + parseInt(ShortTerm26) + parseInt(ShortTerm36) + parseInt(ShortTerm46) + parseInt(ShortTerm56));
    }, [ShortTerm16, ShortTerm26, ShortTerm36, ShortTerm46, ShortTerm56]);



    useEffect(() => {
        // Load oldRegimeValue from local storage when the component mounts
        const savedOldRegimeValue = localStorage.getItem('oldRegimeValue');
        if (savedOldRegimeValue !== null) {
            setOldRegimeValue(parseFloat(savedOldRegimeValue));
        }
    }, []);

    useEffect(() => {
        // Update oldRegimeValue when output changes
        if (output && output.NbalancePayable !== undefined) {
            setOldRegimeValue(output.NbalancePayable);
        }
    }, [output]);


  


   


    return (
        <div className="App">
            <div className="spacer_2"></div> {/* Spacer div */}
            <div className="personal-info-title">Personal Information</div>
            <div className="your-container_2">
                {/* Old Regime Box */}
                <div className="value-box-2" id="oldRegime" value={ output.NbalancePayable}>
                    <div className="permanent-text" style={{ fontSize: '16px',fontWeight: 'bold' }}>
                        Old Regime:
                    </div>
                    <div className="value">
                        {oldRegimeValue !== null ? oldRegimeValue : 'Loading...'}
                    </div>
                </div>
            </div>

    
            {/* <div className="spacer"></div> Spacer div */}

            <div className="form-group-1">
                <div className="HTML_Part_9">
                    <label htmlFor="Name">Name:</label>
                    <input
                        type="taxt"
                        id="name"
                        value={name}
                        onChange={(e) => {
                            setName(e.target.value); // Call setName with the new value
                            handleInputChange(e);    // Call handleInputChange with the event object
                        }}
                    />
                </div>
                <div className="HTML_Part_Select">
                    <label htmlFor="Name">Select:</label>
                    <div>
                        <Select
                            inputId="nameDropdown"
                            value={options.find((option) => option.value === manuallyEnteredName)}
                            options={options}
                            onChange={handleNameChange}
                            styles={{
                                control: (provided) => ({
                                    ...provided,
                                    minHeight: '20px', // Adjust the minimum height as needed
                                    height: '20px', // Adjust the height as needed
                                    borderColor: 'black', // Set your desired border color
                                    fontSize: '0px',
                                }),
                                dropdownIndicator: (provided) => ({
                                    ...provided,
                                    display: 'none', // Hide the down arrow
                                }),
                            }}
                        />
                    </div>
                </div>
            </div>
            <div className="form-group-1"> {/* Add a new form-group-2 for the second row */}
                <div className="HTML_Part_9">
                    <label htmlFor="Assessment Year">Assessment Year:</label>
                    <select
                        id="Assessment Year"
                        value={financialYear}
                        onChange={(e) => {
                            setFinancialYear(e.target.value);
                            handleInputChange(e);
                        }}
                        className="input-field"
                    >
                        <option value="2022-2023">2022-2023</option>
                        <option value="2023-2024">2023-2024</option>
                        <option value="2024-2025">2024-2025</option>
                    </select>
                </div>
                <div className="HTML_Part_9">
                    <label htmlFor="region">Regime:</label>
                    <select
                        id="region"
                        value={region}
                        onChange={(e) => {
                            setRegion(e.target.value);
                            handleInputChange(e);
                        }}
                    >
                        <option value="Old">Old</option>
                        <option value="New">New</option>
                    </select>
                </div>
            </div>
            <div className="form-group-1"> {/* Add a new form-group-3 for the third row */}
                <div className="HTML_Part_9">
                    <label htmlFor="filingDate">Filing Date:</label>
                    <input
                        type="date"
                        id="filingDate"
                        value={filingDate}
                        onChange={(e) => {
                            setFilingDate(e.target.value);
                            handleInputChange(e);
                        }}
                    />
                </div>
                <div className="HTML_Part_9">
                    <label htmlFor="dueDate">Due Date:</label>
                    <input
                        type="date"
                        id="dueDate"
                        value={dueDate}
                        onChange={(e) => {
                            setDueDate(e.target.value);
                            handleInputChange(e);
                        }}
                    />
                </div>
            </div>
            <div className="form-group-1"> {/* Add a new form-group-4 for the fourth row */}
                <div className="HTML_Part_9">
                    <label htmlFor="gender">Gender:</label>
                    <select
                        id="gender"
                        value={gender}
                        onChange={(e) => {
                            setGender(e.target.value);
                            handleInputChange(e);
                        }}
                    >
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div className="HTML_Part_9">
                    <label htmlFor="residentStatus">Resident Status:</label>
                    <select
                        id="residentStatus"
                        value={residentStatus}
                        onChange={(e) => {
                            setResidentStatus(e.target.value);
                            handleInputChange(e);
                        }}
                    >
                        <option value="resident">Resident</option>
                        <option value="non-resident">Non-Resident</option>
                        <option value="nri">NRI</option>
                    </select>
                </div>
            </div>
            <div>
                </div>
                <div className="form-group-1"> {/* Add a new form-group-3 for the third row */}
                <div className="HTML_Part_9">
                    <label htmlFor="filingDateNew">Dath Of Birth:</label>
                    <input
                        type="date"
                        id="filingDateNew"
                        value={filingDateNew}
                        onChange={handleDateChange}
                        
                    />
                </div>
                <div className="HTML_Part_9">
                    <label htmlFor="ageGroup">Age Category:</label>
                    <select
                        id="ageGroup"
                        value={ageGroup}
                        onChange={(e) => {
                            setAgeGroup(e.target.value);
                            handleInputChange(e);
                        }}
                    >
                       <option value="age 60">Age 60</option>
                        <option value="age 60 to 80">Age 60 to 80</option>
                        <option value="age l 80">Age 80 Above </option>
                    </select>
                </div>
            </div>
            <div>
               


                
</div>
            


               <div className="spacer"></div> {/* Spacer div */}
            <div className="spacer"></div> {/* Spacer div */}

            <div className="app">
                
                <div className="capital-info-title">Capital Gain Breakup</div>
                <table cellPadding="1" cellSpacing="1">
                    <thead>
                        <tr>
                            <th></th>
                            <th colSpan={2.5} style={{ fontSize: '15px' }}>Short term</th>
                            <th colSpan={3.5} style={{ fontSize: '15px' }}>Long Term</th>
                        </tr>
                        <tr>
                            <th></th>
                            <th>111A-15%</th>
                            <th>Others-Slab Rate</th>
                            <th>112A-10%</th>
                            <th>Others-10%</th>
                            <th>Others-20%</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th>15/6</th>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm11"
                                            value={ShortTerm11}
                                            onChange={(e) => {
                                                handleInputChange(e);
                                                setShortTerm11(e.target.value);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm13"
                                            value={ShortTerm13}
                                            onChange={(e) => {
                                                setShortTerm13(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm14"
                                            value={ShortTerm14}
                                            onChange={(e) => {
                                                setShortTerm14(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm15"
                                            value={ShortTerm15}
                                            onChange={(e) => {
                                                setShortTerm15(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm16"
                                            value={ShortTerm16}
                                            onChange={(e) => {
                                                setShortTerm16(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>


                            <th>15/9</th>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm21"
                                            value={ShortTerm21}
                                            onChange={(e) => {
                                                setShortTerm21(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm23"
                                            value={ShortTerm23}
                                            onChange={(e) => {
                                                setShortTerm23(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm24"
                                            value={ShortTerm24}
                                            onChange={(e) => {
                                                setShortTerm24(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm25"
                                            value={ShortTerm25}
                                            onChange={(e) => {
                                                setShortTerm25(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm26"
                                            value={ShortTerm26}
                                            onChange={(e) => {
                                                setShortTerm26(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>

                            </td>
                        </tr>
                        <tr>
                            <th>15/12</th>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm31"
                                            value={ShortTerm31}
                                            onChange={(e) => {
                                                setShortTerm31(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm33"
                                            value={ShortTerm33}
                                            onChange={(e) => {
                                                setShortTerm33(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm34"
                                            value={ShortTerm34}
                                            onChange={(e) => {
                                                setShortTerm34(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm35"
                                            value={ShortTerm35}
                                            onChange={(e) => {
                                                setShortTerm35(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm36"
                                            value={ShortTerm36}
                                            onChange={(e) => {
                                                setShortTerm36(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>

                        </tr>
                        <tr>
                            <th>15/3</th>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm41"
                                            value={ShortTerm41}
                                            onChange={(e) => {
                                                setShortTerm41(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>

                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm43"
                                            value={ShortTerm43}
                                            onChange={(e) => {
                                                setShortTerm43(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm44"
                                            value={ShortTerm44}
                                            onChange={(e) => {
                                                setShortTerm44(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm45"
                                            value={ShortTerm45}
                                            onChange={(e) => {
                                                setShortTerm45(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm46"
                                            value={ShortTerm46}
                                            onChange={(e) => {
                                                setShortTerm46(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>

                        </tr>
                        <tr>
                            <th>31/3</th>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm51"
                                            value={ShortTerm51}
                                            onChange={(e) => {
                                                setShortTerm51(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>

                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm53"
                                            value={ShortTerm53}
                                            onChange={(e) => {
                                                setShortTerm53(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm54"
                                            value={ShortTerm54}
                                            onChange={(e) => {
                                                setShortTerm54(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm55"
                                            value={ShortTerm55}
                                            onChange={(e) => {
                                                setShortTerm55(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="ShortTerm56"
                                            value={ShortTerm56}
                                            onChange={(e) => {
                                                setShortTerm56(e.target.value);
                                                handleInputChange(e);
                                            }}
                                        />
                                    </div>
                                </div>
                            </td>

                        </tr>
                        <tr>
                            <th>Total</th>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="Total1"
                                            value={Total1}
                                            onChange={(e) => {
                                                setTotal1(e.target.value);
                                                handleInputChange(e);
                                            }}
                                            disabled={true}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="Total3"
                                            value={Total3}
                                            onChange={(e) => {
                                                setTotal3(e.target.value);
                                                handleInputChange(e);
                                            }}
                                            disabled={true}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="Total4"
                                            value={Total4}
                                            onChange={(e) => {
                                                setTotal4(e.target.value);
                                                handleInputChange(e);
                                            }}
                                            disabled={true}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="Total5"
                                            value={Total5}
                                            onChange={(e) => {
                                                setTotal5(e.target.value);
                                                handleInputChange(e);
                                            }}
                                            disabled={true}
                                        />
                                    </div>
                                </div>
                            </td>
                            <td>
                                <div className="">
                                    <div className="">
                                        <input
                                            type="number"
                                            id="Total5"
                                            value={Total6}
                                            onChange={(e) => {
                                                setTotal6(e.target.value);
                                                handleInputChange(e);
                                            }}
                                            disabled={true}
                                        />
                                    </div>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <button
                    ref={calculateButtonRef}
                    type="submit"
                    className="submit-button_1"
                    style={{ display: 'none' }}
                    onClick={() => {
                        handleCalculateClick(); // Trigger calculation first
                    }}
                >
                    Calculate
                </button>
            </div>
        </div>
    );
}

const Page2 = ({ handleCalculateInPage1, dataFromPage1, selectedName, handleOutputUpdate }) => {
    // Define state variables and their initial values
    // const [houseproperty, sethouseproperty] = useState('0');
    // const [business_profession, setbusiness_profession] = useState('0');
    const [taxWithoutSurcharge, settaxWithoutSurcharge] = useState('0');
    const [lessRebate87A, setLessRebate87A] = useState('0');
    
    const [tds, setTDS] = useState('0');
    const [agriculturalIncome, setAgriculturalIncome] = useState('0');
   
    const [incomeTaxNormal, setIncomeTaxNormal] = useState('0');
    const [incomeTaxSpecial, setIncomeTaxSpecial] = useState('0');
    const [gross_total_income, setgrosstotalincome] = useState(0);
    const [capitalgain_1, setcapitalgain] = useState(0);
    const [intA, setintA] = useState(0);
    const [intB, setintB] = useState(0);
    const [intC, setintC] = useState(0);
    const [dueDate_1, setDueDate] = useState("");
    const [filingDate1, setFilingDate] = useState("");
    // const [deductionUnderChapterVIA, setDeductionUnderChapterVIA] = useState('0');
    const [deductionunderchaptervip, setdeductionunderchaptervip] = useState('0');
    const [calculateClicked, setCalculateClicked] = useState(false);
    const [inputModified, setInputModified] = useState(false);
    const [output, setOutput] = useState('');
  
    const [response, setResponse] = useState('');
    const [showCalculateMessage, setShowCalculateMessage] = useState(false);
    const [secondApiOutput, setSecondApiOutput] = useState({});
    const [selectedName_1, setSelectedName] = useState('');
    const [newFieldValue, setNewFieldValue] = useState('');
    const [options, setOptions] = useState([]);
    const [newRegimeValue, setNewRegimeValue] = useState(0);
    const [deductionVI, setDeductionVI] = useState(/* initial value */);
    const [aeighthC, setAeighthC] = useState(/* initial value */);
    // const [basicsalary, setbasicsalary] = useState([]);
    const ShortTerm11 = dataFromPage1.ShortTerm11;
    const [isSalaryPopupComplete, setIsSalaryPopupComplete] = useState(false);
 
    const [grosstotalincome, setGrossTotalIncome] = useState('');
    const [totalIncome, setTotalIncome] = useState('');
    const [taxwoSurcharge, setTaxwoSurcharge] = useState('');
    
    const [lessrebate87A, setLessrebate87A] = useState('');
    const [surcharge, setSurcharge] = useState('');
    const [educationCess, setEducationCess] = useState('')
    const [taxPayable, setTaxPayable] = useState('')
    
    const [balancePayable, setBalancePayable] = useState('')
    //
    const [taxPayableRefundable, setTaxPayableRefundable] = useState('')
    const [inccomeTax, setInccomeTax] = useState('')
    const [t234A, setT234A] = useState('')
    const [t234B, setT234B] = useState('')
    const [t234C, setT234C] = useState('')
    const [total_234, setTotal_234] = useState('')

    const [normalTax, setNormalTax] = useState('')
    const [specialTax, setSpecialTax] = useState('')
    const [totalTax, setTotalTax] = useState('')
    const [taxableIncome, setTaxableIncome] = useState('')
    const [oldRegimeValue, setOldRegimeValue] = useState('')
    
    
    




    // console.log(ShortTerm11);
    const ShortTerm13 = dataFromPage1.ShortTerm13;
    const ShortTerm14 = dataFromPage1.ShortTerm14;
    const ShortTerm15 = dataFromPage1.ShortTerm15;
    const ShortTerm16 = dataFromPage1.ShortTerm16;
    const ShortTerm21 = dataFromPage1.ShortTerm21;
    const ShortTerm23 = dataFromPage1.ShortTerm23;
    const ShortTerm24 = dataFromPage1.ShortTerm24;
    const ShortTerm25 = dataFromPage1.ShortTerm25;
    const ShortTerm26 = dataFromPage1.ShortTerm26;
    const ShortTerm31 = dataFromPage1.ShortTerm31;
    const ShortTerm33 = dataFromPage1.ShortTerm33;
    const ShortTerm34 = dataFromPage1.ShortTerm34;
    const ShortTerm35 = dataFromPage1.ShortTerm35;
    const ShortTerm36 = dataFromPage1.ShortTerm36;
    const ShortTerm41 = dataFromPage1.ShortTerm41;
    const ShortTerm43 = dataFromPage1.ShortTerm43;
    const ShortTerm44 = dataFromPage1.ShortTerm44;
    const ShortTerm45 = dataFromPage1.ShortTerm45;
    const ShortTerm46 = dataFromPage1.ShortTerm46;
    const ShortTerm51 = dataFromPage1.ShortTerm51;
    const ShortTerm53 = dataFromPage1.ShortTerm53;
    const ShortTerm54 = dataFromPage1.ShortTerm54;
    const ShortTerm55 = dataFromPage1.ShortTerm55;
    const ShortTerm56 = dataFromPage1.ShortTerm56;
    const region = dataFromPage1.region;
    const financialYear = dataFromPage1.financialYear;
    const filingDate = dataFromPage1.filingDate;
    const dueDate = dataFromPage1.dueDate;
    const gender = dataFromPage1.gender;
    const residentStatus = dataFromPage1.residentStatus;
    const capitalgain = dataFromPage1.capitalgain;
    const name = dataFromPage1.name;
    const Total1 = dataFromPage1.Total1;
    const Total2 = dataFromPage1.Total2;
    const Total3 = dataFromPage1.Total3;
    const Total4 = dataFromPage1.Total4;
    const Total5 = dataFromPage1.Total5;
    const Total6 = dataFromPage1.Total6;
    const [taxMethod, setTaxMethod] = useState('N'); // Default value 'N', assuming taxMethod is a string state
    const sum = Total1 + Total3 + Total4 + Total5 + Total6;
    // console.log(sum)

    const handleDeleteRecord = () => {
        const nameToDelete = selectedName; // The name to delete

        // Check if the name exists in local storage
        if (localStorage.getItem(nameToDelete)) {
            localStorage.removeItem(nameToDelete); // Delete the record
            alert(`${nameToDelete}'s record has been deleted.`);
        } else {
            alert(`${nameToDelete}'s record does not exist.`);
        }

        window.location.reload();
    };
    
    
    const handleFieldAndInputChange_1 = (fieldName, value, e) => {
        handlePopupFieldChange_1(fieldName, value);
        handleInputChange(e);
    };

    const handleInputChange = (e) => {
        setShowCalculateMessage(true);
        switch (e.target.id) {

            case 'basicsalary':
                setbasicsalary(e.target.value);
                break;
            case 'houseproperty':
                sethouseproperty(e.target.value);
                break;
            case 'business_profession':
                setbusiness_profession(e.target.value);
                break;

            case 'deductionunderchaptervip':
                setdeductionunderchaptervip(e.target.value);
                break;

            case 'agriculturalIncome':
                setAgriculturalIncome(e.target.value);
                break;


            default:
                break;
        }


        // Set calculateClicked to false when any input field is changed
        setCalculateClicked(false);
    };




       

    <Page1 handleInputChange={handleInputChange} />

    const handleFieldAndInputChange = (fieldName, value, e) => {
        handlePopupFieldChange_2(fieldName, value);
        handleInputChange(e);
    };


    const handleFieldAndInputChange_7 = (fieldName, value, e) => {
        setPopupFields_7((prevFields) => ({
            ...prevFields,
            [fieldName]: parseFloat(value),
        }));

        // Assuming you want to update LTCG_4 based on the "Other Sources Includes Dividend" field
        if (fieldName === "Other Sources Includes Dividend") {
            setLTCG_4(parseFloat(value));
        }

        // Handle other field-specific logic if needed

        // Assuming you want to trigger the handleSubmit_2 function
        if (e.target.value === 'submit2') {
            handleSubmit(e);
        }
    };

    useEffect(() => {
        if (selectedName) {
            // Retrieve the data associated with the selectedName from local storage
            const userDataJSON = localStorage.getItem(selectedName);

            if (userDataJSON) {
                // If data is available, parse it and update the state variables
                const userData = JSON.parse(userDataJSON);
                setbasicsalary(userData.input.Salary);
                setbusiness_profession(userData.input.BusinessProfession);
               // setLessRebate87A(userData.output.lessRebate87A);
                sethouseproperty(userData.input.HouseProperty);
                setgrosstotalincome(userData.input.gross_total_income);
                setcapitalgain(userData.input.total_sum)

            }
        }
    }, [selectedName]);
    console.log(sum);



    useEffect(() => {
        // Set the default date when the component mounts
        setDueDate('2024-07-31');
    }, []);

    const [openPopup_1, setOpenPopup_1] = useState(false);
    const [popupFields_1, setPopupFields_1] = useState({
        'Advance Tax 1st inst': 0,
        "Advance Tax 2nd inst": 0,
        "Advance Tax 3rd inst": 0,
        "Advance Tax 4th inst": 0,
        "Advance Tax 5th inst": 0,
    });


    const [advanceTax1STInst, setadvanceTax1stInst] = useState(0);
    const handlePopupFieldChange_1 = (fieldName, value) => {
        setPopupFields_1((prevFields) => ({
            ...prevFields,
            [fieldName]: parseFloat(value),
        }));
    };

    const calculateAndSetDeduction_1 = () => {
        const sum = Object.values(popupFields_1).reduce((acc, val) => acc + parseFloat(val), 0);
        setadvanceTax1stInst(sum);
        setOpenPopup_1(false); // Close the popup
    };

    const [openPopup_2, setOpenPopup_2] = useState(false);
    const [popupFields_2, setPopupFields_2] = useState({
        "SA Tax Paid 1": { amount: 0, date: "" },
        "SA Tax Paid 2": { amount: 0, date: "" },
        "SA Tax Paid 3": { amount: 0, date: "" },
        "SA Tax Paid 4": { amount: 0, date: "" },
        "SA Tax Paid 5": { amount: 0, date: "" },
    });

    const [STCG_1, setSTCG_1] = useState(0);

    const handlePopupFieldChange_2 = (fieldName, key, value) => {
        setPopupFields_2((prevFields) => ({
            ...prevFields,
            [fieldName]: {
                ...prevFields[fieldName],
                [key]: value,
            },
        }));
    };

    const calculateAndSetDeduction_2 = () => {
        const sum = Object.values(popupFields_2).reduce((acc, val) => acc + parseFloat(val.amount), 0);
        setSTCG_1(sum);
        setOpenPopup_2(false); // Close the popup
    };

    // Calculate the total SA Tax Paid amount
    const totalSATAxPaid = Object.values(popupFields_2).reduce((acc, val) => acc + parseFloat(val.amount), 0);


    const [openPopup_7, setOpenPopup_7] = useState(false);
const [popupFields_7, setPopupFields_7] = useState({
    "Saving Interest": 0,
    "FD Interest": 0,
    "Dividend Income": 0,
    "Other Income": 0,
    "Dividend": 0,
    "15/6": 0,
    "15/9": 0,
    "15/12": 0,
    "15/3": 0,
    "31/3": 0,
});
const [LTCG_4, setLTCG_4] = useState(0);
const [popupMessage, setPopupMessage] = useState("");

const handlePopupFieldChange_7 = (fieldName, value) => {
    setPopupFields_7((prevFields) => ({
        ...prevFields,
        [fieldName]: parseFloat(value),
    }));
    // Whenever a field changes, recalculate deduction
    calculateAndSetDeduction_7();
};

const calculateAndSetDeduction_7 = () => {
    // Calculate deduction
    const sum = Object.values(popupFields_7).reduce((acc, val) => acc + parseFloat(val), 0) - popupFields_7["Dividend"];
    setLTCG_4(sum); // Assuming this is the correct calculation for deduction

    // Remove the logic that sets popupMessage
    setOpenPopup_7(false);
};






    const [openPopupChapterVIADeductions, setOpenPopupChapterVIADeductions] = useState(false);
    const [chapterVIADeductionsFields, setChapterVIADeductionsFields] = useState({
        "80C": 0,
        "Chapter VIA": 0,
    });

    const [deductionUnderChapterVIA, setDeductionUnderChapterVIA] = useState(0);

    const handleChapterVIADeductionsFieldChange = (fieldName, value) => {
        setChapterVIADeductionsFields((prevFields) => ({
            ...prevFields,
            [fieldName]: parseFloat(value),
        }));
    };

    const calculateAndSetChapterVIADeductions = () => {
        const totalChapterVIADeductions = Object.values(chapterVIADeductionsFields).reduce((acc, val) => acc + parseFloat(val), 0);
        setDeductionUnderChapterVIA(totalChapterVIADeductions);
        setOpenPopupChapterVIADeductions(false); // Close the Chapter VIA Deductions popup
    };

    const [openPopup80C, setOpenPopup80C] = useState(false);
    const [popupFields80C, setPopupFields80C] = useState({
        "LIC": 0,
        "Providend Fund": 0,
        "PPF": 0,
        "Housing Loan Repayment": 0,
        "NPS": 0,
        "ELLS": 0,
        "Tution Fees": 0,
        "Others": 0,
    });

    const handlePopupFieldChange80C = (fieldName, value) => {
        setPopupFields80C((prevFields) => ({
            ...prevFields,
            [fieldName]: parseFloat(value),
        }));
    };

    const calculateAndSet80C = () => {
        const total80C = Object.values(popupFields80C).reduce((acc, curr) => acc + curr, 0);
        setChapterVIADeductionsFields((prevFields) => ({
            ...prevFields,
            "80C": total80C,
        }));
        setOpenPopup80C(false); // Close the 80C popup
    };

    const [openPopupChapterVIA, setOpenPopupChapterVIA] = useState(false);
    const [popupFieldsChapterVIA, setPopupFieldsChapterVIA] = useState({
        "80D Self": 0,
        "80D Parents": 0,
        "80DD": 0,
        "80DDB": 0,
        "80 CCD (1B)": 0,
        "80 CCD (2)": 0,
        "80 EEA": 0,
        "80 FFB": 0,
        "80 U": 0,
        "80 E ": 0,
        "80 G(50%)": 0,
        "80 G (100%)": 0,
        "80 GGA": 0,
        "80 GGC": 0,
        "80 TTA": 0,
        "80 TTB": 0,
    });

    const handlePopupFieldChangeChapterVIA = (fieldName, value) => {
        setPopupFieldsChapterVIA((prevFields) => ({
            ...prevFields,
            [fieldName]: parseFloat(value),
        }));
    };

    const calculateAndSetChapterVIA = () => {
        const chapterVIAValue = Object.values(popupFieldsChapterVIA).reduce((acc, currentValue) => acc + currentValue, 0);
        setChapterVIADeductionsFields((prevFields) => ({
            ...prevFields,
            "Chapter VIA": chapterVIAValue,
        }));
        setOpenPopupChapterVIA(false); // Close the Chapter VIA popup
    };




    useEffect(() => {
        // Load options from local storage
        const localStorageKeys = Object.keys(localStorage);
        const nameOptions = localStorageKeys.map((key) => ({
            value: key,
            label: key,
        }));
        setOptions(nameOptions);
    }, []);


    useEffect(() => {
        // Calculate the sum of all fields except "Dividend" and "Other Income Includes Dividend"
        const sum = Object.keys(popupFields_7)
            .filter((key) => key !== "Dividend" && key !== "Other Sources Includes Dividend")
            .reduce((acc, key) => acc + popupFields_7[key], 0);

        // Update the "Dividend" field with the calculated sum
        setPopupFields_7((prevFields) => ({
            ...prevFields,
            Dividend: sum,
        }));
    }, [popupFields_7]);





    useEffect(() => {
        // Check if it's the initial page load (calculateClicked is still false)
        if (!calculateClicked) {
            // Programmatically click the Calculate button
            document.querySelector('.submit-button_2').click();
        }
    }, []);

    useEffect(() => {
        // Function to get today's date in the format "YYYY-MM-DD"
        const getTodayDate = () => {
            const today = new Date();
            const year = today.getFullYear();
            let month = today.getMonth() + 1;
            let day = today.getDate();

            // Add leading zeros if month/day is a single digit
            if (month < 10) {
                month = `0${month}`;
            }
            if (day < 10) {
                day = `0${day}`;
            }

            return `${year}-${month}-${day}`;
        };

        // Set the filing date to today's date
        setFilingDate(getTodayDate());
    }, []);

    const handleResetClick = () => {
        // Reload the page
        window.location.reload();
    };

    // console.log(basicsalary);

    useEffect(() => {
        // Load newRegimeValue from local storage when the component mounts
        const savedNewRegimeValue = localStorage.getItem('newRegimeValue');
        if (savedNewRegimeValue !== null) {
          setNewRegimeValue(parseFloat(savedNewRegimeValue));
        }
      }, []);
    
      useEffect(() => {
        if (output && output.RbalancePayable !== undefined) {
          setNewRegimeValue(output.RbalancePayable);
        }
      }, [output]);









const calculateButtonRef = useRef(null);

const [openPopupSalary, setOpenPopupSalary] = useState(false);
const [salaryFields, setSalaryFields] = useState({
    "Salary + DA": 0,
    "HRA Received": 0,
    "Other Allowances": 0,
    "Less : Allowances u/s 10":0,
    "Professional Tax": 0,
    "Standard Deduction": 50000,
});

const [basicsalary, setbasicsalary] = useState(0);

const handleSalaryFieldChange = (fieldName, value) => {
    setSalaryFields((prevFields) => ({
        ...prevFields,
        [fieldName]: parseFloat(value),
    }));
};

const calculateAndSetSalary = () => {
    const totalSalary = salaryFields["Salary + DA"] + salaryFields["HRA Received"] + salaryFields["Other Allowances"];
    const adjustedSalary = totalSalary - salaryFields["Less : Allowances u/s 10"] - salaryFields["Professional Tax"] - salaryFields["Standard Deduction"];
    
    // Ensure adjusted salary is not less than zero
    const basicSalaryAdjusted = Math.max(0, adjustedSalary);
    setbasicsalary(basicSalaryAdjusted);
    setOpenPopupSalary(false); // Close the salary popup
};

const [openPopupHouseProperty, setOpenPopupHouseProperty] = useState(false);
const [housePropertyFields, setHousePropertyFields] = useState({
    "Self Occupied": 0,
    "Rented House Property": 0,
});

const [houseproperty, sethouseproperty] = useState(0);

const handleHousePropertyFieldChange = (fieldName, value) => {
    setHousePropertyFields((prevFields) => ({
        ...prevFields,
        [fieldName]: parseFloat(value),
    }));
};

const calculateAndSetHouseProperty = () => {
    const totalHouseProperty = Object.values(housePropertyFields).reduce((acc, val) => acc + parseFloat(val), 0);
    sethouseproperty(totalHouseProperty);
    setOpenPopupHouseProperty(false); // Close the house property popup
};

const [openPopupSelfOccupied, setOpenPopupSelfOccupied] = useState(false);
const [selfOccupiedFields, setSelfOccupiedFields] = useState({
    "Interest on House Loan": 0,
});

const handleSelfOccupiedFieldChange = (fieldName, value) => {
    setSelfOccupiedFields((prevFields) => ({
        ...prevFields,
        [fieldName]: parseFloat(value),
    }));
};

const calculateAndSetSelfOccupied = () => {
    // Calculate total for "Self Occupied" field
    const totalSelfOccupied = Object.values(selfOccupiedFields).reduce((acc, val) => acc + parseFloat(val), 0);
    
    // Set the calculated total for "Self Occupied"
    setHousePropertyFields((prevFields) => ({
        ...prevFields,
        "Self Occupied": Math.max(totalSelfOccupied, 0), // Ensure non-negative value
    }));

    setOpenPopupSelfOccupied(false); // Close the Self Occupied popup
};

const [openPopupRentedHouseProperty, setOpenPopupRentedHouseProperty] = useState(false);
const [rentedHousePropertyFields, setRentedHousePropertyFields] = useState({
    "Rent Received": 0,
    "Property Tax": 0,
    "Interest on House Loan": 0,
    "Repair Charges": 0,
});

const handleRentedHousePropertyFieldChange = (fieldName, value) => {
    setRentedHousePropertyFields((prevFields) => ({
        ...prevFields,
        [fieldName]: parseFloat(value),
    }));
};

const calculateAndSetRentedHouseProperty = () => {
    // Calculate total for "Rented House Property"
    const totalRentedHouseProperty = Object.values(rentedHousePropertyFields).reduce((acc, val) => acc + parseFloat(val), 0);
    
    // Set the calculated total for "Rented House Property"
    setHousePropertyFields(prevFields => ({
        ...prevFields,
        "Rented House Property": Math.max(totalRentedHouseProperty, 0), // Ensure non-negative value
    }));
    
    setOpenPopupRentedHouseProperty(false); // Close the Rented House Property popup
};



    const [openPopupBusinessProfession, setOpenPopupBusinessProfession] = useState(false);
    const [businessProfessionFields, setBusinessProfessionFields] = useState({
        "Business": 0,
        "Profession": 0,
    });

    const [business_profession, setbusiness_profession] = useState(0);

    const handleBusinessProfessionFieldChange = (fieldName, value) => {
        setBusinessProfessionFields((prevFields) => ({
            ...prevFields,
            [fieldName]: parseFloat(value),
        }));
    };

    const calculateAndSetBusinessProfession = () => {
        const totalBusinessProfession = Object.values(businessProfessionFields).reduce((acc, val) => acc + parseFloat(val), 0);
        setbusiness_profession(totalBusinessProfession);
        setOpenPopupBusinessProfession(false); // Close the business/profession popup

       
    };

    const generatePayload = (taxMethod) => {
        // Create your payload here using the provided taxMethod
        let payload = {}; // Initialize an empty payload
    
        // Your payload generation logic here based on the taxMethod
        
        return payload;
    };



    const handleSubmit = async (e) => {
        e.preventDefault();
        setCalculateClicked(true);
        setInputModified(false);
        
       
        try {
            let payload = {}; // Initialize an empty payload
           
         
    
            if (e.target.value === 'submit2') {
                payload = {
                    "first_payload": {
                        "Salary": {
                            SalaryDA: salaryFields["Salary + DA"],
                            HRAReceived: salaryFields["HRA Received"],
                            OtherAllowances: salaryFields["Other Allowances"],
                            LessAllowancesu10: salaryFields["Less : Allowances u/s 10"],
                            ProfessionalTax: salaryFields["Professional Tax"],
                            StandardDeduction: salaryFields["Standard Deduction"]
                        },
                        "HouseProperty": {
                            "SelfOccupiedInterestonHouLoan": housePropertyFields["Self Occupied"],
                           "RentReceived": rentedHousePropertyFields["Rent Received"], // Update with dynamic value
                           "PropertyTax": rentedHousePropertyFields["Property Tax"],
                            "RentedHousePropertyInterestonHouLoan": housePropertyFields["Rented House Property"],
                            "RepairCharges": rentedHousePropertyFields["Repair Charges"] // Updated key name
    
                        },
                        "BusinessProfession": {
                            "Business": businessProfessionFields["Business"],
                            "Profession": businessProfessionFields["Profession"],
                        },
                        "OtherSources": {
                            "SavingInterest": popupFields_7["Saving Interest"],
                            "FDInterest": popupFields_7["FD Interest"],
                            "DividendIncome": popupFields_7["Dividend Income"],
                            "OtherIncome": popupFields_7["Other Income"]
                        },
                        "DeductionVIAeighthC": {
                            
                                "eighthLIC": popupFields80C["LIC"],
                                "eighthProvidendFund": popupFields80C["Providend Fund"],
                                "eighthPPF": popupFields80C["PPF"],
                                "eighthHousingLoanRepayment": popupFields80C["Housing Loan Repayment"],
                                "eighthNPS": popupFields80C["NPS"],
                                "eighthELLS": popupFields80C["ELLS"],
                                "eighthTutionFees": popupFields80C["Tution Fees"],
                                "eighthOthers": popupFields80C["Others"],
                                "eighthDSelf": popupFieldsChapterVIA["80D Self"],
                                "eighthDParents": popupFieldsChapterVIA["80D Parents"],
                                "eighthDD": popupFieldsChapterVIA["80DD"],
                                "eighthDDB": popupFieldsChapterVIA["80DDB"],
                                "eighthCCDoneB": popupFieldsChapterVIA["80 CCD (1B)"],
                                "eighthCCDtwo": popupFieldsChapterVIA["80 CCD (2)"],
                                "eighthEEA": popupFieldsChapterVIA["80 EEA"],
                                "eighthFFB": popupFieldsChapterVIA["80 FFB"],
                                "eighthU": popupFieldsChapterVIA["80 U"],
                                "eighthE": popupFieldsChapterVIA["80 E "],
                                "eighthGfiftypercent": popupFieldsChapterVIA["80 G(50%)"],
                                "eighthGhundredpercent": popupFieldsChapterVIA["80 G (100%)"],
                                "eighthGGA": popupFieldsChapterVIA["80 GGA"],
                                "eighthGGC": popupFieldsChapterVIA["80 GGC"],
                                "eighthTTA": popupFieldsChapterVIA["80 TTA"],
                                "eighthTTB": popupFieldsChapterVIA["80 TTB"]
                        }
                
                        
    
                    },
                    "second_payload": {
                        "AdvanceTax": {
                            "FifthInst": popupFields_1["Advance Tax 5th inst"],
                            "FirstInst": popupFields_1["Advance Tax 1st inst"],
                            "ForthInst": popupFields_1["Advance Tax 4th inst"],
                            "SecondInst": popupFields_1["Advance Tax 2nd inst"],
                            "ThirdInst": popupFields_1["Advance Tax 3rd inst"]
                        },
                        "AgricultureIncome":  parseFloat(agriculturalIncome),
                        "blnIncAgriInc": "false",
                        "BusinessProfession":{} ,
                        "DedutionUSCHVIA": {},
                        "Divident_115BBDAAmt": 0,
                        "Divident_115BBDAAmt_1503":popupFields_7["15/3"] ,
                        "Divident_115BBDAAmt_1506":  popupFields_7["15/6"],
                        "Divident_115BBDAAmt_1509":  popupFields_7["15/9"],
                        "Divident_115BBDAAmt_1512": popupFields_7["15/12"],
                        "Divident_115BBDAAmt_3103":  popupFields_7["31/3"],
                        "Divident_Income":  popupFields_7["Dividend"],
                        "DOB": "/Date(599596200000+0530)/",
                        "dtDate01062001": "/Date(991333800000+0530)/",
                        "dtDate01072010": "/Date(1277922600000+0530)/",
                        "dtDate01092003": "/Date(1062354600000+0530)/",
                        "Due_Date": "/Date(1659205800000+0530)/",
                        "Filing_Date": "/Date(1657218600000+0530)/",
                        "Gender": "M",
                      
                        "IS_115BA_BAA_BAB": "null",
                        "ITR_Status": "01",
                        "LastDayAY": "/Date(1648665000000+0530)/",
                        "lngAgriTax": 0,
                        "Lottery_WinAmt": 0,
                        "Lottery_WinAmt_1503": 0,
                        "Lottery_WinAmt_1506": 0,
                        "Lottery_WinAmt_1509": 0,
                        "Lottery_WinAmt_1512": 0,
                        "Lottery_WinAmt_3103": 0,
                        "LTCG_10Per": 0,
                        "LTCG_10Per_1503": parseFloat(ShortTerm15),
                        "LTCG_10Per_1506": parseFloat(ShortTerm25),
                        "LTCG_10Per_1509":  parseFloat(ShortTerm35),
                        "LTCG_10Per_1512": parseFloat(ShortTerm45),
                        "LTCG_10Per_3103":  parseFloat(ShortTerm55),
                        "LTCG_112A_10Per": 0,
                        "LTCG_112A_10Per_1503": parseFloat(ShortTerm14),
                        "LTCG_112A_10Per_1506":parseFloat(ShortTerm24),
                        "LTCG_112A_10Per_1509":  parseFloat(ShortTerm34),
                        "LTCG_112A_10Per_1512": parseFloat(ShortTerm44),
                        "LTCG_112A_10Per_3103": parseFloat(ShortTerm55),
                        "LTCG_20Per": 0,
                        "LTCG_20Per_1503":parseFloat(ShortTerm16), 
                        "LTCG_20Per_1506": parseFloat(ShortTerm26),
                        "LTCG_20Per_1509": parseFloat(ShortTerm36),
                        "LTCG_20Per_1512": parseFloat(ShortTerm46),
                        "LTCG_20Per_3103": parseFloat(ShortTerm56),
                        "OtherSources": {},
                        "Relief_Amt": 0,
                        "ResiStatus": "R",
                        "Salary": {},
                        "selefAssments": [],
                        "Self_AssAmt": 0,
                        "STCG_15Per": 0,
                        "STCG_15Per_1503":parseFloat(ShortTerm11) ,
                        "STCG_15Per_1506":parseFloat(ShortTerm21) ,
                        "STCG_15Per_1509": parseFloat(ShortTerm31),
                        "STCG_15Per_1512": parseFloat(ShortTerm41),
                        "STCG_15Per_3103": parseFloat(ShortTerm51),
                        "STCG_Normal": 0,
                        "STCG_Normal_1503": parseFloat(ShortTerm13),
                        "STCG_Normal_1506": parseFloat(ShortTerm23),
                        "STCG_Normal_1509": parseFloat(ShortTerm33),
                        "STCG_Normal_1512": parseFloat(ShortTerm43),
                        "STCG_Normal_3103": parseFloat(ShortTerm53),
                        "strAY": "2023-2024",
                        "T80C_In": 0,
                        "TaxMethod": region === 'Old' ? "N" : "R",
                        "TDSAmt": 0,
                        selefAssments: [totalSATAxPaid],
                        strAY: financialYear,
                        whichSubmit: e.target.value,
                
                    }
                };
            }
             
            
            
            
    


        

            
        
        
        

        
    
            const response = await axios.post('http://tax-calculator1.4.sinewave.co.in/api/calculate-tax/', payload);
            const responseData = response.data;
    
            // Update response data
            setResponse(responseData);
    
            // Handle output update
            handleOutputUpdate(responseData);

            
    
            // Create userData object
            const userData = {
                input: payload,
                response: {
                    first_api_response: responseData.first_api_response, // Assuming this is how the response is structured
                    second_api_response: responseData.second_api_response, // Assuming this is how the response is structured
                    InterestUS: responseData.second_api_response.InterestUS
                }
            };


           
                



 
           
             

            
         // Update newRegimeValue based on TaxMethod
            
            const salary = userData.response.first_api_response.Salary;
            const houseProperty = userData.response.first_api_response.HouseProperty;
            const BusinessProfession = userData.response.first_api_response.BusinessProfession;
            const OtherSources = userData.response.first_api_response.OtherSources;
            const AeighthC = userData.response.first_api_response.AeighthC;
            const DeductionVI = userData.response.first_api_response.DeductionVI;
            const DeductionVI_and_AeighthC_Total = userData.response.first_api_response.DeductionVI_and_AeighthC_Total;
            const LTCG_total = userData.response.first_api_response.LTCG_total;
            const STCG_total = userData.response.first_api_response.STCG_total;
            const LTCG_and_STCG_Total = userData.response.first_api_response.LTCG_and_STCG_Total;
            const TotalIncome = userData.response.second_api_response.TotalIncome;
            const GrossTotalIncome = userData.response.second_api_response.TotalIncome;
            const TaxwoSurcharge = userData.response.second_api_response.TaxwoSurcharge;
            const Lessrebate87A = userData.response.second_api_response.Lessrebate87A;
            const Surcharge = userData.response.second_api_response.Surcharge;
            const EducationCess = userData.response.second_api_response.EducationCess;
            const TaxPayable = userData.response.second_api_response.TaxPayable;
            const BalancePayable = userData.response.second_api_response.BalancePayable;
            const TaxPayableRefundable = userData.response.second_api_response.TaxPayableRefundable;
            const InccomeTax = userData.response.second_api_response.InccomeTax;
    
            const T234A = userData.response.InterestUS.T234A;
            const T234B = userData.response.InterestUS.T234B;
            const T234C = userData.response.InterestUS.T234C;
            const Total_234 = userData.response.InterestUS.Total_234;
            const T234C_1506 = userData.response.InterestUS.T234C_1506;
            const T234C_1509 = userData.response.InterestUS.T234C_1509;
            const T234C_1512 = userData.response.InterestUS.T234C_1512;
            const T234C_1503 = userData.response.InterestUS.T234C_1503;
    
            const NormalTax = userData.response.second_api_response.NormalTax;
            const SpecialTax = userData.response.second_api_response.SpecialTax;
            const TotalTax = userData.response.second_api_response.TotalTax;
            const message = userData.response.second_api_response.message;
        
     
            setGrossTotalIncome(GrossTotalIncome);
            setTotalIncome(TotalIncome);
            setTaxwoSurcharge(TaxwoSurcharge);
            setLessrebate87A(Lessrebate87A);
            setSurcharge(Surcharge);
            setEducationCess(EducationCess);
            setTaxPayable(TaxPayable);
            setBalancePayable(BalancePayable);
            setOldRegimeValue(oldRegimeValue)
           ////
           setTaxPayableRefundable(TaxPayableRefundable);
           setInccomeTax(InccomeTax);
           setT234A(T234A);
           setNormalTax(NormalTax);
           setSpecialTax(SpecialTax);
           setTotalTax(TotalTax);
           setT234B(T234B);
           setT234C(T234C);




        
          
        

            // Store userData object in localStorage
            const key = `${name}`;
            const userDataJSON = JSON.stringify(userData);
            localStorage.setItem(key, userDataJSON);
    
            console.log(payload); // Output the payload
        } catch (error) {
            console.error(error);
            setOutput('An error occurred. Please try again.');
        }
    };


    useEffect(() => {
        // Load newRegimeValue from local storage when the component mounts
        const savedNewRegimeValue = localStorage.getItem('newRegimeValue');
        if (savedNewRegimeValue !== null) {
            setNewRegimeValue(parseFloat(savedNewRegimeValue));
        }
    }, []);

    useEffect(() => {
        if (output && output.RbalancePayable !== undefined) {
            setNewRegimeValue(output.RbalancePayable);
        }
    }, [output]);

   
    
   
   
                    
 
    return (
        <div className="App">
          <div className="spacer_2"></div> {/* Spacer div */}
          <div className="tax-Information">Tax Information</div>
          <div className="your-container">
            {/* New Regime Box */}
            <div className="value-box" id="newRegime" style={{ marginLeft: '18px', marginTop: '8px' }}>
              <div className="permanent-text-2" style={{ fontSize: '16px',  marginright: '12px', fontWeight: 'bold'}}>
                New Regime:
              </div>
              <div className="value">{newRegimeValue}</div>
            </div>
          </div>
        
      
            <img src="SINE_2.png" alt="ABC Logo" className="logo" />
            <div className="button-container">
                {isSalaryPopupComplete && (
                    <button
                        ref={calculateButtonRef}
                        type="submit"
                        className="submit-button_2"
                        style={{ display: 'none' }}
                        value={'submit2'}
                        onClick={handleSubmit}
                    >
                        Calculate
                    </button>
                )}
            </div>
            <div className="form-group-1">
                <div className="HTML_Part_10">
                    <label htmlFor="basicsalary" onClick={() => setOpenPopupSalary(true)} className="blue-link">Salary:</label>
                    <input
                        type="number"
                        id="basicsalary"
                        value={basicsalary}
                        onChange={(e) => setbasicsalary(e.target.value)}
                        disabled={true}
                    />
                </div>

                {openPopupSalary && (
                    <div className="popup">
                        <div className="popup-header-title">Salary Information</div>
                        {Object.keys(salaryFields).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label htmlFor={fieldName}>{fieldName}:</label>
                                <input
                                    type="number"
                                    value={salaryFields[fieldName]}
                                    onChange={(e) => handleSalaryFieldChange(fieldName, e.target.value)}

                                />
                            </div>
                        ))}
                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetSalary(); }}>OK</button>
                        </div>
                    </div>
                )}
                <div className="HTML_Part_10">
                    <label htmlFor="lessRebate87A">Less Rebate 87A:</label>
                    <input
                        type="number"
                        id="lessRebate87A"
                        value={lessrebate87A}
                        onChange={(e) => setLessRebate87A(e.target.value)}
                    />
                </div>
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label
                        htmlFor="houseproperty"
                        onClick={() => {
                            setOpenPopupHouseProperty(true);
                            setOpenPopupSelfOccupied(false); // Close Self Occupied popup if open
                            setOpenPopupRentedHouseProperty(false); // Close Rented House Property popup if open
                        }}
                        className="blue-link"
                    >
                        House Property:
                    </label>
                    <input
                        type="number"
                        id="houseproperty"
                        value={houseproperty}
                        onChange={(e) => sethouseproperty(e.target.value)}
                        disabled={true}
                    />
                </div>

                {openPopupHouseProperty && (
                    <div className="popup">
                        <div className="popup-header-title">House Property Information</div>
                        {Object.keys(housePropertyFields).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label
                                    htmlFor={fieldName}
                                    onClick={() => {
                                        if (fieldName === "Self Occupied") {
                                            setOpenPopupSelfOccupied(true);
                                            setOpenPopupRentedHouseProperty(false); // Close Rented House Property popup if open
                                        } else if (fieldName === "Rented House Property") {
                                            setOpenPopupRentedHouseProperty(true);
                                            setOpenPopupSelfOccupied(false); // Close Self Occupied popup if open
                                        }
                                    }}
                                    className="blue-link"
                                >
                                    {fieldName}:
                                </label>
                                <input
                                    type="number"
                                    value={housePropertyFields[fieldName]}
                                    onChange={(e) => handleHousePropertyFieldChange(fieldName, e.target.value)}
                                    disabled={true}
                                />
                            </div>
                        ))}
                        <div className="popup-button">
                           <button onClick={(e) => { e.preventDefault(); calculateAndSetHouseProperty(); }}>OK</button>
                        </div>
                    </div>
                )}

                {/* Popup for "Self Occupied" */}
                {openPopupSelfOccupied && (
                    <div className="popup">
                        <div className="popup-header-title">Self Occupied Information</div>
                        {Object.keys(selfOccupiedFields).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label htmlFor={fieldName} className="black-label">{fieldName}:</label>
                                <input
                                    type="number"
                                    value={selfOccupiedFields[fieldName]}
                                    onChange={(e) => handleSelfOccupiedFieldChange(fieldName, e.target.value)}
                                />
                            </div>
                        ))}
                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetSelfOccupied(); }}>OK</button>
                        </div>
                    </div>
                )}

                {/* Popup for "Rented House Property" */}
                {openPopupRentedHouseProperty && (
                    <div className="popup">
                        <div className="popup-header-title">Rented House Property Information</div>
                        {Object.keys(rentedHousePropertyFields).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label htmlFor={fieldName} className="black-label">{fieldName}:</label>
                                <input
                                    type="number"
                                    value={rentedHousePropertyFields[fieldName]}
                                    onChange={(e) => handleRentedHousePropertyFieldChange(fieldName, e.target.value)}
                                />
                            </div>
                        ))}
                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetRentedHouseProperty(); }}>OK</button>
                        </div>
                    </div>
                )}
                <div className="HTML_Part_10">
                    <label htmlFor="surcharge">Surcharge:</label>
                    <input
                        type="number"
                        id="surcharge"
                        value={surcharge}
                        onChange={(e) => setSurcharge(e.target.value)}
                    />
                </div>
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="business_profession" onClick={() => setOpenPopupBusinessProfession(true)} className="blue-link">Business/Prof:</label>
                    <input
                        type="number"
                        id="business_profession"
                        value={business_profession}
                        onChange={(e) => setbusiness_profession(e.target.value)}
                        disabled={true}
                    />
                </div>

                {openPopupBusinessProfession && (
                    <div className="popup">
                        <div className="popup-header-title">Business/Profession Information</div>
                        {Object.keys(businessProfessionFields).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label htmlFor={fieldName}>{fieldName}:</label>
                                <input
                                    type="number"
                                    value={businessProfessionFields[fieldName]}
                                    onChange={(e) => handleBusinessProfessionFieldChange(fieldName, e.target.value)}
                                />
                            </div>
                        ))}

                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetBusinessProfession(); }}>OK</button>
                        </div>
                    </div>
                )}
                <div className="HTML_Part_10">
                    <label htmlFor="educationCess">Education Cess:</label>
                    <input
                        type="number"
                        id="educationCess"
                        value={educationCess}
                        onChange={(e) => setEducationCess(e.target.value)}
                    />
                </div>
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="Capital Gain">Capital Gain:</label>
                    <input
                        type="number"
                        id="capitalgain"
                        value={sum}
                        onChange={(e) => setcapitalgain(e.target.value)}
                    />
                </div>
                <div className="HTML_Part_10">
                    <label htmlFor="Tax Payable">Tax Payable:</label>
                    <input
                        type="number"
                        id="taxPayable"
                        value={taxPayable}
                        onChange={(e) => setTaxPayable(e.target.value)}
                    />
                </div>
            </div>
            {/* <div className="spacer"></div> Spacer div */}
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="otherIncome" onClick={() => setOpenPopup_7(true)} className="blue-link" >Other Sources:</label>
                    <input
                        type="number"
                        id="LTCG_4"
                        value={LTCG_4}
                        onChange={(e) => handleInputChange(e)}
                        disabled={true}
                    />
                </div>
                {openPopup_7 && (
                    <div className="popup">
                        <div className="popup-header-title">Other Sources</div>
                        {Object.keys(popupFields_7).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label htmlFor={fieldName}>{fieldName}:</label>
                                <input
                                    type="number"
                                    value={popupFields_7[fieldName]}
                                    onChange={(e) => handleFieldAndInputChange_7(fieldName, e.target.value, e)}
                                    disabled={fieldName === "Dividend"}
                                />
                            </div>
                        ))}
                        <div className="popup-message">{popupMessage}
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetDeduction_7(); }}>OK</button>

                        </div>
                    </div>
                )}
                <div className="HTML_Part_10">
                    <label htmlFor="TDS">TDS:</label>
                    <input
                        type="number"
                        id="tds"
                        value={tds}
                        onChange={(e) => setTDS(e.target.value)}
                    />
                </div>
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="grosstotalincome">Gross Total Income:</label>
                    <input
                        type="number"
                        id="grosstotalincome"
                        value={grosstotalincome}
                        onChange={(e) => setGrossTotalIncome(e.target.value)}
                       
                    />
                </div>
                <div className="HTML_Part_10">
                    <label htmlFor="advanceTax2ndInst" onClick={() => setOpenPopup_1(true)} className="blue-link" >Advance Tax Paid:</label>
                    <input
                        type="number"
                        id="advanceTax2ndInst"
                        value={advanceTax1STInst}
                        onChange={(e) => handleInputChange(e)}
                        disabled={false}
                    />
                </div>
                {openPopup_1 && (
                    <div className="popup">
                        <div className="popup-header-title">Advance Tax Paid</div>
                        {Object.keys(popupFields_1).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label htmlFor={fieldName}>{fieldName}:</label>
                                <input
                                    type="number"
                                    value={popupFields_1[fieldName]}
                                    onChange={(e) => handleFieldAndInputChange_1(fieldName, e.target.value, e)}
                                />
                            </div>

                        ))}
                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetDeduction_1(); }}>OK</button>
                        </div>
                    </div>
                )}
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label
                        htmlFor="deductionunderchaptervip"
                        onClick={() => setOpenPopupChapterVIADeductions(true)}
                        className="blue-link"
                    >
                        Chapter VIA Ded:
                    </label>
                    <input
                        type="number"
                        id="deductionunderchaptervip"
                        value={deductionUnderChapterVIA}
                        onChange={(e) => setDeductionUnderChapterVIA(parseFloat(e.target.value))}
                        disabled={true}
                    />
                </div>

                {openPopupChapterVIADeductions && (
                    <div className="popup">
                        <div className="popup-header-title">Chapter VIA Deductions Information</div>
                        {Object.keys(chapterVIADeductionsFields).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label
                                    htmlFor={fieldName}
                                    onClick={() => {
                                        if (fieldName === "80C") {
                                            setOpenPopup80C(true);
                                        } else if (fieldName === "Chapter VIA") {
                                            setOpenPopupChapterVIA(true);
                                        }
                                    }}
                                    className={`blue-link ${fieldName === "80C" || fieldName === "Chapter VIA" ? "blue-link" : ""}`}
                                >
                                    {fieldName}:
                                </label>
                                <input
                                    type="number"
                                    value={chapterVIADeductionsFields[fieldName]}
                                    onChange={(e) => handleChapterVIADeductionsFieldChange(fieldName, e.target.value)}
                                />
                            </div>
                        ))}
                        {/* Total Chapter VIA Deductions */}
                        <div key="Total Chapter VIA Deductions" className="popup-field-total">
                            <label>Total Chapter VIA Deductions:</label>
                            <span>{deductionUnderChapterVIA}</span> {/* Replace with the function that calculates the total */}
                        </div>
                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetChapterVIADeductions(); }}>OK</button>
                        </div>
                    </div>
                )}

                {/* Popup for "80C" */}
                {openPopup80C && (
                    <div className="popup">
                        <div className="popup-header-title">80C Information</div>
                        {Object.keys(popupFields80C).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label htmlFor={fieldName} className="black-label">{fieldName}:</label>
                                <input
                                    type="number"
                                    value={popupFields80C[fieldName]}
                                    onChange={(e) => handlePopupFieldChange80C(fieldName, e.target.value)}
                                />
                            </div>
                        ))}
                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSet80C(); }}>OK</button>
                        </div>
                    </div>
                )}

                {/* Popup for "Chapter VIA" */}
                {openPopupChapterVIA && (
                    <div className="popup">
                        <div className="popup-header-title">Chapter VIA Information</div>
                        {Object.keys(popupFieldsChapterVIA).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field">
                                <label htmlFor={fieldName} className="black-label">{fieldName}:</label>
                                <input
                                    type="number"
                                    value={popupFieldsChapterVIA[fieldName]}
                                    onChange={(e) => handlePopupFieldChangeChapterVIA(fieldName, e.target.value)}
                                />
                            </div>
                        ))}
                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetChapterVIA(); }}>OK</button>
                        </div>
                    </div>
                )}
                <div className="HTML_Part_10">
                    <label htmlFor="Int u/s 234A">Int u/s 234A:</label>
                    <input
                        type="number"
                        id="intA"
                        value={t234A}
                    
                        onChange={(e) => setintA(e.target.value)}
                    />
                </div>
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="totalIncome">Total Income:</label>
                    <input
                        type="number"
                        id="totalIncome"
                        value={totalIncome}
                        onChange={(e) => setTotalIncome(e.target.value)}
                    />
                </div>
                <div className="HTML_Part_10">
                    <label htmlFor="Int u/s 234B">Int u/s 234B:</label>
                    <input
                        type="number"
                        id="intB"
                        value={t234B}
                        onChange={(e) => setT234B(e.target.value)}
                    />
                </div>
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="agriculturalIncome">Agricultural Income:</label>
                    <input
                        type="number"
                        id="agriculturalIncome"
                        value={agriculturalIncome}
                        onChange={(e) => setAgriculturalIncome(e.target.value)}
                    />
                </div>
                <div className="HTML_Part_10">
                    <label htmlFor="Int u/s 234C">Int u/s 234C:</label>
                    <input
                        type="number"
                        id="intC"
                        value={t234C}
                        onChange={(e) =>setT234C(e.target.value)}
                    />
                </div>
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="Income Tax Normal">Income Tax Normal:</label>
                    <input
                        type="number"
                        id="incomeTaxNormal"
                        value={normalTax}
                        onChange={(e) => setIncomeTaxNormal(e.target.value)}
                    />
                </div>
                <div className="HTML_Part_10">
                    <label htmlFor="SA Tax Paid" onClick={() => setOpenPopup_2(true)} className="blue-link" >SA Tax Paid:</label>

                    <input
                        type="number"
                        id="STCG_1"
                        value={STCG_1}
                        onChange={(e) => handleInputChange(e)}
                        disabled={true}
                    />
                </div>
                {openPopup_2 && (
                    <div className="popup">
                        <div className="popup-header-title">SA Tax Paid</div>
                        {Object.keys(popupFields_2).map((fieldName, index) => (
                            <div key={fieldName} className="popup-field_2">
                                <label htmlFor={fieldName}>{fieldName} Amount:</label>
                                <input
                                    type="number"
                                    value={popupFields_2[fieldName].amount}
                                    onChange={(e) => handlePopupFieldChange_2(fieldName, "amount", e.target.value)}
                                />
                                <label htmlFor={`${fieldName}_date`}>Date:</label>
                                <input
                                    type="date"
                                    id={`${fieldName}_date`}
                                    value={popupFields_2[fieldName].date}
                                    onChange={(e) => handlePopupFieldChange_2(fieldName, "date", e.target.value)}
                                />
                            </div>
                        ))}
                        {/* Total SA Tax Paid */}

                        <div key="Total SA Tax Paid" className="popup-field-total">
                            <label>Total SA Tax Paid:</label>
                            <span>{totalSATAxPaid}</span> {/* Replace with the function that calculates the total */}
                        </div>
                        <div className="popup-button">
                            <button onClick={(e) => { e.preventDefault(); calculateAndSetDeduction_2(); }}>OK</button>
                        </div>
                    </div>
                )}
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="Income Tax Special">Income Tax Special:</label>
                    <input
                        type="number"
                        id="incomeTaxSpecial"
                        value={specialTax}
                        onChange={(e) => setIncomeTaxSpecial(e.target.value)}
                    />
                </div>
                <div className="HTML_Part_10">
                    <label htmlFor="Balance Payable/Refundable">Balance Payable<br /> /Refundable:</label>
                    <input
                        type="number"
                        id="balancePayable"
                        value={taxPayableRefundable}
                        onChange={(e) => setBalancePayable(e.target.value)}
                    />
                </div>
            </div>
            <div className="form-group-1" style={{ marginTop: '15px' }}>
                <div className="HTML_Part_10">
                    <label htmlFor="Tax Without Surcharge">Tax Without<br /> Surcharge:</label>
                    <input
                        type="number"
                        id="taxWithoutSurcharge"
                        value={taxwoSurcharge}
                        onChange={(e) => settaxWithoutSurcharge(e.target.value)}
                    />
                </div>
            </div>

            <div className="spacer_3"></div> {/* Spacer div */}
            <div className="button-container">
                <button id="delete-button" className="submit-button_1" onClick={handleDeleteRecord}>Delete Record</button>
                <button type="submit" className="submit-button_2" value={'submit2'} onClick={handleSubmit}>Calculate</button>
                <button id="reset-button" onClick={handleResetClick}>Reset</button>
            </div>
        </div >

    );


}


const MainPage = () => {
    const [dataFromPage1, setDataFromPage1] = useState({});
    const [selectedName, setSelectedName] = useState('');
    const [output, setOutput] = useState(''); // Add output state

    const handleCalculateInPage1 = (data) => {
        setDataFromPage1(data);
    };

    const handleNameSelect = (name) => {
        setSelectedName(name);
    };

    // Add this function to update the output state
    const handleOutputUpdate = (newOutput) => {
        setOutput(newOutput);
    };

    return (
        <React.Fragment>
            <section>
                <div className="grid-container">
                    <div className="page">
                        <Page1
                            handleCalculate={handleCalculateInPage1}
                            handleNameSelect={handleNameSelect}
                            output={output} // Pass output to Page1
                        />
                    </div>
                    <div className="page">
                        <Page2
                            handleCalculateInPage1={handleCalculateInPage1}
                            dataFromPage1={dataFromPage1}
                            selectedName={selectedName}
                            handleOutputUpdate={handleOutputUpdate} // Pass the handler to update output
                            TaxPayableRefundable={dataFromPage1.taxPayableRefundable} // Pass TaxPayableRefundable as prop
                        />
                    </div>
                </div>
            </section>
        </React.Fragment>
    );
};
export default MainPage;


