import React from "react";

const TodoItem = ({ item, viewCompleted, editItem, handleDelete }) => {
  return (
    <li
      key={item.id}
      className="list-group-item d-flex justify-content-between align-items-center"
    >
      <span
        className={`todo-title mr-2 ${viewCompleted ? "completed-todo" : ""}`}
        title={item.description}
      >
        {item.title}
      </span>
      <span>
        <button
          className="btn btn-secondary mr-2"
          onClick={() => editItem(item)}
        >
          Edit
        </button>
        <button className="btn btn-danger" onClick={() => handleDelete(item)}>
          Delete
        </button>
      </span>
    </li>
  );
};

export default TodoItem;
