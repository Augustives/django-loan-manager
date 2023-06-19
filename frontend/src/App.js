import axios from 'axios';
import React, { useState } from 'react';
import './App.css';


const SimpleForm = () => {
  const [value, setValue] = useState('');
  const [name, setName] = useState('');
  const [cpf, setCpf] = useState('');
  const [country, setCountry] = useState('BR')
  const [state, setState] = useState('')
  const [city, setCity] = useState('')
  const [street, setStreet] = useState('');
  const [postalCode, setPostalCode] = useState('');
  const [additionalInfo, setAdditionalInfo] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    const data = {
      "value": value,
      "customer": {
          "name": name,
          "cpf": cpf,
          "address": {
              "country": country,
              "state": state,
              "city": city,
              "street": street,
              "postal_code": postalCode,
              "additional_info": additionalInfo
          }   
      }
  };

  try {
    const response = await axios.post('http://localhost:8000/loan-proposals/', data);
    if (response.status === 201) {
      alert(`Loan proposal submitted successfully! Proposal ID="${response.data.id}"`);
    }
  } catch (error) {
    // alert(error)
    alert(`Loan proposal submission failed! Error=${JSON.stringify(error.response.data)}`);
  }
  };

  return (
    <form onSubmit={handleSubmit} className="form">
      <h2 className="title">Register Loan Proposal</h2>
      <label>
        Loan Value:
        <input
          type="number"
          value={value}
          onChange={(event) => setValue(event.target.value)}
          className="input"
        />
      </label>
      <br />
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={(event) => setName(event.target.value)}
          className="input"
        />
      </label>
      <br />
      <label>
        CPF:
        <input
          type="text"
          value={cpf}
          onChange={(event) => setCpf(event.target.value)}
          className="input"
        />
      </label>
      <br />
      <label>
        Country:
        <select
          value={country}
          onChange={(event) => setCountry(event.target.value)}
          className="input"
        >
          <option value="BR">Brazil</option>
        </select>
      </label>
      <br />
      <label>
        State:
        <input
          type="text"
          value={state}
          onChange={(event) => setState(event.target.value)}
          className="input"
        />
      </label>
      <br />
      <label>
        City:
        <input
          type="text"
          value={city}
          onChange={(event) => setCity(event.target.value)}
          className="input"
        />
      </label>
      <br />
      <label>
        Street:
        <input
          type="text"
          value={street}
          onChange={(event) => setStreet(event.target.value)}
          className="input"
        />
      </label>
      <br />
      <label>
        Postal Code:
        <input
          type="text"
          value={postalCode}
          onChange={(event) => setPostalCode(event.target.value)}
          className="input"
        />
      </label>
      <br />
      <label>
        Additional Address Info:
        <input
          type="text"
          value={additionalInfo}
          onChange={(event) => setAdditionalInfo(event.target.value)}
          className="input"
        />
      </label>
      <br />
      <button type="submit" className="button">Submit</button>
    </form>
  );
};

export default SimpleForm;
