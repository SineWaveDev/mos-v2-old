import React from 'react';
import Form from 'react-bootstrap/Form';

function NameInputField({ name, selectedName, onNameChange, onSelectedNameChange }) {
    return (
        <Form.Group controlId="name">
            <Form.Label>Name:</Form.Label>
            <Form.Control
                type="text"
                value={name}
                onChange={(e) => {
                    onNameChange(e.target.value);
                }}
            />
            <Form.Select
                id="nameDropdown"
                value={selectedName}
                onChange={(e) => {
                    onSelectedNameChange(e.target.value);
                }}
            >
                {Object.keys(localStorage).map((name) => (
                    <option key={name} value={name}>
                        {name}
                    </option>
                ))}
            </Form.Select>
        </Form.Group>
    );
}

export default NameInputField;
