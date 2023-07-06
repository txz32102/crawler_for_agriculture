import React from "react";

const TagList = ({ tags }) => {
  return (
    <div>
      {tags.length > 0 && (
        <div>
          <h3>Tags:</h3>
          <ul>
            {tags.map((tag, index) => (
              <li key={index}>{tag}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default TagList;
