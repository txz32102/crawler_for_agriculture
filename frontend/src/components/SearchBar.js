import React, { Component } from "react";
import TagList from "./TagList";

class SearchBar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      url: "",
      keyword: "",
      tags: []
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
      body: JSON.stringify({ url: url, keyword: keyword })
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Response:", data);
        console.log("Tags:", data.tags);
        this.setState({ tags: data.tags });
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    this.setState({ url: "", keyword: "" });
  };

  render() {
    const { url, keyword, tags } = this.state;
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input
            type="text"
            name="url"
            placeholder="Enter URL"
            value={url}
            onChange={this.handleChange}
            key="urlInput"
          />
          <input
            type="text"
            name="keyword"
            placeholder="Enter Keyword"
            value={keyword}
            onChange={this.handleChange}
            key="keywordInput"
          />
          <button type="submit">Search</button>
        </form>

        <TagList tags={tags} />
      </div>
    );
  }
}

export default SearchBar;
