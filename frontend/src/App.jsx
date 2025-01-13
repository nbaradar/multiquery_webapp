//useState is the React hook that manages state (data that changes)
import React, { useState } from "react";
//Your custom components
import ChatHistory from "./components/ChatHistory";
import ChatInput from "./components/ChatInput";

//Functional component. React calls this whenever it needs to render/re-rencer your app
function App() {
    //These are state variables.
    //They store data that changes over time
    const [chatHistory, setChatHistory] = useState([]);
    const [llmOptions, setLlmOptions] = useState({
        ChatGPT: true,
        Gemini: false,
        Grok: true,
    });

    //Event Handler. Updates the chathistory 
    const handleSendMessage = (message) => {
        setChatHistory((prev) => [
        ...prev,
        { user: "User", message },
        { user: "LLM", message: `Response to: ${message}` }, // Mock response
        ]);
    };

    //Event Handler. Toggles state of LLM option
    const toggleLlmOption = (option) => {
        setLlmOptions((prev) => ({
        ...prev,
        [option]: !prev[option],
        }));
    };

    //Defines what the component renders. React uses this JSX code to create the HTML structure
    return (
        <div className="h-screen flex flex-col">
        {/* Chat History */}
        <div className="flex-grow bg-gray-100 p-4 overflow-y-auto">
            {/* Chat History */}
            <ChatHistory chatHistory={chatHistory} />
        </div>

        {/* Chat Input */}
        <div className="border-t p-4 bg-white">
            <ChatInput
            onSend={handleSendMessage}
            llmOptions={llmOptions}
            toggleLlmOption={toggleLlmOption}
            />
        </div>
        </div>
    );
}
//This export statement is making the App component available to other files
//In src/index.js, App is imported and rendered into the DOM
export default App;
