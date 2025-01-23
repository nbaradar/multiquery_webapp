//useState is the React hook that manages state (data that changes)
import React, { useState } from "react";
//Your custom components
// import ChatHistory from "./components/ChatHistory";
// import ChatInput from "./components/ChatInput";

//import axios from "axios";
//const API_URL = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

//New Components
import QueryDisplay from "./components/QueryDisplay";
import ResultsWindow from "./components/ResultWindow";
import InputSection from "./components/InputSection";
import ChatList from "./components/ChatList";
import { fetchResults } from "./api";

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
    const providerColors = {
      ChatGPTProvider: {
        "bg": "bg-zinc-200",
        "text": "text-zinc-450"
      },
      GeminiProvider: {
        "bg": "bg-blue-200",
        "text": "text-blue-450"
      },
      GrokProvider: {
        "bg": "bg-slate-200",
        "text": "text-slate-450"
      },
      ClaudeProvider: {
        "bg": "bg-orange-100",
        "text": "bg-orange-400"
      }
    }

    //Event Handler. Updates the results window. Handles query submission
    const handleSendQuery = async (newQuery) => {
        setQuery(newQuery); //Update the displayed query
        try{
          const data = await fetchResults(newQuery, activeProviders);
          console.log(data)
          let provider_results = []

          for(const provider in data.responses){
            const response = data.responses[provider]

            const bg_color = providerColors[provider].bg || "bg-red-200"; //fallback if no provider found in mapping
            const text_color = providerColors[provider].text || "bg-red-500"
            provider_results.push({ provider: provider, response: response, bg_color: bg_color, text_color: text_color})
          }
          setResults(provider_results)
        } catch (error) {
          console.error(error);
          alert("Failed to fetch results.");
        }
    };

    //Event Handler. Toggles state of LLM option
    const toggleProvider = (provider) => {
        //This anonymous function updates the activeProviders object in App.jsx
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
