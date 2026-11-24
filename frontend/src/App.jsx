import { useState, useEffect } from "react";
import { get_items, post_item } from "#fetch_helpers";
import "./App.css";

function App() {
  const [test, setTest] = useState([]);

  useEffect(() => {
    // make custom hook for this
    async function get_fetch() {
      const data = get_items();
      setTest(data);
    }
    get_fetch();
  }, [test]);

  return (
    <>
      <h1>{test}</h1>
    </>
  );
}

export default App;
