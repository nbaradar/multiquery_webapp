/*
This component is responsible for displaying the chat history (a list of messages exchanged between the user and the LLM).
It receives the chat history as a prop (data passed from a parent component, in this case, App.jsx).
*/

import React from "react";

//This is a functional component. It takes the prop chatHistory. 
const ChatHistory = ({ chatHistory }) => {
    //This JSX return block defines what the component renders
    return (
        <div>
        <h2 className="font-bold text-lg mb-4">Chat History</h2>
        {/* chatHistory is an array of message objects. 
            The map() function interates over the array, creating a new JSX element for each message 
            
            The key={index} attributes helps React identify each element uniquely to optimize rendering.
            */}
        {chatHistory.map((entry, index) => (
            <div key={index} className="mb-4">
            <div className={`font-semibold ${entry.user === "User" ? "text-blue-600" : "text-green-600"}`}>
                {entry.user}:
            </div>
            <div className="text-gray-800">{entry.message}</div>
            </div>
        ))}
        </div>
    );
};

//Makes this compoment available to other files
export default ChatHistory;
