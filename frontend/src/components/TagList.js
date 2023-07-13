import React from "react";

const TagList = ({ tags }) => {
  const isLink = (url) => {
    const pattern = /^(https?:\/\/)?([\w.-]+)\.([a-z]{2,})(:\d{2,5})?([\/\w.-]*)*\/?$/;
    return pattern.test(url);
  };

  return (
    <div>
      <div>
        <h3>Tags:</h3>
        <ul>
          {tags.map((tag, index) => (
            <li key={index}>
              {isLink(tag) ? (
                <a href={tag} target="_blank" rel="noopener noreferrer">
                  {tag}
                </a>
              ) : (
                tag
              )}
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Other Links:</h3>
        <ul>
          <li>
            <a href="https://www.bing.com" target="_blank" rel="noopener noreferrer">
              bing
            </a>
          </li>
        </ul>
      </div>
    </div>
  );
};


export default TagList;
