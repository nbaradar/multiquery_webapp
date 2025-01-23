/* InputSection
Contains
    - Dropdown menu to toggle LLM providers
    - Input field for the query
    - Submit button to send the query and display results
*/

import React, { useState } from "react";

const InputSection = ({ onSend, activeProviders, toggleProvider }) => {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (message.trim()) {
      onSend(message);
      setMessage("");
    }
  };

  return (
    <div className="p-4 border-t flex items-center space-x-4">
      {/* Dropdown Menu */}
      <div className="dropdown dropdown-top">
        <label tabIndex={0} className="btn btn-secondary">
          Providers
        </label>
        <ul
          tabIndex={0}
          className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
        >
          {Object.keys(activeProviders).map((provider) => (
            <li key={provider} className="flex items-center justify-between">
              <span>{provider}</span>
              <input
                type="checkbox"
                checked={activeProviders[provider]}
                onChange={() => toggleProvider(provider)}
                className="toggle toggle-primary"
              />
            </li>
          ))}
        </ul>
      </div>

      {/* Input Field */}
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your query..."
        className="textarea textarea-bordered border flex-grow"
      ></textarea>

      {/* Submit Button */}
      <button onClick={handleSend} className="btn btn-primary">Submit</button>
    </div>
  );
};

export default InputSection;
