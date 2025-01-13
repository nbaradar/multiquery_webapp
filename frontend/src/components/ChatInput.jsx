/*
This component is responsible for 
    - Displaying a text input field where users can type their messages
    - Providing a submit button to send the message
    - Including a dropdown menu for selecting LLM options with switches to toggle them on and off
*/

import React, { useState } from "react";

//Functional Component. Recieves 3 props: 
//  onSend: handles sending messages. Function parent from App.jsx
//  llmOptions: Object representing state of LLM toggles
//  toggleLlmOption: A function to toggle the state of an LLM option
const ChatInput = ({ onSend, llmOptions, toggleLlmOption }) => {
    //Current value of the text input field
    //Initially, the message is an empty string
    const [message, setMessage] = useState("");

    //Event Handler. 
    const handleSend = () => {
        //Checks if message is not empty. 
        if (message.trim()) {
            //Send the message and clear the input field. 
            //This sends it to App.jsx to then call handleSendMessage()
            onSend(message);
            setMessage("");
        }
    };

    //The JSX defines the layout and behavior of the component
    return (
        <div className="flex items-center space-x-4">
        {/* Dropdown Menu 
            Displays the LLM options as a dropdown. Each option has a toggle switch 
        */}
        <div className="dropdown">
            <label tabIndex={0} className="btn btn-secondary">
            LLM Options
            </label>
            <ul tabIndex={0} className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52">
            {/*Object.keys gets the list of LLM names 
                We loop through the LLM names and render checkboxes for each*/}
            {Object.keys(llmOptions).map((option) => (
                <li key={option} className="flex items-center justify-between">
                <span>{option}</span>
                <input
                    type="checkbox"
                    checked={llmOptions[option]}
                    onChange={() => toggleLlmOption(option)}
                    className="toggle toggle-primary"
                />
                </li>
            ))}
            </ul>
        </div>

        {/* Input Field 
            Let's the user type a message. The value attribute binds the input to the message state
            onChange updates the message state whenever the user types*/}
        <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Enter your query..."
            className="input input-bordered flex-grow"
        />

        {/* Submit Button 
            Sends the message when clicked. 
            The onClick event triggers the handleSend function*/}
        <button style={{ backgroundColor: '#9d9dbf', color: 'white' }} onClick={handleSend} className="btn btn-primary">
            Submit
        </button>
        </div>
    );
};

//Makes this component available to other files. 
export default ChatInput;
