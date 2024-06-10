// TaxCalculator.js (Common Parent Component)
import React, { useState } from 'react';
import Page1 from './Page1';
import Page2 from './Page2';

const TaxCalculator = () => {
    // Shared state for tax calculations
    const [basicsalary, setbasicsalary] = useState('0');
    const [houseproperty, sethouseproperty] = useState('0');
    // ... other state variables ...

    // Function to handle combined submission
    const handleCombinedSubmit = async () => {
        // Create payloads for Page1 and Page2
        const payloadPage1 = {
            // ... construct payload for Page1 ...
        };

        const payloadPage2 = {
            // ... construct payload for Page2 ...
        };

        // Combine both payloads and send them to the server
        const combinedPayload = {
            Page1Data: payloadPage1,
            Page2Data: payloadPage2,
        };

        try {
            // Send the combined payload to the server
            const response = await axios.post('http://tax-calculator1.4.sinewave.co.in/api/calculate-tax/', combinedPayload);
            console.log(response.data);
            // Handle the response as needed
        } catch (error) {
            console.error(error);
            // Handle errors
        }
    };

    return (
        <div className="App">
            {/* Render both Page1 and Page2 */}
            <Page1
                basicsalary={basicsalary}
                houseproperty={houseproperty}
                // ... pass other state variables ...
                onSubmit={handleCombinedSubmit} // Pass the combined submit function
            />
            <Page2
                basicsalary={basicsalary}
                houseproperty={houseproperty}
                // ... pass other state variables ...
                onSubmit={handleCombinedSubmit} // Pass the combined submit function
            />
        </div>
    );
};

export default TaxCalculator;
