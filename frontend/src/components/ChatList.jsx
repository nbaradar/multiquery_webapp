import React from "react";

const ChatList = () => {
  return (
    <div className="p-4">
      <h3 className="font-bold text-lg mb-4">Chats</h3>
      <ul>
        <li className="mb-2 cursor-pointer">Chat 1</li>
        <li className="mb-2 cursor-pointer">Chat 2</li>
        <li className="mb-2 cursor-pointer">Chat 3</li>
      </ul>
    </div>
  );
};

export default ChatList;
