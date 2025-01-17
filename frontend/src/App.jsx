//useState is the React hook that manages state (data that changes)
import React, { useState } from "react";
//Your custom components
// import ChatHistory from "./components/ChatHistory";
// import ChatInput from "./components/ChatInput";

import axios from "axios";

//New Components
import QueryDisplay from "./components/QueryDisplay";
import ResultsWindow from "./components/ResultWindow";
import InputSection from "./components/InputSection";
import ChatList from "./components/ChatList";

const API_URL = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

//Functional component. React calls this whenever it needs to render/re-rencer your app
function App() {
    //These are state variables.
    //They store data that changes over time
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);
    const [activeProviders, setActiveProviders] = useState({
        ChatGPT: true,
        Gemini: true,
        Grok: true,
        Claude: false
    });

    //Event Handler. Updates the results window. Handles query submission
    const handleSendQuery = (newQuery) => {
        setQuery(newQuery); //Update the displayed query

        setResults([
          { provider: "ChatGPT", response: `${newQuery} is blah`, color: "bg-gray-400" },
          { provider: "Gemini", response: `${newQuery} is blah`, color: "blue" },
          { provider: "Claude", response: `${newQuery} is blah`, color: "orange" },
          { provider: "Grok", response: `${newQuery} is blah`, color: "purple" },
        ]);
    };

    //Event Handler. Toggles state of LLM option
    const toggleProvider = (provider) => {
        setActiveProviders((prev) => ({
        ...prev,
        [provider]: !prev[provider],
        }));
    };

    //Defines what the component renders. React uses this JSX code to create the HTML structure
    return (
        <div className="h-screen flex">
      {/* Left-Side Navigation (Chat List Placeholder) */}
      <div className="w-1/6 border-r bg-gray-100">
        <ChatList />
      </div>

      {/* Main Content */}
      <div className="flex-grow flex flex-col">
        {/* Top Section */}
        <QueryDisplay query={query} activeProviders={activeProviders} />

        {/* Middle Section */}
        <ResultsWindow results={results} />

        {/* Bottom Section */}
        <InputSection
          onSend={handleSendQuery}
          activeProviders={activeProviders}
          toggleProvider={toggleProvider}
        />
      </div>
    </div>
    );
}
//This export statement is making the App component available to other files
//In src/index.js, App is imported and rendered into the DOM
export default App;
