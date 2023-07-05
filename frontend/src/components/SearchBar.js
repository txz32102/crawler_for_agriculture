import React, { Component } from "react";

class SearchBar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      url: "",
      keyword: "",
      tags: []  // Add the 'tags' state property
    };
  }
  

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    const { url, keyword } = this.state;
    
    fetch("/api/crawler/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url, keyword })
    })
      .then((response) => response.json())
      .then((data) => {
        // Process the response data
        console.log("Response:", data);
        // Update the state with the received tags
        this.setState({ tags: data.tags });
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  
    // Reset the form
    this.setState({ url: "", keyword: "" });
  };
  

  render() {
    const { url, keyword } = this.state;
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input
            type="text"
            name="url"
            placeholder="Enter URL"
            value={url}
            onChange={this.handleChange}
            key="urlInput" // Add key for the URL input field
          />
          <input
            type="text"
            name="keyword"
            placeholder="Enter Keyword"
            value={keyword}
            onChange={this.handleChange}
            key="keywordInput" // Add key for the keyword input field
          />
          <button type="submit">Search</button>
        </form>
      </div>
    );
  }
  
  
}

export default SearchBar;
