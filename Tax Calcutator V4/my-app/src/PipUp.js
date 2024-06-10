
import React, { useState } from 'react';

function PopUp() {
    const [popupFields, setPopupFields] = useState({
        field_1: 0,
        field_2: 0,
        field_3: 0,
        field_4: 0,
        field_5: 0,
    });

    const [deductionUnderChapterVIA, setDeductionUnderChapterVIA] = useState(0);

    const handlePopupFieldChange = (fieldName, value) => {
        setPopupFields((prevFields) => ({
            ...prevFields,
            [fieldName]: parseFloat(value),
        }));
    };

    const calculateAndSetDeduction = () => {
        const sum = Object.values(popupFields).reduce((acc, val) => acc + val, 0);
        setDeductionUnderChapterVIA(sum);
    };

    return (
        <div>
            {/* Your other form groups */}
            <div className="form-group">
                <label htmlFor="deductionunderchaptervip">Deduction Under Chapter VIA:</label>
                <input
                    type="number"
                    id="deductionunderchaptervip"
                    value={deductionUnderChapterVIA}
                    onChange={(e) => setDeductionUnderChapterVIA(parseFloat(e.target.value))}
                />
                <button onClick={() => setOpenPopup(true)}>Edit Deduction</button>
            </div>

            {/* Popup */}
            {openPopup && (
                <div className="popup">
                    <input
                        type="number"
                        value={popupFields.field_1}
                        onChange={(e) => handlePopupFieldChange('field_1', e.target.value)}
                    />
                    {/* Repeat for field_2, field_3, field_4, field_5 */}
                    <button onClick={() => calculateAndSetDeduction()}>OK</button>
                </div>
            )}
        </div>
    );
}

export default PopUp;
